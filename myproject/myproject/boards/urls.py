from django.conf.urls import url
from django.urls import path

from .views import *

urlpatterns = [
    url(r'^$', view=home, name='home'),
    path('list', view=list_board, name='list_board')
]
