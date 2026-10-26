"""
preguntas.py
Banco de contenido de "PRL Quest" (UD 3 · Factores de riesgo y su prevención).
Para añadir contenido basta con copiar un elemento de la lista correspondiente.
No hace falta tocar app.py.
"""

# ---------------------------------------------------------------------------
# Estructura de la unidad: familias de riesgo y factores
# ---------------------------------------------------------------------------
SEG, MED, CAR, ORG = (
    "Condiciones de seguridad",
    "Condiciones medioambientales",
    "Carga de trabajo",
    "Organización del trabajo",
)
FAMILIAS = [SEG, MED, CAR, ORG]

FACTORES = {  # factor -> familia a la que pertenece
    "Lugares de trabajo": SEG,
    "Maquinaria y herramientas": SEG,
    "Riesgo eléctrico": SEG,
    "Riesgo de incendio": SEG,
    "Ruido": MED,
    "Vibraciones": MED,
    "Radiaciones": MED,
    "Temperatura": MED,
    "Iluminación": MED,
    "Agentes químicos": MED,
    "Agentes biológicos": MED,
    "Carga física": CAR,
    "Carga mental": CAR,
    "Pantallas de visualización de datos": CAR,
    "Riesgos psicosociales": ORG,
}

CAMPOS_RIESGO = {
    "familia": {"nombre": "Familia de riesgos (apartado de la unidad)", "opciones": FAMILIAS},
    "factor": {"nombre": "Factor de riesgo", "opciones": list(FACTORES)},
}


def _riesgo(titulo, enunciado, factor, justificacion, pista):
    return {
        "titulo": titulo,
        "enunciado": enunciado,
        "respuesta": {"familia": FACTORES[factor], "factor": factor},
        "justificacion": justificacion,
        "pista": pista,
    }


CASOS_RIESGO = [
    _riesgo("📡 Instalador de telefonía",
            "Un instalador de telefonía móvil se sube a una escalera a 3 metros de altura.",
            "Lugares de trabajo",
            "Caída de personas a distinto nivel. Los trabajos en altura (más de 2 m) se tratan dentro de los lugares de trabajo.",
            "Piensa en caídas, suelos, barandillas y alturas."),
    _riesgo("🏭 Carretilla elevadora",
            "Un operario maneja palés con una carretilla elevadora en el almacén.",
            "Maquinaria y herramientas",
            "Una carretilla es una máquina: riesgo de golpes, atrapamientos y atropellos.",
            "¿Es un equipo de trabajo con motor?"),
    _riesgo("⚡ Cuadro eléctrico",
            "Un técnico manipula el cuadro eléctrico sin verificar que no hay tensión.",
            "Riesgo eléctrico",
            "Contacto con partes activas: hay que verificar la ausencia de tensión antes de operar.",
            "Mira los miliamperios."),
    _riesgo("💥 Almacén de explosivos",
            "En el almacén de una empresa de explosivos no se toman medidas ante la posible chispa "
            "por electricidad estática.",
            "Riesgo de incendio",
            "Una chispa es un foco de calor (energía de activación); hay que prevenir la electricidad estática en ambientes inflamables.",
            "Fíjate en el tetraedro del fuego."),
    _riesgo("🔨 La llave inglesa-martillo",
            "Un peón usa la llave inglesa como martillo mientras sujeta un clavo y se golpea los dedos.",
            "Maquinaria y herramientas",
            "Usar una herramienta no adecuada para la tarea es una de las causas de riesgo con herramientas.",
            "Herramienta equivocada para la tarea."),
    _riesgo("🪚 Máquina de corte sin CE",
            "Un trabajador, sin autorización, usa una máquina de corte sin marcado CE ni manual de "
            "instrucciones y se amputa dos dedos.",
            "Maquinaria y herramientas",
            "Toda máquina debe llevar marcado CE y manual en castellano; faltaban además resguardos y formación.",
            "Cortes y amputaciones: ¿con qué se producen?"),
    _riesgo("🥤 Diferencial puenteado",
            "En una embotelladora han puenteado el interruptor diferencial para que no salte y hay "
            "cables pelados con empalmes de cinta aislante.",
            "Riesgo eléctrico",
            "Se anula una protección contra contactos indirectos y hay partes activas accesibles (contacto directo).",
            "El diferencial corta la corriente ante una derivación."),
    _riesgo("🍅 Invernadero en verano",
            "Un trabajador recoge tomates en un invernadero de plástico donde en verano se llega a 45-50 ºC.",
            "Temperatura",
            "Estrés térmico por exceso de calor: puede producir golpe de calor, deshidratación y mareos.",
            "Agente físico del ambiente."),
    _riesgo("🥶 Aula a 15 ºC",
            "La calefacción de un aula se apaga por las tardes y la profesora mide 15 ºC.",
            "Temperatura",
            "Exceso de frío: la normativa fija unas condiciones mínimas (en trabajos sedentarios, 17-27 ºC).",
            "La normativa fija un rango de grados."),
    _riesgo("☢️ Auxiliar en radiología",
            "Una auxiliar de enfermería trabaja en radiología de un hospital.",
            "Radiaciones",
            "Rayos X: radiaciones ionizantes (cáncer profesional, efectos sobre la reproducción).",
            "Energía electromagnética que se propaga por el espacio."),
    _riesgo("🔊 Taller a 88 dB",
            "En un taller de una empresa industrial se mide un nivel de 88 dB.",
            "Ruido",
            "Supera los 85 dB: uso obligatorio de EPIs y medidas técnicas y organizativas (el límite es 87 dB).",
            "Se mide en decibelios."),
    _riesgo("🚧 Martillo neumático",
            "Un operario rompe el asfalto con un martillo neumático y nota pérdida de sensibilidad en los dedos.",
            "Vibraciones",
            "Transmisión mano-brazo: síndrome del dedo blanco o de Raynaud.",
            "El cuerpo se mueve alternativamente de un lado a otro."),
    _riesgo("🖨️ Imprenta con poca luz",
            "En una imprenta (exigencias visuales muy altas) solo hay 300 lux y los trabajadores sufren fatiga visual.",
            "Iluminación",
            "Para exigencias visuales muy altas la normativa pide 1.000 lux.",
            "La luz se mide en lux."),
    _riesgo("🎨 Pintor con disolventes",
            "Un pintor trabaja con disolventes sin ventilación y se marea y se queda somnoliento.",
            "Agentes químicos",
            "Los disolventes son anestésicos: producen somnolencia y pérdida de conocimiento; entran sobre todo por vía respiratoria.",
            "Contaminante en forma de líquido o vapor."),
    _riesgo("🩸 Extracción de sangre",
            "Una enfermera extrae sangre a un paciente.",
            "Agentes biológicos",
            "Riesgo de contagio por microorganismos (hepatitis B, SIDA…): medicina preventiva, EPIs e higiene.",
            "Virus, bacterias, hongos…"),
    _riesgo("💧 Depuradora de aguas",
            "Un operario limpia los lodos acumulados en el fondo de un tanque de una depuradora de aguas residuales.",
            "Agentes biológicos",
            "Contacto con material contaminado: riesgo de infección por microorganismos.",
            "El contagio puede ser por material contaminado."),
    _riesgo("🥩 Contractura en el matadero",
            "Un trabajador de un matadero sufre una contractura lumbar al levantar una caja de carne de cordero.",
            "Carga física",
            "Manipulación manual de cargas (esfuerzo y peso elevados): lumbalgias, hernias, contracturas.",
            "Esfuerzo muscular."),
    _riesgo("🧽 Limpieza de piezas en el suelo",
            "Un trabajador limpia piezas metálicas muy grandes directamente sobre el suelo, en cuclillas o inclinado.",
            "Carga física",
            "Posturas forzadas: producen trastornos musculoesqueléticos.",
            "Son las posturas lo que daña."),
    _riesgo("🥕 Ayudante de cocina",
            "Un ayudante de cocina pasa gran parte de la jornada pelando y cortando verduras con movimientos "
            "continuos de muñeca y le sale una tendinitis.",
            "Carga física",
            "Movimientos repetitivos: tendinitis, síndrome del túnel carpiano, epicondilitis.",
            "Mismos movimientos, una y otra vez."),
    _riesgo("🛫 Controlador aéreo",
            "Un controlador aéreo debe manejar mucha información y tomar decisiones correctas en poco tiempo.",
            "Carga mental",
            "Exigencias mentales: cantidad de información y tiempo disponible para decidir.",
            "Fatiga mental, no muscular."),
    _riesgo("☎️ Operadora de telefonía móvil",
            "Una operadora de una compañía móvil atiende un gran volumen de llamadas y de información.",
            "Carga mental",
            "Ejemplo típico de carga mental por volumen de información. Daños: cansancio, estrés, insomnio.",
            "Ejemplo del propio libro junto al controlador aéreo."),
    _riesgo("🖥️ Monitor delante de la ventana",
            "Una administrativa trabaja con el monitor justo delante de la ventana, con reflejos, y acaba con "
            "los ojos cansados y dolor de cuello.",
            "Pantallas de visualización de datos",
            "Fatiga visual y muscular típicas de las PVD. El ordenador debe ir en un lateral (90º) respecto a la luz.",
            "Usa un ordenador, y los ojos sufren."),
    _riesgo("🚪 Despacho sin compañeros",
            "Trasladan a un trabajador a un despacho sin compañeros y sin tener nada que hacer.",
            "Riesgos psicosociales",
            "Aislamiento social y tareas sin sentido: conductas de acoso laboral (mobbing).",
            "Se deriva de cómo está organizado el trabajo y las relaciones."),
    _riesgo("😶 Sin ilusión y agotada",
            "Una empleada está agotada emocionalmente, ha perdido el entusiasmo y trata con rechazo a los clientes.",
            "Riesgos psicosociales",
            "Burnout: insatisfacción laboral prolongada con agotamiento, baja realización personal y actitud negativa.",
            "Síndrome de «estar quemado»."),
    _riesgo("🔥 Soldadura junto a inflamables",
            "Se hacen trabajos de soldadura, con salto de chispas, al lado de productos inflamables mal almacenados.",
            "Riesgo de incendio",
            "Foco de calor (energía de activación) + combustible + comburente: riesgo de incendio.",
            "Combustible, comburente, energía de activación…"),
    _riesgo("🚪 Salida de emergencia bloqueada",
            "En un local la salida de evacuación está tapada con cajas y la puerta abre hacia dentro.",
            "Lugares de trabajo",
            "Las salidas de evacuación deben estar despejadas, señalizadas, con iluminación de seguridad y puertas que abran hacia fuera.",
            "Es una condición mínima del lugar de trabajo."),
]


