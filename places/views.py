import requests
from django.conf import settings
from django.http import JsonResponse
from django.views import View

def nominatim_search(request):
    query = request.GET.get('q', 'museum')
    url = 'https://nominatim.openstreetmap.org/search'
    params = {
        'q': query,
        'format': 'json',
        'limit': 5,
    }
    headers = {
        'User-Agent': 'watu-test-app/1.0 (contact@example.com)'  # Replace with your contact info
    }
    response = requests.get(url, params=params, headers=headers)
    data = response.json()
    return JsonResponse(data, safe=False)
