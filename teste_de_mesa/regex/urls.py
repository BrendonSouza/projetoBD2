from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.employee_form,name='employee_insert'), # get and post req. for insert operation
    path('<int:id>/', views.employee_form,name='employee_update'), # get and post req. for update operation
    path('delete/<int:id>/',views.employee_delete,name='employee_delete'),
    path('list/',views.employee_list,name='employee_list'), # get req. to retrieve and display all records
    path('config/',views.config,name='config'),
    path('testcase/', views.InsertCodeView.as_view(),name='testcase'),
    path('tabletest/',views.table_test,name='table_test'),
    path('result/',views.result,name='result'),
]