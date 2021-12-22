from django.urls import path,include
from .views.patients import *
from .views.appointments import *
from .views.prescriptions import *
from rest_framework.routers import SimpleRouter
from .views.doctors import *


router = SimpleRouter()
router.register('patients',PatientViewSet,basename='patient')
router.register('doctors',DoctorViewset,basename="doctor")
router.register('appointments',AppointViewSet,basename="appointment")
router.register("prescription",PrescriptionViewSet,basename="prescription")
router.register("medicine",MedicineViewSet,basename="medicine")


urlpatterns = [
    path('',include(router.urls)),
    path('patient-accounts/login/',PatientLoginApiView.as_view()),
    path('patient-accounts/me/update/',PatientUpdateApiView.as_view()),
    

    path('doctor-accounts/login',DoctorLoginApiView.as_view()),

    
]
