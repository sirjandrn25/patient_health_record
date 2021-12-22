from rest_framework.generics import GenericAPIView
from ..serializers.doctors import *
from rest_framework.viewsets import ModelViewSet
from ..models.doctors import *
from rest_framework.response import Response
from .authentication import *
from ..permissions import *


class DoctorViewset(ModelViewSet):
    queryset=Doctor.objects.all()
    serializer_class = DoctorSerializer



class DoctorLoginApiView(GenericAPIView):
    serializer_class = DoctorLoginSerializer

    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            doctor = serializer.validated_data('email')
            data = {
                
                'email':doctor
            }
            token = create_access_token(data=data)
            return Response({'token':token})
        return Response(serializer.errors,status=400)