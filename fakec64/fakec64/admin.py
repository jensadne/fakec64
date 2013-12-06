from django.contrib import admin

from .models import Disk, File, Memory

admin.site.register(Disk)
admin.site.register(File)
admin.site.register(Memory)
