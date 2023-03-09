from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"companyapp/index.html")
def about(request):
    return render(request,"companyapp/about.html")  
def service(request):
    return render(request,"companyapp/service.html")   
def portfolio(request):
    return render(request,"companyapp/portfolio.html")
def contact(request):
    return render(request,"companyapp/contact.html")       