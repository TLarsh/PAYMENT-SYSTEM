
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from django.contrib.auth import get_user_model
User = get_user_model()

class SignupView(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, format=None):
        data = self.request.data
        email = data['email']
        name = data['name']
        password = data['password']
        password2 = data['password2']
        
        if password == password2:
            
            if User.objects.filter(email=email).exists():
                return Response({'error':'email already exist'})
            else:
                if len(password) < 6:
                    return Response({'error':'password must be more than 6 characters'})
                else:
                    user = User.objects.create_user(email=email, name=name, password=password)
                    user.save()
                    return Response({'success':'Account successfully created'})
        else:
            return Response({'error':'password does not match'})