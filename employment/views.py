from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse

from .models import *
from .serializers import *

from rest_framework.parsers import JSONParser
from rest_framework.generics import RetrieveAPIView


@csrf_exempt
def departmentApi(request, id=0):
    if request.method == 'GET':
        departments = Department.objects.all()
        departments_serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(departments_serializer.data, status=201, safe=False)

    elif request.method == 'POST':
        department_data = JSONParser().parse(request)
        department_serializer = DepartmentSerializer(data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Added Successfully",department_serializer.data, status=201, safe=False)
        return JsonResponse("Failed to Add ",department_serializer.data, status=404, safe=False)

    elif request.method == 'PUT':
        department_data = JSONParser().parse(request)
        department_serializer = DepartmentSerializer(data=department_data, instance=Department.objects.get(id=id))
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Updated Successfully",department_serializer.data, status=201, safe=False)
        return JsonResponse("Failed to Update ",department_serializer.data, status=404, safe=False)

    elif request.method == 'DELETE':
        department_data = JSONParser().parse(request)
        department_serializer = DepartmentSerializer(data=department_data, instance=Department.objects.get(id=id))
        if department_serializer.is_valid():
            department_serializer.delete()
            return JsonResponse("Deleted Successfully",department_serializer.data, status=201, safe=False)
        return JsonResponse("Failed to Delete ",department_serializer.data, status=404, safe=False)




class DepartmentDetailView(RetrieveAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class EmployeeDetailView(RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer