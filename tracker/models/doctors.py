from django.db import models
from .abstracts import *
from .departments import Department


class Doctor(Person):
    specialist = models.CharField(max_length=100,blank=True)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name