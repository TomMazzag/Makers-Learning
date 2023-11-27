class CatFacts:

    def __init__(self, response):
        self.response = response

    def provide(self):
        return f"Cat fact: {self._get_cat_fact()['fact']}"

    # Again, don't stub this method.
    def _get_cat_fact(self):
        response = self.response.get("https://catfact.ninja/fact")
        return response.json()