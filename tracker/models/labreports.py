from django.db import models
from .appointments import *


class LabReport(models.Model):
    appointment = models.OneToOneField(Appointment,on_delete=models.CASCADE)
    testing_time = models.DateTimeField()
    report_type = models.CharField(max_length=20)
    pressure = models.CharField(max_length=10)
    height=models.FloatField()
    weight = models.CharField(max_length=10)
    report_time = models.DateTimeField()
    test_description = models.CharField(max_length=300)

    
    