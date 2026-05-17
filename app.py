import streamlit as st
import database as db
import analyzer as az
import orchestrator as ox

# Page setup - Keep centered layout per AGENTS.md rules
st.set_page_config(page_title="SmartLaunch AI", layout="centered", initial_sidebar_state="expanded")

# Initialize database on startup
db.init_db()

# --- ADVANCED ANTIGRAVITY CSS SYSTEM ---
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    
    /* Global Styles */
    * {
        font-family: 'Inter', sans-serif;
    }
    
    /* Main App Background */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #0f172a 100%);
    }
    
    /* Main Title with Gradient */
    .main-title {
        font-size: 3.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 50%, #a855f7 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0.5rem;
        text-align: center;
        animation: fadeInDown 0.8s ease-out;
        text-shadow: 0 0 40px rgba(99, 102, 241, 0.3);
    }
    
    /* Subtitle Styling */
    .subtitle {
        text-align: center;
        color: #94a3b8;
        font-size: 1.2rem;
        font-weight: 500;
        margin-bottom: 2rem;
    }
    
    /* ANTIGRAVITY FLOATING CARDS */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background: rgba(17, 24, 39, 0.7) !important;
        backdrop-filter: blur(16px) !important;
        border: 1px solid rgba(139, 92, 246, 0.2) !important;
        border-top: 2px solid transparent !important;
        border-image: linear-gradient(90deg, #6366f1, #8b5cf6, #a855f7) 1 !important;
        border-radius: 16px !important;
        padding: 2rem !important;
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.5), 0 10px 10px -5px rgba(0, 0, 0, 0.04) !important;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
        position: relative;
    }
    
    div[data-testid="stVerticalBlockBorderWrapper"]::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 2px;
        background: linear-gradient(90deg, #6366f1, #8b5cf6, #a855f7);
        border-radius: 16px 16px 0 0;
    }
    
    div[data-testid="stVerticalBlockBorderWrapper"]:hover {
        transform: translateY(-4px) scale(1.01);
        box-shadow: 0 25px 50px -12px rgba(99, 102, 241, 0.4), 0 0 30px rgba(139, 92, 246, 0.3) !important;
        border: 1px solid rgba(139, 92, 246, 0.4) !important;
    }
    
    /* PREMIUM BUTTON STYLING WITH LIFT EFFECT */
    .stButton > button {
        background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 0.875rem 2.5rem !important;
        font-weight: 700 !important;
        font-size: 1.1rem !important;
        box-shadow: 0 10px 25px -5px rgba(99, 102, 241, 0.5), 0 0 20px rgba(139, 92, 246, 0.3) !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        text-transform: uppercase;
        letter-spacing: 1px;
        position: relative;
        overflow: hidden;
    }
    
    .stButton > button::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
        transition: left 0.5s;
    }
    
    .stButton > button:hover::before {
        left: 100%;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px) scale(1.02) !important;
        box-shadow: 0 15px 35px -5px rgba(99, 102, 241, 0.7), 0 0 30px rgba(139, 92, 246, 0.5) !important;
        background: linear-gradient(135deg, #7c3aed 0%, #a855f7 100%) !important;
    }
    
    .stButton > button:active {
        transform: translateY(-1px) scale(0.98) !important;
        box-shadow: 0 8px 20px -5px rgba(99, 102, 241, 0.5) !important;
    }
    
    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #111827 0%, #0f172a 100%) !important;
        border-right: 1px solid rgba(139, 92, 246, 0.2) !important;
        box-shadow: 5px 0 20px rgba(0, 0, 0, 0.3);
    }
    
    section[data-testid="stSidebar"] h1 {
        color: #e2e8f0 !important;
        font-weight: 700 !important;
    }
    
    /* Metric Card Styling */
    div[data-testid="stMetricValue"] {
        font-size: 2.5rem !important;
        font-weight: 800 !important;
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    div[data-testid="stMetricLabel"] {
        color: #94a3b8 !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
        text-transform: uppercase;
        letter-spacing: 1.5px;
    }
    
    /* ADVANCED TAB STYLING */
    .stTabs [data-baseweb="tab-list"] {
        gap: 12px;
        background: rgba(17, 24, 39, 0.6);
        padding: 0.75rem;
        border-radius: 16px;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(139, 92, 246, 0.2);
    }
    
    .stTabs [data-baseweb="tab"] {
        background: transparent;
        border-radius: 10px;
        color: #94a3b8;
        font-weight: 600;
        padding: 0.875rem 2rem;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        border: 1px solid transparent;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background: rgba(99, 102, 241, 0.15);
        color: #c7d2fe;
        transform: translateY(-2px);
        border: 1px solid rgba(139, 92, 246, 0.3);
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%) !important;
        color: white !important;
        box-shadow: 0 8px 20px -5px rgba(99, 102, 241, 0.5) !important;
        transform: translateY(-2px);
    }
    
    /* Alert Boxes with Floating Effect */
    .stAlert {
        border-radius: 12px !important;
        border: none !important;
        backdrop-filter: blur(10px) !important;
        box-shadow: 0 10px 20px -5px rgba(0, 0, 0, 0.3) !important;
    }
    
    /* Success Alert */
    div[data-testid="stAlert"][data-baseweb="notification"] > div:first-child {
        background: rgba(16, 185, 129, 0.15) !important;
        border-left: 4px solid #10b981 !important;
    }
    
    /* Warning Alert */
    .stWarning {
        background: rgba(245, 158, 11, 0.15) !important;
        border-left: 4px solid #f59e0b !important;
    }
    
    /* Info Alert */
    .stInfo {
        background: rgba(59, 130, 246, 0.15) !important;
        border-left: 4px solid #3b82f6 !important;
    }
    
    /* Code Block Styling */
    .stCodeBlock {
        background: rgba(15, 23, 42, 0.9) !important;
        border: 1px solid rgba(99, 102, 241, 0.3) !important;
        border-radius: 10px !important;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3) !important;
    }
    
    /* File Uploader with Antigravity Effect */
    div[data-testid="stFileUploader"] {
        background: rgba(17, 24, 39, 0.6) !important;
        border: 2px dashed rgba(139, 92, 246, 0.4) !important;
        border-radius: 16px !important;
        padding: 2.5rem !important;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
        backdrop-filter: blur(10px);
    }
    
    div[data-testid="stFileUploader"]:hover {
        border-color: rgba(139, 92, 246, 0.7) !important;
        background: rgba(99, 102, 241, 0.08) !important;
        transform: translateY(-2px);
        box-shadow: 0 10px 25px -5px rgba(99, 102, 241, 0.3) !important;
    }
    
    /* Live Pipeline Status Cards */
    .pipeline-status {
        background: rgba(17, 24, 39, 0.8);
        border: 1px solid rgba(139, 92, 246, 0.3);
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        backdrop-filter: blur(12px);
        box-shadow: 0 8px 20px -5px rgba(0, 0, 0, 0.4);
        transition: all 0.3s ease;
    }
    
    .pipeline-status:hover {
        transform: translateX(5px);
        border-color: rgba(139, 92, 246, 0.5);
    }
    
    .skill-processing {
        color: #fbbf24;
        font-weight: 600;
        font-size: 1.1rem;
        animation: pulse 2s infinite;
    }
    
    .skill-complete {
        color: #10b981;
        font-weight: 600;
        font-size: 1.1rem;
    }
    
    /* Checkbox Styling */
    .stCheckbox {
        padding: 0.75rem 0;
    }
    
    .stCheckbox > label {
        color: #cbd5e1 !important;
        font-weight: 500 !important;
        font-size: 1.05rem !important;
    }
    
    /* Animations */
    @keyframes fadeInDown {
        from {
            opacity: 0;
            transform: translateY(-30px);
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
            opacity: 0.6;
        }
    }
    
    @keyframes glow {
        0%, 100% {
            box-shadow: 0 0 20px rgba(99, 102, 241, 0.3);
        }
        50% {
            box-shadow: 0 0 30px rgba(139, 92, 246, 0.5);
        }
    }
    
    /* Spinner Animation */
    div[data-testid="stSpinner"] > div {
        border-color: #8b5cf6 !important;
        border-top-color: transparent !important;
    }
    
    /* Section Headers */
    h3 {
        color: #e2e8f0 !important;
        font-weight: 700 !important;
        margin-bottom: 1.5rem !important;
        font-size: 1.5rem !important;
    }
    
    /* Divider */
    hr {
        border-color: rgba(139, 92, 246, 0.2) !important;
        margin: 2.5rem 0 !important;
    }
    
    /* Expander Styling */
    .streamlit-expanderHeader {
        background: rgba(17, 24, 39, 0.6) !important;
        border-radius: 10px !important;
        border: 1px solid rgba(139, 92, 246, 0.2) !important;
    }
    
    .streamlit-expanderHeader:hover {
        background: rgba(99, 102, 241, 0.1) !important;
        border-color: rgba(139, 92, 246, 0.4) !important;
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR: ACTIVITY LOG ---
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

# Upload Section
st.markdown("### 📥 Workspace Upload")
with st.container(border=True):
    uploaded_file = st.file_uploader("Drag & drop project archive", type=["zip"])
    analyze_btn = st.button("⚡ Run Smart Launch", use_container_width=True, type="primary")

st.markdown("---")

# Results Section
st.markdown("### 🤖 Orchestration Pipeline")

if analyze_btn and uploaded_file is not None:
    # Initial analysis
    result = az.analyze_zip(uploaded_file)
    
    if result["success"]:
        # Create orchestrator instance
        orchestrator = ox.create_orchestrator()
        
        # Live Pipeline View with st.empty() blocks
        st.markdown("#### 🔄 Live Execution Status")
        
        # Create placeholder containers for live updates
        skill1_placeholder = st.empty()
        skill2_placeholder = st.empty()
        skill3_placeholder = st.empty()
        
        # Store results for later display
        skill_results = {}
        
        # Execute workflow and display live updates
        for update in orchestrator.run_onboarding_workflow(result["file_list"], result["project_type"]):
            skill_name = update["skill_name"]
            status = update["status"]
            progress = update["progress"]
            
            # Determine which placeholder to update
            if progress == 33:
                placeholder = skill1_placeholder
            elif progress == 66:
                placeholder = skill2_placeholder
            else:
                placeholder = skill3_placeholder
            
            # Display processing status
            if status == "processing":
                placeholder.markdown(f"""
                <div class="pipeline-status">
                    <span class="skill-processing">🔄 Dispatching Skill {progress//33}: {skill_name}...</span>
                </div>
                """, unsafe_allow_html=True)
            else:
                placeholder.markdown(f"""
                <div class="pipeline-status">
                    <span class="skill-complete">✅ Skill {progress//33} Complete: {skill_name}</span>
                </div>
                """, unsafe_allow_html=True)
                
                # Store results
                skill_results[skill_name] = update["data"]
        
        # Log to database
        db.log_upload(uploaded_file.name, result["project_type"], result["file_count"])
        
        st.success(f"🎉 Orchestration Complete! Processed {result['file_count']} files through 3 AI skills.")
        
        st.markdown("---")
        
        # Interactive Content Tabs
        st.markdown("### 📊 Orchestration Results")
        
        tab1, tab2, tab3 = st.tabs([
            "🌳 Repository Structure", 
            "🔒 Security Audit", 
            "📋 Setup Guide"
        ])
        
        # Tab 1: Repository Structure (Skill 1)
        with tab1:
            if "Repository Structure Mapping" in skill_results:
                data = skill_results["Repository Structure Mapping"]
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Total Files", data["total_files"])
                with col2:
                    st.metric("Directories", data["total_directories"])
                with col3:
                    st.metric("Complexity", data["complexity_score"])
                
                st.markdown("#### 📁 Directory Tree Preview")
                with st.container(border=True):
                    tree_text = "\n".join(data["tree_preview"])
                    st.code(tree_text, language="")
                
                st.markdown("#### 📊 File Type Distribution")
                with st.container(border=True):
                    for ext, count in sorted(data["file_type_distribution"].items(), key=lambda x: x[1], reverse=True)[:10]:
                        st.markdown(f"**`.{ext}`** — {count} files")
        
        # Tab 2: Security Audit (Skill 2)
        with tab2:
            if "Security & Configuration Audit" in skill_results:
                data = skill_results["Security & Configuration Audit"]
                
                # Security Score
                score = data["security_score"]
                score_color = "#10b981" if score >= 70 else "#f59e0b" if score >= 40 else "#ef4444"
                
                st.markdown(f"""
                <div style="text-align: center; padding: 2rem; background: rgba(17, 24, 39, 0.6); border-radius: 12px; border: 2px solid {score_color};">
                    <h2 style="color: {score_color}; font-size: 3rem; margin: 0;">{score}/100</h2>
                    <p style="color: #94a3b8; margin: 0.5rem 0 0 0;">Security Score</p>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown("#### ⚠️ Security Findings")
                
                if data["security_risks"]:
                    for risk in data["security_risks"]:
                        severity_emoji = "🔴" if risk["severity"] == "high" else "🟡"
                        with st.container(border=True):
                            st.markdown(f"{severity_emoji} **{risk['issue']}**")
                            st.markdown(f"💡 *{risk['recommendation']}*")
                else:
                    st.success("✅ No security risks detected!")
                
                st.markdown("#### 📝 Recommendations")
                with st.container(border=True):
                    for rec in data["recommendations"]:
                        st.markdown(f"• {rec}")
                
                if data["exposed_keys_count"] > 0:
                    st.warning(f"⚠️ Found {data['exposed_keys_count']} files that may contain sensitive data")
        
        # Tab 3: Setup Guide (Skill 3)
        with tab3:
            if "Onboarding Asset Generation" in skill_results:
                data = skill_results["Onboarding Asset Generation"]
                
                st.markdown("#### ⚡ Quick Start Commands")
                with st.container(border=True):
                    for cmd in data["terminal_commands"]:
                        st.markdown(f"**Step {cmd['step']}:** {cmd['description']}")
                        st.code(cmd["command"], language="bash")
                
                st.markdown("#### ✅ Setup Checklist")
                with st.container(border=True):
                    for step in data["quick_start_steps"]:
                        st.checkbox(step, key=f"check_{step}")
                
                st.markdown("#### 🎫 Tracking Tickets")
                for ticket in data["tracking_tickets"]:
                    with st.expander(f"{ticket['id']}: {ticket['title']}"):
                        st.markdown(f"**Priority:** {ticket['priority']}")
                        st.markdown(f"**Status:** {ticket['status']}")
                        st.markdown(f"**Description:** {ticket['description']}")
                
                st.markdown("#### 🛠️ Prerequisites")
                with st.container(border=True):
                    for tool in data["prerequisite_tools"]:
                        st.markdown(f"• {tool}")
                
                st.info(f"⏱️ Estimated Setup Time: **{data['estimated_setup_time']}**")
    else:
        st.error(f"❌ Failed to parse archive: {result['error']}")
        
elif analyze_btn and uploaded_file is None:
    st.warning("⚠️ Please upload a `.zip` archive file first.")
else:
    st.info("💡 Upload a project archive and click **Run Smart Launch** to begin orchestration.")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #64748b; font-size: 0.9rem; padding: 1rem;">
    Powered by IBM watsonx Orchestrate • Made with Bob
</div>
""", unsafe_allow_html=True)

# Made with Bob
