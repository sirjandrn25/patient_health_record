from rest_framework.generics import GenericAPIView
from ..serializers.labreports import *
from rest_framework.viewsets import ModelViewSet
from ..models.labreports import *
from rest_framework.response import Response
from .authentication import *
from ..permissions import *
from rest_framework.decorators import action




class LabReportViewSet(ModelViewSet):
    queryset = LabReport.objects.all()
    serializer_class = LabReportSerializer

