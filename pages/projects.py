import streamlit as st
from auth import require_login
from translations import TRANSLATIONS

require_login()

if "lang" not in st.session_state:
    st.session_state.lang = "en"

lang = st.session_state.lang
t = TRANSLATIONS[lang]

# --- Page Configuration ---
st.set_page_config(
    page_title=t["nav_projects"], page_icon=":material/folder_open:", layout="wide"
)

# Custom container styling
st.markdown(
    """
    <style>
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

# Header Section
st.title(t["nav_projects"])
st.markdown("---")

# Load projects from translations.py
projects = t.get("projects_list", [])

if not projects:
    st.info(
        "Noch keine Projekte eingetragen." if lang == "de" else "No projects added yet."
    )
else:
    # Loop through and display each project using the robust expander layout
    for project in projects:
        title = project.get("title", "Ohne Titel" if lang == "de" else "Untitled")
        desc = project.get("desc", "")
        tech_stack = project.get("tech_stack", "")
        date = project.get("date", "")
        project_link = project.get("link", None)

        # Labels based on language
        lbl_date = "Date" if lang == "en" else "Datum"
        lbl_tech = "Tech Stack" if lang == "en" else "Tech-Stack"
        lbl_link = "Visit Project" if lang == "en" else "Projekt ansehen"

        with st.expander(f"{title}", expanded=False):
            # Metadata rows with unified Date field
            st.markdown(
                f"**{lbl_date}:** {date}",
                unsafe_allow_html=True,
            )
            st.markdown(f"**{lbl_tech}:** `{tech_stack}`")

            # Divider
            st.markdown("---")

            # Project Description
            st.markdown(
                f"<div style='color: rgba(255,255,255,0.85); line-height: 1.6; margin-bottom: 1rem;'>{desc}</div>",
                unsafe_allow_html=True,
            )

            # Optional Link at the very end of description
            if project_link:
                st.link_button(f"🔗 {lbl_link}", project_link)
