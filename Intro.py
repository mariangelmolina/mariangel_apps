import streamlit as st

# Configuración de página
st.set_page_config(
    page_title="Portafolio de Proyectos IA | Mariangel",
    page_icon="🌿",
    layout="wide"
)

# Estilos CSS generales para la estructura y botones
st.markdown("""
    <style>
    /* Fondo principal */
    .stApp {
        background-color: #F8FAF8;
    }
    
    /* Botones principales en verde sage profundo */
    div.stButton > a, div.stLinkButton > a {
        background-color: #3B5243 !important;
        color: #FFFFFF !important;
        border-radius: 8px !important;
        border: none !important;
        font-weight: 600 !important;
    }
    
    div.stButton > a:hover, div.stLinkButton > a:hover {
        background-color: #293B2F !important;
        color: #FFFFFF !important;
    }

    /* Fondo de la barra lateral */
    section[data-testid="stSidebar"] {
        background-color: #EBF0EC !important;
    }
    </style>
""", unsafe_allow_html=True)

# Encabezado Principal (Con color forzado en verde oscuro)
st.markdown('<h1 style="text-align: center; color: #1E2B23; font-weight: 700;">Portafolio de Aplicaciones de IA 🌿✨</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; color: #4A5D50; font-size: 1.1rem; margin-bottom: 2rem;">Explora mis proyectos interactivos de Procesamiento de Lenguaje Natural, Visión por Computador y Multimodalidad</p>', unsafe_allow_html=True)

st.markdown("---")

# Sidebar con perfil y descripción
with st.sidebar:
    st.markdown('<h2 style="color: #1E2B23;">👤 Mariangel Molina</h2>', unsafe_allow_html=True)
    st.markdown('<p style="color: #3B5243; font-weight: 600;">Diseño Interactivo & Proyectos de IA</p>', unsafe_allow_html=True)
    st.markdown(
        '<p style="color: #2D3A31;">Bienvenido a mi portafolio. Aquí encontrarás una colección de herramientas interactivas '
        'desarrolladas con Inteligencia Artificial, que abarcan desde el procesamiento de texto y voz '
        'hasta visión por computador y análisis de datos.</p>',
        unsafe_allow_html=True
    )
    st.markdown("---")
    
    # Filtro por Categorías
    categoria = st.selectbox(
        "🔍 Filtrar por categoría:",
        ["Todas", "Audio & Voz", "Texto & NLP", "Visión por Computador"]
    )

# Lista completa de 11 aplicaciones
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
    },
    {
        "titulo": "Chat PDF con LLM (RAG)",
        "categoria": "Texto & NLP",
        "icono": "📄",
        "descripcion": "Agente conversacional basado en RAG para realizar consultas y preguntas sobre documentos PDF.",
        "url": "https://chatpdf-rcydkkt5ppxrlxl8ixjfju.streamlit.app/",
        "etiqueta": "Consultar PDF"
    },
    {
        "titulo": "Interpretación de Imágenes (GPT-4o)",
        "categoria": "Visión por Computador",
        "icono": "👁️",
        "descripcion": "Análisis multimodales e interpretación detallada de imágenes en tiempo real.",
        "url": "https://visionapp-c8frnbrhc5lewgb8v4rgt6.streamlit.app/",
        "etiqueta": "Interpretar Imagen"
    }
]

# Filtrado dinámico
if categoria != "Todas":
    apps_filtradas = [app for app in apps if app["categoria"] == categoria]
else:
    apps_filtradas = apps

# Renderizado de Grid de Tarjetas
cols_per_row = 3
for i in range(0, len(apps_filtradas), cols_per_row):
    cols = st.columns(cols_per_row)
    chunk = apps_filtradas[i:i + cols_per_row]
    
    for idx, app in enumerate(chunk):
        with cols[idx]:
            with st.container(border=True):
                # Título, categoría y descripción con colores oscuros forzados por HTML
                st.markdown(f'<h3 style="color: #1E2B23; font-size: 1.15rem; font-weight: 700; margin-bottom: 0.2rem;">{app["icono"]} {app["titulo"]}</h3>', unsafe_allow_html=True)
                st.markdown(f'<p style="color: #5A6B5D; font-size: 0.85rem; font-weight: 600; margin-bottom: 0.5rem;">Categoría: {app["categoria"]}</p>', unsafe_allow_html=True)
                st.markdown(f'<p style="color: #2D3A31; font-size: 0.92rem; min-height: 50px;">{app["descripcion"]}</p>', unsafe_allow_html=True)
                st.link_button(app['etiqueta'], app['url'], use_container_width=True)
