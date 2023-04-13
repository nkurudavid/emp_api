from django.urls import path
from . import views

urlpatterns = [
    path('departments/', views.departmentApi, name='departments'),
    path('departments/<int:pk>', views.departmentApi, name='department_info'),

    path('employees/', views.employeeApi, name='employees'),
    path('employees/<int:pk>', views.employeeApi,name='employee_info'),
    path('employee/saveFile', views.SaveFile),
]