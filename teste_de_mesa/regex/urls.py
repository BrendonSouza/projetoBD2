from django.urls import path
from . import views
# Rotas da aplicação 
urlpatterns = [
    path('', views.employee_form,name='employee_insert'),
    path('<int:id>/', views.employee_form,name='employee_update'),
    path('config/',views.config,name='config'),
    path('testcase/', views.InsertCodeView.as_view(),name='testcase'),
    path('testelist/',views.test_list,name='testelist'),
    path('lists/<int:id>/',views.lists,name='lists'),
]