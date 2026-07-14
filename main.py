import os
import base64
from pathlib import Path
import streamlit as st
from dotenv import load_dotenv
from translations import TRANSLATIONS

load_dotenv()

# App paths
dir_path = Path(__file__).parent
PROFILE_IMAGE = dir_path / "files" / "profile.jpg"
LOGIN_BACKGROUND = dir_path / "files" / "login_background.png"
BACKGROUND = dir_path / "files" / "background.png"
LOGO_IMAGE = dir_path / "files" / "profile-img.png"

PASSWORD = os.getenv("PASSWORD")

# --- Initialize session state variables early ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "info_shown" not in st.session_state:
    st.session_state.info_shown = False
if "show_popup_next" not in st.session_state:
    st.session_state.show_popup_next = False
if "lang" not in st.session_state:
    st.session_state.lang = "de"  # Defaulting to German


# Callback to change language instantly
def change_language():
    if st.session_state.lang_selector == "Deutsch 🇩🇪":
        st.session_state.lang = "de"
    else:
        st.session_state.lang = "en"


# --- Render Language Selector in Sidebar (Available Everywhere) ---
_ = TRANSLATIONS[st.session_state.lang]  # Reference active language dictionary

# Safely determine the starting index based on current 'lang' state
default_index = 0 if st.session_state.lang == "de" else 1

st.sidebar.selectbox(
    label=f"⚙️ {_['lang_label']}",
    options=["Deutsch 🇩🇪", "English 🇬🇧"],
    index=default_index,
    key="lang_selector",
    on_change=change_language,
)


def hide_navigation():
    """Hides the navigation links/menu in the sidebar during login, but keeps the sidebar visible for the language selector."""
    st.markdown(
        """
        <style>
            /* Hides the auto-generated navigation section in the sidebar */
            div[data-testid="stSidebarNav"] {display: none;}
        </style>
        """,
        unsafe_allow_html=True,
    )


def login():
    """
    Display a password input form for the user.
    Returns True if the password is correct.
    """
    if not st.session_state.logged_in:
        set_background(LOGIN_BACKGROUND)
        st.title(_["login_title"])
        password_input = st.text_input(
            _["password_label"], type="password", key="pw_input"
        )

        if st.button(_["login_button"], use_container_width=True):
            if password_input == PASSWORD:
                st.session_state.logged_in = True
                st.success(_["login_success"])

                if not st.session_state.info_shown:
                    st.session_state.show_popup_next = True

                st.rerun()
            else:
                st.error(_["login_error"])
        return False

    else:
        return True


def set_background(background_image_path: Path):
    """Set a background image for the screen."""
    if not background_image_path.exists():
        return None

    with open(background_image_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()

        st.markdown(
            f"""
                <style>
                .stApp {{
                    background-image: linear-gradient(
                        rgba(0, 0, 0, 0.55),
                        rgba(0, 0, 0, 0.55)
                    ),
                    url("data:image/jpg;base64,{encoded_image}");
                    background-size: cover;
                    background-repeat: no-repeat;
                    background-position: center top;
                    background-attachment: fixed;
                }}

                .block-container {{
                    max-width: 55% !important;
                    background-color: rgba(255, 255, 255, 0.08);
                    border-radius: 15px;
                    padding: 2rem;
                    margin-top: 5rem;
                }}
                </style>
                """,
            unsafe_allow_html=True,
        )


def run() -> None:
    """Main function to set up and run the Streamlit app with navigation."""

    # Check login first
    if not login():
        hide_navigation()  # Only hides the navigation menu, leaving the language dropdown intact.
        return

    set_background(BACKGROUND)

    # --- Force Logo ABOVE the Navigation Menu ---
    if LOGO_IMAGE.exists():
        st.logo(str(LOGO_IMAGE))
        st.markdown(
            """
            <style>
                /* Add the margin below the entire header container */
                div[data-testid="stSidebarHeader"] {
                    padding-top: 0px !important;
                    padding-bottom: 0px !important;
                    margin-bottom: 4rem !important;
                }

                /* Apply your custom logo dimensions and top margin */
                .stLogo {
                  height: 90px !important; 
                  width: 90px !important; 
                  margin-top: 54px !important; 
                  border-radius: 50%;
                  object-fit: cover;
                  border: 3px solid #4CAF50;
                }
            </style>
            """,
            unsafe_allow_html=True,
        )

    # Navigation pages with dynamic language titles
    page = st.navigation(
        {
            "": [
                st.Page(
                    dir_path / "pages" / "profile.py",
                    title=_["nav_profile"],
                    icon=":material/account_circle:",
                ),
                st.Page(
                    dir_path / "pages" / "skills.py",
                    title=_["nav_skills"],
                    icon=":material/psychology:",
                ),
                st.Page(
                    dir_path / "pages" / "cv.py",
                    title=_["nav_cv"],
                    icon=":material/description:",
                ),
                st.Page(
                    dir_path / "pages" / "certifications.py",
                    title=_["nav_certifications"],
                    icon=":material/workspace_premium:",
                ),
                st.Page(
                    dir_path / "pages" / "projects.py",
                    title=_["nav_projects"],
                    icon=":material/deployed_code:",
                ),
                st.Page(
                    dir_path / "pages" / "contact.py",
                    title=_["nav_contact"],
                    icon=":material/mail:",
                ),
            ]
        }
    )

    page.run()


if __name__ == "__main__":
    run()
