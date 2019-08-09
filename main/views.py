from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Max                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
import random

import sys
sys.path.append("..")
from gonggo.models import Gonggo


# Create your views here.
def mainIndex(request):
    
    data = Gonggo.objects.all().order_by('id')
    return render(request, 'main/index.html',{"gonggo":data})