# ---------------------------------------------------------------------------
# Incendios: clase de fuego y extintor
# ---------------------------------------------------------------------------
A_, B_, C_, D_, E_ = (
    "Clase A · Sólidos",
    "Clase B · Líquidos",
    "Clase C · Gaseosos",
    "Clase D · Metales",
    "Eléctrico (equipo con tensión)",
)
POLVO, CO2, METAL = (
    "Polvo polivalente ABC",
    "CO₂ (anhídrido carbónico)",
    "Extintor específico para metales",
)
CAMPOS_FUEGO = {
    "clase": {"nombre": "Tipo de fuego", "opciones": [A_, B_, C_, D_, E_]},
    "extintor": {"nombre": "Extintor adecuado", "opciones": [POLVO, CO2, METAL]},
}


def _fuego(titulo, enunciado, clase, extintor, justificacion, pista):
    return {
        "titulo": titulo, "enunciado": enunciado,
        "respuesta": {"clase": clase, "extintor": extintor},
        "justificacion": justificacion, "pista": pista,
    }


CASOS_FUEGO = [
    _fuego("🗑️ Papelera ardiendo", "Una papelera con papeles y cartón empieza a arder.",
           A_, POLVO,
           "Combustible sólido que deja brasas. El CO₂ no apaga las brasas de tipo A; el polvo ABC sí.",
           "Madera, cartón y tejidos."),
    _fuego("🔌 Cuadro eléctrico", "Hay un incendio en un cuadro eléctrico.",
           E_, CO2,
           "Con electricidad hay que usar CO₂: el polvo podría conducir la corriente.",
           "Presencia de electricidad."),
    _fuego("💻 Equipo informático", "De un equipo informático sale humo y se ven llamas.",
           E_, CO2,
           "En equipos electrónicos/informáticos se usa CO₂ (el polvo dañaría los componentes).",
           "Evita ensuciar los componentes."),
    _fuego("⛽ Gasolina en el taller", "Se produce un fuego en un taller mecánico provocado por la gasolina.",
           B_, [POLVO, CO2],
           "Líquido inflamable (clase B): sirven el polvo ABC y el CO₂.",
           "Gasolina y disolventes."),
    _fuego("🔩 Almacén de metales", "Un almacén de materias primas metálicas: hierro, sodio, etc., se incendia.",
           D_, METAL,
           "Metales combustibles: para metales se usan extintores específicos para cada metal.",
           "Sodio, potasio…"),
    _fuego("🛢️ Bombona de butano", "Se incendia una bombona de gas butano.",
           C_, POLVO,
           "Gases inflamables (clase C): el polvo polivalente sirve para A, B y C.",
           "Butano y propano."),
    _fuego("🪵 Palés de madera", "Se prende una pila de palés de madera en el patio.",
           A_, POLVO,
           "Sólido que deja brasas: el polvo ABC es el más habitual.",
           "Sólido con brasas."),
    _fuego("🖥️ Sala de servidores", "Hay llamas en un rack de servidores de una sala de ordenadores.",
           E_, CO2,
           "Equipos informáticos con tensión: CO₂, que no deja residuo ni conduce.",
           "Piensa en la electricidad."),
    _fuego("🎨 Disolventes derramados", "Se prenden unos disolventes derramados en el taller de pintura.",
           B_, [POLVO, CO2],
           "Líquidos inflamables: clase B.",
           "Sustancias líquidas inflamables."),
]


