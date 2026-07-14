import base64
import streamlit as st
from auth import require_login
from storage import download_file, file_exists
from translations import TRANSLATIONS  # Import the central dictionary

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

        # Encode bytes to base64
        base64_pdf = base64.b64encode(pdf_bytes).decode("utf-8")
        pdf_data_url = f"data:application/pdf;base64,{base64_pdf}"

        # Render a button to view the PDF in fullscreen
        st.markdown(
            f"""
            <a href="{pdf_data_url}" target="_blank" style="text-decoration: none; display: block; margin-bottom: 1.2rem;">
                <div style="
                    background-color: #1e1e1e;
                    color: #ffffff;
                    padding: 0.6rem 1rem;
                    border: 1px solid #333333;
                    border-radius: 8px;
                    text-align: center;
                    font-size: 0.95rem;
                    font-weight: 500;
                    cursor: pointer;
                    width: 100%;
                    box-sizing: border-box;
                    transition: all 0.2s ease-in-out;
                " 
                onmouseover="this.style.backgroundColor='#2a2a2a'; this.style.borderColor='#555555';" 
                onmouseout="this.style.backgroundColor='#1e1e1e'; this.style.borderColor='#333333';">
                    {_["view_fullscreen"]}
                </div>
            </a>
            """,
            unsafe_allow_html=True,
        )

        # Embedded Preview
        pdf_display = f"""
            <iframe 
                src="{pdf_data_url}#toolbar=0&navpanes=0&statusbar=0" 
                width="100%" 
                height="850px" 
                type="application/pdf"
                style="border: 1px solid #333333; border-radius: 8px; box-shadow: 0px 4px 16px rgba(0,0,0,0.4);"
            >
            </iframe>
        """
        st.markdown(pdf_display, unsafe_allow_html=True)
