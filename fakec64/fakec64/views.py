from django.http import HttpResponse, HttpResponseBadRequest

from .forms import CommandForm


def validate_command(request):
    form = CommandForm(request.POST)
    if not form.is_valid():
        return HttpResponseBadRequest('syntax error') 
    print form.cleaned_data['command']
    return HttpResponse('ok')
