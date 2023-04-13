from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse

from .models import *
from .serializers import *

from rest_framework.parsers import JSONParser
from rest_framework.generics import RetrieveAPIView


@csrf_exempt
def departmentApi(request, id=None):
    if request.method == 'GET':
        departments = Department.objects.all()
        departments_serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(departments_serializer.data, status=200, safe=False)

    elif request.method == 'POST':
        department_data = JSONParser().parse(request)
        department_serializer = DepartmentSerializer(data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Added Successfully", status=201, safe=False)
        return JsonResponse("Failed to Add ", status=400, safe=False)

    elif request.method == 'PUT':
        department_data = JSONParser().parse(request)
        department_serializer = DepartmentSerializer(data=department_data, instance=Department.objects.get(id=id))
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Updated Successfully", status=201, safe=False)
        return JsonResponse("Failed to Update ", status=400, safe=False)

    elif request.method == 'DELETE':
        department = Department.objects.get(id=id)
        if department:
            department.delete()
            return JsonResponse("Deleted Successfully", status=301, safe=False)
        return JsonResponse("Failed to Delete ", status=400, safe=False)



@csrf_exempt
def employeeApi(request, id=None):
    if request.method == 'GET':
        employees = Employee.objects.all()
        employees_serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(employees_serializer.data, status=200, safe=False)

    elif request.method == 'POST':
        employee_data = JSONParser().parse(request)
        employee_serializer = EmployeeSerializer(data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Added Successfully", status=201, safe=False)
        return JsonResponse("Failed to Add ", status=400, safe=False)

    elif request.method == 'PUT':
        employee_data = JSONParser().parse(request)
        employee_serializer = EmployeeSerializer(data=employee_data, instance=Employee.objects.get(id=id))
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Updated Successfully", status=201, safe=False)
        return JsonResponse("Failed to Update ", status=400, safe=False)

    elif request.method == 'DELETE':
        employee = Employee.objects.get(id=id)
        if employee:
            employee.delete()
            return JsonResponse("Deleted Successfully", status=301, safe=False)
        return JsonResponse("Failed to Delete ", status=400, safe=False)