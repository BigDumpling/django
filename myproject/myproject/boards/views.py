from django.http import HttpResponse

from .models import TBoard


# Create your views here.

def home(request):
    return HttpResponse('Hello World!')


def list_board(request):
    board = TBoard.objects.all()
    print(board)
    name_list = [value.description for value in board]
    return HttpResponse(name_list)
