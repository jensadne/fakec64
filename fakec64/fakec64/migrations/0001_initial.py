# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Disk'
        db.create_table(u'fakec64_disk', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('device', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('content', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'fakec64', ['Disk'])

        # Adding model 'File'
        db.create_table(u'fakec64_file', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('disk', self.gf('django.db.models.fields.related.ForeignKey')(related_name='files', to=orm['fakec64.Disk'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=24)),
            ('content', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal(u'fakec64', ['File'])


    def backwards(self, orm):
        # Deleting model 'Disk'
        db.delete_table(u'fakec64_disk')

        # Deleting model 'File'
        db.delete_table(u'fakec64_file')


    models = {
        u'fakec64.disk': {
            'Meta': {'object_name': 'Disk'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'device': ('django.db.models.fields.PositiveIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'fakec64.file': {
            'Meta': {'object_name': 'File'},
            'content': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'disk': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'files'", 'to': u"orm['fakec64.Disk']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '24'})
        }
    }

    complete_apps = ['fakec64']