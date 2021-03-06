from django.db import models


class Disk(models.Model):
    device = models.PositiveIntegerField()
    content = models.TextField()

    def load_file(self, filename):
        if not filename in self.content:
            return None
        return self.files.get(name=filename)


class File(models.Model):
    disk = models.ForeignKey(Disk, related_name='files')
    name = models.CharField(max_length=24) 
    content = models.CharField(max_length=256)


class Memory(models.Model):
    address = models.PositiveIntegerField()
    value = models.CharField(max_length=1)
