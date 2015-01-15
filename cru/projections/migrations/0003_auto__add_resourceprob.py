# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ResourceProb'
        db.create_table(u'projections_resourceprob', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=0)),
            ('month', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('labor_category', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('cnt', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=2)),
        ))
        db.send_create_signal(u'projections', ['ResourceProb'])


    def backwards(self, orm):
        # Deleting model 'ResourceProb'
        db.delete_table(u'projections_resourceprob')


    models = {
        u'projections.client': {
            'Meta': {'object_name': 'Client'},
            'client_id': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'projections.forecast': {
            'Meta': {'object_name': 'Forecast'},
            'business_unit_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'client_id': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'client_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'contract_type': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'forecast_date': ('django.db.models.fields.DateField', [], {}),
            'forecasted_total_hours': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '0'}),
            'forecasted_total_revenue': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'industry_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'labor_category': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'month': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'percent': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '0'}),
            'person': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'prime_sub': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'probability': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '0'}),
            'project_code': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'project_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'quarter': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'rate': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'risk_adjusted_total_revenue': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'role_type': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'sector_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'service_area_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'workdays': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'year': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '0'})
        },
        u'projections.laborcategory': {
            'Meta': {'object_name': 'LaborCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'projections.resourceprob': {
            'Meta': {'object_name': 'ResourceProb'},
            'cnt': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'labor_category': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'month': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'year': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '0'})
        }
    }

    complete_apps = ['projections']