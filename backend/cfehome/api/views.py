import json
from django.http import JsonResponse

def api_home(request, *args, **kwargs):
    body = request.body
    print(body)
    return JsonResponse({'message': 'Hi there, this is your Django API response!!'})
