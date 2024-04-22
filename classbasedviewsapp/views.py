from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.
class Getinput(View):
    def get(self,request):
        return render(request,'getinput.html')
class Postinput(View):
    def post(self,request):
        return render(request,'postinput.html')
class Add(View):
    def get(self,request):
        x=int(request.GET["t1"])
        y=int(request.GET["t2"])
        z=x+y
        con_dict = {"res": z}
        return render(request,'result.html',context=con_dict)
    def post(self,request):
        x=int(request.POST["t1"])
        y=int(request.POST["t2"])
        z=x+y
        con_dict={"res":z}
        return render(request,'result.html',context=con_dict)
