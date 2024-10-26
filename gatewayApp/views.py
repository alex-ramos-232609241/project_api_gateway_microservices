import json
import requests
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Microservice URLs
USER_SERVICE_URL = 'http://localhost:8001/users/'
ORDER_SERVICE_URL = 'http://localhost:8002/orders/'
PRODUCT_SERVICE_URL = 'http://localhost:8003/products/'

@csrf_exempt
def proxy_users(request, path):
    url = USER_SERVICE_URL + path
    headers = dict(request.headers)

    if request.method == "GET":
        response = requests.get(url, headers=request.headers)
    elif request.method == "POST":
        try:
            data = json.loads(request.body.decode('utf-8')) if request.body else {}
        except json.JSONDecodeError:
            return HttpResponse("Invalid JSON", status=400)
        response = requests.post(url, json=data, headers=headers)
    
    elif request.method == "PUT":
        try:
            data = json.loads(request.body.decode('utf-8')) if request.body else {}
        except json.JSONDecodeError:
            return HttpResponse("Invalid JSON", status=400)
        response = requests.put(url, json=data, headers=headers)
    elif request.method == "DELETE":
        response = requests.delete(url, headers=request.headers)

    return HttpResponse(response.content, status=response.status_code, content_type=response.headers['Content-Type'])

@csrf_exempt
def proxy_orders(request, path):

    url = ORDER_SERVICE_URL + path
    headers = dict(request.headers)

    if request.method == "GET":
    
        response = requests.get(url, headers=request.headers)
    
    elif request.method == "POST":
    
        try:
            data = json.loads(request.body.decode('utf-8')) if request.body else {}
        except json.JSONDecodeError:
            return HttpResponse("Invalid JSON", status=400)
        response = requests.post(url, json=data, headers=headers)
    
    elif request.method == "PUT":
        try:
            data = json.loads(request.body.decode('utf-8')) if request.body else {}
        except json.JSONDecodeError:
            return HttpResponse("Invalid JSON", status=400)
        response = requests.put(url, json=data, headers=headers)

    elif request.method == "DELETE":
        response = requests.delete(url, headers=request.headers)

    return HttpResponse(response.content, status=response.status_code, content_type=response.headers['Content-Type'])

@csrf_exempt
def proxy_products(request, path):

    url = PRODUCT_SERVICE_URL + path
    headers = dict(request.headers)

    if request.method == "GET":
       
        response = requests.get(url, headers=request.headers)
    
    elif request.method == "POST":
        
        try:
            data = json.loads(request.body.decode('utf-8')) if request.body else {}
        
        except json.JSONDecodeError:
            return HttpResponse("Invalid JSON", status=400)
        response = requests.post(url, json=data, headers=headers)
    
    elif request.method == "PUT":
        try:
            data = json.loads(request.body.decode('utf-8')) if request.body else {}
        except json.JSONDecodeError:
            return HttpResponse("Invalid JSON", status=400)
        response = requests.put(url, json=data, headers=headers)
    
    elif request.method == "DELETE":
        response = requests.delete(url, headers=request.headers)

    return HttpResponse(response.content, status=response.status_code, content_type=response.headers['Content-Type'])
