# lib/GetRequester.py

import requests

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content  # raw body (bytes)

    def load_json(self):
        response = requests.get(self.url)
        return response.json()  # parsed Python dict/list
