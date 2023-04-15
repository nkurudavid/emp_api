from rest_framework import serializers
from .models import *
import logging

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer()
    class Meta:
        model = Employee
        fields = '__all__'

    def create(self, validated_data):
        logging.debug(validated_data)
        return super().create(validated_data)