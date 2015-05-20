from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader, RequestContext
from .models import Question, Choice
from django.http import Http404
from django.shortcuts import get_object_or_404, get_list_or_404
from django.core.urlresolvers import reverse

from django.views import generic
# Create your views here.
# def index(req):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     # # output = ','.join([q.question_text for q in latest_question_list])
#     # # return HttpResponse(output)
#     template = loader.get_template('polls/index.html')
#     context = RequestContext(req, {
#         'latest_question_list': latest_question_list,
#     })
#     return HttpResponse(template.render(context))
#
# def detail(req, question_id):
#     # try:
#     #     question = Question.objects.get(pk = question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exit")
#     question = get_object_or_404(Question, pk=question_id)
#     return render(req, 'polls/detail.html', {'question': question})
#
#
# def result(req, question_id):
#     # return HttpResponse("You're looking at result of question %s." % question_id)
#     question = get_object_or_404(Question, pk=question_id)
#     return render(req, 'polls/result.html', {'question': question})

# 使用 generic view
# generic.ListView 用于显示一个列表的数据对象
class IndexView(generic.ListView):
    # 指定显示的url字符串，默认是 <app name>/<model name>_detail.html.
    template_name = 'polls/index.html'
    # context_object_name = '' # 指定list 对象的名字，默认为 <模块名（question）>_list
    # 使用默认的名字 需要修改模板以匹配

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    template_name = 'polls/detail.html'
    model = Question

class ResultView(generic.DetailView):
    template_name = 'polls/result.html'
    model = Question

def vote(req, question_id):
    # return HttpResponse("You're voting on question %s." % question_id)
    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=req.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(req, "polls/detail.html", {'question': question, 'error_message': "You didn't select a choice"})

    else:
        selected_choice.votes += 1
        selected_choice.save()
        # 成功处理一个POST 数据之后，需要 重定向防止用户使用back 而提交多次
        return HttpResponseRedirect(reverse("polls:result", args=(question.id,)))