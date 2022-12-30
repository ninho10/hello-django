from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse(f'<h1>Hello World sou o {nome} tenho {idade} anos </h1>')


