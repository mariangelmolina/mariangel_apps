import streamlit as st

# Configuración de página
st.set_page_config(
    page_title="Portafolio de Proyectos IA | Mariangel",
    page_icon="🌿",
    layout="wide"
)

# Estilos CSS personalizados en tonos Sage Green
st.markdown("""
    <style>
    /* Estilos generales */
    .stApp {
        background-color: #F4F6F4;
    }
    
    /* Encabezado */
    .main-header {
        text-align: center;
        color: #2D3A31;
        font-family: 'Inter', sans-serif;
        font-weight: 700;
        margin-bottom: 0.2rem;
    }
    .sub-header {
        text-align: center;
        color: #5A6B5D;
        font-size: 1.05rem;
        margin-bottom: 2rem;
    }

    /* Tarjetas estilizadas */
    div[data-testid="stContainer"] {
        background-color: #FFFFFF;
        border: 1px solid #D1DED3 !important;
        border-radius: 12px !important;
        padding: 1.2rem;
        box-shadow: 0px 4px 12px rgba(45, 58, 49, 0.03);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    
    /* Botones principales con tono Sage Green */
    div.stButton > a, div.stLinkButton > a {
        background-color: #3D5A45 !important;
        color: #FFFFFF !important;
        border-radius: 8px !important;
        border: none !important;
        font-weight: 500 !important;
    }
    
    div.stButton > a:hover, div.stLinkButton > a:hover {
        background-color: #2D4333 !important;
        color: #FFFFFF !important;
    }

    /* Barra lateral */
    section[data-testid="stSidebar"] {
        background-color: #EAEFEA;
        border-right: 1px solid #D1DED3;
    }
    </style>
""", unsafe_allow_html=True)

# Encabezado Principal
st.markdown('<h1 class="main-header">Portafolio de Aplicaciones de IA 🌿✨</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Explora mis proyectos interactivos de Procesamiento de Lenguaje Natural, Visión por Computador y Multimodalidad</p>', unsafe_allow_html=True)

# Sidebar con perfil y descripción
with st.sidebar:
    st.header("👤 Mariangel Molina")
    st.caption("Diseño Interactivo & Proyectos de IA")
    st.write(
        "Bienvenido a mi portafolio. Aquí encontrarás una colección de herramientas interactivas "
        "desarrolladas con Inteligencia Artificial, que abarcan desde el procesamiento de texto y voz "
        "hasta visión por computador y análisis de datos."
    )
    st.markdown("---")
    
    # Filtro por Categorías
    categoria = st.selectbox(
        "🔍 Filtrar por categoría:",
        ["Todas", "Audio & Voz", "Texto & NLP", "Visión por Computador"]
    )

# Definición de
