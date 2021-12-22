from .departments import *
from .doctors import *
from .patients import *



class Appointment(models.Model):
    
    schedule_date_time = models.DateTimeField()
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    is_approve = models.BooleanField(default=False)
    is_reject = models.BooleanField(default=False)
    description = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.doctor.full_name} --> {self.patient.full_name}"