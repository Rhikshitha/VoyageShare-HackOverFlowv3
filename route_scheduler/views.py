from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def home(request):
    try:
        token = request.COOKIES.get('jwt')
        if not token:
            print(token)
            return redirect("login")

            
        return render(request,"index.html")
    except Exception as e:
        return HttpResponse(f"{e}")

def passenger(request):
    try:
        token = request.COOKIES.get('jwt')
        if not token:
            print(token)
            return redirect("login")


        return render(request,"passangerMap.html")
    except Exception as e:
        return HttpResponse(f"{e}")


@csrf_exempt
def set_route(request):
    data = json.loads(request.body.decode('utf-8'))
    route=data["route"]
    source=data["source"]
    destination=data["destination"]
    print(source,destination)
    return JsonResponse({"data":"Done"})