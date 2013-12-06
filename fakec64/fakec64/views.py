import re

from django.http import HttpResponse, HttpResponseBadRequest

from .forms import CommandForm
from .models import Disk, File, Memory

memory = {}
for cell in Memory.objects.all():
    memory[cell.address] = cell.value

load_re = re.compile(r'^load( )?"((\$|[a-z0-9]+))",8')
peek_re = re.compile(r'^peek ([0-9]+)')


def validate_command(request):
    form = CommandForm(request.POST)
    if not form.is_valid():
        print form.errors
        return HttpResponseBadRequest('syntax error') 

    disk = Disk.objects.get(pk=1)

    print form.cleaned_data['command']
    cmd = form.cleaned_data['command'].lower()
    if cmd.startswith('load'):
        filename = load_re.match(cmd).groups()[1]
        print filename
        if filename == '$':
            request.session['disk_loaded'] = True
            return HttpResponse('')
        try:
            fil = disk.load_file(filename=filename.upper())
            request.session['file_loaded'] = fil.pk
            return HttpResponse('ready.'.upper())
        except File.DoesNotExist:
            return HttpResponse('file not found'.upper())

    if cmd.startswith('list') and request.session.get('disk_loaded', False):
        return HttpResponse(disk.content)
    if cmd.startswith('run'):
        if not request.session.get('file_loaded'):
            return HttpResponse('syntax error')
        fil = disk.files.get(pk=request.session['file_loaded'])
        return HttpResponse(fil.content.upper())
    if cmd.startswith('peek'):
        address = int(peek_re.match(cmd).groups()[0])
        return HttpResponse(memory.get(address, '').upper())

    return HttpResponse('syntax error')
