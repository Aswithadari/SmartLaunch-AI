import zipfile
import io

def analyze_zip(uploaded_file):
    """Scans the in-memory ZIP file to detect project architecture."""
    try:
        with zipfile.ZipFile(io.BytesIO(uploaded_file.getvalue())) as z:
            file_list = z.namelist()
            file_count = len(file_list)
            
            # Default values
            project_type = "Unknown Stack"
            commands = []
            missing_env = True
            
            # Rule engine
            for file in file_list:
                if "requirements.txt" in file:
                    project_type = "Python 🐍"
                    commands = ["pip install -r requirements.txt", "python app.py"]
                elif "package.json" in file:
                    project_type = "Node.js 🟢"
                    commands = ["npm install", "npm start"]
                
                if ".env" in file:
                    missing_env = False
                    
            return {
                "success": True,
                "project_type": project_type,
                "commands": commands,
                "missing_env": missing_env,
                "file_count": file_count
            }
    except Exception as e:
        return {"success": False, "error": str(e)}
        