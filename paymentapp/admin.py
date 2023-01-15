from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Wallet)
admin.site.register(Holder)
admin.site.register(Deposite)
admin.site.register(Withdraw)
admin.site.register(Transfer)