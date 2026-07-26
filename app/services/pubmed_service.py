import requests


class PubMedService:

    BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"

    def search(self, query: str, max_results: int = 5):
        """
        Search PubMed and return PubMed IDs.
        """

        response = requests.get(
            f"{self.BASE_URL}/esearch.fcgi",
            params={
                "db": "pubmed",
                "term": query,
                "retmode": "json",
                "retmax": max_results,
                "sort": "relevance"
            },
            timeout=20
        )

        response.raise_for_status()

        data = response.json()

        return data["esearchresult"]["idlist"]

    def fetch_details(self, pmids: list):
        """
        Fetch article details from PubMed.
        """

        if not pmids:
            return []

        response = requests.get(
            f"{self.BASE_URL}/esummary.fcgi",
            params={
                "db": "pubmed",
                "id": ",".join(pmids),
                "retmode": "json"
            },
            timeout=20
        )

        response.raise_for_status()

        data = response.json()

        articles = []

        for pmid in pmids:

            article = data["result"].get(pmid)

            if not article:
                continue

            articles.append({
                "source": "PubMed",
                "pmid": pmid,
                "title": article.get("title"),
                "journal": article.get("fulljournalname"),
                "year": article.get("pubdate"),
                "authors": [
                    author.get("name")
                    for author in article.get("authors", [])
                ],
                "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
            })

        return articles

    def search_articles(self, query: str, max_results: int = 5):
        """
        Search PubMed and return article details.
        """

        pmids = self.search(query, max_results)

        return self.fetch_details(pmids)