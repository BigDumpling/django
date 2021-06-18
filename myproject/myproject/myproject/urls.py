"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path

admin.site.site_title = '管理后台'
admin.site.site_header = '博客 管理后台'

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('board/', include('boards.urls'))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 不能放到应用的 urls.py文件里
handler404 = 'myproject.views.response_error_404_handler'
