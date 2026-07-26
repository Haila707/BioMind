import uuid
from datetime import datetime


class ReportBuilder:

    def build(self, request: str, responses: list):

        report = {
            "report_id": str(uuid.uuid4()),
            "generated_at": datetime.utcnow().isoformat(),
            "status": "completed",
            "version": "1.1.0",
            "request": request,
            "analysis": "",
            "scientific_evidence": "",
            "healthcare_recommendation": "",
            "confidence": None,
            "references": [],
            "warnings": [],
            "next_steps": []
        }

        confidence_scores = []

        for response in responses:

            confidence_scores.append(response["confidence"])

            report["references"].extend(response["references"])
            report["warnings"].extend(response["warnings"])
            report["next_steps"].extend(response["next_steps"])

            if response["agent"] == "Laboratory Agent":
                report["analysis"] = response["summary"]

            elif response["agent"] == "Research Agent":
                report["scientific_evidence"] = response["summary"]

            elif response["agent"] == "Healthcare Agent":
                report["healthcare_recommendation"] = response["summary"]

        if confidence_scores:
            report["confidence"] = round(
                sum(confidence_scores) / len(confidence_scores),
                2
            )

        return report