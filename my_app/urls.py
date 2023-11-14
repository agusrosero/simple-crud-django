from django.urls import path
from . import views


urlpatterns = [
    path('listar/', views.list_person, name='list_person'),
    path('listar/<int:id>/', views.list_by_id, name='list_by_id'),
    path('crear/', views.create_person, name='create_person'),
    path('editar/<int:id>/', views.update_person, name='update_person'),
    path('eliminar/<int:id>/', views.delete_person, name='delete_person'),
]
