class Selector:

    def select_agents(self, request: str):

        request = request.lower()

        laboratory_keywords = [
            "cbc",
            "blood",
            "lab",
            "laboratory",
            "sample",
            "culture",
            "urine",
            "microbiology",
            "analysis",
            "test",
            "result"
        ]

        research_keywords = [
            "research",
            "study",
            "paper",
            "journal",
            "evidence",
            "pubmed",
            "systematic review",
            "meta-analysis"
        ]

        healthcare_keywords = [
            "patient",
            "clinical",
            "hospital",
            "treatment",
            "guideline",
            "recommendation",
            "diagnosis",
            "care"
        ]

        # Laboratory requests
        if any(word in request for word in laboratory_keywords):
            return [
                "Laboratory Agent",
                "Research Agent",
                "Healthcare Agent"
            ]

        # Research requests
        if any(word in request for word in research_keywords):
            return [
                "Research Agent",
                "Healthcare Agent"
            ]

        # Healthcare requests
        if any(word in request for word in healthcare_keywords):
            return [
                "Healthcare Agent",
                "Research Agent"
            ]

        # Default
        return [
            "Laboratory Agent",
            "Research Agent",
            "Healthcare Agent"
        ]