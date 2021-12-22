from rest_framework.generics import GenericAPIView
from ..serializers.patients import PatientLoginSerializer, PatientSerializer, PatientUpdateSerializer
from rest_framework.viewsets import ModelViewSet
from ..models.patients import Patient
from rest_framework.response import Response
from .authentication import *
from ..permissions import *
# from rest_framework.authentication import TokenAuthentication

class PatientViewSet(ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticatedPatientOrReadOnly]

    def retieve(self,request,pk):
        patient = self.get_object()



class PatientUpdateApiView(GenericAPIView):
    serializer_class = PatientUpdateSerializer
    permission_classes = [IsAuthenticatedPatientOrReadOnly]

    
    def put(self,request):
        email = request.data.pop('patient')[0]
        
        patient = Patient.objects.filter(email=email).first()
        
    
        serializer = self.serializer_class(data=request.data,instance=patient,partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
        
        return Response(serializer.errors,status=400)


class PatientLoginApiView(GenericAPIView):
    serializer_class = PatientLoginSerializer
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            print(serializer.validated_data)
            patient = serializer.validated_data.get('email')
           
            data = {
                
                'email':patient
            }
            token = create_access_token(data=data)
            return Response({'token':token})
        return Response(serializer.errors,status=400)
    

