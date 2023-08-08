#handling forms to be displayed  by the users
from django.forms import ModelForm
from.models  import *
#from spareapp.models import *
class AddForm(ModelForm):
    class Meta:
        model = Product
        fields = ['received_quantity']
        
class SaleForm(ModelForm):
    class Meta:
        model = Sale
        fields = ['quantity','amount_received','issued_to']
        
    