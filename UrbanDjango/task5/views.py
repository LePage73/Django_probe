from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.http import HttpResponse
from .forms import Reg_Forms

# Create your views here.

TITLE_HTML = {'title' : 'Форма регистрации HTML'}
TITLE_Django = {'title' : 'Форма регистрации Django'}

USER_LIST = ['vasily', 'serg63', 'urban', 'admin', 'olga', 'python', 'spring']

class Sign_HTML(View):
    my_context = {}
    info = {}
    template_name = ''
    def get(self, request):
        return render(request, self.template_name, self.my_context | self.info)
    def post(self,request):
        list_err = []
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        age = request.POST.get('age')
        if username.lower() in USER_LIST: list_err.append('Такой пользователь существует')
        if password != confirm_password: list_err.append('Пароль и подверждение не совпадают')
        if int(age) < 18: list_err.append('Вам должно быть больше 18 лет')
        if len(list_err) == 0: return HttpResponse(f'Приветствуем, {username}!') # регистрация прошла удачно
        self.info.clear()
        self.info['error'] = list_err
        return render(request, self.template_name, self.my_context | self.info) # Ошибка, опять выводим форму регистрации
                                                                                # И передаем ей перечень ошибок
    pass
Sign_HTML.template_name = 'fifth_task/tmpl_HTML.html'
Sign_HTML.my_context = TITLE_HTML    # добавляем свой контекст

class Sign_Django(View):
    my_context = {}
    info = {}
    template_name = ''
    def get(self, request):
        return render(request, self.template_name, self.my_context | self.info)
    def post(self,request):
        list_err = []
        form = Reg_Forms(request.POST)
        if form.is_valid():
            if form.cleaned_data['username'].lower() in USER_LIST: list_err.append('Такой пользователь существует')
            if form.cleaned_data['password'] != form.cleaned_data['confirm_password']: list_err.append(
                'Пароль и подверждение не совпадают')
            if int(form.cleaned_data['age']) < 18: list_err.append('Вам должно быть больше 18 лет')
            if len(list_err) == 0: return HttpResponse(
                f'Приветствуем, {form.cleaned_data['username']}!')  # регистрация прошла удачно
        self.info.clear()
        self.info['error'] = list_err
        self.info['form'] = form
        return render(request, self.template_name, self.my_context | self.info)
    pass
Sign_Django.template_name = 'fifth_task/tmpl_Django.html'
Sign_Django.my_context = TITLE_Django # добавляем свой контекст




