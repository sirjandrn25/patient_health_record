from rest_framework.generics import GenericAPIView
from tracker.serializers.appointments import AppointmentSerializer
from ..serializers.patients import AvatarUpdateSerializer, PatientLoginSerializer, PatientSerializer, PatientUpdateSerializer
from rest_framework.viewsets import ModelViewSet
from ..models.patients import Patient
from rest_framework.response import Response
from .authentication import *
from ..permissions import *
from rest_framework.decorators import action
# from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView

class PatientViewSet(ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticatedPatientOrReadOnly]

    

    
    
        

class PatientAppointmentApiView(APIView):
    permission_classes = [IsAuthenticatedPatient]
    def get(self,request):
        patient = Patient.objects.filter(email=request.data.get('patient')).first()
        appointments = Appointment.objects.filter(patient=patient)
        serializer = AppointmentSerializer(appointments,many=True)
        return Response(serializer.data)




class PatientUpdateApiView(GenericAPIView):
    serializer_class = PatientUpdateSerializer
    permission_classes = [IsAuthenticatedPatient]

    
    def get(self,request):
        
        patient = Patient.objects.filter(email=request.data.get('patient')).first()
        # print(request.data)
        
        serializer = self.serializer_class(patient)
        
        return Response(serializer.data)

    def put(self,request):
        email = request.data.pop('patient')
        print(email)
        
        patient = Patient.objects.filter(email=email).first()
        
    
        serializer = self.serializer_class(data=request.data,instance=patient,partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
        
        return Response(serializer.errors,status=400)


# class PatientAvatarUpdateView(GenericAPIView):
#     serializer_class = AvatarUpdateSerializer
#     permission_classes = [IsAuthenticatedPatient]
#     def patch(self,request):
#         patient = Patient.objects.filter(email=request.data.get('patient')).first()
#         return Response(patient)

class PatientLoginApiView(GenericAPIView):
    serializer_class = PatientLoginSerializer
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            
            patient = serializer.validated_data.get('email')
           
            data = {
                
                'email':patient
            }
            token = create_access_token(data=data)
            return Response({'token':token})
        return Response(serializer.errors,status=400)
    


# class PatientProfileApiView(GenericAPIView):
#     serializer_class = PatientSerializer
#     permission_classes = [IsAuthenticatedPatient]
#     def get(self,request):
#         patient = Patient.objects.filter(email=request.data.get('email')).first()
#         serializer = self.serializer_class(patient)
#         return Response(serializer.data)


#     def put(sef,request):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)
    