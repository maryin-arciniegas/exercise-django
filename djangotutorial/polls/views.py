import json

from django.http import HttpResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from .models import Question

@csrf_exempt
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def detail(request, question_id):
    question_db = Question.objects.filter(id=question_id)
    return HttpResponse(question_db)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

@csrf_exempt
def create_question(request):
    body =request.POST.dict()
    text = body['text']
    q = Question(question_text=text, pub_date=timezone.now())
    q.save()
    return HttpResponse(f'Se creo la pregunta con id {q.id}' )

@csrf_exempt
def update_question(request, question_id):
    from django.http import QueryDict
    data = QueryDict(request.body).dict()
    text = data['text']
    question_db = Question.objects.get(pk=question_id)
    question_db.question_text = text
    question_db.pub_date = timezone.now()
    question_db.save()
    return HttpResponse (f'se ha actualizado la pregunta con id {question_id} por el texto {question_db}')

@csrf_exempt
def delete_question(request, question_id):
    question_db = Question.objects.get(pk=question_id)
    question_db.is_active = False
    question_db.save()
    return HttpResponse(f'se ha eliminado la pregunta con id {question_id} con el texto {question_db}')







