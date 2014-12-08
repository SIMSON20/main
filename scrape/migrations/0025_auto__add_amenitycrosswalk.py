# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AmenityCrossWalk'
        db.create_table('scrape_amenitycrosswalk', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('amenity', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['property.Amenity'])),
            ('scrape_title', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal('scrape', ['AmenityCrossWalk'])


    def backwards(self, orm):
        # Deleting model 'AmenityCrossWalk'
        db.delete_table('scrape_amenitycrosswalk')


    models = {
        'main.city': {
            'Meta': {'object_name': 'City'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '100', 'blank': 'True'}),
            'multi_university': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'state': ('localflavor.us.models.USStateField', [], {'max_length': '2'})
        },
        'property.amenity': {
            'Meta': {'ordering': "['amenity']", 'object_name': 'Amenity'},
            'amenity': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'max_length': '100', 'blank': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '100', 'blank': 'True'}),
            'special': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'type': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '3', 'blank': 'True'})
        },
        'school.school': {
            'Meta': {'object_name': 'School'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['main.City']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'max_length': '100'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '6'}),
            'link': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '100', 'blank': 'True'}),
            'long': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '6'}),
            'mascot': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '50', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'scrape.amenitycrosswalk': {
            'Meta': {'object_name': 'AmenityCrossWalk'},
            'amenity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['property.Amenity']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'scrape_title': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'scrape.apartment': {
            'Meta': {'object_name': 'Apartment'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'exists': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '6'}),
            'long': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '6'}),
            'phone': ('localflavor.us.models.PhoneNumberField', [], {'null': 'True', 'max_length': '20', 'blank': 'True'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['school.School']"}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scrape.Source']"}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'zip_cd': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '15', 'blank': 'True'})
        },
        'scrape.apartmentamenity': {
            'Meta': {'object_name': 'ApartmentAmenity'},
            'apartment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scrape.Apartment']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'scrape.apartmentfloorplan': {
            'Meta': {'object_name': 'ApartmentFloorPlan'},
            'apartment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scrape.Apartment']"}),
            'bath_count': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '1'}),
            'bed_count': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'sq_ft': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'scrape.apartmentimage': {
            'Meta': {'object_name': 'ApartmentImage'},
            'apartment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scrape.Apartment']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'scrape.log': {
            'Meta': {'ordering': "['-date']", 'object_name': 'Log'},
            'apartment_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.City']"}),
            'comment': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '50', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        'scrape.source': {
            'Meta': {'object_name': 'Source'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['scrape']