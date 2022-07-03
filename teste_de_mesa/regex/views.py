from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee, Programas, ProgramaO, ProgramaP, DadosTm
from rest_framework.views import APIView
import tokenize
from io import BytesIO
from datetime import date

class InsertCodeView(APIView):
    def post(self, request):
        prog_p = request.POST.get('prog_p')
        prog_o = request.POST.get('prog_o')
        
        prog = str(prog_p)

        data = date.today()

        # o = ProgramaO(dt_codificacao=data, codigo_o=str(prog_o))
        # p = ProgramaP(dt_codificacao=data, codigo_p=str(prog_p))
        # o.save()
        # p.save()

        # DadosTm(linha=t[2][0], variavel_o=t[1], variavel_p=t[1], codigo_linha=t[4])

        tokens_p = tokenize.tokenize(BytesIO(prog.encode('utf-8')).readline)

        for t in tokens_p:
            if t[0] == 63 or t[0] == 4 or t[0] == 0: 
                continue
            else: 

                dados_tm = DadosTm(linha=t[2][0], variavel_o=t[1], variavel_p=t[1], codigo_linha=t[4])
                dados = Programas(programa_p=t[1], programa_o=t[1])    

                dados_tm.save()            
                dados.save()

        return redirect('/list')   

def employee_list(request):
    context = {'employee_list': Programas.objects.all()}
    return render(request, "regex/employee_list.html", context)

def config(request):
    context = {'config': Employee.objects.all()}
    return render(request, "regex/config.html", context)

def test_case(request):
    context = {'test_case': Employee.objects.all()}
    return render(request, "regex/test_case.html", context)

def table_test(request):
    context = {'table_test': Employee.objects.all()}
    return render(request, "regex/table_test.html", context)

def result(request):
    context = {'result': Employee.objects.all()}
    return render(request, "regex/result.html", context)

def employee_form(request, id=0):

    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, "regex/employee_form.html", {'form': form})

    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/list')


def employee_delete(request,id):
    employee = Programas.objects.get(pk=id)
    employee.delete()
    return redirect('/list')
