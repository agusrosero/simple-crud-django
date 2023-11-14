from django.shortcuts import render
from .models import Person
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


# Create your views here.
@csrf_exempt
def list_person(request):
    if request.method == 'GET':
        persons = Person.objects.all()
        person_json = [{'id': person.id, 'name': person.name, 'last_name': person.last_name, 'age': person.age, 'address': person.address} for person in persons]
        return JsonResponse({'Personas': person_json})
    return JsonResponse({'Mensaje': 'Solicitud no valida'})

@csrf_exempt
def list_by_id(request, id):
    if request.method == 'GET':
        person = Person.objects.get(id=id)
        data = {
            'id': person.id,
            'name': person.name,
            'last_name': person.last_name,
            'age': person.age,
            'address': person.address
        }
        return JsonResponse({'Persona': data})
    return JsonResponse({'Mensaje': 'Solicitud no valida'})

@csrf_exempt
def create_person(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        last_name = data.get('last_name')
        age = data.get('age')
        address = data.get('address')
        if name and last_name and age and address:
            person = Person(name=name, last_name=last_name, age=age, address=address)
            person.save()
            return JsonResponse({'Mensaje': 'Persona creada con exito'})
        return JsonResponse({'Mensaje': 'Solicitud no válida'}, status=400)
    return JsonResponse({'Mensaje': 'Metodo no permitido'}, status=405)

@csrf_exempt
def update_person(request, id):
    if request.method == 'PUT':
        data = json.loads(request.body)
        name = data.get('name')
        last_name = data.get('last_name')
        age = data.get('age')
        address = data.get('address')
        if name and last_name and age and address:
            person = Person.objects.get(id=id)
            person.name = name
            person.last_name = last_name
            person.age = age
            person.address = address
            person.save()
            return JsonResponse({'Mensaje': 'Persona editada con exito'})
        return JsonResponse({'Mensaje': 'Solicitud no válida'}, status=400)
    return JsonResponse({'Mensaje': 'Metodo no permitido'}, status=405)

@csrf_exempt
def delete_person(request, id):
    if request.method == 'DELETE':
        person = Person.objects.get(id=id)
        person.delete()
        return JsonResponse({'Mensaje': 'Persona eliminada con exito'})
    return JsonResponse({'Mensaje': 'Metodo no permitido'}, status=405)
