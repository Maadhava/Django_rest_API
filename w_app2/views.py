from django.shortcuts import render
from rest_framework import viewsets
from w_app2.serializer import studentsSerializer
from w_app2.models import students
# Create your views here.


class studentsViewset(viewsets.ModelViewSet):
    serializer_class = studentsSerializer
    queryset = students.objects.all()
    lookup_field='stud_id'
