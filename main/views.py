from django.shortcuts import render
from django.http import HttpResponse
from gonggo.models import Gonggo

# Create your views here.
def mainIndex(request):
    gonggoes=Gonggo.objects.all()
    context = {'gonggoes':gongoes}
    return render(request, 'main/index.html',context)
