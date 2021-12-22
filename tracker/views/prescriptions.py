from rest_framework.generics import GenericAPIView
from ..serializers.prescriptions import *
from rest_framework.viewsets import ModelViewSet
from ..models.prescriptions import *
from rest_framework.response import Response
from .authentication import *
from ..permissions import *
from rest_framework.decorators import action
from rest_framework.views import APIView

class PrescriptionViewSet(ModelViewSet):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSeriailizer
    
    @action(detail=True,methods =["get"])
    def medicines(self,request,pk):
        prescription = self.get_object()
        medicines = Medicine.objects.filter(prescription=prescription)
        serializer = MedicineSerializer(medicines,many=True)

        return Response(serializer.data)
    


class LatestPresciptionMedicinesApi(APIView):
    permission_classes = [IsAuthenticatedPatient]
    def get(self,request):
        
        patient = Patient.objects.filter(email=request.data.get('patient')).first()
        appointment = Appointment.objects.filter(patient=patient).last()
        if appointment:
            prescription = Prescription.objects.filter(appointment=appointment).last()
            medicines = Medicine.objects.filter(prescription=prescription)
            serializer = MedicineSerializer(medicines,many=True)
            return Response(serializer.data)
        return Response({'detail':'appointment not found'},status=400)








class MedicineViewSet(ModelViewSet):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
