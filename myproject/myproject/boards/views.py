from django.http import HttpResponse
from django.template import loader

from .models import TBoard


# Create your views here.

def index(request):
    board = TBoard.objects.all()
    context = {'context': board}
    template = loader.get_template('boards/index.html')
    return HttpResponse(template.render(context, request))


def list_board(request):
    board = TBoard.objects.all()
    print(board)
    name_list = [value.description for value in board]
    return HttpResponse(name_list)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
