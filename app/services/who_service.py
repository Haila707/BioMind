import requests


class WHOService:

    SEARCH_URL = "https://www.who.int/search"

    def search_articles(self, query: str):

        try:

            response = requests.get(
                self.SEARCH_URL,
                params={
                    "query": query
                },
                timeout=20
            )

            if response.status_code != 200:

                return []

            return [
                {
                    "source": "WHO",
                    "title": "WHO Search Results",
                    "query": query,
                    "url": response.url
                }
            ]

        except Exception as e:

            print("WHO Service Error:", e)
            return []