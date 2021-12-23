from rest_framework.generics import GenericAPIView
from ..serializers.doctors import *
from rest_framework.viewsets import ModelViewSet
from ..models.doctors import *
from rest_framework.response import Response
from .authentication import *
from ..permissions import *
from rest_framework.views import APIView
from ..serializers.appointments import *

class DoctorViewset(ModelViewSet):
    queryset=Doctor.objects.all()
    serializer_class = DoctorSerializer



class DoctorLoginApiView(GenericAPIView):
    serializer_class = DoctorLoginSerializer

    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            doctor = serializer.validated_data.get('email')
            data = {
                
                'email':doctor
            }
            token = create_access_token(data=data)
            return Response({'token':token})
        return Response(serializer.errors,status=400)




class DoctorProfileApiView(GenericAPIView):
    serializer_class = DoctorUpdateSerializer
    permission_classes = [IsAuthenticatedDoctor]

    def get(self,request):
        doctor_email = request.data.get('doctor')
        doctor = Doctor.objects.filter(email=doctor_email).first()
        serializer = self.serializer_class(doctor)
        return Response(serializer.data)

    def put(self,request):
        doctor_email = request.data.get('doctor')
        doctor = Doctor.objects.filter(email=doctor_email).first()
        serializer = self.serializer_class(data=request.data,instance=doctor,partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=400)

class DoctorAppointmentsApiView(APIView):
    permission_classes = [IsAuthenticatedDoctor]
    def get(self,request):
        doctor_email = request.data.get('doctor')
        doctor = Doctor.objects.filter(email=doctor_email).first()
        appointments = Appointment.objects.filter(doctor=doctor)
        serializer = AppointmentSerializer(appointments,many=True)
        return Response(serializer.data)


class DoctorAvailabiltiyApiView(ModelViewSet):
    serializer_class = DoctorAvailabilitySerializer
    queryset = Availability.objects.all()