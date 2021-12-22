from rest_framework.permissions import BasePermission
from tracker.models.appointments import Appointment
from tracker.models.doctors import Doctor
from .views.authentication import get_authenticate_user
from rest_framework import permissions

class IsAuthenticatedPatientOrReadOnly(BasePermission):
    def has_permission(self,request,view):
        if request.method == 'GET':
            return True
        
        header = request.META.get('HTTP_AUTHORIZATION')
        if header:
            payload = get_authenticate_user(header.split(' ')[1])
            print(payload)
            if payload:
                request.data.update({'patient':payload.get('email')})
            return payload
        return False

class IsAuthenticated(BasePermission):
    def has_permission(self,request,view):
        if request.method == 'GET':
            return True
        
        header = request.META.get('HTTP_AUTHORIZATION')
        if header:
            payload = get_authenticate_user(header.split(' ')[1])
            print(payload)
            if payload:
                request.data.update({'patient':payload.get('email')})
            return payload
        return False
    
    def has_object_permission(self,request,view,obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        header = request.META.get('HTTP_AUTHORIZATION')
        if header:
            payload = get_authenticate_user(header.split(' ')[1])
            if payload:
                doctor = Doctor.objects.filter(email=payload.get('email')).first()
                if obj.doctor == doctor:
                    return True
        return False


# class IsDoctorAppointment(BasePermission):
#     def has_permission(self,request,view):
#         doctor_email = request.data.get('doctor')
#         doctor = Doctor.objects.filter(email=doctor_email).first()
#         appointment = Appointment.objects.filter(id=request.data.get('appointment')).first()
#         if appointment:

        

        

    

class IsAuthenticatedDoctorOrReadOnly(BasePermission):
    def has_permission(self,request,view):
        if request.method == 'GET' and request.method=="POST":
            return True
        
        header = request.META.get('HTTP_AUTHORIZATION')
        if header:
            payload = get_authenticate_user(header.split(' ')[1])
            print(payload)
            if payload:
                request.data.update({'doctor':payload.get('doctor')})
            return payload
        return False
