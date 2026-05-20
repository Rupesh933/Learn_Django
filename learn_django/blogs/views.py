from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Employees

# Create your views here.

def home(request):
    employees = Employees.objects.all()
    context = {
        'employees':employees
    }
    return render(request,'home.html', context)

def employee_details(reqest, pk):
    try:
        employee = Employees.objects.get(pk=pk)
        context = {
            'employee' : employee
        }
        return render(reqest, 'employee_details.html', context)
        # return HttpResponse(employee) 
    except : 
        raise Http404
    