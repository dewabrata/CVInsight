import os
import time
from datetime import datetime

import requests
import streamlit as st

st.set_page_config(
    page_title="JuaraCoding - AI CV Parser",
    page_icon=":shark:",
    menu_items={
        'Get Help': "mailto:dewabrata@gmail.com",
        'About': "# Dewabrata. JuaraCoding. All rights reserved."
    }
)

model_options = {
    "DeepSeek (Local: R1-1.5B)": "deepseek-r1:1.5b",
    "DeepSeek (Local: R1-8B)": "deepseek-r1:8b",
    "DeepSeek (Local: R1-14B)": "deepseek-r1:14b",
    "DeepSeek (API)": "deepseek-api",
    "Gemini (Google)": "gemini",
    "ChatGPT (OpenAI)": "chatgpt",
    "Ollama (Local: custom)": "ollama",
    "Claude (Antrhopic)": "claude"
}

# Get the backend URL from environment variables
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000/api/v1")

# Custom CSS to enhance UI
st.markdown(
    """
    <style>
        .stApp { margin-top: -50px; }
        hr { border: 1px solid #ddd; }
        .scrollable-container { height: 400px; overflow-y: auto; }
    </style>
    """,
    unsafe_allow_html=True,
)

def format_date(date_str):
    """Formats a date string from 'YYYY-MM-DD' to 'Month YYYY'."""
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").strftime("%B %Y")
    except Exception as e:
        return date_str  # Return as is if formatting fails

def display_cv_data(cv_data):
    """Helper function to display CV data"""
    # Create two columns
    col1, col2 = st.columns([2, 1])  # 2:1 ratio for better visibility

    # Column 1: Formatted CV
    with col1:
        st.subheader("📜 Extracted Information")
        st.write("---")
        st.write(f"**👤 Name:** {cv_data.get('name', 'N/A')}")
        st.write(f"**📧 Title:** {cv_data.get('title', 'N/A')}")

        # Contact
        if "contact" in cv_data and cv_data["contact"]:
            contact = cv_data["contact"]
            st.write("---")
            st.subheader("📞 Contact")
            st.write(f"**Email:** {contact.get('email', 'N/A')}")
            st.write(f"**Phone:** {contact.get('phone', 'N/A')}")
            st.write(f"**Location:** {contact.get('location', 'N/A')}")
            st.write(f"**Linkedin:** {contact.get('linkedin', 'N/A')}")
            st.write(f"**Github:** {contact.get('github', 'N/A')}")
            if "other_links" in contact and contact["other_links"]:
                st.write(f"**Other Links:**")
                for link in contact["other_links"]:
                    st.markdown(f"- [{link}]({link})")

        # Education
        if "education" in cv_data and cv_data["education"]:
            st.write("---")
            st.subheader("🎓 Education")
            for edu in cv_data["education"]:
                st.write(f"**{edu.get('degree', 'N/A')} in {edu.get('field_of_study', 'N/A')}**")
                st.write(f"🏫 {edu.get('institution', 'N/A')}")
                st.write(f"📍 {edu.get('location', 'N/A')}")
                st.write(f"🗓️ {format_date(edu.get('start_date', 'N/A'))} - {format_date(edu.get('end_date', 'N/A'))}")
                st.markdown("<hr style='border:1px solid #ccc; margin:5px 0;'>", unsafe_allow_html=True)

        # Work Experience
        if "experience" in cv_data and cv_data["experience"]:
            st.write("---")
            st.subheader("💼 Work Experience")
            for exp in cv_data["experience"]:
                st.write(f"**{exp.get('position', 'N/A')} at {exp.get('company', 'N/A')}**")
                st.write(f"📍 {exp.get('location', 'N/A')}")
                st.write(f"🗓️ {format_date(exp.get('start_date', 'N/A'))} - {format_date(exp.get('end_date', 'N/A'))}")
                st.write(f"📝 {exp.get('responsibilities', 'N/A')}")
                st.markdown("<hr style='border:1px solid #ccc; margin:5px 0;'>", unsafe_allow_html=True)

        # Projects
        if "projects" in cv_data and cv_data["projects"]:
            st.write("---")
            st.subheader("📁 Projects")
            for project in cv_data["projects"]:
                st.write(f"**{project.get('title', 'N/A')}**")
                st.write(f"📝 {project.get('description', 'N/A')}")
                st.write(f"🛠 Technologies: {', '.join(project.get('technologies_used', []))}")
                st.write(f"🗓️ {format_date(project.get('start_date', 'N/A'))} - {format_date(project.get('end_date', 'N/A'))}")
                st.markdown("<hr style='border:1px solid #ccc; margin:5px 0;'>", unsafe_allow_html=True)

        # Certifications
        if "certifications" in cv_data and cv_data["certifications"]:
            st.write("---")
            st.subheader("📜 Certifications")
            for cert in cv_data["certifications"]:
                st.write(f"**{cert.get('name', 'N/A')}**")
                st.write(f"🏢 {cert.get('issuing_organization', 'N/A')}")
                st.write(f"🗓️ {format_date(cert.get('issue_date', 'N/A'))} - {format_date(cert.get('expiration_date', 'N/A'))}")
                st.write(f"🔖 Credential ID: {cert.get('credential_id', 'N/A')}")
                st.markdown("<hr style='border:1px solid #ccc; margin:5px 0;'>", unsafe_allow_html=True)

        # Skills
        if "skills" in cv_data and cv_data["skills"]:
            st.write("---")
            st.subheader("🛠 Skills")
            st.write(", ".join(cv_data["skills"]))

        # Skills from work experience
        if "skills_from_work_experience" in cv_data and cv_data["skills_from_work_experience"]:
            st.write("---")
            st.subheader("🛠 Skills from work experience")
            st.write(", ".join(cv_data["skills_from_work_experience"]))

    # Column 2: Raw JSON Data
    with col2:
        st.subheader("🛠 Raw JSON Data")
        st.json(cv_data)

