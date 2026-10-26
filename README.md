# 🦺 PRL Quest

Juego interactivo hecho con **Streamlit** para practicar la **UD 3 · Factores de riesgo y su prevención**
(Prevención de Riesgos Laborales): condiciones de seguridad, medioambientales, carga de trabajo,
organización del trabajo y evaluación de riesgos.

## 🎮 Modos de juego

| Modo | Qué hace |
|---|---|
| 🔺 Identifica el riesgo | 26 situaciones reales: elige la familia y el factor de riesgo. |
| 🔥 Incendios y extintores | 9 casos: tipo de fuego (A, B, C, D, eléctrico) y extintor adecuado. |
| ⚖️ Evalúa el riesgo | 12 casos con el método del INSST: probabilidad × consecuencias = nivel de riesgo, con su acción preventiva. |
| 🔢 Ordena la secuencia | Pasos del extintor, daños de la corriente, escalera del ruido, niveles de riesgo, cargas manuales. |
| 🚦 Señales de seguridad | 17 preguntas sobre tipo, forma y color. |
| ✅ Verdadero o falso | 30 afirmaciones con explicación (con trampas). |
| 🧠 Quiz de teoría | 47 preguntas, filtrables por bloque de la unidad. |
| ⚡ Reto mixto | 15 preguntas al azar y nota final. |
| 🪑 Revisa tu puesto (PVD) | Autoevaluación de tu puesto con pantalla (Práctica 11). |
| 📖 Chuleta | Cifras clave, matriz de riesgos y señales. |

Incluye puntos, racha 🔥, niveles (de *Becario* a *Inspector de Trabajo*) y precisión.

## 📁 Estructura

```
├── app.py            # Interfaz y lógica del juego
├── preguntas.py      # Banco de casos y preguntas (aquí se añade contenido)
├── requirements.txt  # Dependencias
└── README.md
```

## ▶️ Ejecutar en local

```bash
git clone https://github.com/TU_USUARIO/prl-quest.git
cd prl-quest
python -m venv .venv
source .venv/bin/activate      # En Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## ☁️ Publicarlo gratis (Streamlit Community Cloud)

1. Sube este proyecto a un repositorio **nuevo** de GitHub.
2. Entra en <https://share.streamlit.io> con tu cuenta de GitHub.
3. Pulsa **Create app**, elige el repositorio, rama `main` y archivo principal `app.py`.
4. Pulsa **Deploy** y comparte el enlace.

## ➕ Añadir tus propias preguntas

Edita `preguntas.py`:

- **Caso de riesgo / fuego / evaluación**: copia una llamada a `_riesgo(...)`, `_fuego(...)` o `_eval(...)`.
- **Verdadero/falso**: añade una tupla `("afirmación", True/False, "explicación")`.
- **Quiz**: copia una llamada a `_q(...)` (la respuesta correcta se escribe primero; el juego baraja las opciones).
- **Ordenar**: añade un diccionario a `ORDENAR` con los pasos en el orden correcto.

## 👥 Autores

Manuel Ramos Perca · Joel Flores Lopez
