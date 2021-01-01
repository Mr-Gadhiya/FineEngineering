from django.shortcuts import render
from django.http import HttpResponse
from .models import Product , Inquiry

# Create your views here.
def index(request):

    prod = Product.objects.all()
    n = len(prod)
    params = {'range':range(n),'product':prod}
    if request.method=="POST":
        name = request.POST.get('name','')
        phone = request.POST.get('phone','')
        subject = request.POST.get('subject','')
        message = request.POST.get('message','')
        ord = Inquiry(name=name,phone=phone,subject=subject,message=message)
        ord.save()
    # return render(request,'/')
    return render(request,'fine/index.html', params)
 
# def inquiry(request):
#     if request.method=="POST":
#         name = request.POST.get('name','')
#         phone = request.POST.get('phone','')
#         subject = request.POST.get('subject','')
#         message = request.POST.get('message','')
#         ord = Inquiry(name=name,phone=phone,subject=subject,message=message)
#         ord.save()
#         print(ord)
#     return render(request,'/')