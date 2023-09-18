from django.shortcuts import render
from .models import Fields
# Create your views here.
def Welcome_View(request):
    name='abdelkhalek'

    hi=Fields.object.all()
    context = {'name': hi}
    return render (request,'base.html',context)


def Courses_Info(request):
    return render (request,'Courses/Courses_Info.html')

