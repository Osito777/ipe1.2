"""
PRL Quest 🦺 · Juego interactivo sobre factores de riesgo laboral y su prevención.
Ejecutar con:  streamlit run app.py
"""
import random

import streamlit as st

from preguntas import (
    ACCIONES, BLOQUES, CAMPOS_EVAL, CAMPOS_FUEGO, CAMPOS_RIESGO, CASOS_EVAL,
    CASOS_FUEGO, CASOS_RIESGO, CHULETA, CONS, MATRIZ, ORDENAR, PROB, PVD_ITEMS,
    QUIZ, SENALES, VERDADERO_FALSO,
)

st.set_page_config(page_title="PRL Quest", page_icon="🦺", layout="centered")

# ---------------------------------------------------------------------------
# Configuración del juego
# ---------------------------------------------------------------------------
PUNTOS_CAMPO = 2      # puntos por cada apartado acertado al clasificar/ordenar
BONUS_PERFECTO = 4    # extra si aciertas todo
PUNTOS_PREGUNTA = 5   # puntos por pregunta de opción múltiple / V-F
TAM_RETO = 15         # preguntas del reto mixto

NIVELES = [
    (0, "Becario 🦺"),
    (30, "Aprendiz con casco ⛑️"),
    (80, "Delegado de prevención 📋"),
    (150, "Técnico de prevención 🧑‍🔧"),
    (250, "Inspector de Trabajo 🕵️"),
]

MODOS = [
    "🏠 Inicio",
    "🔺 Identifica el riesgo",
    "🔥 Incendios y extintores",
    "⚖️ Evalúa el riesgo",
    "🔢 Ordena la secuencia",
    "🚦 Señales de seguridad",
    "✅ Verdadero o falso",
    "🧠 Quiz de teoría",
    "⚡ Reto mixto",
    "🪑 Revisa tu puesto (PVD)",
    "📖 Chuleta",
]

# Todo lo de opción múltiple en el mismo formato
VF_ITEMS = [
    {"enunciado": txt, "opciones": ["Verdadero", "Falso"], "correcta": 0 if ok else 1,
     "explicacion": expl, "barajar": False}
    for txt, ok, expl in VERDADERO_FALSO
]
POOL_RETO = QUIZ + VF_ITEMS + SENALES

BLOQUE_ID = {"Todos los bloques": "q0", **{b: f"q{i + 1}" for i, b in enumerate(BLOQUES)}}


# ---------------------------------------------------------------------------
# Estado y puntuación
# ---------------------------------------------------------------------------
def iniciar_estado():
    for clave, valor in {"puntos": 0, "racha": 0, "mejor_racha": 0,
                         "aciertos": 0, "intentos": 0}.items():
        st.session_state.setdefault(clave, valor)


def nivel_actual():
    nombre = NIVELES[0][1]
    for minimo, titulo in NIVELES:
        if st.session_state.puntos >= minimo:
            nombre = titulo
    return nombre


def siguiente_nivel():
    for minimo, titulo in NIVELES:
        if st.session_state.puntos < minimo:
            return minimo, titulo
    return None


def registrar(aciertos, intentos, puntos, perfecto):
    s = st.session_state
    s.aciertos += aciertos
    s.intentos += intentos
    s.puntos += puntos
    if perfecto:
        s.racha += 1
        s.mejor_racha = max(s.mejor_racha, s.racha)
    else:
        s.racha = 0


def reiniciar_modo(modo):
    for clave in [k for k in st.session_state if k.startswith(f"{modo}_")]:
        del st.session_state[clave]


def preparar_cola(modo, total, limite=None):
    """Crea (una sola vez) el orden aleatorio de preguntas de un modo."""
    if f"{modo}_orden" not in st.session_state:
        orden = list(range(total))
        random.shuffle(orden)
        st.session_state[f"{modo}_orden"] = orden[:limite] if limite else orden
        st.session_state[f"{modo}_pos"] = 0
        st.session_state[f"{modo}_res"] = None
        st.session_state[f"{modo}_ok"] = 0


def avanzar(modo):
    st.session_state[f"{modo}_pos"] += 1
    st.session_state[f"{modo}_res"] = None


