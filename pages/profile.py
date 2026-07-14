import streamlit as st
from auth import require_login
from translations import TRANSLATIONS

require_login()

if "lang" not in st.session_state:
    st.session_state.lang = "en"

t = TRANSLATIONS[st.session_state.lang]

# --- Page Configuration ---
st.set_page_config(
    page_title=t["nav_profile"], page_icon=":material/account_circle:", layout="wide"
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

    /* Metric Cards Styling with Equal Height Enforced */
    .metric-card {
        background-color: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 1rem;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        
        /* Enforce equal height using Flexbox and min-height */
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        min-height: 110px;
        height: 100%;
    }
    .metric-value {
        font-size: 1.6rem;
        font-weight: 700;
        color: #4CAF50;
        margin-bottom: 0.2rem;
        line-height: 1.2;
    }
    .metric-label {
        font-size: 0.75rem;
        color: #b0b0b0;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        line-height: 1.3;
    }
    
    /* Cover Letter Highlight Container */
    .cover-letter-container {
        background-color: rgba(255, 255, 255, 0.02);
        border: 1px solid rgba(76, 175, 80, 0.2);
        border-left: 4px solid #4CAF50;
        padding: 1.5rem;
        border-radius: 4px 16px 16px 4px;
        margin-bottom: 2rem;
        line-height: 1.6;
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

# --- Header / Identity Block ---
st.title("Behdad Tabrizi")
st.subheader(t["prof_sub_title"])
st.markdown(
    f"<small style='color: #888;'>{t['prof_location']}</small>", unsafe_allow_html=True
)
st.markdown("---")

# --- Key Metrics Row (4 Cards with absolute height alignment) ---
kpi1, kpi2, kpi3, kpi4 = st.columns(4)

with kpi1:
    st.markdown(
        f'<div class="metric-card"><div class="metric-value">{t["kpi_exp_val"]}</div><div class="metric-label">{t["kpi_exp_lbl"]}</div></div>',
        unsafe_allow_html=True,
    )
with kpi2:
    st.markdown(
        f'<div class="metric-card"><div class="metric-value">{t["kpi_ihk_val"]}</div><div class="metric-label">{t["kpi_ihk_lbl"]}</div></div>',
        unsafe_allow_html=True,
    )
with kpi3:
    st.markdown(
        f'<div class="metric-card"><div class="metric-value">{t["kpi_math_val"]}</div><div class="metric-label">{t["kpi_math_lbl"]}</div></div>',
        unsafe_allow_html=True,
    )
with kpi4:
    st.markdown(
        f'<div class="metric-card"><div class="metric-value">{t["kpi_aws_val"]}</div><div class="metric-label">{t["kpi_aws_lbl"]}</div></div>',
        unsafe_allow_html=True,
    )

st.markdown("<br>", unsafe_allow_html=True)

# --- Main Layout (Two Columns Split) ---
left_col, right_col = st.columns([1.8, 1], gap="large")

with left_col:
    st.markdown(f"### {t['prof_pitch_title']}")
    st.markdown(t["prof_pitch_body"], unsafe_allow_html=True)

    st.markdown(f"### {t['section_cv_overview']}")

    tab_exp, tab_edu, tab_skills = st.tabs(
        [t["tab_exp"], t["tab_edu"], t["tab_skills"]]
    )

    with tab_exp:
        st.markdown(t["exp_content"])
    with tab_edu:
        st.markdown(t["edu_content"])
    with tab_skills:
        sc1, sc2 = st.columns(2)
        with sc1:
            st.markdown(t["skills_tech_head"])
            st.markdown(t["skills_tech_body"])
        with sc2:
            st.markdown(t["skills_soft_head"])
            st.markdown(t["skills_soft_body"])

with right_col:
    # Verhindert den Zeilenumbruch der Überschrift "Kernkompetenzen"
    st.markdown(
        f"""
        <h3 style="white-space: nowrap; overflow: hidden; text-overflow: ellipsis; margin-bottom: 1rem;">
            {t['sidebar_head']}
        </h3>
        """,
        unsafe_allow_html=True,
    )

    with st.container(border=True):
        st.markdown(t["sidebar_facts"])
        st.markdown(t["sidebar_fact_nat"])
        st.markdown(t["sidebar_fact_lic"])
        st.markdown("---")
        st.markdown(t["sidebar_lang_head"])
        st.markdown(t["sidebar_lang_body"])
        st.markdown("---")
        st.markdown(t["sidebar_stack_head"])
        st.markdown("- **Frontend:** Next.js, React, TypeScript, Angular")
        st.markdown("- **Backend:** Node.js, Express, Python, REST APIs")
        st.markdown("- **Cloud & DB:** AWS, Docker, PostgreSQL, CI/CD")

# --- Footer ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.info(t["footer_tip"])
