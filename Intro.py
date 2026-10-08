import streamlit as st

# Configuración de página
st.set_page_config(
    page_title="Portafolio de Proyectos IA | Mariangel",
    page_icon="✨",
    layout="wide"
)

# Estilos CSS personalizados para mejorar la legibilidad y estética
st.markdown("""
    <style>
    .main-header {
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        text-align: center;
        color: #6C757D;
        margin-bottom: 2rem;
    }
    .card-title {
        font-weight: 600;
        font-size: 1.15rem;
        margin-bottom: 0.5rem;
    }
    .card-desc {
        color: #4A5568;
        font-size: 0.92rem;
        min-height: 55px;
    }
    </style>
""", unsafe_allow_html=True)

# Encabezado Principal
st.markdown('<h1 class="main-header">Portafolio de Aplicaciones de IA ✨🎨</h1>', unsafe_allow_html=True)
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
    st.divider()
    
    # Filtro por Categorías
    categoria = st.selectbox(
        "🔍 Filtrar por categoría:",
        ["Todas", "Audio & Voz", "Texto & NLP", "Visión por Computador"]
    )

# Definición de la lista de aplicaciones
apps = [
    {
        "titulo": "Primera App Multimodal",
        "categoria": "Audio & Voz",
        "icono": "🎙️",
        "descripcion": "Interfaz interactiva inicial para explorar capacidades multimodales.",
        "url": "https://mariangelmolina-interfacesmultimodales-app-vnplvq.streamlit.app/",
        "etiqueta": "Explorar App 1"
    },
    {
        "titulo": "Texto a Audio",
        "categoria": "Audio & Voz",
        "icono": "🔊",
        "descripcion": "Convierte textos ingresados por el usuario en fragmentos de audio sintetizado.",
        "url": "https://mariangelmolina-interfacesmultimodales-app-app2-py-2rgvnp.streamlit.app/",
        "etiqueta": "Convertir Texto"
    },
    {
        "titulo": "Traductor Multilingüe",
        "categoria": "Texto & NLP",
        "icono": "🌐",
        "descripcion": "Aplicación para traducir texto entre múltiples idiomas en tiempo real.",
        "url": "https://traductor-e3zjruc6qjogwcforpug4c.streamlit.app/",
        "etiqueta": "Abrir Traductor"
    },
    {
        "titulo": "Análisis de Sentimientos",
        "categoria": "Texto & NLP",
        "icono": "💬",
        "descripcion": "Clasifica el tono de oraciones en positivo, negativo o neutro mediante NLP.",
        "url": "https://sentimenta-sdrnptcwg634agvf3nvaer.streamlit.app/",
        "etiqueta": "Analizar Sentimiento"
    },
    {
        "titulo": "OCR Cámara en Vivo",
        "categoria": "Visión por Computador",
        "icono": "📷",
        "descripcion": "Reconocimiento óptico de caracteres para extraer texto directo desde la cámara.",
        "url": "https://speechtotext-dn6gvxjgmtyveee2sanid3.streamlit.app/",
        "etiqueta": "Probar OCR Cámara"
    },
    {
        "titulo": "OCR en Imágenes",
        "categoria": "Visión por Computador",
        "icono": "🖼️",
        "descripcion": "Extrae e interpreta texto contenido dentro de archivos de imagen subidos.",
        "url": "https://speechtotext-iaapprzghsvvdgpkvcxxivu.streamlit.app/",
        "etiqueta": "Probar OCR Imagen"
    },
    {
        "titulo": "Demo TF-IDF en Español",
        "categoria": "Texto & NLP",
        "icono": "📊",
        "descripcion": "Demostración de extracción de palabras clave utilizando el algoritmo TF-IDF.",
        "url": "https://tdfesp-2bdwmdgwk5jph3vuudxvie.streamlit.app/",
        "etiqueta": "Ver Demo TF-IDF"
    },
    {
        "titulo": "Word Cloud Studio",
        "categoria": "Texto & NLP",
        "icono": "☁️",
        "descripcion": "Generador visual de nubes de palabras personalizadas a partir de bloques de texto.",
        "url": "https://wordcloud-2ahmd8tykjqcevuv4rcaff.streamlit.app/",
        "etiqueta": "Crear Word Cloud"
    },
    {
        "titulo": "Detección de Objetos (YOLOv5)",
        "categoria": "Visión por Computador",
        "icono": "🎯",
        "descripcion": "Identificación y delimitación de múltiples objetos en imágenes mediante redes neuronales.",
        "url": "https://yolov5-8wnljwxjxrnepdslw7vua6.streamlit.app/",
        "etiqueta": "Detectar Objetos"
    }
]

# Filtrado dinámico
if categoria != "Todas":
    apps_filtradas = [app for app in apps if app["categoria"] == categoria]
else:
    apps_filtradas = apps

# Renderizado de Grid de Tarjetas (3 columnas)
cols_per_row = 3
for i in range(0, len(apps_filtradas), cols_per_row):
    cols = st.columns(cols_per_row)
    chunk = apps_filtradas[i:i + cols_per_row]
    
    for idx, app in enumerate(chunk):
        with cols[idx]:
            with st.container(border=True):
                st.markdown(f"### {app['icono']} {app['titulo']}")
                st.caption(f"Categoría: **{app['categoria']}**")
                st.write(app['descripcion'])
                st.link_button(app['etiqueta'], app['url'], use_container_width=True)

