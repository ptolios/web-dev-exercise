import time
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


def api(request):
    if request.method == "POST":
        result = request.POST.getlist("data")
        print("Waiting....")
        time.sleep(2)
        print("Go!")
        return JsonResponse(sorted(result), safe=False)
    else:
        return HttpResponse("No GET data")
