from django.shortcuts import render
from django.utils import timezone
from .models import Post, Question, Choice
from django.http import HttpResponse
from django.template import loader

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'web/post_list.html', {'posts': posts})

#def index(request):
#    return render(request, 'web/index.html', {});

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('web/index.html')
    #output = ', '.join([q.question_text for q in latest_question_list])
    context = {
        'latest_question_list': latest_question_list,
    }
    #return HttpResponse(output)
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    return HttpResponse("you're looking at question. " % question_id)

def results(request, question_id):
    response = "you're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("you're votiong on question %s." % question_id)