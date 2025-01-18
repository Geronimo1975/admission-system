import os

def create_project_structure():
    base_dir = "/home/dci-student/Projects/admission-system"
    directories = [
        "config",
        "src",
        "templates",
        "tests",
        "uploads",
    ]
    files = {
        "config/config.yaml": "",
        "src/__init__.py": "",
        "src/app.py": "",
        "src/models.py": "",
        "src/auth.py": "",
        "src/gdpr.py": "",
        "src/document_upload.py": "",
        "src/university_portal.py": "",
        "src/chatbot.py": "",
        "src/voice_bot.py": "",
        "src/whatsapp_bot.py": "",
        "src/salesforce.py": "",
        "src/ai_evaluation.py": "",
        "src/video_interview_server.py": "",
        "src/email_sender.py": "",
        "templates/index.html": "",
        "templates/gdpr_dashboard.html": "",
        "templates/video_interview.html": "",
        "templates/university_dashboard.html": "",
        "templates/chat.html": "",
        "templates/agent_dashboard.html": "",
        "tests/__init__.py": "",
        "tests/test_auth.py": "",
        "tests/test_video_interview.py": "",
        "tests/test_ai_evaluation.py": "",
        "tests/test_salesforce.py": "",
        "tests/test_document_upload.py": "",
        "requirements.txt": "",
        "README.md": "# Admission University Project\n"
    }
    
    # Create directories
    for directory in directories:
        os.makedirs(os.path.join(base_dir, directory), exist_ok=True)
    
    # Create files
    for file_path, content in files.items():
        full_path = os.path.join(base_dir, file_path)
        with open(full_path, "w") as f:
            f.write(content)
    
    print(f"Project structure for '{base_dir}' created successfully!")

if __name__ == "__main__":
    create_project_structure()
