from rest_framework import serializers
from ..models.patients import *
from tracker.models import patients
from django.contrib.auth.hashers import check_password, make_password



class PatientUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"
        read_only_fields = ['id','created_at','email']


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient

        exclude = ['created_at']


    def validate(self,validated_data):
        password = validated_data.get('password')

        if len(password)<8:
            errors = {
                'password':['at least 8 charecters are required']
            }
        elif password.isdigit():
            errors = {
                'password':['only numeric values not allowed']
            }
        else:
            validated_data['password'] = make_password(password)
            return validated_data
        raise serializers.ValidationError(errors)
        
            

class PatientLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=120)
    password = serializers.CharField(min_length=8,max_length=100)

    def valid(self,validated_data):
        email = validated_data.get('email')
        password = validated_data.get('password')
        patient = Patient.objects.filter(email=email).first()
        if patient:
            if check_password(password,patient.password):
                return validated_data
            else:
                errors ={
                    'password':['password does not match']
                }
        else:
            errors = {
                'email':['this email id does not exists']
            }
            
        raise serializers.ValidationError(errors)

    