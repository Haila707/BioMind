import requests


class ClinicalTrialsService:

    BASE_URL = "https://clinicaltrials.gov"

    def search(self, query: str):

        try:

            return [
                {
                    "source": "ClinicalTrials.gov",
                    "title": f"Clinical Trials related to {query}",
                    "url": f"https://clinicaltrials.gov/search?term={query.replace(' ', '+')}"
                }
            ]

        except Exception:

            return []