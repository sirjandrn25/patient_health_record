from rest_framework.generics import GenericAPIView
from tracker.models.appointments import Appointment
from ..serializers.appointments import *
from rest_framework.viewsets import ModelViewSet
from ..models.doctors import *
from rest_framework.response import Response
from .authentication import *
from ..permissions import *
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from ..serializers.prescriptions import *
from ..models.prescriptions import *

class AppointViewSet(ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        pk = self.kwargs.get('pk')
        obj = get_object_or_404(self.get_queryset(), pk=self.kwargs["pk"])
        self.check_object_permissions(self.request, obj)
        return obj

    def create(self,request):
        patient_email = request.data.get('patient')
        patient = Patient.objects.filter(email=patient_email).first()
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(patient=patient)
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)
    

    @action(detail=True,methods=['get'])
    def prescriptions(self,request,pk):
        appointment = self.get_object()
        prescription=Prescription.objects.filter(appointment=appointment).first()
        serializer = PrescriptionSeriailizer(prescription)
        return Response(serializer.data)
    
    


