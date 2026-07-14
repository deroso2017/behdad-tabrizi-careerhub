import io
import fitz
import streamlit as st
from auth import require_login
from storage import download_file, file_exists
from translations import TRANSLATIONS

require_login()

# Fetch active language from session state (defaults to German)
lang = st.session_state.get("lang", "de")
_ = TRANSLATIONS[lang]

# Configure page dynamically based on active language dictionary (set to wide layout for constraints)
st.set_page_config(
    page_title=_["cv_page_title"], page_icon=":material/contact_page:", layout="wide"
)

# --- Custom Styling for 70% Content Restraints ---
st.markdown(
    """
    <style>
    /* Enforce maximum width of the app canvas to exactly 85% and center it */
    .block-container {
        max-width: 85% !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
        margin: 0 auto !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title(_["cv_title"])

# Dynamic language path validation and loading
if lang == "de":
    pdf_path = "cv/de/lebenslauf90.pdf"
else:
    pdf_path = "cv/en/cv.pdf"

if file_exists(pdf_path):
    with st.spinner(_["cv_spinner"]):
        pdf_bytes = download_file(pdf_path)

        import base64

        base64_pdf = base64.b64encode(pdf_bytes).decode("utf-8")
        pdf_data_url = f"data:application/pdf;base64,{base64_pdf}"

        st.markdown(
            f"""
            <a href="{pdf_data_url}" target="_blank" style="text-decoration: none; display: block; margin-bottom: 1.2rem;">
                <div style="
                    background-color: #1e1e1e; color: #ffffff;
                    padding: 0.6rem 1rem; border: 1px solid #333333;
                    border-radius: 8px; text-align: center;
                    font-size: 0.95rem; font-weight: 500; cursor: pointer;
                    width: 100%; box-sizing: border-box;
                ">{_["view_fullscreen"]}</div>
            </a>
            """,
            unsafe_allow_html=True,
        )

        pdf = fitz.open(stream=io.BytesIO(pdf_bytes), filetype="pdf")
        for i in range(pdf.page_count):
            pix = pdf[i].get_pixmap(dpi=150)
            st.image(pix.tobytes("png"), use_container_width=True)
