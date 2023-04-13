from django.urls import path
from . import views

urlpatterns = [
    path('departments', views.departmentApi, name='departments'),
    path('departments/<int:id>', views.departmentApi,),

    # path('department_detail/<int:pk>/', DepartmentDetailView.as_view(), name='department_detail'),
    # path('employee_detail/<int:pk>/', EmployeeDetailView.as_view(), name='employee_detail'),
]