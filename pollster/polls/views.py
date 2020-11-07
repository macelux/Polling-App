from django.shortcuts import get_object_or_404,render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse

 
from .models import Question, Choice

#get questions and display them
def index(req):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = { 'latest_question_list': latest_question_list}
    return render(req, 'polls/index.html', context)


#show specific question and choices
def details(req,question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exist')
    return render(req, 'polls/details.html', {'question': question})

#get questions and display result
def results(req, question_id):
    question= get_object_or_404(Question, pk=question_id)
    return render(req, 'polls/result.html', {'question' : question})

# vote for a question choice
def vote(request, question_id):
    # print (request.POST['choice])
    question = get_object_or_404(Question, pk= question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/details.html', {
            'question': question, 'error_message': "you didn't select a choice"
        })
    else:
        selected_choice.votes +=1
        selected_choice.save()
        # return HttpResponseRedirect to prevent user form
        # submitting the form twice when they click the back button
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))