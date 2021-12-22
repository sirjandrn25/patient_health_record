from rest_framework import serializers
from tracker.models.prescriptions import Medicine, Prescription


class PrescriptionSeriailizer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = "__all__"
        read_only_fields = ['id','created_at']


class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = "__all__"
        read_only_fields = ['id']