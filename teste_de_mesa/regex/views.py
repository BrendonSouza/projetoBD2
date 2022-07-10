from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee
from .models import TesteDeMesa, Agrupamento, AgrupamentoIndex
from rest_framework.views import APIView
from .tokens import save_test

class InsertCodeView(APIView):
    def post(self, request):
        save_test(request.POST.get('prog_o'), request.POST.get('prog_p'))
        return redirect('/testelist')   

def lists(request, id):
    context = {'valores': AgrupamentoIndex.objects.all(), 
        'linhas': Agrupamento.objects.all(), 'id': id}
    return render(request, "lists.html", context)

def test_list(request):
    context = {'testes': TesteDeMesa.objects.all()}
    return render(request, "test_list.html", context)

def config(request):
    context = {'config': Employee.objects.all()}
    return render(request, "config.html", context)

def employee_form(request, id=0):

    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, "employee_form.html", {'form': form})

    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/list')
