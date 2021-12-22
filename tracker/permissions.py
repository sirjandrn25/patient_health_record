from rest_framework.permissions import BasePermission
from .views.authentication import get_authenticate_user

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

    

class IsAuthenticatedDoctorOrReadOnly(BasePermission):
    def has_permission(self,request,view):
        if request.method == 'GET':
            return True
        
        header = request.META.get('HTTP_AUTHORIZATION')
        if header:
            payload = get_authenticate_user(header.split(' ')[1])
            print(payload)
            if payload:
                request.data.update({'patient':payload.get('doctor')})
            return payload
        return False