def pantalla_final(modo, titulo):
    orden = st.session_state[f"{modo}_orden"]
    ok = st.session_state[f"{modo}_ok"]
    total = len(orden)
    st.success(f"🏁 ¡Completado! Has acertado **{ok} de {total}** en «{titulo}».")
    if ok / total >= 0.8:
        st.balloons()
        st.write("Nota: **Sobresaliente** 🎉")
    elif ok / total >= 0.5:
        st.write("Nota: **Aprobado**, ¡pero puedes mejorarlo! 💪")
    else:
        st.write("Nota: **A repasar** la chuleta 📖 y volver a intentarlo.")
    st.button("🔁 Jugar otra vez", on_click=reiniciar_modo, args=(modo,), key=f"again_{modo}")


def como_lista(valor):
    return list(valor) if isinstance(valor, (list, tuple)) else [valor]


# ---------------------------------------------------------------------------
# Barra lateral
# ---------------------------------------------------------------------------
def barra_lateral():
    s = st.session_state
    st.sidebar.title("🦺 PRL Quest")
    modo = st.sidebar.radio("Elige modo de juego", MODOS, key="modo_menu")
    st.sidebar.divider()
    st.sidebar.metric("Puntos", s.puntos)
    c1, c2 = st.sidebar.columns(2)
    c1.metric("Racha 🔥", s.racha)
    c2.metric("Mejor racha", s.mejor_racha)
    precision = (s.aciertos / s.intentos * 100) if s.intentos else 0
    st.sidebar.write(f"**Nivel:** {nivel_actual()}")
    st.sidebar.write(f"**Precisión:** {precision:.0f}% ({s.aciertos}/{s.intentos})")
    prox = siguiente_nivel()
    if prox:
        minimo, titulo = prox
        st.sidebar.progress(min(s.puntos / minimo, 1.0))
        st.sidebar.caption(f"Te faltan {minimo - s.puntos} puntos para {titulo}")
    else:
        st.sidebar.caption("¡Nivel máximo alcanzado!")
    if st.sidebar.button("🗑️ Reiniciar todo"):
        st.session_state.clear()
        st.rerun()
    return modo


# ---------------------------------------------------------------------------
# Modo genérico: clasificar casos con varios desplegables
# ---------------------------------------------------------------------------
def modo_clasificador(modo, titulo, descripcion, casos, campos, pie=None):
    st.header(titulo)
    st.caption(f"{descripcion} {PUNTOS_CAMPO} puntos por apartado + {BONUS_PERFECTO} de bonus si aciertas todo.")
    preparar_cola(modo, len(casos))
    pos = st.session_state[f"{modo}_pos"]
    orden = st.session_state[f"{modo}_orden"]
    if pos >= len(orden):
        pantalla_final(modo, titulo)
        return

    idx = orden[pos]
    caso = casos[idx]
    st.progress(pos / len(orden), text=f"Caso {pos + 1} de {len(orden)}")
    st.subheader(caso["titulo"] + ("  🆕" if caso.get("nuevo") else ""))
    st.info(caso["enunciado"])

    res = st.session_state[f"{modo}_res"]
    if res is None:
        with st.expander("💡 Pista"):
            st.write(caso["pista"])
        with st.form(f"form_{modo}_{idx}"):
            elegido = {}
            for clave, campo in campos.items():
                elegido[clave] = st.selectbox(
                    campo["nombre"], campo["opciones"], index=None,
                    placeholder="Elige una opción…", key=f"{modo}_{idx}_{clave}",
                )
            enviar = st.form_submit_button("Comprobar ✅", type="primary")
        if enviar:
            if None in elegido.values():
                st.warning("Responde todos los apartados antes de comprobar.")
            else:
                aciertos = sum(elegido[k] in como_lista(caso["respuesta"][k]) for k in campos)
                perfecto = aciertos == len(campos)
                puntos = aciertos * PUNTOS_CAMPO + (BONUS_PERFECTO if perfecto else 0)
                registrar(aciertos, len(campos), puntos, perfecto)
                st.session_state[f"{modo}_ok"] += 1 if perfecto else 0
                st.session_state[f"{modo}_res"] = {
                    "elegido": elegido, "aciertos": aciertos,
                    "puntos": puntos, "perfecto": perfecto,
                }
                st.rerun()
    else:
        if res["perfecto"]:
            st.success(f"🎯 ¡Perfecto! {res['aciertos']}/{len(campos)} · +{res['puntos']} puntos")
        else:
            st.error(f"Has acertado {res['aciertos']}/{len(campos)} · +{res['puntos']} puntos")
        filas = []
        for clave, campo in campos.items():
            correcta = caso["respuesta"][clave]
            tu = res["elegido"][clave]
            filas.append({
                "Apartado": campo["nombre"],
                "Tu respuesta": tu,
                "Correcta": " / ".join(como_lista(correcta)),
                "": "✅" if tu in como_lista(correcta) else "❌",
            })
        st.dataframe(filas, hide_index=True)
        st.markdown(f"**Explicación:** {caso['justificacion']}")
        if pie:
            pie(caso)
        st.button("Siguiente caso ➡️", on_click=avanzar, args=(modo,), type="primary")


