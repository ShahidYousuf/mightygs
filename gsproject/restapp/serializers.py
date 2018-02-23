from .models import Question, Subject
from rest_framework import serializers



class QuestionSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Question
        fields = ('section','text', 'a', 'b', 'c', 'd', 'answer')

class SubjectSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)
    class Meta:
        model = Subject
        fields= ('subject', 'questions')
        