# Register your models here.

from django.contrib import admin

from .models import *

admin.site.register(TBoard)
admin.site.register(TTopic)
admin.site.register(TPost)
admin.site.register(TConstant)
