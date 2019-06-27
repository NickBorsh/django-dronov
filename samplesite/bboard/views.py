from django.http import HttpResponse


def index(request):
    return HttpResponse('Здесь когда-нибудь будет список объявлений')