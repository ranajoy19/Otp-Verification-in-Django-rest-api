from .views import *
from django.urls import path



urlpatterns = [
    path('register/',Registration.as_view(),name='register'),
    path('verify_otp/',Verify_Otp.as_view(),name='verify_otp')
]
