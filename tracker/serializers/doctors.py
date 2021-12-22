from rest_framework import serializers
from ..models.doctors import *
from django.contrib.auth.hashers import make_password,check_password




class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"
        read_only_fields = ['id','created_at']

    def valid(self,validated_data):
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
    

class DoctorLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=120)
    password = serializers.CharField(min_length=8,max_length=100)

    def valid(self,validated_data):
        email = validated_data.get('email')
        password = validated_data.get('password')
        doctor = Doctor.objects.filter(email=email).first()
        if doctor:
            if check_password(password,doctor.password):
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
