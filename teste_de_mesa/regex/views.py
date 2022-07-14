from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee
from .models import TesteDeMesa, Agrupamento, AgrupamentoIndex
from rest_framework.views import APIView
from .tokens import save_test

# View responsável por pegar os dados do programa o e p. 
class InsertCodeView(APIView):
    # Método post da view. 
    def post(self, request):
        # inserindo programa o e p na função save_test. 
        save_test(request.POST.get('prog_o'), request.POST.get('prog_p'))
        # Direcionando para rota de lista de testes. 
        return redirect('/testelist')   

# Busca os dados específicos de um teste com base no id do teste. 
def lists(request, id):
    context = {'valores': AgrupamentoIndex.objects.all(), 
        'linhas': Agrupamento.objects.all(), 'id': id}
    return render(request, "lists.html", context)
# Lista todos os testes já feitos. 
def test_list(request):
    context = {'testes': TesteDeMesa.objects.all()}
    return render(request, "test_list.html", context)
# Parte responsável pela inserção do código o e p.
def config(request):
    context = {'config': Employee.objects.all()}
    return render(request, "config.html", context)
# Gera o formulário para pegar os dados do programa o e p. 
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