# ---------------------------------------------------------------------------
# Evaluación de riesgos (método INSST)
# ---------------------------------------------------------------------------
PROB = ["Baja", "Media", "Alta"]
CONS = ["Ligeramente dañinas", "Dañinas", "Extremadamente dañinas"]
NIVELES_RIESGO = ["Trivial", "Tolerable", "Moderado", "Importante", "Intolerable"]

MATRIZ = {
    "Baja": ["Trivial", "Tolerable", "Moderado"],
    "Media": ["Tolerable", "Moderado", "Importante"],
    "Alta": ["Moderado", "Importante", "Intolerable"],
}
ACCIONES = {
    "Trivial": "No requiere acción específica.",
    "Tolerable": "No se necesita mejorar la acción preventiva, aunque se pueden considerar mejoras que no supongan "
                 "una carga económica importante. Se requieren comprobaciones periódicas.",
    "Moderado": "Se deben hacer esfuerzos para reducir el riesgo, invirtiendo en las medidas precisas, "
                "que deben implantarse en un periodo de tiempo determinado.",
    "Importante": "No debe comenzarse el trabajo hasta que se haya reducido el riesgo. "
                  "Puede que se precisen recursos considerables para controlarlo.",
    "Intolerable": "No se debe continuar ni comenzar el trabajo hasta que se reduzca el riesgo.",
}

CAMPOS_EVAL = {
    "prob": {"nombre": "Probabilidad", "opciones": PROB},
    "cons": {"nombre": "Consecuencias", "opciones": CONS},
    "nivel": {"nombre": "Nivel de riesgo resultante", "opciones": NIVELES_RIESGO},
}


def _eval(titulo, enunciado, prob, cons, pista, nuevo=False):
    nivel = MATRIZ[prob][CONS.index(cons)]
    return {
        "titulo": titulo, "enunciado": enunciado,
        "respuesta": {"prob": prob, "cons": cons, "nivel": nivel},
        "justificacion": f"Probabilidad {prob.lower()} + consecuencias {cons.lower()} = riesgo {nivel.lower()}.",
        "pista": pista, "nuevo": nuevo,
    }


CASOS_EVAL = [
    _eval("🧴 Pegamentos tóxicos",
          "Sustancias tóxicas (pegamentos). La probabilidad es media y las consecuencias son ligeramente dañinas.",
          "Media", "Ligeramente dañinas", "Cruza la fila «media» con la columna «ligeramente dañinas»."),
    _eval("⚙️ Golpes con partes móviles",
          "Riesgos mecánicos, sobre todo golpes con partes en movimiento de la máquina: probabilidad media y consecuencias dañinas.",
          "Media", "Dañinas", "Fila media, columna dañinas."),
    _eval("🔥 Quemaduras por soldadura",
          "Quemaduras por soldadura. La probabilidad es alta por la ausencia de protección y las consecuencias son dañinas.",
          "Alta", "Dañinas", "Fila alta, columna dañinas."),
    _eval("🩹 Pequeño corte",
          "Un pequeño corte ligeramente dañino y cuya probabilidad de que ocurra es baja.",
          "Baja", "Ligeramente dañinas", "La combinación más suave de la tabla."),
    _eval("🍳 Quemadura en la cocina",
          "Una quemadura con el fuego de la cocina, que es dañina, y cuya probabilidad de que ocurra es media.",
          "Media", "Dañinas", "Quemaduras = consecuencia dañina."),
    _eval("🧪 Intoxicación con benceno",
          "Una intoxicación con benceno, que es extremadamente dañina, con probabilidad media de que ocurra.",
          "Media", "Extremadamente dañinas", "Intoxicaciones graves = extremadamente dañinas."),
    _eval("🏗️ Andamio sin arnés",
          "Un operario trabaja a 6 metros de altura sobre un andamio sin barandilla ni arnés, todos los días. "
          "Puede morir si cae.",
          "Alta", "Extremadamente dañinas", "Un accidente mortal es lo más grave.", True),
    _eval("⚡ Cuadro en tensión",
          "Se trabaja a diario en un cuadro eléctrico sin verificar la ausencia de tensión. Un contacto puede ser mortal.",
          "Alta", "Extremadamente dañinas", "Probabilidad alta + consecuencia mortal.", True),
    _eval("👀 Cansancio ocular",
          "Una persona de oficina tiene alguna vez irritación de ojos leve, que mejora con un descanso; "
          "la probabilidad de que ocurra es baja.",
          "Baja", "Ligeramente dañinas", "Irritación de ojos y dolores de cabeza son ligeramente dañinos.", True),
    _eval("🖐️ Atrapamiento sin resguardo",
          "En una prensa sin resguardos, la probabilidad de atrapamiento es media y puede causar una amputación.",
          "Media", "Extremadamente dañinas", "Amputaciones = extremadamente dañinas.", True),
    _eval("💦 Suelo mojado señalizado",
          "Un pasillo se moja a veces, pero está señalizado y se limpia enseguida (probabilidad baja). "
          "Un resbalón podría causar un esguince (consecuencias dañinas).",
          "Baja", "Dañinas", "Baja probabilidad + consecuencia dañina.", True),
    _eval("💻 Dolor de cabeza por pantalla",
          "Jornadas largas ante el ordenador sin pausas: dolores de cabeza leves con probabilidad alta.",
          "Alta", "Ligeramente dañinas", "Ligeramente dañino, pero ocurre muy a menudo.", True),
]


