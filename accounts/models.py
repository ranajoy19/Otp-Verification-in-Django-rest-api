from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
import uuid
from django.conf import settings


# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    phone= models.CharField(max_length=12)
    is_email_verified=models.BooleanField(default=False)
    is_mobile_verified=models.BooleanField(default=False)
    otp=models.CharField(max_length=6,null=True,blank=True)
    email_verification_token= models.CharField(max_length=250,null=True,blank=True)
    forget_password =models.CharField(max_length=250,null=True,blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()


# @receiver(post_save, sender= User)
# def send_email_token(sender,instance,created, **kwargs):
#     if created:
#
#         try:
#             subject ='Your email need to be verifed'
#             message =f'Hi click on the link to verify email http://127.0.0.1:8000/{uuid.uuid4()}/'
#
#             email_form=settings.EMAIL_HOST_USER
#             recipient_list=[instance.email]
#             send_mail(subject,message,email_form,recipient_list)
#
#         except Exception as e:
#             print(e)