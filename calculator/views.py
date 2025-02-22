from django.shortcuts import render
from django.http import JsonResponse
from .utils import calculate_distance

def distance_view(request):
    iata1 = request.GET.get('iata1')
    iata2 = request.GET.get('iata2')

    if not iata1 or not iata2:
        return JsonResponse({'error': 'Please provide two IATA codes'}, status=400)

    distance = calculate_distance(iata1,iata2)
    if distance is None:
        return JsonResponse({'error': 'One or both airports not found'}, status=404)

    return JsonResponse({'distance_km': round(distance, 2)})