# ---------------------------------------------------------------------------
# Ordena la secuencia (el orden de la lista ES el orden correcto)
# ---------------------------------------------------------------------------
ORDENAR = [
    {
        "titulo": "🧯 Usar un extintor, paso a paso",
        "enunciado": "Ordena los 5 pasos para usar correctamente un extintor.",
        "pasos": [
            "Conocer el tipo de extintor adecuado",
            "Descolgar el extintor y dejarlo en vertical en el suelo",
            "Quitar la anilla de seguridad",
            "Hacer una descarga de prueba al aire, con el viento no en contra",
            "Dirigir el chorro a la base de las llamas, en zig-zag, a 1 metro",
        ],
        "explicacion": "Primero se elige el extintor correcto; después se prepara, se quita la anilla, se prueba la descarga y se ataca la base del fuego.",
    },
    {
        "titulo": "⚡ Daños de la electricidad",
        "enunciado": "Ordena de menor a mayor intensidad (mA / A) los efectos de la corriente en el cuerpo humano.",
        "pasos": [
            "1 a 3 mA: cosquilleos",
            "5 a 10 mA: contracciones musculares y calambres",
            "10 mA: tetanización (no puedes soltarte)",
            "25 mA: parada cardio-respiratoria",
            "60-75 mA: fibrilación ventricular",
            "1 A - 5 A: paro cardiaco reversible y quemaduras graves",
        ],
        "explicacion": "A más intensidad, más daño. Además influyen el tiempo de contacto y la trayectoria (corazón, tórax o cerebro).",
    },
    {
        "titulo": "🔊 La escalera del ruido",
        "enunciado": "Ordena de menor a mayor nivel sonoro.",
        "pasos": [
            "Conversación normal (≈ 55 dB)",
            "Empieza a ser perjudicial: medidas técnicas y EPIs disponibles (80 dB)",
            "Uso obligatorio de EPIs (85 dB)",
            "Límite que nunca debe superarse (87 dB de media)",
            "Umbral del dolor (120 dB)",
            "Límite de pico que nunca debe superarse (140 dB)",
        ],
        "explicacion": "80 dB: medidas y EPIs voluntarios · 85 dB: EPIs obligatorios · 87 dB: límite máximo de media · 140 dB: límite de pico.",
    },
    {
        "titulo": "🚦 Niveles de riesgo",
        "enunciado": "Ordena los niveles de riesgo del método INSST de menos a más grave.",
        "pasos": ["Trivial", "Tolerable", "Moderado", "Importante", "Intolerable"],
        "explicacion": "Trivial → no hay que hacer nada · Intolerable → no se puede ni empezar ni continuar el trabajo.",
    },
    {
        "titulo": "📦 Límites de carga manual",
        "enunciado": "Ordena de menor a mayor los pesos relacionados con la manipulación manual de cargas.",
        "pasos": [
            "Aparece riesgo a partir de 3 kg",
            "15 kg: recomendado para mujeres, jóvenes y personas de edad avanzada",
            "25 kg: carga máxima general",
            "40 kg: trabajadores entrenados y de forma esporádica",
        ],
        "explicacion": "3 kg es el umbral de riesgo; 25 kg el máximo general; 15 kg para colectivos sensibles y 40 kg en casos entrenados y esporádicos.",
    },
]


# ---------------------------------------------------------------------------
# Verdadero o falso
# ---------------------------------------------------------------------------
VERDADERO_FALSO = [
    ("La señalización elimina los riesgos laborales.", False,
     "La señalización es una técnica complementaria: estimula nuestros sentidos para apercibirnos del peligro, pero no elimina el riesgo."),
    ("Los trabajos en altura son los que se realizan a más de 2 metros de altura.", True,
     "Esa es la definición que da el libro dentro de los lugares de trabajo."),
    ("Las puertas de un lugar de trabajo deben tener una anchura mínima de 80 cm.", True,
     "Puertas: 80 cm. Escaleras y pasillos: 1 metro."),
    ("Las puertas de las salidas de evacuación deben poder abrirse hacia dentro.", False,
     "Deben poder abrirse hacia fuera, estar despejadas, señalizadas y con iluminación de seguridad."),
    ("Con 10 mA se produce tetanización: no puedes separarte voluntariamente del contacto.", True,
     "La tetanización es un agarrotamiento que impide soltarse."),
    ("Los interruptores diferenciales domésticos suelen saltar con 30 mA.", True,
     "Cortan la corriente cuando hay una derivación."),
    ("Un extintor de CO₂ apaga bien las brasas de los fuegos de tipo A.", False,
     "El CO₂ es útil para fuegos tipo B y no apaga las brasas de tipo A (sólidos)."),
    ("En equipos eléctricos o informáticos conviene usar CO₂ en vez de polvo.", True,
     "El polvo podría conducir la corriente y dañar los componentes."),
    ("El oxígeno del aire es el comburente del tetraedro del fuego.", True,
     "El tetraedro: combustible, comburente, energía de activación y reacción en cadena."),
    ("A partir de 80 dB y hasta 85 dB, la empresa debe ofrecer protectores, pero su uso es voluntario.", True,
     "A partir de 85 dB el uso de los EPIs es obligatorio."),
    ("El límite de ruido que nunca debe superarse es de 87 dB de media o 140 dB de pico.", True,
     "A partir de 80 dB de media (135 dB de pico) hay que tomar medidas técnicas y organizativas."),
    ("El ruido de pico o impacto se mide con un sonómetro.", False,
     "Se mide con analizadores de impactos en dB(C). El sonómetro es para el ruido continuo; el dosímetro, para el discontinuo."),
    ("El síndrome del dedo blanco o de Raynaud está relacionado con las vibraciones mano-brazo.", True,
     "Se pierde sensibilidad y funcionalidad en los dedos."),
    ("Las radiaciones ultravioletas e infrarrojas son radiaciones ionizantes.", False,
     "Son no ionizantes (como el radar, las microondas o el láser). Ionizantes: rayos X, alfa, beta, gamma."),
    ("En trabajos sedentarios, como en oficinas, la temperatura debe estar entre 17 y 27 ºC.", True,
     "En trabajos ligeros, entre 14 y 25 ºC."),
    ("La principal vía de entrada de los contaminantes químicos es la digestiva.", False,
     "Es la vía respiratoria, aunque también pueden entrar por la vía digestiva o por la piel y heridas."),
    ("El amianto es un contaminante neumoconiótico.", True,
     "Se almacena en los pulmones provocando problemas e incluso la muerte."),
    ("Para los agentes biológicos del grupo 4 existen tratamientos eficaces.", False,
     "En el grupo 4 (ébola, viruela) no hay tratamientos eficaces."),
    ("La carga máxima manual general es de 25 kg.", True,
     "15 kg para mujeres, jóvenes y personas de edad avanzada; hasta 40 kg en trabajadores entrenados y de forma esporádica."),
    ("La pantalla del ordenador debe situarse por encima del nivel de los ojos.", False,
     "Nunca por encima del nivel de los ojos, para que el cuello no tenga que flexionarse hacia arriba."),
    ("El ordenador debe colocarse en un lateral de la habitación, a 90º de la ventana.", True,
     "Así los ojos no tienen que adaptarse a la luz ni se refleja la luz en la pantalla."),
    ("El burnout es una insatisfacción laboral que se prolonga en el tiempo.", True,
     "Genera agotamiento emocional, baja realización personal y actitud negativa hacia los clientes."),
    ("El estrés laboral es el desequilibrio entre las exigencias del trabajo y los recursos del trabajador.", True,
     "Depende tanto del trabajo como de la capacidad de la persona."),
    ("El mobbing solo incluye agresiones físicas.", False,
     "Incluye ataques organizativos, aislamiento social, ataques a la vida privada, rumores, insultos…"),
    ("Probabilidad baja y consecuencias ligeramente dañinas dan un riesgo trivial.", True,
     "Es la combinación más suave de la tabla del INSST."),
    ("Ante un riesgo intolerable se puede seguir trabajando mientras se prepara la mejora.", False,
     "No se debe continuar ni comenzar el trabajo hasta que se reduzca el riesgo."),
    ("Toda máquina debe llevar marcado CE y un manual de instrucciones en castellano.", True,
     "El marcado CE indica que cumple la normativa de seguridad."),
    ("La evaluación de riesgos se hace una sola vez, al inicio de la actividad.", False,
     "Se hace por cada puesto al inicio y periódicamente, siempre que haya cambios, daños o insuficiencia de las medidas."),
    ("En el acoso sexual es decisiva la intención del autor de la conducta.", False,
     "Es irrelevante: lo importante es que la conducta sea no deseada, no recíproca y molesta para quien la recibe."),
    ("El uso del amianto se prohibió definitivamente en España en 2001.", True,
     "Se limitó en 1984 y 1993, pero no se prohibió definitivamente hasta 2001."),
]


