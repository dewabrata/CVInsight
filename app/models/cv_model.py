from typing import List, Optional, Dict
from pydantic import BaseModel, Field
from datetime import datetime

class EducationQualificationCheck(BaseModel):
    meets_requirements: bool
    candidate_education: str
    required_education: str
    notes: str
    improvement_suggestions: List[str]

class WorkExperienceCheck(BaseModel):
    meets_duration: bool
    years_required: int
    years_actual: int
    notes: str
    experience_quality_comments: str
    areas_for_growth: List[str]

class SkillDevelopmentRecommendation(BaseModel):
    skill: str
    current_level: str
    target_level: str
    improvement_path: str

class TechnicalSkillsCheck(BaseModel):
    required_skills: List[str]
    matching_skills: List[str]
    missing_skills: List[str]
    proficiency_level: str
    skill_development_recommendations: List[SkillDevelopmentRecommendation]

class BasicQualificationCheck(BaseModel):
    education: EducationQualificationCheck
    work_experience: WorkExperienceCheck
    technical_skills: TechnicalSkillsCheck

class ExecutiveSummary(BaseModel):
    overview: str
    key_finding: str
    recommendation: str
    overall_comments: str

class RelevantExperience(BaseModel):
    role: str
    company: str
    duration: str
    relevance_score: float
    key_achievements: List[str]
    enhancement_suggestions: List[str]
    reviewer_comments: str

class RelevantProject(BaseModel):
    name: str
    description: str
    skills_demonstrated: List[str]
    project_impact_analysis: str
    improvement_areas: List[str]

class ExperienceEnhancementSuggestions(BaseModel):
    recommended_projects: List[str]
    suggested_roles: List[str]
    skill_application_tips: List[str]

class PositionSpecificAnalysis(BaseModel):
    relevant_experience: List[RelevantExperience]
    transferable_skills: List[str]
    relevant_projects: List[RelevantProject]
    experience_enhancement_suggestions: ExperienceEnhancementSuggestions

class Strength(BaseModel):
    strength: str
    relevance: str
    leverage_suggestions: List[str]

class Gap(BaseModel):
    gap: str
    impact: str
    mitigation_suggestion: str
    development_timeline: str
    recommended_resources: List[str]

class CVImprovementSuggestions(BaseModel):
    content_improvements: List[str]
    formatting_suggestions: List[str]
    achievement_highlighting_tips: List[str]

class StrengthsAndWeaknesses(BaseModel):
    key_strengths: List[Strength]
    gaps: List[Gap]
    cv_improvement_suggestions: CVImprovementSuggestions

class Education(BaseModel):
    degree: Optional[str] = None
    field_of_study: Optional[str] = None
    institution: Optional[str] = None
    location: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    result: Optional[str] = None


class Experience(BaseModel):
    position: Optional[str] = None
    company: Optional[str] = None
    location: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    responsibilities: Optional[str] = None


class Project(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    technologies_used: List[str] = Field(default_factory=list)


class Certification(BaseModel):
    name: Optional[str] = None
    issuing_organization: Optional[str] = None
    issue_date: Optional[str] = None
    expiration_date: Optional[str] = None
    credential_id: Optional[str] = None


class Contact(BaseModel):
    email: Optional[str] = None
    phone: Optional[str] = None
    location: Optional[str] = None
    linkedin: Optional[str] = None
    github: Optional[str] = None
    other_links: list[str] = Field(default_factory=list)


class InterviewQuestion(BaseModel):
    question: str
    rationale: str
    expected_response_points: List[str]

class UpskillingRecommendation(BaseModel):
    skill: str
    suggested_resources: List[str]
    timeline: str
    priority_level: str

class CareerDevelopmentPath(BaseModel):
    short_term_goals: List[str]
    long_term_potential: str
    growth_opportunities: List[str]

class ScoreBreakdown(BaseModel):
    technical_fit: float
    experience_fit: float
    education_fit: float
    overall_potential: float

class Recommendation(BaseModel):
    suitability_score: float
    score_breakdown: ScoreBreakdown
    interview_questions: List[InterviewQuestion]
    upskilling_recommendations: List[UpskillingRecommendation]
    career_development_path: CareerDevelopmentPath

class StructureImprovement(BaseModel):
    section: str
    current_state: str
    suggested_changes: str
    expected_impact: str

class ContentEnhancement(BaseModel):
    area: str
    suggestion: str
    example: str

class ProfessionalBranding(BaseModel):
    linkedin_profile_suggestions: List[str]
    portfolio_recommendations: List[str]
    professional_certification_suggestions: List[str]

class CVEnhancementRecommendations(BaseModel):
    structure_improvements: List[StructureImprovement]
    content_enhancements: List[ContentEnhancement]
    professional_branding: ProfessionalBranding

class EmploymentGap(BaseModel):
    period: str
    duration: str
    concern_level: str
    explanation_suggestions: List[str]

class CulturalFit(BaseModel):
    alignment_score: float
    matching_values: List[str]
    potential_concerns: List[str]
    adaptation_suggestions: List[str]

class SalaryRange(BaseModel):
    min: float
    max: float
    currency: str
    market_data_source: str
    negotiation_points: List[str]

class RedFlags(BaseModel):
    employment_gaps: List[EmploymentGap]
    inconsistencies: List[str]
    mitigation_strategies: List[str]

class OptionalAnalysis(BaseModel):
    cultural_fit: CulturalFit
    salary_range: SalaryRange
    red_flags: RedFlags

class Metadata(BaseModel):
    analysis_date: datetime
    job_title: str
    company_name: str
    analyzer_comments: str

class CVAnalysisResponse(BaseModel):
    executive_summary: ExecutiveSummary
    basic_qualification_check: BasicQualificationCheck
    position_specific_analysis: PositionSpecificAnalysis
    strengths_and_weaknesses: StrengthsAndWeaknesses
    recommendation: Recommendation
    cv_enhancement_recommendations: CVEnhancementRecommendations
    optional_analysis: OptionalAnalysis
    metadata: Metadata

class CVModel(BaseModel):
    name: str
    title: Optional[str] = None
    contact: Contact
    education: List[Education] = Field(default_factory=list)
    experience: List[Experience] = Field(default_factory=list)
    projects: List[Project] = Field(default_factory=list)
    certifications: List[Certification] = Field(default_factory=list)
    skills: List[str] = Field(default_factory=list)
    skills_from_work_experience: List[str] = Field(default_factory=list)
