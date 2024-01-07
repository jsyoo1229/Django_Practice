from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseNotFound, Http404

articles = {
    'sports': 'sports page',
    'finance': 'finance page',
    'politics': 'politics page'
}

def news_view(request, topic):
    try:
        result = articles[topic]
        return HttpResponse(result)
    except:
        raise Http404('404 Generic Error')

def simple_view(request):
    return HttpResponse('simple view')

def add(request, num1, num2):
    add_result = num1 + num2
    result = f"{num1} + {num2} = {add_result}"
    return HttpResponse(str(result))


# Create your views here.