# ---------------------------------------------------------------------------
# Quiz de teoría. Se escribe la correcta primero; el juego baraja las opciones.
# ---------------------------------------------------------------------------
BLOQUES = [
    "Condiciones de seguridad",
    "Condiciones medioambientales",
    "Carga de trabajo",
    "Organización del trabajo",
    "Evaluación de riesgos",
    "Educación en valores y entorno laboral",
]
BLOQUE_SENALES = "Señalización"


def _q(bloque, enunciado, correcta, incorrectas, explicacion):
    return {
        "bloque": bloque, "enunciado": enunciado,
        "opciones": [correcta] + list(incorrectas), "correcta": 0,
        "explicacion": explicacion,
    }


QUIZ = [
    # --- Condiciones de seguridad ---
    _q(BLOQUES[0], "¿Qué altura mínima deben tener los espacios de trabajo en general?",
       "3 metros", ["2 metros", "2,5 metros", "4 metros"],
       "3 m de altura (2,5 m en locales comerciales y despachos), 2 m² libres y 10 m³ de volumen por trabajador."),
    _q(BLOQUES[0], "¿Cuál es la altura mínima de una barandilla?",
       "90 cm", ["50 cm", "1,5 m", "2 m"],
       "90 cm, con protección inferior para impedir el paso."),
    _q(BLOQUES[0], "¿Cuál de estas es una medida de protección colectiva frente a máquinas?",
       "Usar resguardos para no entrar en contacto con la máquina",
       ["Llevar ropa holgada", "Quitar el marcado CE", "Ignorar el manual de instrucciones"],
       "También pantallas contra proyecciones y dispositivos como células fotoeléctricas o el doble mando."),
    _q(BLOQUES[0], "¿Qué dispositivo de seguridad detiene la máquina al detectar la presencia humana?",
       "Célula fotoeléctrica", ["Doble mando", "Ropa ajustada", "Marcado CE"],
       "El doble mando obliga a usar ambas manos; la célula fotoeléctrica detiene la máquina."),
    _q(BLOQUES[0], "Un contacto eléctrico indirecto se produce cuando…",
       "se toca un dispositivo que normalmente no conduce la electricidad pero, por un fallo, sí lo hace",
       ["se tocan cables o enchufes en tensión", "te acercas a más de 1.000 V sin tocar", "usas guantes aislantes"],
       "Ej.: tocar la parte exterior de una lavadora con una derivación interna."),
    _q(BLOQUES[0], "¿Qué intensidad puede producir fibrilación ventricular si pasa por el corazón?",
       "60-75 mA", ["1-3 mA", "10 mA", "25 mA"],
       "El corazón se vuelve anárquico y no bombea la sangre de forma regular."),
    _q(BLOQUES[0], "¿Para qué sirve la toma de tierra?",
       "Para que la corriente se derive hacia tierra en lugar de circular por el cuerpo",
       ["Para aumentar la tensión", "Para cortar la luz", "Para señalizar la instalación"],
       "Son cables con poca resistencia que van a tierra: la electricidad prefiere ese camino."),
    _q(BLOQUES[0], "¿Qué factor es el más importante en los daños de la electricidad?",
       "El nivel de intensidad (mA)", ["El color del cable", "La hora del día", "La altura del trabajador"],
       "También influyen el tiempo de contacto y la trayectoria de la corriente."),
    _q(BLOQUES[0], "¿Cuál NO es un elemento del tetraedro del fuego?",
       "Agua", ["Combustible", "Comburente", "Reacción en cadena"],
       "Los 4 elementos: combustible, comburente, energía de activación y reacción en cadena."),
    _q(BLOQUES[0], "Los fuegos de líquidos como la gasolina son de clase…",
       "B", ["A", "C", "D"],
       "A sólidos · B líquidos · C gaseosos · D metales."),
    _q(BLOQUES[0], "¿Qué extintor es el más habitual y sirve para fuegos A, B y C?",
       "Polvo polivalente (ABC)", ["CO₂", "Específico de metales", "Hidrocarburos halogenados"],
       "Los hidrocarburos halogenados están en desuso por perjudicar la capa de ozono."),
    _q(BLOQUES[0], "¿Cuál de estas es una causa de riesgo con herramientas?",
       "Abandonarlas en lugares peligrosos", ["Mantenerlas ordenadas", "Revisarlas periódicamente", "Formar a los trabajadores"],
       "Causas: herramientas no adecuadas, abandono, transporte inadecuado y falta de mantenimiento."),
    # --- Condiciones medioambientales ---
    _q(BLOQUES[1], "¿A partir de qué nivel sonoro empieza a ser perjudicial el ruido para la salud?",
       "80 dB", ["40 dB", "55 dB", "120 dB"],
       "Una conversación normal ronda los 55 dB; el umbral del dolor está en 120 dB."),
    _q(BLOQUES[1], "¿Con qué se mide el ruido continuo?",
       "Con sonómetros", ["Con dosímetros", "Con analizadores de impactos", "Con luxómetros"],
       "Dosímetros: ruido discontinuo. Analizadores de impactos en dB(C): ruido de pico."),
    _q(BLOQUES[1], "Si se superan los 85 dB, ¿cada cuánto se hacen audiometrías?",
       "Cada 3 años", ["Cada año", "Cada 5 años", "Nunca"],
       "Cada 5 años si se superan los 80 dB, y cada 3 si se superan los 85 dB."),
    _q(BLOQUES[1], "¿Qué medida frente al ruido es prioritaria por ir dirigida al foco?",
       "Sustituir la maquinaria ruidosa por otra menos ruidosa",
       ["Entregar tapones", "Colocar pantallas", "Hacer audiometrías"],
       "Actuar sobre el foco es mejor que actuar sobre el medio o sobre el trabajador."),
    _q(BLOQUES[1], "La transmisión de vibraciones al cuerpo entero se da al…",
       "conducir camiones, autobuses o vehículos de obras públicas",
       ["usar una motosierra", "usar un martillo neumático", "manejar una pulidora"],
       "Mano-brazo: herramientas. Cuerpo entero: vehículos. Daños: lumbalgias, hernias, mareos."),
    _q(BLOQUES[1], "Los rayos X son un ejemplo de radiación…",
       "ionizante", ["no ionizante", "infrarroja", "láser"],
       "Las ionizantes pueden causar muerte celular, cáncer y modificar el código genético."),
    _q(BLOQUES[1], "¿Qué EPI se usa frente a las radiaciones en trabajos de soldadura?",
       "Pantallas faciales", ["Tapones", "Mascarillas de polvo", "Guantes de nitrilo"],
       "En sanidad se usa protección frente a rayos X."),
    _q(BLOQUES[1], "¿A qué temperatura interna se produce el golpe de calor?",
       "42-44 ºC", ["37 ºC", "35 ºC", "30 ºC"],
       "El organismo humano mantiene 37 ºC; por debajo de 35 ºC hay hipotermia."),
    _q(BLOQUES[1], "¿Cuántos lux se recomiendan como ejemplo en una oficina?",
       "300 lux", ["100 lux", "1.000 lux", "10 lux"],
       "Almacén: 100 lux · oficina: 300 lux · imprenta: 1.000 lux."),
    _q(BLOQUES[1], "Los disolventes son agentes químicos…",
       "anestésicos", ["irritantes", "cancerígenos", "neumoconióticos"],
       "Producen somnolencia y pérdida del conocimiento, lo que puede causar accidentes laborales."),
    _q(BLOQUES[1], "La higiene industrial consiste en…",
       "recoger muestras, llevarlas al laboratorio y compararlas con los valores límite de exposición",
       ["etiquetar los productos", "lavarse las manos", "eliminar todo contaminante"],
       "Se basa en que «la dosis hace el veneno»."),
    _q(BLOQUES[1], "Tuberculosis, hepatitis B y brucelosis son agentes biológicos del grupo…",
       "3", ["1", "2", "4"],
       "Grupo 3: enfermedad grave con probabilidad de propagación, con tratamiento."),
    _q(BLOQUES[1], "¿Cuánto tiempo se debe disponer para el cambio de ropa e higiene personal ante agentes biológicos?",
       "10 minutos", ["2 minutos", "1 hora", "No hace falta"],
       "Además: no mezclar la ropa de trabajo con la personal y no beber ni comer en el lugar de trabajo."),
    # --- Carga de trabajo ---
    _q(BLOQUES[2], "¿A partir de qué peso aparece riesgo en la manipulación manual de cargas?",
       "3 kg", ["1 kg", "10 kg", "25 kg"],
       "La carga máxima general es de 25 kg."),
    _q(BLOQUES[2], "¿Qué carga máxima se recomienda para mujeres, jóvenes y personas de edad avanzada?",
       "15 kg", ["10 kg", "18 kg", "25 kg"],
       "En trabajadores entrenados y de forma esporádica puede llegar a 40 kg."),
    _q(BLOQUES[2], "Al manipular una carga correctamente hay que…",
       "doblar las rodillas y mantener la espalda recta", ["doblar la espalda con las piernas rectas", "juntar los pies al máximo", "alejar la carga del cuerpo"],
       "También: pies firmes y separados, sujetarla firme y cargarla cerca del cuerpo."),
    _q(BLOQUES[2], "El síndrome del túnel carpiano aparece por…",
       "movimientos repetitivos de la muñeca", ["ruido excesivo", "temperaturas bajas", "radiaciones"],
       "Antiguamente «enfermedad del escribiente»; hoy puede aparecer por el uso del ratón."),
    _q(BLOQUES[2], "Un ejemplo típico de trabajo con carga mental elevada es…",
       "un controlador aéreo", ["un peón de obra", "un jardinero", "un mozo de almacén"],
       "Mucha información y decisiones correctas en poco tiempo. Daños: cansancio, estrés, insomnio…"),
    _q(BLOQUES[2], "¿A qué altura deben estar la mesa y el teclado respecto al suelo?",
       "60-75 cm", ["30-40 cm", "90-100 cm", "Da igual"],
       "Además: la mesa debe permitir apoyar los antebrazos y el ratón debe tener reposamuñecas."),
    _q(BLOQUES[2], "¿Cada cuánto se recomienda una pausa de 10 minutos ante pantallas?",
       "Cada 2 horas", ["Cada 15 minutos", "Cada 8 horas", "Nunca"],
       "También conviene alternar con otras tareas en trabajos monótonos."),
    _q(BLOQUES[2], "La iluminación recomendada ante una pantalla es de unos…",
       "300 lux", ["50 lux", "1.000 lux", "5.000 lux"],
       "Y evitar reflejos, deslumbramientos y el parpadeo de los caracteres."),
    # --- Organización del trabajo ---
    _q(BLOQUES[3], "El burnout provoca 3 efectos. ¿Cuál NO es uno de ellos?",
       "Exceso de entusiasmo", ["Agotamiento emocional", "Baja realización personal", "Actitud negativa con los clientes"],
       "Es el síndrome de «estar quemado»."),
    _q(BLOQUES[3], "La insatisfacción laboral nace de…",
       "la diferencia entre las expectativas y la realidad del puesto", ["tener mucho tiempo libre", "cobrar demasiado", "trabajar en equipo"],
       "Depende también de la importancia que el trabajador da a esa diferencia."),
    _q(BLOQUES[3], "Tratar a una persona como si no existiera es una conducta de…",
       "ataque con aislamiento social (mobbing)", ["ataque a la vida privada", "agresión física", "ataque organizativo"],
       "Otras: prohibir que hablen con la víctima o rehusar la comunicación por gestos."),
    _q(BLOQUES[3], "¿Cuál es una medida preventiva psicosocial?",
       "Rotación de puestos y autonomía en la toma de decisiones", ["Jornadas más largas", "Estilo autoritario", "Eliminar descansos"],
       "También: pausas, turnos conocidos con antelación, salario justo, liderazgo participativo y formación."),
    _q(BLOQUES[3], "La personalidad tipo A es la del trabajador…",
       "orientado a la tarea y perfeccionista", ["tranquilo y relajado", "sin formación", "que evita el trabajo"],
       "Es una característica del trabajador que puede interactuar con las condiciones de la empresa."),
    # --- Evaluación de riesgos ---
    _q(BLOQUES[4], "El método INSST combina dos características de cada riesgo. ¿Cuáles?",
       "Probabilidad y consecuencias", ["Coste y duración", "Edad y sexo", "Frecuencia y color"],
       "Su combinación da el nivel de riesgo."),
    _q(BLOQUES[4], "Probabilidad media y consecuencias dañinas dan un riesgo…",
       "Moderado", ["Trivial", "Importante", "Intolerable"],
       "Se deben hacer esfuerzos para reducir el riesgo en un tiempo determinado."),
    _q(BLOQUES[4], "Ante un riesgo importante…",
       "no debe comenzarse el trabajo hasta reducir el riesgo", ["no hace falta actuar", "basta con comprobaciones periódicas", "se puede continuar igual"],
       "Si es intolerable, no se debe ni continuar ni comenzar el trabajo."),
    _q(BLOQUES[4], "¿Cuándo se debe realizar la evaluación de riesgos?",
       "En cada puesto al inicio de la actividad y periódicamente ante cambios o daños", ["Solo una vez en la vida", "Solo si hay una inspección", "Solo en la industria"],
       "Principio: cuando no se pueden evitar los riesgos, se evalúan."),
    # --- Educación en valores y entorno laboral ---
    _q(BLOQUES[5], "¿Por qué se popularizó el amianto en la década de los 50?",
       "Era abundante, barato, buen aislante térmico y soportaba temperaturas extremas",
       ["Era muy caro y exclusivo", "Era ecológico", "Era un nuevo tipo de plástico"],
       "Se usó en construcción naval y en tejados y tuberías de edificios; su uso en España no se prohibió definitivamente hasta 2001."),
    _q(BLOQUES[5], "¿Cómo daña el amianto al organismo?",
       "Sus fibras se inhalan y colonizan los pulmones", ["Se absorbe por la piel y causa quemaduras", "Daña la vista", "Provoca sordera"],
       "Causa enfisema, cáncer de pleura o peritoneo, y puede ser mortal."),
    _q(BLOQUES[5], "Un mito sobre el acoso sexual es que…",
       "las víctimas son siempre mujeres", ["existe en todos los sectores", "es una conducta no deseada", "puede ser verbal"],
       "Otro mito: que existen víctimas «típicas» relacionadas con los cánones de belleza."),
    _q(BLOQUES[5], "¿Qué distingue el acoso sexual del flirteo?",
       "Que la conducta es no deseada, no recíproca y se impone", ["Que la hace un superior", "Que se hace en horario de trabajo", "La intención del autor"],
       "La atención sexual es acoso cuando se convierte en desagradable para quien la recibe."),
    _q(BLOQUES[5], "Según la OIT, ¿qué mujeres tienen más probabilidad de ser acosadas?",
       "Viudas, separadas, divorciadas, con contratos irregulares o en trabajos muy masculinizados", ["Solo las directivas", "Las que tienen estudios superiores", "Las que tienen empleo estable"],
       "Existe relación con la dependencia económica y la vulnerabilidad general."),
]


