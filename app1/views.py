from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm
from .forms import *
import json
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *



# Create your views here.
def home(request):
    data = Project.objects.all().values()
    print(data)

    return render(request,'index.html')

def register(request):
    form = UserRegistrationForm(request.POST)
    if request.method=="POST":
        
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created. You can log in now!')
            return redirect('login')
        else:
            print(form.errors)
    else:
        form=UserRegistrationForm()
        return render(request,'register.html',context={"forum":form})
        
    return render(request,'register.html',context={"forum":form})

def createproject(request):
    form_info = Info(request.POST or None )
    if request.method == "POST":
        if form_info.is_valid():
            form_info.save()
        else:
            print(form_info.errors)
        return redirect(project)


    return render(request,'createproject.html',context={'form':form_info})

def project(request):
        
    project_info = Project.objects.all().values()
    return render(request,'project.html',context={'data':project_info})

def edit(request,pk):
    project_info = Project.objects.get(id=pk)
    form_info = Info(request.POST or None,instance=project_info )
    if request.method == "POST":
        if form_info.is_valid():
            form_info.save()
        else:
            print(form_info.errors)
        return redirect(project)

    project_info = Form.objects.all().values()
    return render(request,'edit.html',context={'form':form_info})

def delete(request,pk):
    project_info = Project.objects.get(id=pk)
    project_info.delete()
    return redirect(project) 

def myproject(request):
    
    project_info = Project.objects.filter(created_by=request.user.username).values()
    return render(request,'myprojects.html',context={'data':project_info})

class ClientDt(APIView):
    def get(self,request):
        data = Client.objects.all().values()
        serializer = ClientData(data,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=ClientData(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=400)

class ClientDetail(APIView):

    def get(self,request,id):
        ct_dt = Client.objects.get(id=id)
        serializer = ClientData(ct_dt)
        return Response(serializer.data)

    def put(self,request,id):
        ct_dt = Client.objects.get(id=id)
        serializer=ClientData(data=request.data,instance=ct_dt)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=400)
    
    def delete(self,request,id):
        ct_dt = Client.objects.get(id=id)
        ct_dt.delete()
        return Response(status=204)




class ProjectDt(APIView):
    def get(self,request):
        data = Project.objects.filter(created_by=request.user.username).values()
        serializer = ProjectData(data,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=ProjectData(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=400)

class ProjectDetail(APIView):

    def get(self,request,id):
        pt_dt = Project.objects.get(id=id)
        serializer = ProjectData(pt_dt)
        return Response(serializer.data)

    def put(self,request,id):
        pt_dt = Project.objects.get(id=id)
        serializer=ProjectData(data=request.data,instance=pt_dt)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=400)
    
    def delete(self,request,id):
        pt_dt = Project.objects.get(id=id)
        pt_dt.delete()
        return Response(status=204)