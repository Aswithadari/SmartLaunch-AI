import streamlit as st
import database as db
import analyzer as az

# Page setups
st.set_page_config(page_title="SmartLaunch AI", layout="wide", initial_sidebar_state="expanded")

# Initialize database on startup
db.init_db()

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
st.title("🚀 SmartLaunch AI")
st.subheader("Automated Repository Setup & Onboarding Engine")
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