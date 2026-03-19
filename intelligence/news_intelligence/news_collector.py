import requests

class NewsCollector:

    def fetch(self):

        url = "https://newsapi.org/v2/top-headlines?category=business&apiKey=YOUR_KEY"

        try:
            r = requests.get(url, timeout=5)
            data = r.json()
            return [a["title"] for a in data["articles"]]
        except:
            return []
