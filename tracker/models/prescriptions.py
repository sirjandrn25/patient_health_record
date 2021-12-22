from django.db import models
from .appointments import *


class Prescription(models.Model):
    description = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    appointment = models.ForeignKey(Appointment,on_delete=models.CASCADE)


class Medicine(models.Model):
    medicine_name = models.CharField(max_length=150)
    morning = models.BooleanField(default=False)
    day = models.BooleanField(default=False)
    night = models.BooleanField(default=False)
    after_milk = models.BooleanField(default=False)
    prescription = models.ForeignKey(Prescription,on_delete=models.CASCADE)
    no_of_days = models.IntegerField()
    def __str__(self):
        return self.medicine_name

