from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *
from .helper import *
# Create your views here.

class Registration(APIView):
    def post(self,request):
        try:
            serializer= Userserializer(data=request.data)
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status': 403, 'error': serializer.errors})
            serializer.save()

            return Response({'status': 202, 'payload': serializer.data,
                             'message': 'an email OTP sent on your number and email'})

        except Exception as e:
            print(e)
            return Response({'status': 404,'message': 'something went wrong'})



class Verify_Otp(APIView):

    def post(self,request):

        try:
            data = request.data

            user_obj = User.objects.get(phone=data['phone'])
            otp = data.get('otp')




            if user_obj.otp == otp:
                user_obj.is_mobile_verified = True
                user_obj.save()
                return Response({'status': 200, 'message': 'You otp is Verified'})

            return Response({'status': 200, 'message': 'You otp is Wrong'})



        except Exception as e:

            print(e)
        return Response({'status': 404, 'message': 'something went wrong'})


    def patch(self, request):

        try:
            data = request.data

            user_obj=User.objects.filter(phone= data.get('phone'))

            if not user_obj.exists():
                return Response({'status': 404, 'message': 'No user found1!'})


            status ,time = send_otp_mobile_number(data.get('phone'),user_obj[0])

            if status:
                return Response({'status': 200, 'message': 'new otp sent'})

            return Response({'status': 404, 'message': f'Try after few seconds {time}'})

        except Exception as e:

            print(e)
        return Response({'status': 404, 'message': 'something went wrong'})
