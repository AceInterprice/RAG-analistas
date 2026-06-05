import streamlit as st
import requests

API_URL = "http://localhost:8000/api"

st.set_page_config(
    page_title="Generador de Informes",
    layout="wide"
)

st.title("Sistema de generación de informes con IA")

# =========================
# SELECCIÓN DE MÓDULO
# =========================
modulo = st.sidebar.selectbox(
    "Selecciona módulo",
    [
        "Redacción Policial",
        "Redacción Policial con Audio",
        "Marco Legal",
        "Extractor de Datos"
    ]
)

# =========================
# INPUT SEGÚN MÓDULO
# =========================

audio_file = None
prompt = ""

if modulo == "Redacción Policial con Audio":

    audio_file = st.file_uploader(
        "Seleccione un archivo de audio",
        type=["wav", "mp3", "m4a"]
    )

else:

    prompt = st.text_area(
        "Narrativa del caso:",
        height=300,
        placeholder="Escriba aquí los hechos..."
    )

# =========================
# MAPEO DE ENDPOINTS
# =========================

endpoints = {
    "Redacción Policial": "redaccion-policial",
    "Redacción Policial con Audio": "redaccion-policial-audio",
    "Marco Legal": "marco-legal",
    "Extractor de Datos": "extractor-datos"
}

# =========================
# EJECUCIÓN
# =========================

if st.button("Ejecutar"):

    endpoint = endpoints.get(modulo)

    if not endpoint:
        st.error("Módulo no válido")
        st.stop()

    with st.spinner("Procesando..."):

        try:

            # ==================================
            # REDACCIÓN POLICIAL CON AUDIO
            # ==================================
            if modulo == "Redacción Policial con Audio":

                if not audio_file:
                    st.warning("Seleccione un archivo de audio.")
                    st.stop()

                response = requests.post(
                    f"{API_URL}/{endpoint}",
                    files={
                        "archivo": (
                            audio_file.name,
                            audio_file,
                            audio_file.type
                        )
                    }
                )

            # ==================================
            # RESTO DE MÓDULOS
            # ==================================
            else:

                if not prompt.strip():
                    st.warning("Ingrese una narrativa.")
                    st.stop()

                response = requests.post(
                    f"{API_URL}/{endpoint}",
                    json={
                        "texto": prompt
                    }
                )

            # ==================================
            # RESPUESTA
            # ==================================

            if response.status_code == 200:

                data = response.json()

                # Para audio mostramos transcripción
                if modulo == "Redacción Policial con Audio":

                    st.subheader("Transcripción")

                    st.write(
                        data.get(
                            "transcripcion",
                            "Sin transcripción"
                        )
                    )

                st.subheader("Resultado")

                st.write(
                    data.get(
                        "resultado",
                        "Sin resultado"
                    )
                )

            else:

                st.error(
                    f"Error {response.status_code}: {response.text}"
                )

        except Exception as e:

            st.error(
                f"Error de conexión: {e}"
            )