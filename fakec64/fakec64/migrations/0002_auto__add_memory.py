# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Memory'
        db.create_table(u'fakec64_memory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('address', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'fakec64', ['Memory'])


    def backwards(self, orm):
        # Deleting model 'Memory'
        db.delete_table(u'fakec64_memory')


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
        },
        u'fakec64.memory': {
            'Meta': {'object_name': 'Memory'},
            'address': ('django.db.models.fields.PositiveIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        }
    }

    complete_apps = ['fakec64']