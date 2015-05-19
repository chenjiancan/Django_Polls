from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(req):
    return HttpResponse("Hey boy!")


def detail(req, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def result(req, question_id):
    return HttpResponse("You're looking at result of question %s." % question_id)

def vote(req, question_id):
    return HttpResponse("You're voting on question %s." % question_id)