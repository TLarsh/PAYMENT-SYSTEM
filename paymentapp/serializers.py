from .models import (
    Transfer,
    Wallet,
    Withdraw,
    Deposite,
    Holder,
)

from rest_framework import serializers


class HolderSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Holder
        fields = ('__all__')

class WalletSerializer(serializers.ModelSerializer):
    holder = HolderSerializer()
    # balance = serializers.DecimalField(max_digits=12, decimal_places=2)
    class Meta:
        
        # user = serializers.fieldName = models.
        # read_only_fields = ('user', )
        model = Wallet
        fields = ('__all__')

class DepositeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposite
        fields = ('__all__')
        
class WithdrawSerializer(serializers.ModelSerializer):
    class Meta:
        model = Withdraw
        fields = ('__all__')
        
class WalletDetailSerializer(serializers.ModelSerializer):
    holder = HolderSerializer()
    balance = serializers.DecimalField(max_digits=12, decimal_places=2)
    class Meta:
        model = Wallet
        fields = ['holder', 'address', 'balance']
        
class TransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfer
        fields = ('__all__')