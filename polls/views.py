from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Question
from django.http import Http404
from django.shortcuts import render

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    question = Question.objects_or_404(Question, pk=question_id)
    return render(request, 'polls/detais.html', {'question': question})

def results(request, question_id):
    reponse = "You're looking at the results of question %s."
    return  HttpResponse(reponse % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)




