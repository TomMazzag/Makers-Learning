class ActivitySuggester:
    def __init__(self, requester):  # requester is usually `requests`
        self.requester = requester

    def suggest(self):
        response = self._make_request_to_api()
        return f"Why not: {response['activity']}"

    def _make_request_to_api(self):
        # We use 'self.requester' rather than 'requests'
        response = self.requester.get("http://www.boredapi.com/api/activity")
        return response.json()

