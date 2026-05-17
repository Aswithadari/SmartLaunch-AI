import streamlit as st
import time
import zipfile
from io import BytesIO
import sqlite3
from datetime import datetime

# Configure the visual layout of the page
st.set_page_config(page_title="SmartLaunch AI", layout="wide")

# SQLite Database Helper Functions
def init_database():
    """Initialize SQLite database with uploads table"""
    conn = sqlite3.connect('history.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS uploads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            project_name TEXT NOT NULL,
            tech_stack TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def save_upload_record(project_name, tech_stack):
    """Save a new upload record to the database"""
    conn = sqlite3.connect('history.db')
    cursor = conn.cursor()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute('''
        INSERT INTO uploads (timestamp, project_name, tech_stack)
        VALUES (?, ?, ?)
    ''', (timestamp, project_name, tech_stack))
    conn.commit()
    conn.close()

def get_recent_uploads(limit=5):
    """Retrieve the most recent upload records"""
    conn = sqlite3.connect('history.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT timestamp, project_name, tech_stack
        FROM uploads
        ORDER BY id DESC
        LIMIT ?
    ''', (limit,))
    records = cursor.fetchall()
    conn.close()
    return records

# Initialize database on app start
init_database()

# Sidebar - Recent Uploads History
st.sidebar.title("📜 Recent Uploads History")
recent_uploads = get_recent_uploads(5)
if recent_uploads:
    for timestamp, project_name, tech_stack in recent_uploads:
        st.sidebar.markdown(f"**{project_name}**")
        st.sidebar.caption(f"{tech_stack} • {timestamp}")
        st.sidebar.divider()
else:
    st.sidebar.info("No upload history yet. Analyze your first project!")

# Main Header
st.title("🚀 SmartLaunch AI: Automated Repository Setup & Onboarding Engine")
st.subheader("Drop an undocumented project folder here to instantly generate your setup guide.")

# Drag and Drop File Uploader
uploaded_file = st.file_uploader("Upload Project Folder (.zip)", type=["zip"])

# Execution Button
if st.button("Analyze Repository"):
    if uploaded_file is not None:
        # We will connect watsonx Orchestrate here later!
        with st.spinner("Analyzing repository structure..."):
            # Extract file list from uploaded ZIP
            zip_bytes = BytesIO(uploaded_file.read())
            with zipfile.ZipFile(zip_bytes, 'r') as zip_ref:
                file_list = zip_ref.namelist()
            
            # Rule-based project analysis
            project_type = "Unknown Stack"
            commands = []
            
            # Check for Python project
            if any('requirements.txt' in file_path for file_path in file_list):
                project_type = "Python 🐍"
                commands.append("pip install -r requirements.txt")
                commands.append("python app.py")
            
            # Check for Node.js project
            if any('package.json' in file_path for file_path in file_list):
                project_type = "Node.js 🟢"
                commands = []  # Reset commands for Node.js
                commands.append("npm install")
                commands.append("npm start")
            
            # Check for missing .env file
            missing_env = not any('.env' in file_path for file_path in file_list)
            
            time.sleep(2) # Simulating processing time
            
        # Save upload record to database
        save_upload_record(uploaded_file.name, project_type)
        
        st.success("Analysis Complete! Setup mapped.")
        
        # Display detected tech stack
        st.metric(label="Detected Tech Stack", value=project_type)
        
        # Warning for missing .env file
        if missing_env:
            st.warning("⚠️ Missing environment configuration (.env) file detected!")
        
        # Interactive Dashboard with Tabs
        tab1, tab2, tab3 = st.tabs(["📋 Quickstart Commands", "📖 Generated README.md", "🎯 Onboarding Checklist"])
        
        with tab1:
            st.markdown("### Quickstart Commands")
            if commands:
                for cmd in commands:
                    st.code(cmd, language="bash")
            else:
                st.info("No specific commands detected for this project type.")
        
        with tab2:
            st.markdown("### Generated README.md")
            st.info("AI-generated README content will appear here once backend is connected.")
        
        with tab3:
            st.markdown("### Onboarding Checklist")
            st.checkbox("✅ Clone repository", value=False)
            st.checkbox("✅ Install dependencies", value=False)
            st.checkbox("✅ Configure environment variables", value=False)
            st.checkbox("✅ Run setup script", value=False)
            st.checkbox("✅ Start development server", value=False)
            st.checkbox("✅ Run tests", value=False)
    else:
        st.warning("Please upload a .zip file first!")

# Made with Bob
