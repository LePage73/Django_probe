from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


def index(request):
    return render(request, 'index.html')
def func_performance(request):
    return render(request, 'template_func.html')
class Class_performance(TemplateView):
    template_name = 'template_class.html'