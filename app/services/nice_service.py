import requests


class NICEService:

    BASE_URL = "https://www.nice.org.uk"

    def search(self, query: str):

        try:

            return [
                {
                    "source": "NICE",
                    "title": f"NICE Guidance related to {query}",
                    "url": f"https://www.nice.org.uk/search?q={query.replace(' ', '+')}"
                }
            ]

        except Exception:

            return []