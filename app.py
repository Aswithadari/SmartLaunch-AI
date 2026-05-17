import streamlit as st
import database as db
import analyzer as az

# Page setup
st.set_page_config(page_title="SmartLaunch AI", layout="wide", initial_sidebar_state="expanded")

# Initialize database on startup
db.init_db()

# --- CUSTOM CSS INJECTION ---
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    /* Global Styles */
    * {
        font-family: 'Inter', sans-serif;
    }
    
    /* Main Title with Gradient */
    .main-title {
        font-size: 3.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #6366f1 0%, #4f46e5 50%, #7c3aed 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0.5rem;
        text-align: center;
        animation: fadeInDown 0.8s ease-out;
    }
    
    /* Subtitle Styling */
    .subtitle {
        text-align: center;
        color: #94a3b8;
        font-size: 1.2rem;
        font-weight: 500;
        margin-bottom: 2rem;
    }
    
    /* Glassmorphism Card Containers */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background: rgba(30, 41, 59, 0.6) !important;
        backdrop-filter: blur(10px) !important;
        border: 1px solid rgba(255, 255, 255, 0.05) !important;
        border-radius: 16px !important;
        padding: 1.5rem !important;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37) !important;
        transition: all 0.3s ease !important;
    }
    
    div[data-testid="stVerticalBlockBorderWrapper"]:hover {
        border: 1px solid rgba(99, 102, 241, 0.3) !important;
        box-shadow: 0 12px 40px 0 rgba(99, 102, 241, 0.2) !important;
        transform: translateY(-2px);
    }
    
    /* Premium Button Styling */
    .stButton > button {
        background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 0.75rem 2rem !important;
        font-weight: 600 !important;
        font-size: 1.1rem !important;
        box-shadow: 0 4px 15px 0 rgba(99, 102, 241, 0.4) !important;
        transition: all 0.3s ease !important;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px 0 rgba(99, 102, 241, 0.6) !important;
        background: linear-gradient(135deg, #7c3aed 0%, #6366f1 100%) !important;
    }
    
    .stButton > button:active {
        transform: translateY(0px) !important;
        box-shadow: 0 4px 15px 0 rgba(99, 102, 241, 0.4) !important;
    }
    
    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1e293b 0%, #0f172a 100%) !important;
        border-right: 1px solid rgba(255, 255, 255, 0.05) !important;
    }
    
    section[data-testid="stSidebar"] h1 {
        color: #e2e8f0 !important;
        font-weight: 700 !important;
    }
    
    /* Metric Card Styling */
    div[data-testid="stMetricValue"] {
        font-size: 2rem !important;
        font-weight: 700 !important;
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    div[data-testid="stMetricLabel"] {
        color: #94a3b8 !important;
        font-weight: 600 !important;
        font-size: 0.9rem !important;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* Tab Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: rgba(15, 23, 42, 0.5);
        padding: 0.5rem;
        border-radius: 12px;
    }
    
    .stTabs [data-baseweb="tab"] {
        background: transparent;
        border-radius: 8px;
        color: #94a3b8;
        font-weight: 600;
        padding: 0.75rem 1.5rem;
        transition: all 0.3s ease;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background: rgba(99, 102, 241, 0.1);
        color: #c7d2fe;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%) !important;
        color: white !important;
    }
    
    /* Alert Boxes */
    .stAlert {
        border-radius: 12px !important;
        border: none !important;
        backdrop-filter: blur(10px) !important;
    }
    
    /* Success Alert */
    div[data-testid="stAlert"][data-baseweb="notification"] > div:first-child {
        background: rgba(16, 185, 129, 0.1) !important;
        border-left: 4px solid #10b981 !important;
    }
    
    /* Warning Alert */
    .stWarning {
        background: rgba(245, 158, 11, 0.1) !important;
        border-left: 4px solid #f59e0b !important;
    }
    
    /* Info Alert */
    .stInfo {
        background: rgba(59, 130, 246, 0.1) !important;
        border-left: 4px solid #3b82f6 !important;
    }
    
    /* Code Block Styling */
    .stCodeBlock {
        background: rgba(15, 23, 42, 0.8) !important;
        border: 1px solid rgba(99, 102, 241, 0.2) !important;
        border-radius: 8px !important;
    }
    
    /* File Uploader */
    div[data-testid="stFileUploader"] {
        background: rgba(15, 23, 42, 0.5) !important;
        border: 2px dashed rgba(99, 102, 241, 0.3) !important;
        border-radius: 12px !important;
        padding: 2rem !important;
        transition: all 0.3s ease !important;
    }
    
    div[data-testid="stFileUploader"]:hover {
        border-color: rgba(99, 102, 241, 0.6) !important;
        background: rgba(99, 102, 241, 0.05) !important;
    }
    
    /* Checkbox Styling */
    .stCheckbox {
        padding: 0.5rem 0;
    }
    
    .stCheckbox > label {
        color: #cbd5e1 !important;
        font-weight: 500 !important;
    }
    
    /* Animations */
    @keyframes fadeInDown {
        from {
            opacity: 0;
            transform: translateY(-20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes pulse {
        0%, 100% {
            opacity: 1;
        }
        50% {
            opacity: 0.8;
        }
    }
    
    /* Spinner Animation */
    div[data-testid="stSpinner"] > div {
        border-color: #6366f1 !important;
        border-top-color: transparent !important;
    }
    
    /* Section Headers */
    h3 {
        color: #e2e8f0 !important;
        font-weight: 700 !important;
        margin-bottom: 1rem !important;
    }
    
    /* Divider */
    hr {
        border-color: rgba(255, 255, 255, 0.1) !important;
        margin: 2rem 0 !important;
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR: HISTORY ---
with st.sidebar:
    st.title("📜 Activity Log")
    st.markdown("Recent repository scans:")
    history = db.get_recent_history()
    for row in history:
        with st.container(border=True):
            st.caption(f"⏱️ {row[0]}")
            st.markdown(f"**Repo:** {row[1]}")
            st.markdown(f"**Stack:** {row[2]}")

# --- MAIN INTERFACE ---
st.markdown('<h1 class="main-title">🚀 SmartLaunch AI</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Automated Repository Setup & Onboarding Engine</p>', unsafe_allow_html=True)
st.markdown("---")

left_col, right_col = st.columns([1, 2], gap="large")

with left_col:
    st.markdown("### 📥 Workspace Upload")
    with st.container(border=True):
        uploaded_file = st.file_uploader("Drag & drop project archive", type=["zip"])
        analyze_btn = st.button("⚡ Run Smart Launch", use_container_width=True, type="primary")

with right_col:
    st.markdown("### 📊 Engine Output")
    
    if analyze_btn and uploaded_file is not None:
        with st.spinner("🤖 Orchestrating analyzer modules..."):
            result = az.analyze_zip(uploaded_file)
            
        if result["success"]:
            # Log to local SQLite database
            db.log_upload(uploaded_file.name, result["project_type"], result["file_count"])
            
            st.success(f"🎉 Analysis Complete! Scanned {result['file_count']} files safely.")
            
            # Metric Display
            with st.container(border=True):
                st.metric(label="Detected Tech Stack", value=result["project_type"])
            
            if result["missing_env"]:
                st.warning("⚠️ Warning: No configuration environment (.env) file detected in the root hierarchy.")
            
            # Interactive Tabs
            tab1, tab2 = st.tabs(["📋 Setup Guide", "🎯 Progress Checklist"])
            
            with tab1:
                st.markdown("#### Terminal Setup Commands:")
                for cmd in result["commands"]:
                    st.code(cmd, language="bash")
            
            with tab2:
                st.markdown("#### Sandbox Progress Checkpoints:")
                st.checkbox("Initialize environmental workspace state")
                st.checkbox("Download dependencies from package registry")
                st.checkbox("Execute local initialization scripts")
        else:
            st.error(f"Failed to parse target archive: {result['error']}")
            
    elif analyze_btn and uploaded_file is None:
        st.warning("Please feed a `.zip` archive file structure into the upload workspace boundary first.")
    else:
        st.info("Awaiting input data streams. Upload a project file structural compressed archive to view live diagnostic manual generations.")

# Made with Bob
