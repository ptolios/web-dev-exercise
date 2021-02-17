import time
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


def index(request):
    return render(request, "index.html", {})

def api(request):
    # This is the request to the '/api/sort' endpoint
    # The POST data to provide must be a JSON object
    # with a key named "data" that contains 
    # the list to be sorted
    if request.method == "POST":
        result = request.POST.getlist("data")
        # simulate the delay of the response...
        print("Waiting....")
        time.sleep(2)
        print("Go!")
        return JsonResponse(sorted(result), safe=False)
    else:
        return HttpResponse("<h1>This API endpoint only accepts POST requests</h1>")
