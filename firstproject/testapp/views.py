from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
   text = """<h1>Hello World</h1>"""
   return HttpResponse(text)
