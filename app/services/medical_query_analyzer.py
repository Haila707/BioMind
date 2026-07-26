import json

from app.ai.provider import AIProvider


class MedicalQueryAnalyzer:

    def __init__(self):
        self.ai = AIProvider()

    def analyze(self, request: str):

        prompt = f"""
You are a biomedical query analyzer.

Your task is to understand the user's medical request.

Extract every important biomedical concept.

Return ONLY valid JSON.

Schema:

{{
    "conditions": [],
    "laboratory_tests": [],
    "biomarkers": [],
    "genes": [],
    "microorganisms": [],
    "drugs": [],
    "keywords": []
}}

User Request:

{request}
"""

        response = self.ai.generate(prompt)

        try:
            return json.loads(response)

        except Exception:

            print("MedicalQueryAnalyzer JSON parsing failed.")

            return {
                "conditions": [],
                "laboratory_tests": [],
                "biomarkers": [],
                "genes": [],
                "microorganisms": [],
                "drugs": [],
                "keywords": []
            }