# ---------------------------------------------------------------------------
# Señalización (preguntas de opción múltiple con emoji como apoyo visual)
# ---------------------------------------------------------------------------
TIPOS_SENAL = ["Advertencia", "Prohibición", "Obligación", "Salvamento o socorro", "Lucha contra incendios"]


def _senal(enunciado, correcta, explicacion):
    otras = [t for t in TIPOS_SENAL if t != correcta]
    return {"bloque": BLOQUE_SENALES, "enunciado": enunciado,
            "opciones": [correcta] + otras, "correcta": 0, "explicacion": explicacion}


SENALES = [
    _senal("⚠️ Triángulo amarillo con un signo de exclamación («peligro en general»). ¿Qué tipo de señal es?",
           "Advertencia", "Las señales de advertencia son triangulares, de color amarillo (amarillo anaranjado)."),
    _senal("🚭 Círculo con borde rojo y un cigarrillo tachado. ¿Qué tipo de señal es?",
           "Prohibición", "Las de prohibición son circulares y de color rojo."),
    _senal("⛑️ Círculo azul con un casco. ¿Qué tipo de señal es?",
           "Obligación", "Las de obligación son circulares y de color azul (aquí, protección obligatoria de la cabeza)."),
    _senal("🧯 Cuadrado rojo con un extintor. ¿Qué tipo de señal es?",
           "Lucha contra incendios", "Rectangulares o cuadradas y de color rojo."),
    _senal("🚑 Cuadrado verde con una cruz blanca (primeros auxilios). ¿Qué tipo de señal es?",
           "Salvamento o socorro", "Rectangulares o cuadradas y de color verde."),
    _senal("☣️ Triángulo con el símbolo de riesgo biológico. ¿Qué tipo de señal es?",
           "Advertencia", "Triangular y amarilla."),
    _senal("🚿 Cuadrado verde con una ducha de seguridad. ¿Qué tipo de señal es?",
           "Salvamento o socorro", "Como el lavado de ojos, la camilla o las flechas de dirección de evacuación."),
    _senal("🎧 Círculo azul con unos protectores auditivos. ¿Qué tipo de señal es?",
           "Obligación", "Protección obligatoria del oído."),
    _senal("🚜 Círculo rojo con una carretilla elevadora tachada. ¿Qué tipo de señal es?",
           "Prohibición", "Prohibido a los vehículos de manutención."),
    _senal("🚒 Cuadrado rojo con una manguera para incendios. ¿Qué tipo de señal es?",
           "Lucha contra incendios", "También: escalera de mano y teléfono para lucha contra incendios."),
    _senal("⚡ Triángulo amarillo con un rayo. ¿Qué tipo de señal es?",
           "Advertencia", "Riesgo eléctrico."),
    _senal("☢️ Triángulo amarillo con el símbolo de radiactividad. ¿Qué tipo de señal es?",
           "Advertencia", "Materias radiactivas."),
    {"bloque": BLOQUE_SENALES, "enunciado": "¿Qué forma y color tiene una señal de prohibición?",
     "opciones": ["Circular, roja", "Triangular, amarilla", "Circular, azul", "Cuadrada, verde"], "correcta": 0,
     "explicacion": "Prohibición: circular y roja."},
    {"bloque": BLOQUE_SENALES, "enunciado": "¿Qué forma y color tiene una señal de advertencia?",
     "opciones": ["Triangular, amarilla", "Circular, roja", "Circular, azul", "Rectangular, verde"], "correcta": 0,
     "explicacion": "Advertencia: triangular y amarilla (amarillo anaranjado)."},
    {"bloque": BLOQUE_SENALES, "enunciado": "¿Qué forma y color tiene una señal de obligación?",
     "opciones": ["Circular, azul", "Triangular, amarilla", "Circular, roja", "Rectangular, rojo"], "correcta": 0,
     "explicacion": "Obligación: circular y azul."},
    {"bloque": BLOQUE_SENALES, "enunciado": "¿Qué forma y color tiene una señal de primeros auxilios o vía de evacuación?",
     "opciones": ["Rectangular o cuadrada, verde", "Circular, roja", "Triangular, amarilla", "Circular, azul"], "correcta": 0,
     "explicacion": "Salvamento y socorro: rectangular o cuadrada y verde."},
    {"bloque": BLOQUE_SENALES, "enunciado": "Respecto a la señalización de seguridad, ¿cuál de estas frases es correcta?",
     "opciones": ["Es un recurso complementario que no elimina el riesgo",
                  "Elimina los riesgos laborales", "Sustituye a cualquier medida preventiva", "Si se señaliza el peligro, ya se ha eliminado"],
     "correcta": 0, "explicacion": "La señalización estimula nuestros sentidos para apercibirnos del peligro, pero no lo elimina."},
]


