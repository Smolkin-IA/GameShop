from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Main page</h1>')


