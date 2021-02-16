from django.test import Client, TestCase
import json
from pprint import pprint


class TestApi(TestCase):
    def test_api_response(self):
        client = Client()
        post_data = {
            "data": [
                "scene",
                "uncle",
                "tale",
                "aspect",
                "disease",
                "penalty",
                "procedure",
                "agreement",
                "relationship",
                "grocery"
            ]
        }
        response = client.post("/api/sort/", post_data)
        self.assertEqual(sorted(post_data["data"]), response.json())
