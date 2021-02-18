from django.test import Client, TestCase

from utils import quick_sort


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
                "grocery",
            ]
        }
        response = client.post("/api/sort/", post_data)
        self.assertEqual(sorted(post_data["data"]), response.json())


class TestQuickSort(TestCase):
    def test_quicksort(self):
        original: list = [
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
        sorted_list: list = original.copy()
        sorted_list = quick_sort(sorted_list, 0, len(sorted_list) - 1)
        self.assertEqual(sorted(original), sorted_list)
