# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TaggedReferenceProduct'
        db.create_table(u'ecobasa_taggedreferenceproduct', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'ecobasa_taggedreferenceproduct_items', to=orm['taggit.Tag'])),
            ('content_object', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ecobasa.Reference'])),
        ))
        db.send_create_signal(u'ecobasa', ['TaggedReferenceProduct'])

        # Adding model 'TaggedReferenceSkill'
        db.create_table(u'ecobasa_taggedreferenceskill', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'ecobasa_taggedreferenceskill_items', to=orm['taggit.Tag'])),
            ('content_object', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ecobasa.Reference'])),
        ))
        db.send_create_signal(u'ecobasa', ['TaggedReferenceSkill'])

        # Adding model 'TaggedReferenceService'
        db.create_table(u'ecobasa_taggedreferenceservice', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'ecobasa_taggedreferenceservice_items', to=orm['taggit.Tag'])),
            ('content_object', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ecobasa.Reference'])),
        ))
        db.send_create_signal(u'ecobasa', ['TaggedReferenceService'])

        # Adding model 'Reference'
        db.create_table(u'ecobasa_reference', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('giver', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'ecobasa_reference_giver', to=orm['auth.User'])),
            ('receiver_pioneer', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'ecobasa_reference_receiver_pioneer', null=True, to=orm['auth.User'])),
            ('receiver_community', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'ecobasa_reference_receiver_community', null=True, to=orm['cosinnus.CosinnusGroup'])),
            ('date', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('rating', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'ecobasa', ['Reference'])

        # Adding unique constraint on 'Reference', fields ['giver', 'receiver_pioneer']
        db.create_unique(u'ecobasa_reference', ['giver_id', 'receiver_pioneer_id'])

        # Adding unique constraint on 'Reference', fields ['giver', 'receiver_community']
        db.create_unique(u'ecobasa_reference', ['giver_id', 'receiver_community_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Reference', fields ['giver', 'receiver_community']
        db.delete_unique(u'ecobasa_reference', ['giver_id', 'receiver_community_id'])

        # Removing unique constraint on 'Reference', fields ['giver', 'receiver_pioneer']
        db.delete_unique(u'ecobasa_reference', ['giver_id', 'receiver_pioneer_id'])

        # Deleting model 'TaggedReferenceProduct'
        db.delete_table(u'ecobasa_taggedreferenceproduct')

        # Deleting model 'TaggedReferenceSkill'
        db.delete_table(u'ecobasa_taggedreferenceskill')

        # Deleting model 'TaggedReferenceService'
        db.delete_table(u'ecobasa_taggedreferenceservice')

        # Deleting model 'Reference'
        db.delete_table(u'ecobasa_reference')


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
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'cosinnus.cosinnusgroup': {
            'Meta': {'ordering': "(u'name',)", 'object_name': 'CosinnusGroup'},
            'description': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'media_tag': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['cosinnus.TagObject']", 'unique': 'True', 'null': 'True', 'on_delete': 'models.PROTECT', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'blank': 'True'}),
            'users': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'cosinnus_groups'", 'blank': 'True', 'through': u"orm['cosinnus.CosinnusGroupMembership']", 'to': u"orm['auth.User']"})
        },
        u'cosinnus.cosinnusgroupmembership': {
            'Meta': {'unique_together': "((u'user', u'group'),)", 'object_name': 'CosinnusGroupMembership'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'memberships'", 'to': u"orm['cosinnus.CosinnusGroup']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'db_index': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'cosinnus_memberships'", 'to': u"orm['auth.User']"})
        },
        u'cosinnus.tagobject': {
            'Meta': {'object_name': 'TagObject'},
            'group': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'+'", 'null': 'True', 'to': u"orm['cosinnus.CosinnusGroup']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location_place': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255', 'blank': 'True'}),
            'people_name': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255', 'blank': 'True'}),
            'persons': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "u'+'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['auth.User']"}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'visibility': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1', 'blank': 'True'})
        },
        u'ecobasa.caravan': {
            'Meta': {'ordering': "(u'name',)", 'object_name': 'Caravan', '_ormbases': [u'cosinnus.CosinnusGroup']},
            u'cosinnusgroup_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['cosinnus.CosinnusGroup']", 'unique': 'True', 'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'ecobasa.ecobasacommunityprofile': {
            'Meta': {'object_name': 'EcobasaCommunityProfile'},
            'basic_brings_together': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'basic_inhabitants': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'basic_inhabitants_underage': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'basic_membership_status': ('django.db.models.fields.CharField', [], {'default': "u'o'", 'max_length': '2', 'blank': 'True'}),
            'contact_city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'contact_country': ('django.db.models.fields.CharField', [], {'default': "u'ZZ'", 'max_length': '2', 'blank': 'True'}),
            'contact_location': ('osm_field.fields.OSMField', [], {'null': 'True', 'blank': 'True'}),
            'contact_location_lat': ('osm_field.fields.LatitudeField', [], {'null': 'True', 'blank': 'True'}),
            'contact_location_lon': ('osm_field.fields.LongitudeField', [], {'null': 'True', 'blank': 'True'}),
            'contact_show': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'contact_street': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'contact_telephone': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'contact_zipcode': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "u'profile'", 'unique': 'True', 'to': u"orm['cosinnus.CosinnusGroup']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'offers_learning_seminars': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'offers_workshop_spaces': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'video': ('django.db.models.fields.URLField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'visitors_accommodation': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'visitors_num': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'wishlist_materials': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'wishlist_projects': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'wishlist_special_needs': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'wishlist_tools': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'ecobasa.ecobasacommunityprofileseed': {
            'Meta': {'object_name': 'EcobasaCommunityProfileSeed'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'num': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'wishlist_seeds'", 'to': u"orm['ecobasa.EcobasaCommunityProfile']"})
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
            'country': ('django.db.models.fields.CharField', [], {'default': "u'ZZ'", 'max_length': '2', 'blank': 'True'}),
            'ecobasa_member': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'gender': ('django.db.models.fields.CharField', [], {'default': "u'o'", 'max_length': '2', 'blank': 'True'}),
            'has_bus': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tour_how': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'tour_why': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "u'cosinnus_profile'", 'unique': 'True', 'to': u"orm['auth.User']"}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'ecobasa.organiserrole': {
            'Meta': {'object_name': 'OrganiserRole'},
            'cosinnus_group_membership': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cosinnus.CosinnusGroupMembership']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'ecobasa.reference': {
            'Meta': {'unique_together': "((u'giver', u'receiver_pioneer'), (u'giver', u'receiver_community'))", 'object_name': 'Reference'},
            'date': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'giver': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'ecobasa_reference_giver'", 'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rating': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'receiver_community': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'ecobasa_reference_receiver_community'", 'null': 'True', 'to': u"orm['cosinnus.CosinnusGroup']"}),
            'receiver_pioneer': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'ecobasa_reference_receiver_pioneer'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        u'ecobasa.slideshowimage': {
            'Meta': {'ordering': "(u'order', u'id')", 'object_name': 'SlideshowImage'},
            'file': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['filer.Image']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'slideshow': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'images'", 'to': u"orm['ecobasa.SlideshowPlugin']"}),
            'text': ('django.db.models.fields.TextField', [], {'max_length': '255', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'ecobasa.slideshowplugin': {
            'Meta': {'object_name': 'SlideshowPlugin', 'db_table': "u'cmsplugin_slideshowplugin'", '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'ecobasa.taggedinterest': {
            'Meta': {'object_name': 'TaggedInterest'},
            'content_object': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ecobasa.EcobasaUserProfile']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'ecobasa_taggedinterest_items'", 'to': u"orm['taggit.Tag']"})
        },
        u'ecobasa.taggedoffers': {
            'Meta': {'object_name': 'TaggedOffers'},
            'content_object': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ecobasa.Caravan']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'ecobasa_taggedoffers_items'", 'to': u"orm['taggit.Tag']"})
        },
        u'ecobasa.taggedofferscreation': {
            'Meta': {'object_name': 'TaggedOffersCreation'},
            'content_object': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ecobasa.EcobasaCommunityProfile']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'ecobasa_taggedofferscreation_items'", 'to': u"orm['taggit.Tag']"})
        },
        u'ecobasa.taggedoffersservice': {
            'Meta': {'object_name': 'TaggedOffersService'},
            'content_object': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ecobasa.EcobasaCommunityProfile']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'ecobasa_taggedoffersservice_items'", 'to': u"orm['taggit.Tag']"})
        },
        u'ecobasa.taggedoffersskill': {
            'Meta': {'object_name': 'TaggedOffersSkill'},
            'content_object': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ecobasa.EcobasaCommunityProfile']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'ecobasa_taggedoffersskill_items'", 'to': u"orm['taggit.Tag']"})
        },
        u'ecobasa.taggedproduct': {
            'Meta': {'object_name': 'TaggedProduct'},
            'content_object': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ecobasa.EcobasaUserProfile']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'ecobasa_taggedproduct_items'", 'to': u"orm['taggit.Tag']"})
        },
        u'ecobasa.taggedreferenceproduct': {
            'Meta': {'object_name': 'TaggedReferenceProduct'},
            'content_object': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ecobasa.Reference']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'ecobasa_taggedreferenceproduct_items'", 'to': u"orm['taggit.Tag']"})
        },
        u'ecobasa.taggedreferenceservice': {
            'Meta': {'object_name': 'TaggedReferenceService'},
            'content_object': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ecobasa.Reference']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'ecobasa_taggedreferenceservice_items'", 'to': u"orm['taggit.Tag']"})
        },
        u'ecobasa.taggedreferenceskill': {
            'Meta': {'object_name': 'TaggedReferenceSkill'},
            'content_object': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ecobasa.Reference']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'ecobasa_taggedreferenceskill_items'", 'to': u"orm['taggit.Tag']"})
        },
        u'ecobasa.taggedskill': {
            'Meta': {'object_name': 'TaggedSkill'},
            'content_object': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ecobasa.EcobasaUserProfile']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'ecobasa_taggedskill_items'", 'to': u"orm['taggit.Tag']"})
        },
        u'ecobasa.taggedwishskill': {
            'Meta': {'object_name': 'TaggedWishSkill'},
            'content_object': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ecobasa.EcobasaCommunityProfile']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'ecobasa_taggedwishskill_items'", 'to': u"orm['taggit.Tag']"})
        },
        'filer.file': {
            'Meta': {'object_name': 'File'},
            '_file_size': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'folder': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'all_files'", 'null': 'True', 'to': "orm['filer.Folder']"}),
            'has_all_mandatory_data': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'original_filename': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'owned_files'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'polymorphic_ctype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'polymorphic_filer.file_set'", 'null': 'True', 'to': u"orm['contenttypes.ContentType']"}),
            'sha1': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '40', 'blank': 'True'}),
            'uploaded_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'filer.folder': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('parent', 'name'),)", 'object_name': 'Folder'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'filer_owned_folders'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['filer.Folder']"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'uploaded_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'filer.image': {
            'Meta': {'object_name': 'Image', '_ormbases': ['filer.File']},
            '_height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            '_width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'date_taken': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'default_alt_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'default_caption': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'file_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['filer.File']", 'unique': 'True', 'primary_key': 'True'}),
            'must_always_publish_author_credit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'must_always_publish_copyright': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'subject_location': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '64', 'null': 'True', 'blank': 'True'})
        },
        u'taggit.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'taggit.taggeditem': {
            'Meta': {'object_name': 'TaggedItem'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'taggit_taggeditem_tagged_items'", 'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'taggit_taggeditem_items'", 'to': u"orm['taggit.Tag']"})
        }
    }

    complete_apps = ['ecobasa']