from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Department)
admin.site.register(Appointment)
admin.site.register(Prescription)
admin.site.register(Medicine)