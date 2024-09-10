# from django.shortcuts import render # не нужна
from django.views.generic import TemplateView

# Create your views here.
# учим класс добавлять свои переменные в контекст
class Tmpl_trouble(TemplateView):
    my_context: dict
    def get_context_data(self,  *args, **kwargs,): # переопределим для враппинга своего контекста
        context = super().get_context_data(**kwargs)
        context['my_context'] = self.my_context
        return context

# подготовим меню и контент
CONTEXT_INDEX = {'title': 'Главная страница Техподдержки',
                 'menu': [{'menu': 'Переход на главную', 'href': './'},
                           {'menu': 'Проблемы с запуском Windows', 'href': './windows'},
                           {'menu': 'Проблемы с запуском приложений', 'href': './apps'}
                           ]}
CONTEXT_WIN = {'title': 'Проблема с Windows',
               'menu': [{'menu': 'Windows запускается только в "безопасном режиме"', 'button': 'Комплект драйверов'},
                         {'menu': 'При загрузке появляется "синий экран смерти"', 'button': 'Утилита диагностики'},
                         {'menu': 'При загрузке ничего не происходит - черный экран', 'button': 'Вызвать мастера'}
                         ]}
CONTEXT_APPS = {'title': 'Проблема с приложением',
                'menu': [{'menu': 'Приложение не запускается - ничего не происходит', 'button': 'Комплект драйверов'},
                          {'menu': 'Приложение зависает через некоторое время', 'button': 'Утилита диагностики'},
                          {'menu': 'При запуске приложения "Синий экран смерти"', 'button': 'Вызвать мастера'}
                          ]}

# привяжем шаблоны к классам и подключим контекст
class Trbl_index(Tmpl_trouble):
    pass
Trbl_index.template_name = 'third_task/tmpl_index.html'
Trbl_index.my_context = CONTEXT_INDEX # добавляем свой контекст

class Trbl_win(Tmpl_trouble):
    pass
Trbl_win.template_name = 'third_task/tmpl_trouble.html'
Trbl_win.my_context = CONTEXT_WIN # добавляем свой контекст

class Trbl_apps(Tmpl_trouble):
    pass
Trbl_apps.template_name = 'third_task/tmpl_trouble.html'
Trbl_apps.my_context = CONTEXT_APPS # добавляем свой контекст


