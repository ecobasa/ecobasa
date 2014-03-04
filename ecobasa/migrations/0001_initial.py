# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TaggedInterest'
        db.create_table(u'ecobasa_taggedinterest', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'ecobasa_taggedinterest_items', to=orm['taggit.Tag'])),
            ('content_object', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ecobasa.EcobasaUserProfile'])),
        ))
        db.send_create_signal(u'ecobasa', ['TaggedInterest'])

        # Adding model 'TaggedSkill'
        db.create_table(u'ecobasa_taggedskill', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'ecobasa_taggedskill_items', to=orm['taggit.Tag'])),
            ('content_object', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ecobasa.EcobasaUserProfile'])),
        ))
        db.send_create_signal(u'ecobasa', ['TaggedSkill'])

        # Adding model 'TaggedProduct'
        db.create_table(u'ecobasa_taggedproduct', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'ecobasa_taggedproduct_items', to=orm['taggit.Tag'])),
            ('content_object', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ecobasa.EcobasaUserProfile'])),
        ))
        db.send_create_signal(u'ecobasa', ['TaggedProduct'])

        # Adding model 'EcobasaUserProfile'
        db.create_table(u'ecobasa_ecobasauserprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(related_name=u'cosinnus_profile', unique=True, to=orm['auth.User'])),
            ('avatar', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('gender', self.gf('django.db.models.fields.CharField')(default=u'o', max_length=2)),
            ('birth_date', self.gf('django.db.models.fields.DateField')(default=None, null=True, blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(default=u'ZZ', max_length=2)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('zipcode', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('has_bus', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('bus_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('bus_has_driving_license', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('bus_others_can_drive', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('bus_num_passengers', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, null=True, blank=True)),
            ('bus_consumption', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, null=True, blank=True)),
        ))
        db.send_create_signal(u'ecobasa', ['EcobasaUserProfile'])


    def backwards(self, orm):
        # Deleting model 'TaggedInterest'
        db.delete_table(u'ecobasa_taggedinterest')

        # Deleting model 'TaggedSkill'
        db.delete_table(u'ecobasa_taggedskill')

        # Deleting model 'TaggedProduct'
        db.delete_table(u'ecobasa_taggedproduct')

        # Deleting model 'EcobasaUserProfile'
        db.delete_table(u'ecobasa_ecobasauserprofile')


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
        u'ecobasa.ecobasauserprofile': {
            'Meta': {'object_name': 'EcobasaUserProfile'},
            'avatar': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'birth_date': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'bus_consumption': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'bus_has_driving_license': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'bus_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'bus_num_passengers': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'bus_others_can_drive': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'default': "u'ZZ'", 'max_length': '2'}),
            'gender': ('django.db.models.fields.CharField', [], {'default': "u'o'", 'max_length': '2'}),
            'has_bus': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "u'cosinnus_profile'", 'unique': 'True', 'to': u"orm['auth.User']"}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'ecobasa.taggedinterest': {
            'Meta': {'object_name': 'TaggedInterest'},
            'content_object': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ecobasa.EcobasaUserProfile']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'ecobasa_taggedinterest_items'", 'to': u"orm['taggit.Tag']"})
        },
        u'ecobasa.taggedproduct': {
            'Meta': {'object_name': 'TaggedProduct'},
            'content_object': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ecobasa.EcobasaUserProfile']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'ecobasa_taggedproduct_items'", 'to': u"orm['taggit.Tag']"})
        },
        u'ecobasa.taggedskill': {
            'Meta': {'object_name': 'TaggedSkill'},
            'content_object': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ecobasa.EcobasaUserProfile']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'ecobasa_taggedskill_items'", 'to': u"orm['taggit.Tag']"})
        },
        u'taggit.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['ecobasa']