# Import necessary modules
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from . models import *
from . forms import *
from . filters import *
from django.contrib.auth.decorators import login_required
from django.urls import reverse


#importing our model forms.addform,saleform
#import folders also.
#import decorators from django
#import reverse
# View function for the 'index' view
def index(request):
    # This view renders the 'index.html' template from the 'Demi' app.
# View function for the 'aboutUs' view
    return render(request,'Demi/index.html')
def home(request):
    # return render(request,'Demi/home.html')
    products = Product.objects.all().order_by('-id')#here we are querring.this id can be replaced by the choice.
    product_filters = ProductFilter(request.GET,queryset = products)
    products = product_filters.qs
    return render(request,'Demi/home.html',{'products':products,'product_filters':product_filters})



def made_sales(request):
     pass    
    

@login_required
def receipt(request):
    sales = Sale.objects.all().order_by('-id')
    return render(request,'Demi/receipt.html',{'sales':sales})
    




@login_required
def add_to_stock(request,pk):
    issued_item = Product.objects.get(id = pk)
    form = AddForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():

            added_quantity = int(request.POST['received_quantity'])
            issued_item.total_quantity += added_quantity 
            issued_item.save()
            
            print(added_quantity)
            print(issued_item.total_quantity)
            return redirect('home')
    return render(request,'Demi/add_to_stock.html',{'form':form})


@login_required
def product_detail(request,product_id):
    product = Product.objects.get(id=product_id)
    return render(request,'Demi/product_detail.html',{'product': product})

@login_required
def receipt(request):
    sales = Sale.objects.all()
    return render(request,'Demi/receipt.html',{'sales':sales})


@login_required
def give_item(request,pk):
    give_item = Product.objects.get(id=pk)
    made_sales_form = SaleForm(request.POST)
    if request.method =='POST':
        if made_sales_form.is_valid():
            new_sale=made_sales_form.save(commit=False)
            new_sale.item=give_item
            new_sale.unit_price=give_item.unit_price
            new_sale.save()
            print(give_item.item_name)
            print(request.POST['quantity'])
            print(give_item.total_quantity)
            return redirect('receipt')
    return render(request,'Demi/give_item.html',{'made_sales_form':made_sales_form})    
    
    

@login_required
def receipt_detail(request,receipt_id):
    receipt = Sale.objects.get(id = receipt_id)
    return render(request,'Demi/receipt_detail.html',{'receipt':receipt})

@login_required    
def made_sales(request):
    sales = Sale.objects.all()
    total =  sum(items.amount_received for items in sales) 
    change = sum(items.get_change() for items in sales)
    net = total-change
    return render(request,'Demi/made_sales.html',{'sales': sales,'total':total,'change':change,'net':net})
    








 