# ---------------------------------------------------------------------------
# Revisa tu puesto con pantalla (Práctica 11 · autoevaluación PVD)
# ---------------------------------------------------------------------------
PVD_ITEMS = [
    ("Teclado y mobiliario", "La mesa y el teclado están entre 60 y 75 cm del suelo."),
    ("Teclado y mobiliario", "La mesa permite apoyar los antebrazos."),
    ("Teclado y mobiliario", "El ratón tiene reposamuñecas."),
    ("Teclado y mobiliario", "La superficie de la mesa y del teclado es mate (sin reflejos)."),
    ("Teclado y mobiliario", "Mantengo la espalda recta y los antebrazos en ángulo de 90º respecto a la mesa."),
    ("Teclado y mobiliario", "Uso portadocumentos a la misma altura y distancia que la pantalla (si copio documentos)."),
    ("Teclado y mobiliario", "Mi silla tiene 5 pies con ruedas, regula la altura y se reclina (y uso reposapiés si hace falta)."),
    ("Pantalla y luz", "La parte superior de la pantalla no está por encima del nivel de mis ojos."),
    ("Pantalla y luz", "No hay reflejos ni deslumbramientos en la pantalla, y está limpia de polvo."),
    ("Pantalla y luz", "El ordenador está en un lateral de la ventana (a 90º), ni delante ni de espaldas a ella."),
    ("Pantalla y luz", "Tengo una iluminación de unos 300 lux."),
    ("Condiciones y organización", "La temperatura está entre 19 y 23 ºC, sin corrientes de aire."),
    ("Condiciones y organización", "No hay ruidos molestos en el lugar de trabajo."),
    ("Condiciones y organización", "Hago una pausa de 10 minutos cada 2 horas."),
    ("Condiciones y organización", "Alterno el uso de la pantalla con otras tareas."),
]