def pie_evaluacion(caso):
    """Muestra la acción preventiva y la matriz tras evaluar un riesgo."""
    nivel = caso["respuesta"]["nivel"]
    st.warning(f"**Acción preventiva ({nivel}):** {ACCIONES[nivel]}")
    with st.expander("Ver la matriz de evaluación"):
        filas = [{"Probabilidad": p, **{c: MATRIZ[p][i] for i, c in enumerate(CONS)}} for p in PROB]
        st.dataframe(filas, hide_index=True)


# ---------------------------------------------------------------------------
# Modo genérico: preguntas de opción múltiple (quiz, V/F, señales, reto)
# ---------------------------------------------------------------------------
def modo_opciones(modo, titulo, items, limite=None, descripcion="", cabecera=True):
    if cabecera:
        st.header(titulo)
        if descripcion:
            st.caption(descripcion)
    if not items:
        st.info("No hay preguntas en este bloque.")
        return
    preparar_cola(modo, len(items), limite)
    pos = st.session_state[f"{modo}_pos"]
    orden = st.session_state[f"{modo}_orden"]
    if pos >= len(orden):
        pantalla_final(modo, titulo)
        return

    idx = orden[pos]
    item = items[idx]
    st.progress(pos / len(orden), text=f"Pregunta {pos + 1} de {len(orden)}")
    if item.get("bloque") and modo == "reto":
        st.caption(f"Bloque: {item['bloque']}")
    st.markdown(f"### {item['enunciado']}")

    # Opciones barajadas de forma estable (no cambian al recargar la página)
    opciones = list(item["opciones"])
    texto_correcto = opciones[item["correcta"]]
    if item.get("barajar", True):
        random.Random(f"{modo}-{idx}").shuffle(opciones)

    res = st.session_state[f"{modo}_res"]
    if res is None:
        with st.form(f"form_{modo}_{pos}"):
            eleccion = st.radio("Tu respuesta", opciones, index=None, key=f"{modo}_radio_{pos}")
            enviar = st.form_submit_button("Comprobar ✅", type="primary")
        if enviar:
            if eleccion is None:
                st.warning("Elige una opción primero.")
            else:
                ok = eleccion == texto_correcto
                registrar(1 if ok else 0, 1, PUNTOS_PREGUNTA if ok else 0, ok)
                st.session_state[f"{modo}_ok"] += 1 if ok else 0
                st.session_state[f"{modo}_res"] = {"eleccion": eleccion, "ok": ok}
                st.rerun()
    else:
        if res["ok"]:
            st.success(f"✅ ¡Correcto! +{PUNTOS_PREGUNTA} puntos")
        else:
            st.error(f"❌ Has elegido «{res['eleccion']}». La correcta era: **{texto_correcto}**")
        st.info(item["explicacion"])
        st.button("Siguiente ➡️", on_click=avanzar, args=(modo,), type="primary")


