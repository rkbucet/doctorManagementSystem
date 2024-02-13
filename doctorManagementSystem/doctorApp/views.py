from django.shortcuts import render, redirect
from django.http import HttpRequest
from doctorApp.models import *

def home(request):
    doctor = Doctor.objects.all()
    return render(request, 'home.html', {'doctor': doctor})

def insertFun(request):
    speciality = Speciality.objects.all()
    location = Location.objects.all()
    if request.method == 'POST':
        d1 = Doctor()
        d1.name = request.POST['doctorName']
        d1.fees = request.POST['fees']
        d1.speciality = Speciality.objects.get(specialist=request.POST['speciality'])
        d1.experience = request.POST['experience']
        d1.location = Location.objects.get(location = request.POST['location'])
        d1.save()
        return redirect('home')
    else:
        return render(request, 'insert.html', {'speciality': speciality, 'location': location})   



def updateFun(request, id):
    d1 = Doctor.objects.get(id=id)
    place = Location.objects.all()
    speciality = Speciality.objects.all()
    if request.method=='POST':
        d1.name = request.POST['doctorName']
        d1.fees = request.POST['fees']
        d1.speciality = Speciality.objects.get(specialist=request.POST['speciality'])
        d1.experience = request.POST['experience']
        d1.location = Location.objects.get(location = request.POST['location'])
        d1.save()
        return redirect('home')
    else:
        return render(request, 'update.html', {'doctor': d1, 'place': place, 'speciality': speciality, })
    
def deleteFun(request, id):
    d1 = Doctor.objects.get(id=id)
    d1.delete()
    return redirect('/')