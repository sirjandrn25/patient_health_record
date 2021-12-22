from rest_framework.generics import GenericAPIView
from ..serializers.prescriptions import *
from rest_framework.viewsets import ModelViewSet
from ..models.prescriptions import *
from rest_framework.response import Response
from .authentication import *
from ..permissions import *
from rest_framework.decorators import action

class PrescriptionViewSet(ModelViewSet):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSeriailizer

    @action(detail=True,methods =["get"])
    def medicines(self,request,pk):
        prescription = self.get_object()
        medicines = Medicine.objects.filter(prescription=prescription)
        serializer = MedicineSerializer(medicines,many=True)

        return Response(serializer.data)
        



class MedicineViewSet(ModelViewSet):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
