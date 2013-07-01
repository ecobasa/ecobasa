# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SkillName'
        db.create_table(u'skillshare_skillname', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, db_index=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255)),
        ))
        db.send_create_signal(u'skillshare', ['SkillName'])

        # Adding model 'Skill'
        db.create_table(u'skillshare_skill', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'skillshare_skill', to=orm['skillshare.SkillName'])),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'skillshare_skill_creator', to=orm['auth.User'])),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'skillshare_skill_owner', to=orm['auth.User'])),
            ('info', self.gf('django.db.models.fields.TextField')()),
            ('experience', self.gf('django.db.models.fields.CharField')(default='NOV', max_length=3)),
            ('teach', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'skillshare', ['Skill'])

        # Adding unique constraint on 'Skill', fields ['name', 'owner']
        db.create_unique(u'skillshare_skill', ['name_id', 'owner_id'])

        # Adding model 'Badge'
        db.create_table(u'skillshare_badge', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('skill', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'skillshare_badge', to=orm['skillshare.Skill'])),
            ('giver', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('feedback', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'skillshare', ['Badge'])


    def backwards(self, orm):
        # Removing unique constraint on 'Skill', fields ['name', 'owner']
        db.delete_unique(u'skillshare_skill', ['name_id', 'owner_id'])

        # Deleting model 'SkillName'
        db.delete_table(u'skillshare_skillname')

        # Deleting model 'Skill'
        db.delete_table(u'skillshare_skill')

        # Deleting model 'Badge'
        db.delete_table(u'skillshare_badge')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'skillshare.badge': {
            'Meta': {'object_name': 'Badge'},
            'feedback': ('django.db.models.fields.TextField', [], {}),
            'giver': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'skill': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'skillshare_badge'", 'to': u"orm['skillshare.Skill']"})
        },
        u'skillshare.skill': {
            'Meta': {'ordering': "['name']", 'unique_together': "(('name', 'owner'),)", 'object_name': 'Skill'},
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'skillshare_skill_creator'", 'to': u"orm['auth.User']"}),
            'experience': ('django.db.models.fields.CharField', [], {'default': "'NOV'", 'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'skillshare_skill'", 'to': u"orm['skillshare.SkillName']"}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'skillshare_skill_owner'", 'to': u"orm['auth.User']"}),
            'teach': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'skillshare.skillname': {
            'Meta': {'object_name': 'SkillName'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['skillshare']