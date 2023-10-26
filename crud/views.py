from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
# Create your views here.
def home(request):
    context={'title':'CRUD OPERATION'}
    return render(request,"index.html",context)
def create(request):
    context={'title':'Create Record'}
    if request.method=="POST":
        data=request.POST
        
        fname=data.get('fname')
        lname=data.get('lname')
        email=data.get('email')
        mob=data.get('mob')
        address=data.get('address')
        createRecord.objects.create(fname=fname,lname=lname,email=email,mob=mob,address=address)
        messages.success(request,'Add record Sucessfully!!!')
        return redirect('/')
    return render(request,"create.html",context)
def view(request):
    queryset=createRecord.objects.all()
    context={'title':'View Record','query':queryset}
    return render(request,"view.html",context)
def update(request):
    queryset=createRecord.objects.all()
    context={'title':'Update Record','query':queryset}
    return render(request,"update.html",context)
def updatepage(request,id):
    queryset=createRecord.objects.get(id = id)
    context={'title':'Update Record','q':queryset}
    if request.method=="POST":
        data=request.POST
        fname=data.get('fname')
        lname=data.get('lname')
        email=data.get('email')
        mob=data.get('mob')
        address=data.get('address')
        queryset.fname=fname
        queryset.lname=lname
        queryset.email=email
        queryset.mob=mob
        queryset.address=address
        queryset.save() 
        return redirect('/')
    messages.success(request,'Update record Sucessfully!!!')
    return render(request,"create.html",context)
def delete(request):
    queryset=createRecord.objects.all()
    context={'title':'Delete Record','query':queryset}
    return render(request,"delete.html",context)
def deletepage(request,id):
    context={'title':'delete Record'}
    
    queryset=createRecord.objects.get(id=id)
    queryset.delete()
    messages.success(request,'Delete Sucessfully!!!')
    return redirect('/')