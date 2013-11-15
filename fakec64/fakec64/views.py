from django.http import HttpResponse

from .forms import CommandForm


def validate_command(request):
    form = CommandForm(request.POST)
    if not form.is_valid():
        return HttpResponse('syntax error') 
    return HttpResponse('ok')  
