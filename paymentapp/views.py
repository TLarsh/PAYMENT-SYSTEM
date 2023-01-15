from http import client
from multiprocessing.connection import Client
import re
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from django.contrib.auth import get_user_model
User = get_user_model()


from paymentapp.serializers import DepositeSerializer, TransferSerializer, WalletSerializer, WalletDetailSerializer, WithdrawSerializer
from .models import *
from rest_framework.generics import(
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,   
)

# class WalletView(RetrieveUpdateDestroyAPIView):
#     permission_classes = (permissions.AllowAny, )
#     queryset = Wallet.objects.all()
#     serializer_class = WalletSerializer
    
class WalletDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Wallet.objects.all()
    serializer_class = WalletDetailSerializer

    
class CreateWalletView(APIView):
    permission_classes = (permissions.AllowAny, )
    def post(self,request, format=None):
        # user = self.request.data['user']
        first_name = self.request.data['first_name']
        last_name = self.request.data['last_name']
        address = self.request.data['address']
        zipcode = self.request.data['zipcode']
        city = self.request.data['city']
        email = self.request.data['email']
        name = self.request.data['name']
        # user = self.request.user
        # user = User.objects.filter(name=name)
        # email = self.request.data['email']

            
        
        holder = Holder.objects.create(first_name=first_name,
                                    last_name=last_name,
                                    address = address,
                                    zipcode = zipcode,
                                    city = city,
                                    email=email
                                    )
        # return Response(user.set_all)
        wallet = Wallet.objects.create(holder=holder)
        serializer = WalletSerializer(wallet)
        return Response(serializer.data)
    
    
class WithdrawView(ListCreateAPIView):
    permission_classes = (permissions.AllowAny, )
    amount = Deposite.objects.all()
    serializer_class = WithdrawSerializer

class DepositeView(ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    amount = Withdraw.objects.all()
    serializer_class = DepositeSerializer
    
    # def post(self,request, format=None):
    #     data = self.request.data
    #     amount = data['amount']
    #     wallet = data['wallet']
    #     deposite = Deposite.objects.all()
    #     serializer = DepositeSerializer(deposite)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    # serializer_class = DepositeSerializer


        
class TransferView(ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    amount = Transfer.objects.all()
    serializer_class = TransferSerializer
        
        
        
        
        