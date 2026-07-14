import streamlit as st
from auth import require_login
from translations import TRANSLATIONS

require_login()

if "lang" not in st.session_state:
    st.session_state.lang = "en"

t = TRANSLATIONS[st.session_state.lang]

# --- Page Configuration ---
st.set_page_config(
    page_title=t["nav_contact"], page_icon=":material/mail:", layout="wide"
)

# --- Custom Styling for Modern UI & 70% Content Restraints ---
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

    /* Icon Contact Card styling with sleek transitions */
    .icon-contact-card {
        display: block;
        text-decoration: none !important;
        background-color: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.08);
        padding: 1.2rem;
        border-radius: 12px;
        margin-bottom: 1rem;
        transition: all 0.2s ease-in-out;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    .icon-contact-card:hover {
        background-color: rgba(76, 175, 80, 0.05);
        border-color: rgba(76, 175, 80, 0.4);
        transform: translateY(-2px);
    }
    
    .card-content {
        display: flex;
        align-items: center;
        gap: 15px;
    }
    
    .card-icon {
        font-size: 1.8rem;
        min-width: 40px;
        text-align: center;
    }
    
    .card-text {
        color: #fff;
    }
    
    .card-label {
        font-size: 0.75rem;
        color: #888;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .card-value {
        font-size: 1rem;
        font-weight: 600;
    }

    /* --- FORCE STREAMLIT TABS ACCENT COLORS --- */
    div[data-baseweb="tab-list"] button[aria-selected="true"] p,
    div[role="tablist"] button[aria-selected="true"] p {
        color: #4CAF50 !important;
    }
    div[data-baseweb="tab-list"] button:hover p,
    div[role="tablist"] button:hover p {
        color: #4CAF50 !important;
    }
    div[data-baseweb="tab-list"] button:hover {
        background-color: rgba(76, 175, 80, 0.05) !important;
    }
    div[data-testid="stTabsSelectionIndicator"],
    div[role="tablist"] + div[style*="background-color"] {
        background-color: #4CAF50 !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Header Section ---
st.title(t["contact_title"])
st.markdown(f"*{t['contact_subtitle']}*")
st.markdown("---")

# --- Centered Content Column ---
# Creates a layout where the cards take up the central space cleanly
_, center_col, _ = st.columns([0.2, 1, 0.2])

with center_col:
    st.markdown(f"### {t['contact_details_head']}")

    # LinkedIn Card
    st.markdown(
        f"""
        <a href="https://www.linkedin.com/in/behdad-tabrizi-8914b627a/" target="_blank" class="icon-contact-card">
            <div class="card-content">
                <div class="card-icon" style="color: #0077b5;">🔗</div>
                <div class="card-text">
                    <div class="card-label">LinkedIn</div>
                    <div class="card-value">Behdad Tabrizi</div>
                </div>
            </div>
        </a>
        """,
        unsafe_allow_html=True,
    )

    # GitHub Card
    st.markdown(
        f"""
        <a href="https://github.com/deroso2017" target="_blank" class="icon-contact-card">
            <div class="card-content">
                <div class="card-icon" style="color: #fff;">💻</div>
                <div class="card-text">
                    <div class="card-label">GitHub</div>
                    <div class="card-value">Ronitech </div>
                </div>
            </div>
        </a>
        """,
        unsafe_allow_html=True,
    )

    # E-Mail Card
    st.markdown(
        f"""
        <a href="mailto:behdad_g59@yahoo.com" class="icon-contact-card">
            <div class="card-content">
                <div class="card-icon" style="color: #ea4335;">✉️</div>
                <div class="card-text">
                    <div class="card-label">E-Mail</div>
                    <div class="card-value">behdad_g59@yahoo.com</div>
                </div>
            </div>
        </a>
        """,
        unsafe_allow_html=True,
    )

    # Phone Card
    st.markdown(
        f"""
        <a href="tel:+491726971399" class="icon-contact-card">
            <div class="card-content">
                <div class="card-icon" style="color: #34a853;">📱</div>
                <div class="card-text">
                    <div class="card-label">Telefon</div>
                    <div class="card-value">+49 172 697 1399</div>
                </div>
            </div>
        </a>
        """,
        unsafe_allow_html=True,
    )
