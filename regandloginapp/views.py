from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import Reg

class Home(View):
    def get(self,request):
        return render(request,template_name='home.html')

class Reginput(View):
    def get(self,request):
        return render(request,template_name='reginput.html')

class Logininput(View):
    def get(self,request):
        return render(request,template_name='logininput.html')

class Register(View):
    def post(self,request):
        fn=request.POST["t1"]
        ln=request.POST["t2"]
        un=request.POST["t3"]
        pwd=request.POST["t4"]
        cpwd=request.POST["t5"]
        mbno=int(request.POST["t6"])
        emal=request.POST["t7"]
        r1=Reg(FirstName=fn,LastName=ln,Username=un,Password=pwd,Cpassword=cpwd,MobileNumber=mbno,Emailid=emal)
        r1.save()
        return  HttpResponse("Registration successful")

class Login(View):
    def post(self,request):
        uname1=request.POST["un"]
        passwd1=request.POST["pwd"]
        res=Reg.objects.filter(Username=uname1,Password=passwd1)
        if res:
            return HttpResponse("login Successfull")
        else:
            return HttpResponse("login Failed")
