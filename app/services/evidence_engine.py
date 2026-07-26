from app.services.pubmed_service import PubMedService
from app.services.who_service import WHOService
from app.services.cdc_service import CDCService
from app.services.nice_service import NICEService
from app.services.clinical_trials_service import ClinicalTrialsService


class EvidenceEngine:

    def __init__(self):

        self.pubmed = PubMedService()
        self.who = WHOService()
        self.cdc = CDCService()
        self.nice = NICEService()
        self.clinical_trials = ClinicalTrialsService()

    def search(self, medical_query: dict):

        evidence = {
            "pubmed": [],
            "who": [],
            "cdc": [],
            "nice": [],
            "clinical_trials": []
        }

        keywords = []

        # Conditions
        keywords.extend(medical_query.get("conditions", []))

        # Laboratory Tests
        for test in medical_query.get("laboratory_tests", []):

            if isinstance(test, dict):

                if test.get("testName"):
                    keywords.append(test["testName"])

                keywords.extend(test.get("parameters", []))

            else:
                keywords.append(str(test))

        # Biomarkers
        keywords.extend(medical_query.get("biomarkers", []))

        # Genes
        keywords.extend(medical_query.get("genes", []))

        # Microorganisms
        keywords.extend(medical_query.get("microorganisms", []))

        # Drugs
        keywords.extend(medical_query.get("drugs", []))

        # General Keywords
        keywords.extend(medical_query.get("keywords", []))

        cleaned_keywords = []

        for item in keywords:

            if isinstance(item, str):

                item = item.strip()

                if item:
                    cleaned_keywords.append(item)

        cleaned_keywords = list(dict.fromkeys(cleaned_keywords))

        search_query = " ".join(cleaned_keywords)

        print("=" * 70)
        print("Unified Evidence Engine")
        print("=" * 70)
        print("Search Query:")
        print(search_query)
        print("=" * 70)

        # ==========================
        # PubMed
        # ==========================
        try:
            evidence["pubmed"] = self.pubmed.search_articles(search_query)
            print(f"PubMed: {len(evidence['pubmed'])} articles")
        except Exception as e:
            print("PubMed Error:", e)

        # ==========================
        # WHO
        # ==========================
        try:
            evidence["who"] = self.who.search(search_query)
            print(f"WHO: {len(evidence['who'])} results")
        except Exception as e:
            print("WHO Error:", e)

        # ==========================
        # CDC
        # ==========================
        try:
            evidence["cdc"] = self.cdc.search(search_query)
            print(f"CDC: {len(evidence['cdc'])} results")
        except Exception as e:
            print("CDC Error:", e)

        # ==========================
        # NICE
        # ==========================
        try:
            evidence["nice"] = self.nice.search(search_query)
            print(f"NICE: {len(evidence['nice'])} results")
        except Exception as e:
            print("NICE Error:", e)

        # ==========================
        # ClinicalTrials
        # ==========================
        try:
            evidence["clinical_trials"] = self.clinical_trials.search(search_query)
            print(f"ClinicalTrials: {len(evidence['clinical_trials'])} results")
        except Exception as e:
            print("ClinicalTrials Error:", e)

        print("=" * 70)
        print("Evidence Retrieval Finished")
        print("=" * 70)

        return evidence