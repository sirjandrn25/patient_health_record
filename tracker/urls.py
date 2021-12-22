from django.urls import path,include
from .views.patients import *
from .views.appointments import *
from .views.prescriptions import *
from .views.labreports import *
from rest_framework.routers import SimpleRouter
from .views.doctors import *
from .views.departments import *


router = SimpleRouter()
router.register('patients',PatientViewSet,basename='patient')
router.register('doctors',DoctorViewset,basename="doctor")
router.register('appointments',AppointViewSet,basename="appointment")
router.register("prescriptions",PrescriptionViewSet,basename="prescription")
router.register("medicine",MedicineViewSet,basename="medicine")
router.register("labreports",LabReportViewSet,basename="labreport")
router.register("departments",DepartmentViewSet,basename="department")



urlpatterns = [
    path('',include(router.urls)),
    path('patient-accounts/login/',PatientLoginApiView.as_view()),
    path('patient-accounts/me/profile/',PatientUpdateApiView.as_view()),
    path('patient-accounts/me/appointments/',PatientAppointmentApiView.as_view()),
    
    
    path("latest/prescription/medicines/",LatestPresciptionMedicinesApi.as_view()),
    path('doctor-accounts/login',DoctorLoginApiView.as_view()),

    
]
