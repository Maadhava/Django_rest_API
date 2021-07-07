from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
from .models import employees
from .serializers import employeesSerializer

class employeelist(APIView):
    def get(self,request):
        employee1=employees.objects.all()
        serializer=employeesSerializer(employee1,many=True)
        return Response(serializer.data)
    def post(self,request):
        emp_data = request.data
        emp_det = employees.objects.create(firstname=emp_data["firstname"],lastname=emp_data["lastname"],emp_id=emp_data["emp_id"])
        emp_det.save()
        serializer=employeesSerializer(emp_det)
        return Response(serializer.data)

    def put(self):
        pass