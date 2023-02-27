from django.shortcuts import render
from .models import Employee

def home(Request):
    data=Employee.objects.all()
    return render(Request,"index.html",{'data':data})

def delete(Request,id):
    data=Employee.objects.get(id=id)
    if(data):
        data.delete()
    return redirect("/")

def addRecord(Request):
    if(Request.method=="POst"):
        e=Employee()
        e.name=Request.POST.get("name")
        e.name=Request.POST.get("email")
        e.name=Request.POST.get("salary")
        e.name=Request.POST.get("phone")
        e.name=Request.POST.get("city")
        e.name=Request.POST.get("state")
        e.save()
        return redirect("/")
    return render(Request,"add.html")