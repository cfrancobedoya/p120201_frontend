from django.shortcuts import render, HttpResponse
import requests

# Create your views here.
# def ultrasonic(request):
#     return render(request, "ultrasonic/ultrasonic.html")

def ultrasonic(request):
    # Verifica si hay un parámetro value en la petición GET
    if 'value' in request.GET:
        value = request.GET['value']
        placeLatitude = request.GET['placeLatitude']
        placeLength = request.GET['placeLength']
        landArea = request.GET['landArea']
        # Verifica si el value no esta vacio
        if value:
            # Crea el json para realizar la petición POST al Web Service
            args = {
                'type': 'Ultrasonic', 
                'value': value, 
                'placeLatitude': placeLatitude,
                'placeLength': placeLength,
                'landArea': landArea,
            }
            response = requests.post('http://backendpython.azurewebsites.net/ultrasonics/', args)
            # Convierte la respuesta en JSON
            ultrasonic_json = response.json()

    # Realiza una petición GET al Web Services
    response = requests.get('http://backendpython.azurewebsites.net/ultrasonics/')
    # Convierte la respuesta en JSON
    ultrasonics = response.json()
    # Rederiza la respuesta en el template measure
    return render(request, "ultrasonic/ultrasonic.html", {'ultrasonics': ultrasonics})