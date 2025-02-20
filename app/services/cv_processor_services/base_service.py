import json
import logging
from abc import ABC, abstractmethod

from app.models.cv_model import CVModel, Contact, Education, Experience, Project, Certification

logger = logging.getLogger(__name__)

class BaseService(ABC):
    @abstractmethod
    def _call_api(self, text: str) -> CVModel:
        """call the api of specific service."""
        pass

    def parse_cv(self, text: str) -> CVModel:
        structured_data: json = self._call_api(text)
        print(structured_data)

        name = structured_data.get("name", "N/A")
        title = structured_data.get("title", "N/A")
        contact_data = structured_data.get("contact", {})
        # Handle both missing and None cases for other_links
        contact_data["other_links"] = contact_data.get("other_links") or []
        contact = Contact(**contact_data)

        # Handle all list fields, converting None to empty list
        education = [
            Education(**edu) for edu in (structured_data.get("education") or [])
        ]
        experience = [
            Experience(**exp) for exp in (structured_data.get("experience") or [])
        ]
        projects = [
            Project(**proj) for proj in (structured_data.get("projects") or [])
        ]
        certifications = [
            Certification(**cert) for cert in (structured_data.get("certifications") or [])
        ]
        skills = structured_data.get("skills") or []
        skills_from_work_experience = structured_data.get("skills_from_work_experience") or []

        return CVModel(
            name=name,
            title=title,
            contact=contact,
            education=education,
            experience=experience,
            projects=projects,
            certifications=certifications,
            skills=skills,
            skills_from_work_experience=skills_from_work_experience
        )
