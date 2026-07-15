import base64
import io
import fitz
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
        {
            "file": "BTA_Arbeitszeugniss.pdf",
            "title": "Arbeitszeugnis",
            "icon": "📄",
            "category": "Berufserfahrung",
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


@st.cache_data(show_spinner=False)
def get_pdf_bytes(full_path):
    if file_exists(full_path):
        return download_file(full_path)
    return None


@st.dialog("📄 Dokumentenvorschau / Document Preview", width="medium")
def show_pdf_preview(file_name, display_title, folder_path):
    full_path = f"{folder_path}/{file_name}"
    pdf_bytes = get_pdf_bytes(full_path)

    if pdf_bytes:
        st.subheader(display_title)

        base64_pdf = base64.b64encode(pdf_bytes).decode("utf-8")
        pdf_data_url = f"data:application/pdf;base64,{base64_pdf}"
        st.markdown(
            f"""
            <a href="{pdf_data_url}" target="_blank" style="text-decoration: none; display: block; margin-bottom: 1rem;">
                <div style="
                    background-color: #1e1e1e; color: #ffffff;
                    padding: 0.5rem 1rem; border: 1px solid #333333;
                    border-radius: 8px; text-align: center;
                    font-size: 0.9rem; font-weight: 500; cursor: pointer;
                ">↗️ Vollbild / Fullscreen</div>
            </a>
            """,
            unsafe_allow_html=True,
        )

        pdf = fitz.open(stream=io.BytesIO(pdf_bytes), filetype="pdf")
        for i in range(pdf.page_count):
            pix = pdf[i].get_pixmap(dpi=150)
            st.image(pix.tobytes("png"), use_container_width=True)
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
