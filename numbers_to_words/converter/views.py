from django.shortcuts import render
from num2words import num2words


def get_default_lang(request):
    accept_language = request.META.get('HTTP_ACCEPT_LANGUAGE', '')
    if 'de' in accept_language:
        return 'de'
    elif 'cs' in accept_language or 'cz' in accept_language:
        return 'cz'
    elif 'ru' in accept_language:
        return 'ru'
    return 'en'



def convert_number(request):
    number = request.GET.get('number', '')
    lang = request.GET.get('lang', get_default_lang(request))
    words = ''
    if number.isdigit():
        words = num2words(int(number), lang=lang)
    context = {'number': number, 'words': words, 'lang': lang}
    return render(request, 'converter/convert.html', context)


def index(request):
    return render(request, 'converter/index.html')
