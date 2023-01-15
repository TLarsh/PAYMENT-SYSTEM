from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Holder(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    zipcode = models.IntegerField()
    city = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)


class Wallet(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    holder = models.ForeignKey(Holder, on_delete=models.CASCADE)
    address = models.CharField(max_length=225)
    id = models.IntegerField(unique=True, primary_key=True)
    
    @property
    def balance(self):
        deposites = sum([deposite.amount for deposite in Deposite.objects.filter(wallet=self.id)])
        withdraws = sum([withdraw.amount for withdraw in Withdraw.objects.filter(wallet=self.id)])
        transfer = sum([transfer.amount for  transfer in Transfer.Objects.filter(wallet=self.id)])
        total = deposites - withdraws - transfer
        return total
   
   
class Deposite(models.Model):
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)

class Withdraw(models.Model):
    amount = models.DecimalField(decimal_places=2, max_digits=12)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    
class Transfer(models.Model):
    amount = models .DecimalField(max_digits=12, decimal_places=2)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)