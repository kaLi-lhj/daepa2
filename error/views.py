from django.shortcuts import render
from error.models import Error

# Create your views here.
def errMessage(request, message):
    error = Error.objects.values('code_name', 'note')\
            .get(code=message)
    return render(request, 'error/message.html', error)