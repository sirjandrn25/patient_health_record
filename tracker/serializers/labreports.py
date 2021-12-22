from ..models.labreports import *
from rest_framework import serializers


class LabReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabReport
        fields = "__all__"
        