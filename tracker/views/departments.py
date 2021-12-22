from ..serializers.departments import *
from rest_framework.response import Response
from ..models.departments import *
from ..serializers.departments import *
from rest_framework.viewsets import ModelViewSet



class DepartmentViewSet(ModelViewSet):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()