def modo_quiz():
    st.header("🧠 Quiz de teoría")
    st.caption("Elige un bloque de la unidad o juega con todos a la vez.")
    bloque = st.selectbox("Bloque", list(BLOQUE_ID), key="quiz_bloque")
    items = QUIZ if bloque == "Todos los bloques" else [q for q in QUIZ if q["bloque"] == bloque]
    modo_opciones(BLOQUE_ID[bloque], f"Quiz · {bloque}", items, cabecera=False)


# ---------------------------------------------------------------------------
# Modo: ordena la secuencia
# ---------------------------------------------------------------------------
def modo_ordenar():
    modo = "ord"
    st.header("🔢 Ordena la secuencia")
    st.caption(f"Pon cada elemento en su posición correcta. {PUNTOS_CAMPO} puntos por posición + {BONUS_PERFECTO} de bonus si aciertas todas.")
    preparar_cola(modo, len(ORDENAR))
    pos = st.session_state[f"{modo}_pos"]
    orden = st.session_state[f"{modo}_orden"]
    if pos >= len(orden):
        pantalla_final(modo, "Ordena la secuencia")
        return

    idx = orden[pos]
    reto = ORDENAR[idx]
    pasos = reto["pasos"]
    n = len(pasos)
    barajados = list(pasos)
    random.Random(f"ord-{idx}").shuffle(barajados)

    st.progress(pos / len(orden), text=f"Reto {pos + 1} de {len(orden)}")
    st.subheader(reto["titulo"])
    st.info(reto["enunciado"])

    res = st.session_state[f"{modo}_res"]
    if res is None:
        with st.form(f"form_{modo}_{idx}"):
            elegido = [
                st.selectbox(f"Posición {i + 1}", barajados, index=None,
                             placeholder="Elige…", key=f"{modo}_{idx}_{i}")
                for i in range(n)
            ]
            enviar = st.form_submit_button("Comprobar ✅", type="primary")
        if enviar:
            if None in elegido:
                st.warning("Rellena todas las posiciones.")
            elif len(set(elegido)) < n:
                st.warning("No repitas elementos: cada uno va en una sola posición.")
            else:
                aciertos = sum(elegido[i] == pasos[i] for i in range(n))
                perfecto = aciertos == n
                puntos = aciertos * PUNTOS_CAMPO + (BONUS_PERFECTO if perfecto else 0)
                registrar(aciertos, n, puntos, perfecto)
                st.session_state[f"{modo}_ok"] += 1 if perfecto else 0
                st.session_state[f"{modo}_res"] = {"elegido": elegido, "aciertos": aciertos,
                                                    "puntos": puntos, "perfecto": perfecto}
                st.rerun()
    else:
        if res["perfecto"]:
            st.success(f"🎯 ¡Orden perfecto! {res['aciertos']}/{n} · +{res['puntos']} puntos")
        else:
            st.error(f"Has colocado bien {res['aciertos']}/{n} · +{res['puntos']} puntos")
        filas = [{"Posición": i + 1, "Tu respuesta": res["elegido"][i], "Correcto": pasos[i],
                  "": "✅" if res["elegido"][i] == pasos[i] else "❌"} for i in range(n)]
        st.dataframe(filas, hide_index=True)
        st.markdown(f"**Explicación:** {reto['explicacion']}")
        st.button("Siguiente reto ➡️", on_click=avanzar, args=(modo,), type="primary")


# ---------------------------------------------------------------------------
# Modo: autoevaluación del puesto con pantalla
# ---------------------------------------------------------------------------
def modo_pvd():
    st.header("🪑 Revisa tu puesto con pantalla (PVD)")
    st.caption("Autoevaluación de la Práctica 11: marca las medidas que SÍ cumples en tu puesto "
               "(en casa o en clase) y descubre cuáles te faltan.")
    grupo_actual = None
    for i, (grupo, medida) in enumerate(PVD_ITEMS):
        if grupo != grupo_actual:
            st.subheader(grupo)
            grupo_actual = grupo
        st.checkbox(medida, key=f"pvd_{i}")

    if st.button("Ver resultado", type="primary"):
        st.session_state["pvd_mostrar"] = True
    if st.session_state.get("pvd_mostrar"):
        faltan = [m for i, (_, m) in enumerate(PVD_ITEMS) if not st.session_state.get(f"pvd_{i}", False)]
        cumples = len(PVD_ITEMS) - len(faltan)
        pct = cumples / len(PVD_ITEMS)
        st.progress(pct, text=f"Cumples {cumples} de {len(PVD_ITEMS)} medidas ({pct * 100:.0f}%)")
        if not faltan:
            st.success("¡Puesto de trabajo ejemplar! 🏆")
        else:
            st.warning("Medidas que te faltan:")
            for m in faltan:
                st.write(f"- {m}")


