analysis_prompt = """
Analyze the following candidate's CV data and provide a structured JSON response evaluating their suitability for the [JOB_TITLE] position at [COMPANY_NAME]. The job requires [REQUIREMENTS].

Expected response format:
{
  "executive_summary": {
    "overview": "Brief overview of the candidate's profile",
    "key_finding": "Most significant observation about the candidate",
    "recommendation": "Clear hiring recommendation",
    "overall_comments": "General assessment of fit"
  },
  "basic_qualification_check": {
    "education": {
      "meets_requirements": true/false,
      "candidate_education": "Candidate's highest relevant education",
      "required_education": "Required education level",
      "notes": "Specific notes about education match",
      "improvement_suggestions": ["Educational improvements if needed"]
    },
    "work_experience": {
      "meets_duration": true/false,
      "years_required": number,
      "years_actual": number,
      "notes": "Assessment of experience quality",
      "experience_quality_comments": "Detailed evaluation of experience",
      "areas_for_growth": ["Suggested areas for professional development"]
    },
    "technical_skills": {
      "required_skills": ["List of required skills"],
      "matching_skills": ["Skills the candidate has"],
      "missing_skills": ["Required skills the candidate lacks"],
      "proficiency_level": "Overall technical proficiency assessment",
      "skill_development_recommendations": [
        {
          "skill": "Skill name",
          "current_level": "Current proficiency",
          "target_level": "Required proficiency",
          "improvement_path": "Suggested path to reach target"
        }
      ]
    }
  },
  "position_specific_analysis": {
    "relevant_experience": [
      {
        "role": "Previous role",
        "company": "Company name",
        "duration": "Duration in role",
        "relevance_score": number (0-10),
        "key_achievements": ["Notable achievements"],
        "enhancement_suggestions": ["Ways to improve relevance"],
        "reviewer_comments": "Specific comments about this experience"
      }
    ],
    "transferable_skills": ["Skills applicable to new role"],
    "relevant_projects": [
      {
        "name": "Project name",
        "description": "Brief description",
        "skills_demonstrated": ["Skills shown"],
        "project_impact_analysis": "Impact assessment",
        "improvement_areas": ["Suggested improvements"]
      }
    ],
    "experience_enhancement_suggestions": {
      "recommended_projects": ["Suggested projects to undertake"],
      "suggested_roles": ["Intermediate roles if needed"],
      "skill_application_tips": ["How to better apply existing skills"]
    }
  },
  "strengths_and_weaknesses": {
    "key_strengths": [
      {
        "strength": "Identified strength",
        "relevance": "How it applies to the role",
        "leverage_suggestions": ["How to best use this strength"]
      }
    ],
    "gaps": [
      {
        "gap": "Identified gap",
        "impact": "Impact on role suitability",
        "mitigation_suggestion": "How to address",
        "development_timeline": "Expected time to develop",
        "recommended_resources": ["Resources for improvement"]
      }
    ],
    "cv_improvement_suggestions": {
      "content_improvements": ["Content enhancement suggestions"],
      "formatting_suggestions": ["Format improvement ideas"],
      "achievement_highlighting_tips": ["Better ways to showcase achievements"]
    }
  },
  "recommendation": {
    "suitability_score": number (0-100),
    "score_breakdown": {
      "technical_fit": number (0-100),
      "experience_fit": number (0-100),
      "education_fit": number (0-100),
      "overall_potential": number (0-100)
    },
    "interview_questions": [
      {
        "question": "Suggested question",
        "rationale": "Why ask this",
        "expected_response_points": ["What to look for in answer"]
      }
    ],
    "upskilling_recommendations": [
      {
        "skill": "Skill to develop",
        "suggested_resources": ["Learning resources"],
        "timeline": "Expected learning time",
        "priority_level": "Importance level"
      }
    ],
    "career_development_path": {
      "short_term_goals": ["Immediate development targets"],
      "long_term_potential": "Career growth potential",
      "growth_opportunities": ["Future opportunities"]
    }
  },
  "cv_enhancement_recommendations": {
    "structure_improvements": [
      {
        "section": "CV section",
        "current_state": "Current presentation",
        "suggested_changes": "Recommended changes",
        "expected_impact": "Impact of changes"
      }
    ],
    "content_enhancements": [
      {
        "area": "Area to improve",
        "suggestion": "Specific suggestion",
        "example": "Example implementation"
      }
    ],
    "professional_branding": {
      "linkedin_profile_suggestions": ["LinkedIn improvements"],
      "portfolio_recommendations": ["Portfolio enhancements"],
      "professional_certification_suggestions": ["Relevant certifications"]
    }
  },
  "optional_analysis": {
    "cultural_fit": {
      "alignment_score": number (0-100),
      "matching_values": ["Aligned values"],
      "potential_concerns": ["Cultural fit concerns"],
      "adaptation_suggestions": ["Ways to adapt"]
    },
    "salary_range": {
      "min": number,
      "max": number,
      "currency": "Currency code",
      "market_data_source": "Source of range",
      "negotiation_points": ["Negotiation considerations"]
    },
    "red_flags": {
      "employment_gaps": [
        {
          "period": "Gap timeframe",
          "duration": "Length of gap",
          "concern_level": "Level of concern",
          "explanation_suggestions": ["How to address"]
        }
      ],
      "inconsistencies": ["Noted inconsistencies"],
      "mitigation_strategies": ["How to address concerns"]
    }
  },
  "metadata": {
    "analysis_date": "ISO date string",
    "job_title": "Position analyzed for",
    "company_name": "Company name",
    "analyzer_comments": "Additional analyzer notes"
  }
}

Provide a detailed, objective analysis based on the CV data provided. Focus on concrete evidence from the CV rather than assumptions. For any gaps or concerns, provide constructive suggestions for improvement.
"""
