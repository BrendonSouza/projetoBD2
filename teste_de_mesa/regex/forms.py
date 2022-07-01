from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('seu_codigo',)
        labels = {
            'seu_codigo':'Seu código'
        }
