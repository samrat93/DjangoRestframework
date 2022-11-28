from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company,Employee
from api.serializers import CompanySerializer,EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class CompanyViewSet(viewsets.ModelViewSet):
    """ View set for company """

    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    
    # api/v1/companies/<company-id>/employee/
    @action(detail=True,methods=['get'])
    def employee(self,request,pk=None):
        try:
            company = Company.objects.get(pk=pk)
            empList = Employee.objects.filter(company=company)
            emp_serializer = EmployeeSerializer(empList,many=True,context={'request':request})
            return Response(emp_serializer.data)
        except Exception as e:
            return Response({'message':'Data not exists !!!'})


class EmployeeViewSet(viewsets.ModelViewSet):
    """ View set for Employee table """

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

