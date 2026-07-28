from app.ai.provider import AIProvider
from app.ai.prompts import RESEARCH_PROMPT
from app.services.evidence_engine import EvidenceEngine
from app.services.medical_query_analyzer import MedicalQueryAnalyzer


class ResearchAgent:

    def __init__(self):

        self.name = "Research Agent"
        self.role = "Scientific Research"

        self.ai = AIProvider()
        self.evidence = EvidenceEngine()
        self.analyzer = MedicalQueryAnalyzer()

    def process(self, request: str, laboratory_result: dict):

        print("\n========== RESEARCH AGENT START ==========")

        # Analyze medical request
        medical_query = self.analyzer.analyze(request)

        print("=" * 70)
        print("Medical Query Analysis")
        print(medical_query)
        print("=" * 70)

        # Retrieve evidence
        evidence = self.evidence.search(medical_query)

        # Merge all evidence
        all_references = (
            evidence["pubmed"]
            + evidence["who"]
            + evidence["cdc"]
            + evidence["nice"]
            + evidence["clinical_trials"]
        )

        print("=" * 70)
        print("Evidence Summary")
        print("PubMed:", len(evidence["pubmed"]))
        print("WHO:", len(evidence["who"]))
        print("CDC:", len(evidence["cdc"]))
        print("NICE:", len(evidence["nice"]))
        print("ClinicalTrials:", len(evidence["clinical_trials"]))
        print("Total References:", len(all_references))
        print("=" * 70)

        prompt = f"""
{RESEARCH_PROMPT}

Original User Request:
{request}

Medical Query Analysis:
{medical_query}

Laboratory Analysis:
{laboratory_result["summary"]}

Scientific Evidence From Trusted Sources

PubMed:
{evidence["pubmed"]}

WHO:
{evidence["who"]}

CDC:
{evidence["cdc"]}

NICE:
{evidence["nice"]}

ClinicalTrials:
{evidence["clinical_trials"]}
"""

        print("=" * 70)
        print("Prompt Length:", len(prompt))
        print("=" * 70)

        print(">>>>>>>>>> CALLING OLLAMA <<<<<<<<<<")

        ai_response = self.ai.generate(prompt)

        print(">>>>>>>>>> OLLAMA FINISHED <<<<<<<<<<")
        print("AI Response Length:", len(ai_response))
        print("=" * 70)
        print("RESEARCH AGENT FINISHED")
        print("=" * 70)

        return {
            "agent": self.name,
            "role": self.role,
            "summary": ai_response,
            "confidence": 0.92,
            "references": all_references,
            "warnings": [],
            "next_steps": [
                "Review evidence quality.",
                "Compare international guidelines.",
                "Identify conflicting evidence.",
                "Generate evidence-based conclusion."
            ]
        }