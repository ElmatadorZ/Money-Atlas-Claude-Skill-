class NarrativeEngine:

    def detect(self, parsed_news):

        narratives = []

        for item in parsed_news:

            text = item["text"].lower()

            if "rate" in text or "inflation" in text:
                narratives.append({
                    "theme": "MONETARY_POLICY",
                    "bias": "hawkish"
                })

            if "war" in text or "conflict" in text:
                narratives.append({
                    "theme": "GEOPOLITICS",
                    "bias": "risk_off"
                })

        return narratives
