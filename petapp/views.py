from django.shortcuts import render ,redirect
from petapp.models import *
from django.contrib import messages
from math import ceil

def index(request):
    allProds=[]
    catprods=Product.objects.values('Product_Category','id')
    cats={item['Product_Category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(Product_Category=cat)
        n=len(prod)
        nSlides=n // 4 + ceil((n/4)-(n//4))
        allProds.append([prod, range(1,nSlides), nSlides])
    params= {"allProds": allProds}
    return render(request,"app/index.html",params)
    

def contact(request):
    if request.method=='POST':
        name=request.POST.get("name")
        email=request.POST.get("email")
        description=request.POST.get("desc")
        phone=request.POST.get("phone")
        myquery=Contact(name=name,email=email,desc=description,phone=phone)
        myquery.save()
        
        messages.info(request, 'We will get back soon')    
    return render(request,'app/contact.html')

def checkout(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Login & Try Again")
        return redirect('/auth/login')

    if request.method=="POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        amount = request.POST.get('amt')
        email = request.POST.get('email', '')
        address1 = request.POST.get('address1', '')
        address2 = request.POST.get('address2','')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        Orders = Order(item_json=items_json,name=name,amount=amount, email=email, address1=address1,address2=address2,city=city,state=state,zip_code=zip_code,phone=phone)
        print(amount)
        Orders.save()
        update = orderupdate(order_id=Order.order_id,update_desc="the order has been placed")
        update.save()
        thank = True
    return render(request,'app/checkout.html')