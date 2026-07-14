# Behdad Tabrizi — Career Hub 🚀

A comprehensive, multi-lingual professional portfolio and career management application built with **Streamlit**. Showcasing a Full Stack Engineer's expertise, projects, skills, and achievements with an intuitive, password-protected interface.

> **Languages Supported:** 🇩🇪 Deutsch | 🇬🇧 English

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3.9+-3776ab?style=flat-square&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.51.0-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.3.3-150458?style=flat-square&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-1.26.4+-013243?style=flat-square&logo=numpy&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-Cloud-FF9900?style=flat-square&logo=amazon-aws&logoColor=white)
![Boto3](https://img.shields.io/badge/Boto3-AWS_SDK-FF9900?style=flat-square&logo=amazon-aws&logoColor=white)

**Core Technologies:**
- **Python** – Primary language for backend logic and application
- **Streamlit** – Interactive web framework for rapid development
- **Pandas** – Data manipulation and analysis
- **Pillow** – Image processing for profile and document handling
- **PyMuPDF** – PDF viewing and manipulation
- **Boto3** – AWS SDK for cloud integrations
- **Python-dotenv** – Environment variable management
- **Requests** – HTTP client for API calls

---

## 📋 Features

### 🔐 **Secure Access**
- Password-protected application with session management
- Multi-language support (German & English)
- Language selector in sidebar for instant switching

### 👤 **Profile Dashboard**
- Executive summary with professional pitch
- Key performance indicators (KPI cards)
- Profile image and branding
- Multilingual content display

### 📚 **Comprehensive Sections**
- **Profile** – Personal introduction and career overview
- **Skills** – Detailed technology stack and competencies
  - Frontend expertise (React, Next.js, Angular)
  - Backend & database management (Node.js, NestJS, Prisma)
  - Cloud & DevOps (AWS, Docker, Terraform)
  - Additional analytical skills
- **CV / Resume** – PDF viewer and upload capability
- **Projects** – Showcase of major professional projects with descriptions
- **Certifications** – Professional credentials and achievements
- **Contact** – Direct messaging and social network links

### 🌍 **Multi-Language Support**
- Full German (Deutsch) translations
- Complete English interface
- Seamless language switching without page reload

### 🎨 **Modern UI/UX**
- Professional background images
- Custom Streamlit styling
- Logo branding in sidebar
- Responsive design
- Interactive navigation

---

## 📂 Project Structure

```
behdad-tabrizi-careerhub/
├── main.py                    # Entry point with authentication & routing
├── translations.py            # Multi-language content (DE & EN)
├── pages/                     # Multi-page application
│   ├── profile.py            # Profile dashboard & CV overview
│   ├── skills.py             # Technical skills showcase
│   ├── cv.py                 # CV/Resume viewer
│   ├── projects.py           # Professional projects gallery
│   ├── certifications.py      # Credentials display
│   └── contact.py            # Contact form & social links
├── files/                     # Static assets
│   ├── profile.jpg           # Profile photograph
│   ├── profile-img.png       # Logo image
│   ├── login_background.png  # Login screen background
│   └── background.png        # App background
├── requirements.txt           # Python dependencies
├── .env                       # Environment variables (PASSWORD)
└── .streamlit/               # Streamlit configuration
```

### How It Works

1. **Authentication Layer**: User must enter a password (stored in `.env`) to access the application
2. **Language Selection**: Language preference persists in session state
3. **Multi-Page Navigation**: Streamlit's navigation system routes between different sections
4. **Content Rendering**: Translations from `translations.py` are dynamically loaded based on selected language
5. **Static Assets**: Background images, logos, and profile pictures enhance UI/UX

---

## 🚀 Getting Started

### Prerequisites
- Python 3.9 or higher
- pip package manager
- Virtual environment (recommended)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/deroso2017/behdad-tabrizi-careerhub.git
   cd behdad-tabrizi-careerhub
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Create a `.env` file in the root directory:
   ```
   PASSWORD=your_secure_password_here
   ```

5. **Add required assets (optional):**
   Create a `files/` directory and add:
   - `profile.jpg` – Your profile photo
   - `profile-img.png` – Logo/circular profile image
   - `login_background.png` – Login page background
   - `background.png` – Application background

6. **Run the application:**
   ```bash
   streamlit run main.py
   ```

The app will open at `http://localhost:8501` in your default browser.

---

## 📖 Usage

### Basic Navigation
1. Enter the password (from your `.env` file) to log in
2. Use the sidebar to navigate between sections:
   - **Profile** – View career overview
   - **Skills** – Explore technical expertise
   - **CV** – Download or view resume
   - **Projects** – Browse project portfolio
   - **Certifications** – View credentials
   - **Contact** – Get in touch

### Language Switching
- Click the language selector (⚙️) in the top-right sidebar
- Choose between "Deutsch 🇩🇪" or "English 🇬🇧"
- Content refreshes instantly in the selected language

### Admin Features
- Upload or update CV/Resume PDF
- Modify password in `.env` file
- Update profile information via `translations.py`

---

## 🔧 Configuration

### Environment Variables (`.env`)
```
PASSWORD=YourSecurePasswordHere
```

### Customization
Edit `translations.py` to update:
- Profile information and pitch
- Project descriptions and details
- Skill listings and technologies
- Navigation labels
- Any multilingual content

---

## 🌐 Cloud Integration

The application is designed for AWS deployment:
- **Boto3** support for cloud services integration
- Environment-based configuration
- Scalable Streamlit hosting options

---

## 📄 License

**All Rights Reserved**

This project and its source code are proprietary and confidential. The code, design, and content may not be copied, modified, distributed, published, sublicensed, or used for commercial or private purposes without prior written permission from the owner.

Unauthorized use of this software or any part of its source code is strictly prohibited.

For permission requests or inquiries, please contact the project owner.

---

## 👨‍💼 About the Portfolio Owner

**Behdad Tabrizi** — Full Stack Engineer | IT Specialist in Application Development

- 📍 Located in Cologne, Germany
- 🎓 B.Sc. in Mathematics | IHK Certified in Application Development
- 💼 7+ years of IT experience
- ☁️ AWS Cloud Certified (2026)
- 🌍 Multilingual: Farsi, Turkish, Azerbaijani, German, English

---

## 🤝 Contributing

This is a personal portfolio project. Contributions are not accepted. For collaboration inquiries, please contact the owner.

---

## 📬 Get in Touch

Connect through the **Contact** section in the application or visit the portfolio at your hosted Streamlit instance.

---

**Built with ❤️ to showcase professional achievements and expertise in Full Stack Development.**