# ---------------------------------------------------------------------------
# Chuleta
# ---------------------------------------------------------------------------
CHULETA = """
### 🗂️ Estructura de la unidad

| Familia | Factores |
|---|---|
| **Condiciones de seguridad** | Lugares de trabajo · Maquinaria y herramientas · Riesgo eléctrico · Riesgo de incendio |
| **Condiciones medioambientales** | Agentes físicos (ruido, vibraciones, radiaciones, temperatura, iluminación) · Agentes químicos · Agentes biológicos |
| **Carga de trabajo** | Carga física · Carga mental · Pantallas de visualización de datos |
| **Organización del trabajo** | Riesgos psicosociales (insatisfacción, burnout, estrés, mobbing) |

### 🔢 Cifras clave

| Tema | Dato |
|---|---|
| Espacios de trabajo | 3 m de altura (2,5 m en locales comerciales y despachos) · 2 m² y 10 m³ por trabajador |
| Barandillas / escaleras / puertas / pasillos | 90 cm · 1 m · 80 cm · 1 m |
| Trabajos en altura | A más de 2 m |
| Corriente eléctrica | 1-3 mA cosquilleos · 5-10 mA contracciones · 10 mA tetanización · 25 mA parada cardio-respiratoria · 60-75 mA fibrilación · 1-5 A paro reversible y quemaduras |
| Diferencial doméstico | Salta con 30 mA |
| Alta tensión | Más de 1.000 V |
| Ruido | 55 dB conversación · 80 dB medidas y EPIs · 85 dB EPIs obligatorios · 87 dB límite (140 dB pico) · 120 dB dolor |
| Evaluación ruido / audiometrías | Cada 3 años (>80 dB) o cada año (>85 dB) / cada 5 años (>80 dB) o cada 3 (>85 dB) |
| Temperatura | Oficinas 17-27 ºC · trabajos ligeros 14-25 ºC · golpe de calor 42-44 ºC · hipotermia <35 ºC |
| Puesto con pantalla | Mesa y teclado a 60-75 cm · 300 lux · temperatura 19-23 ºC · pausa de 10 min cada 2 h |
| Iluminación mínima | 100 lux (bajas) · 200 (medias) · 500 (altas) · 1.000 (muy altas) |
| Carga manual | Riesgo desde 3 kg · máximo 25 kg · 15 kg (mujeres, jóvenes, edad avanzada) · 40 kg (entrenados, esporádico) |

### 🔥 Fuego y extintores

- **Tetraedro:** combustible + comburente (oxígeno) + energía de activación + reacción en cadena.
- **Clases:** A sólidos · B líquidos · C gaseosos · D metales.
- **Polvo ABC** → A, B y C. **CO₂** → B y equipos eléctricos/informáticos (no apaga brasas de A). **Metales** → extintor específico.
- **Uso:** conocer el extintor → descolgar y dejar en vertical → quitar anilla → descarga de prueba → base de las llamas en zig-zag a 1 m.

### ⚖️ Matriz de evaluación de riesgos (INSST)

| Probabilidad ↓ / Consecuencias → | Ligeramente dañinas | Dañinas | Extremadamente dañinas |
|---|---|---|---|
| **Baja** | Trivial | Tolerable | Moderado |
| **Media** | Tolerable | Moderado | Importante |
| **Alta** | Moderado | Importante | Intolerable |

### 🚦 Señales

| Tipo | Forma | Color |
|---|---|---|
| Prohibición | Circular | Rojo |
| Obligación | Circular | Azul |
| Advertencia | Triangular | Amarillo (anaranjado) |
| Salvamento y socorro | Rectangular o cuadrada | Verde |
| Lucha contra incendios | Rectangular o cuadrada | Rojo |

> La señalización es una técnica **complementaria**: no elimina el riesgo.
"""
