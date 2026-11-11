
import streamlit as st
import unicodedata

st.set_page_config(
    page_title="ARCHIVO 017",
    page_icon="🔒",
    layout="centered"
)

# RESPUESTAS: configura las llaves de los niveles 3 al 7.
# No compartas este archivo con quien vaya a jugar.

RESPUESTAS = [
    "ESPEJO",
    "MIRADA",
    "REFLEJO",
    "VERDAD",
    "CERCA",
    "SIEMPRE",
    "OJALÁ PUDIERAS VERTE CON LOS OJOS CON LOS QUE TE VEO YO"
]

NIVELES = [
    {
        "titulo": "SEÑAL DE ORIGEN",
        "texto": """
Sistema de comunicación antiguo.

`. / ... / .--. / . / .--- / ---`

Identifica el sistema, traduce las señales y
conserva la palabra obtenida.
"""
    },
    {
        "titulo": "CIFRADO POLIALFABÉTICO",
        "texto": """
`QAGEMO`

La primera llave será necesaria para descifrar
esta transmisión.

A=0, B=1... Z=25.

La clave se repite hasta cubrir todo el mensaje.
Para descifrar, resta el valor de cada letra
de la clave al de la letra cifrada.
"""
    },
    {
        "titulo": "TRANSPOSICIÓN",
        "texto": """
`LXJXEXEXROFX`

Las letras no han sido sustituidas:
han cambiado de posición.

Utiliza la segunda llave como encabezado
de una tabla.

Ordena las columnas alfabéticamente,
distribuye el texto cifrado y reconstruye
las filas.

Las X finales son caracteres de relleno.
"""
    },
    {
        "titulo": "DESPLAZAMIENTO MATEMÁTICO",
        "texto": """
`HQDPMP`

Calcula la suma de los valores alfabéticos
de la tercera llave.

Divide el resultado entre 26 y conserva
el resto.

Ese será el desplazamiento utilizado.
Deshazlo para recuperar la siguiente llave.
"""
    },
    {
        "titulo": "COORDENADAS",
        "texto": """
`22 12 13 22 15`

Construye una cuadrícula de 5 × 5.

Coloca primero las letras de la cuarta llave,
sin repetirlas.

Completa con el alfabeto, omitiendo J
y unificando I/J.

Cada pareja indica fila y columna,
en ese orden.
"""
    },
    {
        "titulo": "SEGUNDA TRANSMISIÓN",
        "texto": """
`UMVOPTI`

Se ha utilizado el mismo sistema del nivel 02.

Esta vez, la quinta llave será la clave.

Descifra sin alterar el número de caracteres.
"""
    },
    {
        "titulo": "ÚLTIMA TRANSMISIÓN",
        "texto": """
CLASIFICACIÓN: MÁXIMA

`GREXP GYVQIDPJ ZWZXQ RFR DWW AYFW UWR XDJ UMM XQ KVS QW`

No existen más instrucciones.

Todo lo necesario para resolver esta última
transmisión se encuentra en los niveles anteriores.

La última llave permitirá reconstruir
el mensaje original.
"""
    }
]


def limpiar(texto):
    texto = texto.upper().strip()
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(
        c for c in texto
        if unicodedata.category(c) != "Mn"
    )
    return "".join(c for c in texto if c.isalnum())


if "nivel" not in st.session_state:
    st.session_state.nivel = 0

if "llaves" not in st.session_state:
    st.session_state.llaves = []


# DISEÑO MÓVIL
st.markdown("""
<style>
.stApp {
    background: #080d13;
    color: #dce6ef;
}

.block-container {
    max-width: 600px;
    padding: 1.5rem 1rem 3rem;
}

h1, h2, h3 {
    color: #a9d8ff !important;
    letter-spacing: 2px;
}

p, label {
    color: #dce6ef !important;
}

.expediente {
    border: 1px solid #52718b;
    padding: 20px;
    text-align: center;
    border-radius: 8px;
    background: #101c29;
    margin-bottom: 20px;
}

.advertencia {
    border-left: 3px solid #d5a442;
    padding: 12px;
    background: #171b20;
    margin: 20px 0;
}

.stButton button {
    width: 100%;
    min-height: 48px;
    background: #183a54;
    color: white;
    border: 1px solid #7cbbe8;
    border-radius: 8px;
}

.stTextInput input {
    background: #111b26;
    color: white;
    border: 1px solid #52718b;
    min-height: 45px;
}

</style>
""", unsafe_allow_html=True)


