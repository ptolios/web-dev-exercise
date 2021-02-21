import json
from typing import Dict, List, Union
from django.test import TestCase

from utils import quick_sort


class TestApi(TestCase):
    def test_api_response(self):
        post_data: List = [
            "scene",
            "uncle",
            "tale",
            "aspect",
            "disease",
            "penalty",
            "procedure",
            "agreement",
            "relationship",
            "grocery",
        ]
        response = self.client.post(
            "/api/sort/", post_data, content_type="application/json"
        )
        self.assertEqual(sorted(post_data), response.json())

    def test_post_invalid_data(self):
        post_data: Dict[str, List] = {
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
                "grocery",
            ]
        }
        response = self.client.post(
            "/api/sort/", post_data, content_type="application/json"
        )
        self.assertEqual(response.status_code, 400)

        post_data: List[Union[str, int, float]] = [
            "scene",
            "uncle",
            "tale",
            "aspect",
            "disease",
            654,  # integer
            "procedure",
            "agreement",
            324.84,  # float
            "grocery",
        ]
        response = self.client.post(
            "/api/sort/", post_data, content_type="application/json"
        )
        self.assertEqual(response.status_code, 400)


class TestQuickSort(TestCase):
    def test_quicksort(self):
        original: List = [
            "scene",
            "uncle",
            "tale",
            "aspect",
            "disease",
            "penalty",
            "procedure",
            "agreement",
            "relationship",
            "grocery",
        ]
        sorted_list: List = original.copy()
        sorted_list = quick_sort(sorted_list, 0, len(sorted_list) - 1)
        self.assertEqual(sorted(original), sorted_list)
