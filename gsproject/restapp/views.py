# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Question, Subject
from .serializers import QuestionSerializer, SubjectSerializer


# Create your views here.

class QuestionList(APIView):
    def get(self, request, format=None):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

# sample queries
# www.shahidyousuf.pythonanywhere.com/subjects?subname=HIST
class SubjectList(APIView):
    def get(self, request, format=None):
        subname = request.query_params.get('subname', None)
        subjects = Subject.objects.all()
        if subname is not None:
            subjects = subjects.filter(subject = subname)
            
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data)
