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
MAIN_TITLE = {'title': 'Главная страница Техподдержки'}
MENU = {'menu': [{'menu': 'Главная', 'href': './'},
                 {'menu': 'Windows', 'href': './windows'},
                 {'menu': 'Приложение', 'href': './apps'}
                 ]}

WIN_TITLE = {'title': 'Проблема с Windows'}
WIN_CONTENT_MENU = {'cntxt_menu': [
    {'menu': 'Windows запускается только в "безопасном режиме"', 'button': 'Комплект драйверов'},
    {'menu': 'При загрузке появляется "синий экран смерти"', 'button': 'Утилита диагностики'},
    {'menu': 'При загрузке ничего не происходит - черный экран', 'button': 'Вызвать мастера'}
]}
APPS_TITLE = {'title': 'Проблема с приложением'}
APPS_CONTENT_MENU = {'cntxt_menu': [
    {'menu': 'Приложение не запускается - ничего не происходит ', 'button': 'Комплект драйверов'},
    {'menu': 'Приложение зависает через некоторое время ', 'button': 'Утилита диагностики'},
    {'menu': 'При запуске приложения "Синий экран смерти" ', 'button': 'Вызвать мастера'},
    {'menu': 'Приложение вылетает с ошибкой "404" ', 'button': 'Проверить Интернет'}
]}

# привяжем шаблоны к классам и подключим контекст
class Trbl_index(Tmpl_trouble):
    pass
Trbl_index.template_name = 'fourth_task/tmpl_index_DTL.html'
Trbl_index.my_context = MENU | MAIN_TITLE  # добавляем свой контекст

class Trbl_win(Tmpl_trouble):
    pass
Trbl_win.template_name = 'fourth_task/tmpl_trouble_DTL.html'
Trbl_win.my_context = MENU | WIN_TITLE | WIN_CONTENT_MENU # добавляем свой контекст

class Trbl_apps(Tmpl_trouble):
    pass
Trbl_apps.template_name = 'fourth_task/tmpl_trouble_DTL.html'
Trbl_apps.my_context = MENU | APPS_TITLE | APPS_CONTENT_MENU # добавляем свой контекст


