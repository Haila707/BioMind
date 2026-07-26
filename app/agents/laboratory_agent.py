from app.ai.provider import AIProvider
from app.ai.prompts import LABORATORY_PROMPT


class LaboratoryAgent:

    def __init__(self):
        self.name = "Laboratory Agent"
        self.role = "Laboratory Specialist"
        self.ai = AIProvider()

    def process(self, request: str):

        prompt = f"""
{LABORATORY_PROMPT}

User Request:
{request}
"""

        ai_response = self.ai.generate(prompt)

        return {
            "agent": self.name,
            "role": self.role,

            # النص الكامل الذي يرجعه الذكاء الاصطناعي
            "summary": ai_response,

            # بيانات منظمة ستستخدمها بقية الـ Agents لاحقًا
            "abnormal_findings": [],
            "possible_conditions": [],
            "recommended_tests": [],

            "confidence": 0.85,
            "references": [],
            "warnings": [],

            "next_steps": [
                "Await scientific evidence.",
                "Correlate with clinical findings."
            ]
        }