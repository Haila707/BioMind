from app.ai.provider import AIProvider
from app.ai.prompts import HEALTHCARE_PROMPT


class HealthcareAgent:

    def __init__(self):
        self.name = "Healthcare Agent"
        self.role = "Healthcare Decision Support"
        self.ai = AIProvider()

    def process(
        self,
        request: str,
        laboratory_result: dict,
        research_result: dict
    ):

        prompt = f"""
{HEALTHCARE_PROMPT}

User Request:
{request}

==================================================
LABORATORY ANALYSIS
==================================================

{laboratory_result["summary"]}

==================================================
SCIENTIFIC EVIDENCE
==================================================

{research_result["summary"]}

==================================================
YOUR ROLE
==================================================

You are the final Healthcare Decision Support Agent.

You have already received:
1. The Laboratory analysis.
2. The Scientific evidence.

Your responsibility is NOT to repeat them.

Focus only on:

- Patient safety.
- Clinical workflow.
- Practical healthcare recommendations.
- Risk assessment.
- Suggested follow-up investigations.
- Limitations of the available information.
- When urgent medical evaluation is recommended.

Avoid repeating laboratory values unless absolutely necessary.

Do not rewrite the Laboratory report.

Do not rewrite the Research report.

Provide only the final healthcare perspective.

Do not replace physician judgment.

If the laboratory findings suggest urgent intervention,
clearly explain why.

If additional investigations are needed,
list only the most clinically relevant ones.

If there is insufficient information,
state exactly what is missing before making recommendations.
"""

        ai_response = self.ai.generate(prompt)

        return {
            "agent": self.name,
            "role": self.role,
            "summary": ai_response,
            "confidence": 0.88,
            "references": [],
            "warnings": [],
            "next_steps": [
                "Review clinical guidelines.",
                "Assess patient safety.",
                "Plan appropriate follow-up."
            ]
        }