import base64
import streamlit as st
from auth import require_login
from storage import download_file, file_exists
from translations import TRANSLATIONS

require_login()

if "lang" not in st.session_state:
    st.session_state.lang = "en"

lang = st.session_state.lang
t = TRANSLATIONS[lang]

# --- Page Configuration ---
st.set_page_config(
    page_title=t["nav_certifications"],
    page_icon=":material/workspace_premium:",
    layout="wide",
)

# --- Custom CSS ---
st.markdown(
    """
    <style>
    .block-container {
        max-width: 85% !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
        margin: 0 auto !important;
    }

    /* 1. Make the button have a minimum height of 100px */
    div[data-testid="stButton"] button {
        min-height: 200px !important;
        display: inline-flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: center !important;
        white-space: pre-line !important; /* Preserves your \n line breaks */
        padding: 15px !important;
    }

    /* 2. Target the first line (the emoji icon) and make it 60px */
    div[data-testid="stButton"] button ::first-line {
        font-size: 50px !important;
        line-height: 70px !important; /* Keeps spacing clean below the large icon */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Define certificates list based on language
if lang == "de":
    cert_files = [
        {
            "file": "math-bachelor.pdf",
            "title": "B.Sc. Mathematischer Abschluss",
            "icon": "🎓",
            "category": "Akademisch",
        },
        {
            "file": "b2-plus.pdf",
            "title": "telc Deutsch B2+ Beruf",
            "icon": "🗣️",
            "category": "Sprachen",
        },
        {
            "file": "aws.pdf",
            "title": "AWS Cloud Engineering",
            "icon": "☁️",
            "category": "Cloud & DevOps",
        },
        {
            "file": "ms.pdf",
            "title": "Microsoft Enterprise Solutions",
            "icon": "⚙️",
            "category": "Systeme",
        },
        {
            "file": "ihk.pdf",
            "title": "IHK Fachinformatiker",
            "icon": "💼",
            "category": "Berufsabschluss",
        },
        {
            "file": "fullstack-tech-certifications.pdf",
            "title": "Full Stack Tech Stack Zertifikate",
            "icon": "💻",
            "category": "Programmierung",
        },
    ]
else:
    cert_files = [
        {
            "file": "math-bachelor.pdf",
            "title": "B.Sc. Mathematics Degree",
            "icon": "🎓",
            "category": "Academic",
        },
        {
            "file": "aws.pdf",
            "title": "AWS Cloud Engineering",
            "icon": "☁️",
            "category": "Cloud & DevOps",
        },
        {
            "file": "ms.pdf",
            "title": "Microsoft Certified Professional",
            "icon": "⚙️",
            "category": "Systems",
        },
        {
            "file": "ihk.pdf",
            "title": "IHK Software Developer",
            "icon": "💼",
            "category": "Vocational",
        },
        {
            "file": "fullstack-tech-certifications.pdf",
            "title": "Full Stack Tech Stack",
            "icon": "💻",
            "category": "Software",
        },
        {
            "file": "electrical-equipment-installation.pdf",
            "title": "Electrical Equipment Installation",
            "icon": "⚡",
            "category": "Technical",
        },
    ]

# Header Section
st.title(t["nav_certifications"])
st.markdown("---")


# --- Optimized PDF loading to prevent IDM trigger ---
@st.cache_data(show_spinner=False)
def get_pdf_base64(full_path):
    if file_exists(full_path):
        pdf_bytes = download_file(full_path)
        return base64.b64encode(pdf_bytes).decode("utf-8")
    return None


# --- Popup Modal Dialog (Sleek Frame Preview, No IDM Auto-Download) ---
@st.dialog("📄 Dokumentenvorschau / Document Preview", width="large")
def show_pdf_preview(file_name, display_title, folder_path):
    full_path = f"{folder_path}/{file_name}"
    base64_data = get_pdf_base64(full_path)

    if base64_data:
        st.subheader(display_title)

        # Embedded PDF preview inside Dialog utilizing Data URL without direct file links
        pdf_data_url = f"data:application/pdf;base64,{base64_data}"
        st.markdown(
            f"""
            <iframe 
                src="{pdf_data_url}#toolbar=0&navpanes=0&statusbar=0" 
                width="100%" 
                height="750px" 
                type="application/pdf"
                style="border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; box-shadow: 0px 4px 20px rgba(0,0,0,0.5);"
            >
            </iframe>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.error(f"Dokument '{file_name}' konnte nicht geladen werden.")


# --- Render Grid in 3 Columns ---
cols_per_row = 3
rows = [
    cert_files[i : i + cols_per_row] for i in range(0, len(cert_files), cols_per_row)
]
base_folder = f"certifications/{lang}"

for row in rows:
    cols = st.columns(cols_per_row, gap="large")
    for i, cert in enumerate(row):
        with cols[i]:
            label = f"{cert['icon']}\n{cert['title']}\n{cert['category']}"
            if st.button(label, key=f"btn_{cert['file']}", use_container_width=True):
                show_pdf_preview(cert["file"], cert["title"], base_folder)
