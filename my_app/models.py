from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=75)
    last_name = models.CharField(max_length=75)
    age = models.IntegerField()
    address = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return f'{self.name} {self.last_name}'