# ---------------------------------------------------------------------------
# Inicio y chuleta
# ---------------------------------------------------------------------------
def pantalla_inicio():
    st.title("🦺 PRL Quest")
    st.subheader("Factores de riesgo laboral y su prevención")
    st.write(
        "Practica la **UD 3** jugando: identifica riesgos, elige el extintor adecuado, "
        "evalúa riesgos con el método del INSST y recuerda las cifras clave."
    )
    c1, c2, c3 = st.columns(3)
    c1.metric("Casos de riesgo", len(CASOS_RIESGO) + len(CASOS_FUEGO) + len(CASOS_EVAL))
    c2.metric("Retos de orden", len(ORDENAR))
    c3.metric("Preguntas", len(QUIZ) + len(VF_ITEMS) + len(SENALES))
    st.markdown(
        """
**Modos de juego**
- 🔺 **Identifica el riesgo**: ¿a qué familia y factor pertenece cada situación?
- 🔥 **Incendios y extintores**: tipo de fuego y extintor correcto.
- ⚖️ **Evalúa el riesgo**: probabilidad × consecuencias = nivel de riesgo.
- 🔢 **Ordena la secuencia**: pasos del extintor, daños de la corriente, escalera del ruido…
- 🚦 **Señales de seguridad**: tipo, forma y color.
- ✅ **Verdadero o falso** y 🧠 **Quiz de teoría** (por bloques).
- ⚡ **Reto mixto**: 15 preguntas al azar con nota final.
- 🪑 **Revisa tu puesto (PVD)**: autoevaluación de tu espacio de trabajo.
        """
    )
    st.info("👈 Elige un modo en el menú de la izquierda para empezar.")


# ---------------------------------------------------------------------------
# Programa principal
# ---------------------------------------------------------------------------
def main():
    iniciar_estado()
    modo = barra_lateral()
    if modo == MODOS[0]:
        pantalla_inicio()
    elif modo == MODOS[1]:
        modo_clasificador("riesgo", "🔺 Identifica el riesgo",
                          "Elige la familia y el factor de riesgo de cada situación.",
                          CASOS_RIESGO, CAMPOS_RIESGO)
    elif modo == MODOS[2]:
        modo_clasificador("fuego", "🔥 Incendios y extintores",
                          "Elige el tipo de fuego y el extintor adecuado.",
                          CASOS_FUEGO, CAMPOS_FUEGO)
    elif modo == MODOS[3]:
        modo_clasificador("eval", "⚖️ Evalúa el riesgo",
                          "Método INSST: indica probabilidad, consecuencias y nivel de riesgo.",
                          CASOS_EVAL, CAMPOS_EVAL, pie=pie_evaluacion)
    elif modo == MODOS[4]:
        modo_ordenar()
    elif modo == MODOS[5]:
        modo_opciones("senal", "🚦 Señales de seguridad", SENALES,
                      descripcion="Tipo, forma y color de las señales.")
    elif modo == MODOS[6]:
        modo_opciones("vf", "✅ Verdadero o falso", VF_ITEMS,
                      descripcion="Cuidado con las trampas.")
    elif modo == MODOS[7]:
        modo_quiz()
    elif modo == MODOS[8]:
        modo_opciones("reto", "⚡ Reto mixto", POOL_RETO, limite=TAM_RETO,
                      descripcion=f"{TAM_RETO} preguntas al azar de todos los bloques.")
    elif modo == MODOS[9]:
        modo_pvd()
    else:
        st.header("📖 Chuleta")
        st.markdown(CHULETA)


main()
