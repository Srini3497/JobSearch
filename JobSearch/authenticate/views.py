from django.shortcuts import render

# Create your views here.
def loginpage(req):
    return render(req,"login.html")

def registrationpage(req):
    return render(req,"register.html")