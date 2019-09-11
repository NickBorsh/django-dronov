from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import Bb
from .models import Rubric

'''
Простой вывод информации
def index(request):
    s = 'Список объявлений\r\n\r\n\r\n'
    for bb in Bb.objects.order_by('-published'):
        s += bb.title + '\r\n' + str(bb.content) + '\r\n\r\n'
    return HttpResponse(s, content_type='text/plain; charset=utf-8')

Использование шаблона
def index(request):
    template = loader.get_template('bboard/index.html')
    bbs = Bb.objects.order_by('-published')
    context = {'bbs': bbs}
    return HttpResponse(template.render(context, request))
'''


# Функция-сокращение
def index(request):
    bbs = Bb.objects.all()
    return render(request, 'bboard/index.html', {'bbs': bbs})


def by_rubric(request, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'bbs': bbs, 'rubric': rubrics, 'current_rubric': current_rubric}
    return render (request, 'bboard/by_public.html', context)
