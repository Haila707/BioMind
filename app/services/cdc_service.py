import requests


class CDCService:

    BASE_URL = "https://www.cdc.gov"

    def search(self, query: str):

        try:

            return [
                {
                    "source": "CDC",
                    "title": f"CDC Guidance related to {query}",
                    "url": f"https://www.cdc.gov/search/index.html?query={query.replace(' ', '%20')}"
                }
            ]

        except Exception:

            return []