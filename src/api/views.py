import time
import json
from django.http import HttpResponseBadRequest, HttpResponseNotAllowed, JsonResponse
from django.shortcuts import render

from utils import quick_sort


def index(request):
    return render(request, "index.html", {})


def api(request):
    # This is the request to the '/api/sort' endpoint
    # The POST data to provide must be an array
    if request.method == "POST":
        # Since this is not form data we are receiving
        # we have to use request.body NOT request.POST, see url below
        # https://docs.djangoproject.com/en/3.1/ref/request-response/#django.http.HttpRequest.body
        result = json.loads(request.body.decode("utf-8"))
        # Validation
        # check if the payload is an array of strings
        if isinstance(result, list) and all([isinstance(item, str) for item in result]):
            # simulate the delay of the response...
            print("Waiting....")
            time.sleep(2)
            print("Go!")
            return JsonResponse(quick_sort(result, 0, len(result) - 1), safe=False)
        else:
            return HttpResponseBadRequest()
    else:
        return HttpResponseNotAllowed(["POST"], "<h1>This API endpoint only accepts POST requests</h1>")
