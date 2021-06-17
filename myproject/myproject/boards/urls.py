from django.conf.urls import url
from django.urls import path

from .views import *

app_name = 'boards'
urlpatterns = [
    url(r'^$', view=index, name='index'),
    path('<int:question_id>/', view=detail, name='detail'),
    path('<int:question_id>/results/', view=results, name='results'),
    path('<int:question_id>/vote/', view=vote, name='vote'),
    path('list', view=list_board, name='list_board'),
]
