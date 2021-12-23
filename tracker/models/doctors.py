from django.db import models
from .abstracts import *
from .departments import Department
from django.contrib.postgres.fields import ArrayField

class Doctor(Person):
    specialist = models.CharField(max_length=100,blank=True)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name


class Availability(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    on_holiday = models.BooleanField(default=False)
    available_days = ArrayField(models.IntegerField())
    doctor = models.OneToOneField(Doctor,on_delete=models.CASCADE)

    def __str__(self):
        return self.doctor.full_name

