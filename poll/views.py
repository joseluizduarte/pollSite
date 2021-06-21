from .models import Choice, Question

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from random import choice

# Create your views here.

def home(request):
    questions_list = Question.objects.all()
    context ={
        'questions':questions_list
    }
    return render(request,'poll/home.html',context=context)

def question_detail(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question':question
    }
    return render(request,'poll/detail.html',context=context)

def vote(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        #Redisplay the question vote form
        context = {
            'question':question,
            'error_message':"You didn't select a choice"
            }
        return render(request,'poll/detail.html',context=context)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('poll:results',args=(question.id,)))


def results(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    context = {'question':question}
    return render(request,'poll/results.html',context=context)

def suggestion(request):
    pass

def randomQuestion(request):
    list_question = Question.objects.all()
    random_question = choice(list_question)
    return HttpResponseRedirect(reverse('poll:detail',args=(random_question.id,)))
