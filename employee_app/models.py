from pyexpat import model
from turtle import title
from django.db import models

# Create your models here.

class Position(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Employee(models.Model):
    name = models.CharField(max_length=100)
    idnum = models.CharField(max_length=100)
    phoneNum = models.CharField(max_length=10)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)