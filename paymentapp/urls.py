from django.urls import path
from .views import  (CreateWalletView, 
                     WithdrawView, 
                     DepositeView, 
                     WalletDetailView,
                     TransferView
                     )

urlpatterns = [
    path('wallet/<pk>/', WalletDetailView.as_view(), name = 'wallet'),
    path('create_wallet/', CreateWalletView.as_view(), name = 'create_wallet'),
    path('withdraw/', WithdrawView.as_view(), name="withdraw"),
    path('deposite/', DepositeView.as_view(), name='deposite'),
    path('transfer/', TransferView.as_view(), name='withdraww')
]