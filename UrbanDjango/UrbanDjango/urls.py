"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from task2.views import func_performance, Class_performance, index

# from task3.views import Trbl_win, Trbl_apps, Trbl_index # при проверке третьего задания расскомментируйте эту строку
from task4.views import Trbl_win, Trbl_apps, Trbl_index # и закомментируйте эту
from task5.views import Sign_Django, Sign_HTML

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('func/', func_performance),
    path('class/', Class_performance.as_view()),
    path('troubleshooting/', Trbl_index.as_view()),
    path('troubleshooting/windows', Trbl_win.as_view()),
    path('troubleshooting/apps', Trbl_apps.as_view()),
    path('SignHTML/', Sign_HTML.as_view()),
    path('SignDjango/', Sign_Django.as_view()),
]