# CABECERA
st.markdown("""
<div class="expediente">
    <h1>🔒 ARCHIVO 017</h1>
    <h3>EXPEDIENTE CLASIFICADO</h3>
    <p>DESTINATARIA: JANA</p>
    <p>AUTORIZACIÓN: PERSONAL E INTRANSFERIBLE</p>
    <p>NIVELES: 7</p>
    <p>ESTADO: BLOQUEADO</p>
</div>
""", unsafe_allow_html=True)


st.markdown("### ⚠️ ADVERTENCIA")

st.markdown("""
<div class="advertencia">
Este documento contiene una transmisión cifrada
dividida en siete niveles.

Cada nivel contiene una prueba que deberá
resolverse para acceder al siguiente.

Guarda todas las respuestas.
Cada respuesta será necesaria posteriormente.
</div>
""", unsafe_allow_html=True)


# PROGRESO
nivel = st.session_state.nivel

st.progress(nivel / 7)

st.caption(f"PROGRESO: {nivel}/7 NIVELES COMPLETADOS")


# LLAVES GUARDADAS
with st.expander("🗝️ REGISTRO DE LLAVES"):
    if st.session_state.llaves:
        for i, llave in enumerate(st.session_state.llaves):
            st.write(f"Nivel {i+1}: `{llave}`")
    else:
        st.write("No hay llaves registradas.")


# MOSTRAR NIVEL ACTUAL
if nivel < 7:

    datos = NIVELES[nivel]

    st.markdown("---")
    st.markdown(f"## 🔐 NIVEL {nivel+1:02d}")
    st.markdown(f"### {datos['titulo']}")

    st.markdown(datos["texto"])

    st.markdown("---")

    st.write("**INTRODUCE LA RESPUESTA PARA CONTINUAR**")

    with st.form(key=f"form_{nivel}"):
        respuesta = st.text_input(
            "Respuesta:",
            placeholder="Escribe aquí tu respuesta...",
            label_visibility="collapsed"
        )

        enviar = st.form_submit_button(
            "🔓 VERIFICAR RESPUESTA"
        )

    if enviar:

        correcta = RESPUESTAS[nivel]

        if correcta.startswith("PON_RESPUESTA"):
            st.error(
                "Este nivel todavía no está configurado "
                "por el creador del expediente."
            )

        elif limpiar(respuesta) == limpiar(correcta):

            st.session_state.llaves.append(
                respuesta.strip().upper()
            )

            st.session_state.nivel += 1

            st.success("ACCESO AUTORIZADO")

            st.rerun()

        else:
            st.error("❌ RESPUESTA INCORRECTA")
            st.caption(
                "La transmisión permanece bloqueada."
            )


# FINAL
else:

    st.markdown("---")

    st.markdown("""
    <div class="expediente">
        <h1>🔓 ACCESO AUTORIZADO</h1>
        <h2>ARCHIVO 017</h2>
        <p>LOS SIETE NIVELES HAN SIDO COMPLETADOS.</p>
        <p>LA TRANSMISIÓN ESTÁ DISPONIBLE.</p>
    </div>
    """, unsafe_allow_html=True)

    st.success("EXPEDIENTE COMPLETADO")

    st.markdown("### 🗝️ REGISTRO FINAL")

    for i, llave in enumerate(st.session_state.llaves):
        st.write(f"**LLAVE {i+1}:** {llave}")

    if st.button("REINICIAR EXPEDIENTE"):
        st.session_state.nivel = 0
        st.session_state.llaves = []
        st.rerun()

st.markdown("---")
st.caption(
    "ARCHIVO 017 · SISTEMA DE TRANSMISIÓN CLASIFICADA"
)
