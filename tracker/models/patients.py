from django.db import models
from .abstracts import *


class Patient(Person):

    def __str__(self):
        return self.full_name