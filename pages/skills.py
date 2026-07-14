import streamlit as st
from auth import require_login
from translations import TRANSLATIONS

require_login()

if "lang" not in st.session_state:
    st.session_state.lang = "en"

t = TRANSLATIONS[st.session_state.lang]

# --- Page Configuration ---
st.set_page_config(
    page_title=t["nav_skills"], page_icon=":material/psychology:", layout="wide"
)

# --- Custom Styling for Modern UI & 85% Content Restraints ---
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

    /* Card Layout Styling */
    .skill-card {
        background-color: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-left: 4px solid #4CAF50;
        padding: 1.2rem;
        border-radius: 4px 12px 12px 4px;
        margin-bottom: 1rem;
    }
    
    .skill-title {
        font-size: 1.1rem;
        font-weight: 700;
        color: #fff;
        margin-bottom: 0.4rem;
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

    div[data-baseweb="tab-list"] button:hover,
    div[role="tablist"] button:hover {
        background-color: rgba(76, 175, 80, 0.05) !important;
    }

    div[data-testid="stTabsSelectionIndicator"],
    div[role="tablist"] + div[style*="background-color"],
    div[data-baseweb="tab-highlight"],
    .stTabs [style*="background-color"],
    .stTabs [style*="background-color"] + div {
        background-color: #4CAF50 !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Header Section ---
st.title(t["skills_title"])
st.markdown(f"*{t['skills_subtitle']}*")
st.markdown("---")

# --- Tabs for Tech Stack ---
tab1, tab2, tab3, tab4 = st.tabs(
    [
        t["skills_tab_fe"],
        t["skills_tab_be"],
        t["skills_tab_cloud"],
        t["skills_tab_other"],
    ]
)

with tab1:
    col1, col2 = st.columns(2, gap="large")
    with col1:
        st.markdown(f"### {t['skills_prog_title']}")
        st.markdown("**Next.js / React**")
        st.progress(0.95)
        st.markdown("**TypeScript / JavaScript**")
        st.progress(0.90)
        st.markdown("**Angular**")
        st.progress(0.80)
        st.markdown("**HTML5 / CSS3 / Tailwind**")
        st.progress(0.95)
    with col2:
        st.markdown(f"### {t['skills_focus_title']}")
        st.markdown(
            f"""
            <div class="skill-card">
                <div class="skill-title">{t['skills_fe_card_title']}</div>
                {t['skills_fe_card_desc']}
            </div>
            """,
            unsafe_allow_html=True,
        )

with tab2:
    col1, col2 = st.columns(2, gap="large")
    with col1:
        st.markdown(f"### {t['skills_prog_title']}")
        st.markdown("**Node.js / Express / NestJs**")
        st.progress(0.85)
        st.markdown("**Python (FastAPI / Streamlit / Flask)**")
        st.progress(0.80)
        st.markdown("**SQL (PostgreSQL / MySQL), NoSQL (MongoDB)**")
        st.progress(0.85)
        st.markdown("**REST / GraphQL / tRPC APIs**")
        st.progress(0.90)
    with col2:
        st.markdown(f"### {t['skills_focus_title']}")
        st.markdown(
            f"""
            <div class="skill-card">
                <div class="skill-title">{t['skills_be_card_title']}</div>
                {t['skills_be_card_desc']}
            </div>
            """,
            unsafe_allow_html=True,
        )

with tab3:
    col1, col2 = st.columns(2, gap="large")
    with col1:
        st.markdown(f"### {t['skills_prog_title']}")
        st.markdown("**AWS Services (EC2, S3, IAM, Lambda)**")
        st.progress(0.85)
        st.markdown("**Docker Containerization**")
        st.progress(0.80)
        st.markdown("**CI/CD Automation (GitHub Actions)**")
        st.progress(0.75)
        st.markdown("**Linux / Bash Scripting**")
        st.progress(0.80)
    with col2:
        st.markdown(f"### {t['skills_focus_title']}")
        st.markdown(
            f"""
            <div class="skill-card">
                <div class="skill-title">{t['skills_cloud_card_title']}</div>
                {t['skills_cloud_card_desc']}
            </div>
            """,
            unsafe_allow_html=True,
        )

with tab4:
    col1, col2 = st.columns(2, gap="large")
    with col1:
        st.markdown(f"### {t['skills_prog_title']}")
        st.markdown(f"**{t['skills_other_math']}**")
        st.progress(0.90)
        st.markdown("**Git / Version Control**")
        st.progress(0.95)
        st.markdown("**WordPress / Webflow Ecosystems**")
        st.progress(0.90)
        st.markdown(f"**{t['skills_other_quality']}**")
        st.progress(0.85)
    with col2:
        st.markdown(f"### {t['skills_focus_title']}")
        st.markdown(
            f"""
            <div class="skill-card">
                <div class="skill-title">{t['skills_other_card_title']}</div>
                {t['skills_other_card_desc']}
            </div>
            """,
            unsafe_allow_html=True,
        )

# --- Footer ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.info(t["footer_tip"])
