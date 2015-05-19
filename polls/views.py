from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader, RequestContext
from .models import Question
from django.http import Http404
from django.shortcuts import get_object_or_404, get_list_or_404

# Create your views here.
def index(req):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # # output = ','.join([q.question_text for q in latest_question_list])
    # # return HttpResponse(output)
    template = loader.get_template('polls/index.html')
    context = RequestContext(req, {
        'latest_question_list': latest_question_list,
    })
    return HttpResponse(template.render(context))

def detail(req, question_id):
    # try:
    #     question = Question.objects.get(pk = question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exit")
    question = get_object_or_404(Question, pk=question_id)
    return render(req, 'polls/detail.html', {'question': question})


def result(req, question_id):

    return HttpResponse("You're looking at result of question %s." % question_id)

def vote(req, question_id):
    return HttpResponse("You're voting on question %s." % question_id)