def main():
    # Initialize session state
    if 'cv_data' not in st.session_state:
        st.session_state.cv_data = None
    if 'model_type' not in st.session_state:
        st.session_state.model_type = None

    st.title("JuaraCoding - AI CV Parser")
    st.write("PDF Extractor menggunakan LLM AI.")
    st.write("")
    
    # File uploader
    uploaded_file = st.file_uploader("Upload a CV (.pdf)", type="pdf", help="Only PDF files are supported.")

    if uploaded_file is not None:
        # Dropdown for selecting the parsing method
        model_type = st.selectbox(
            "Select LLM Model",
            options=list(model_options.keys()),
            index=0,
            help="Choose the LLM model for CV parsing."
        )
        st.session_state.model_type = model_type

        # Parse button
        if st.button("🚀 Parse CV", type="primary"):
            with st.spinner("🔍 Processing CV..."):
                start_time = time.time()
                try:
                    # Prepare the file for sending
                    files = {"file": (uploaded_file.name, uploaded_file, uploaded_file.type)}
                    params = {"model_type": model_options[model_type]}
                    response = requests.post(f"{BACKEND_URL}/parse-cv/", files=files, params=params)
                    execution_time = time.time() - start_time
                    
                    if response.status_code == 200:
                        st.session_state.cv_data = response.json()
                        st.success(f"✅ CV Parsing Successful! (Execution Time: {execution_time:.3f} seconds)")
                    else:
                        st.error(f"❌ Error: {response.status_code} - {response.text}")

                except requests.exceptions.RequestException as e:
                    st.error(f"⚠️ Failed to connect to the backend: {e}")
                except Exception as e:
                    st.error(f"⚠️ An unexpected error occurred: {e}")

        # Display CV data if available
        if st.session_state.cv_data:
            display_cv_data(st.session_state.cv_data)

            # Analysis Section
            st.write("---")
            st.subheader("📊 CV Analysis")
            with st.form("analysis_form"):
                job_title = st.text_input("Job Title", help="Enter the position title")
                company_name = st.text_input("Company Name", help="Enter the company name")
                requirements = st.text_area("Job Requirements", help="Enter key job requirements")
                analyze_button = st.form_submit_button("🎯 Analyze CV", type="primary")

            if analyze_button:
                with st.spinner("🔍 Analyzing CV..."):
                    try:
                        # Send raw JSON data for analysis
                        params = {
                            "model_type": model_options[st.session_state.model_type],
                            "job_title": job_title,
                            "company_name": company_name,
                            "requirements": requirements
                        }
                        # Convert CVModel to dict if needed
                        cv_json = st.session_state.cv_data
                        if hasattr(cv_json, 'dict'):
                            cv_json = cv_json.dict()
                            
                        response = requests.post(
                            f"{BACKEND_URL}/analyze-cv/",
                            json=cv_json,
                            params=params
                        )
                        
                        if response.status_code == 200:
                            analysis_result = response.json()
                            
                            st.subheader("📊 Analysis Results")
                            st.write("---")

                            # Raw JSON Data in expander
                            with st.expander("🛠 Raw Analysis Data"):
                                st.json(analysis_result)
                            
                            # Executive Summary
                            st.subheader("📝 Executive Summary")
                            # Display sections if they exist in the response
                            if "executive_summary" in analysis_result:
                                exec_summary = analysis_result["executive_summary"]
                                st.write(f"**Overview:** {exec_summary.get('overview', 'N/A')}")
                                st.write(f"**Key Finding:** {exec_summary.get('key_finding', 'N/A')}")
                                st.write(f"**Recommendation:** {exec_summary.get('recommendation', 'N/A')}")
                                st.write(f"**Overall Comments:** {exec_summary.get('overall_comments', 'N/A')}")
                            
                            # Basic Qualification Check
                            if "basic_qualification_check" in analysis_result:
                                st.write("---")
                                st.subheader("✅ Basic Qualification Check")
                                qual_check = analysis_result["basic_qualification_check"]
                                
                                # Education
                                if "education" in qual_check:
                                    st.write("**🎓 Education**")
                                    edu = qual_check["education"]
                                    st.write(f"Meets Requirements: {'✅' if edu.get('meets_requirements', False) else '❌'}")
                                    st.write(f"Required: {edu.get('required_education', 'N/A')}")
                                    st.write(f"Candidate Has: {edu.get('candidate_education', 'N/A')}")
                                    st.write(f"Notes: {edu.get('notes', 'N/A')}")
                                
                                # Work Experience
                                if "work_experience" in qual_check:
                                    st.write("**💼 Work Experience**")
                                    exp = qual_check["work_experience"]
                                    st.write(f"Meets Duration: {'✅' if exp.get('meets_duration', False) else '❌'}")
                                    st.write(f"Required Years: {exp.get('years_required', 'N/A')}")
                                    st.write(f"Actual Years: {exp.get('years_actual', 'N/A')}")
                                    st.write(f"Quality Assessment: {exp.get('experience_quality_comments', 'N/A')}")
                                
                                # Technical Skills
                                if "technical_skills" in qual_check:
                                    st.write("**🛠 Technical Skills**")
                                    skills = qual_check["technical_skills"]
                                    st.write("Required Skills:", ", ".join(skills.get("required_skills", [])))
                                    st.write("Matching Skills:", ", ".join(skills.get("matching_skills", [])))
                                    st.write("Missing Skills:", ", ".join(skills.get("missing_skills", [])))
                            
                            # Recommendation
                            if "recommendation" in analysis_result:
                                st.write("---")
                                st.subheader("🎯 Final Recommendation")
                                rec = analysis_result["recommendation"]
                                st.write(f"**Suitability Score:** {rec.get('suitability_score', 'N/A')}/100")
                                
                                # Score Breakdown
                                if "score_breakdown" in rec:
                                    scores = rec["score_breakdown"]
                                    st.write("**Score Breakdown:**")
                                    st.write(f"- Technical Fit: {scores.get('technical_fit', 'N/A')}/100")
                                    st.write(f"- Experience Fit: {scores.get('experience_fit', 'N/A')}/100")
                                    st.write(f"- Education Fit: {scores.get('education_fit', 'N/A')}/100")
                                    st.write(f"- Overall Potential: {scores.get('overall_potential', 'N/A')}/100")
                                
                        else:
                            st.error(f"❌ Analysis Error: {response.status_code} - {response.text}")
                    except Exception as e:
                        st.error(f"⚠️ Analysis failed: {e}")

if __name__ == "__main__":
    main()
