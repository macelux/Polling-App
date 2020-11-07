from django.shortcuts import render
 
from .models import Question, Choice

#get questions and display them
def index(req):
    return render(req, 'polls/index.html')