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




class DepartmentDetailView(RetrieveAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class EmployeeDetailView(RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer