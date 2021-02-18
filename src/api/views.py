import time
import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from utils import quick_sort


def index(request):
    return render(request, "index.html", {})

def api(request):
    # This is the request to the '/api/sort' endpoint
    # The POST data to provide must be a JSON object
    # with a key named "data" that contains 
    # the list to be sorted
    if request.method == "POST":
        # Since this is not form data we are receiving
        # we have to use request.body NOT request.POST, see url below
        # https://docs.djangoproject.com/en/3.1/ref/request-response/#django.http.HttpRequest.body
        result = json.loads(request.body.decode("utf-8")).get("data", [])
        # simulate the delay of the response...
        print("Waiting....")
        time.sleep(2)
        print("Go!")
        return JsonResponse(quick_sort(result, 0, len(result) - 1), safe=False)
    else:
        return HttpResponse("<h1>This API endpoint only accepts POST requests</h1>")
