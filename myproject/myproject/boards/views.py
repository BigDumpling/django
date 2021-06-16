from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
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
    # 1. 普通
    # board = TBoard.objects.get(id=question_id)

    # 2. 404页面
    # try:
    #     board = TBoard.objects.get(id=question_id)
    # except TBoard.DoesNotExist:
    #     raise Http404('Boards: %s does not exit ' % question_id)

    # 语法糖
    board = get_object_or_404(TBoard, id=question_id)
    return render(request=request, template_name='boards/detail.html', context={'context': board})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
