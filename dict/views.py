from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def mainIndex(request):
    return render(request, 'dict/index.html')