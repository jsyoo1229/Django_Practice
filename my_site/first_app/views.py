from django.shortcuts import render
from django.http.response import HttpResponse

articles = {
    'sports': 'sports page',
    'finance': 'finance page',
    'politics': 'politics page'
}

def news_view(request, topic):
    return HttpResponse(articles[topic])

def simple_view(request):
    return HttpResponse('simple view')

def add(request, num1, num2):
    add_result = num1 + num2
    result = f"{num1} + {num2} = {add_result}"
    return HttpResponse(str(result))


# Create your views here.
