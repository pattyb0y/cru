from django.db import models

# Create your models here.
# Create your models here.
class LaborCategory(models.Model):

	LABOR_CATEGORY_CHOICES = (
		('Agile - Mid-Level (AGM)'),
		('Agile - Senior (AGS)'),
		('Agile - Lead (AGL)'),
		('Agile - Coach (AGC)'),
		('Business Analyst - Junior (BAJ)'),
		('Business Analyst - Mid-Level (BAM)'),
		('Business Analyst - Senior (BAS)'),
		('Business Analyst - Lead (BAL)'),
		('Business Analyst - Coach (BAC)'),
		('Developer - Junior (DEVJ)'),
		('Developer - Mid-Level (DEVM)'),
		('Developer - Senior (DEVS)'),
		('Developer - Lead (DEVL)'),
		('Developer - Coach (DEVC)'),
		('Engineer - Junior (ENGJ)'),
		('Engineer - Mid-Level (ENGM)'),
		('Engineer - Senior (ENGS)'),
		('Engineer - Lead (ENGL)'),
		('Engineer - Coach (ENGC)'),
		('Executive Manager - Mid-Level (EXMM)'),
		('Executive Manager - Senior (EXMS)'),
		('Manager - Junior (MANJ)'),
		('Manager - Mid-Level (MANM)'),
		('Manager - Senior (MANS)'),
		('Manager - Lead (MANL)'),
		('Account Owner (AO)'),
		('Subject Matter Expert (SMEC)'),
		('Technical Analyst - Junior (TAJ)'),
		('Technical Analyst - Mid-Level (TAM)'),
		('Technical Analyst - Senior (TAS)'),
		('Technical Analyst - Lead (TAL)'),
		('XC - Developer (XCDE)'),
		('XC - Senior Developer (XCDS)'),
		('XC - Lead (XCL)')
	)

class Client(models.Model):
	name = models.CharField(max_length=100)
	client_id = models.CharField(max_length=5)

class Forecast(models.Model):
	forecast_date = models.DateField()
	year = models.DecimalField(max_digits=4, decimal_places=0)
	month = models.PositiveIntegerField()
	quarter = models.CharField(max_length=2)
	workdays = models.PositiveIntegerField()
	person = models.CharField(max_length=100)
	labor_category = models.CharField(max_length=100)
	project_name = models.CharField(max_length=200)
	project_code = models.CharField(max_length=20)
	client_name = models.CharField(max_length=100)
	client_id = models.CharField(max_length=5)
	industry_name = models.CharField(max_length=20)
	sector_name = models.CharField(max_length=20)
	service_area_name = models.CharField(max_length=100)
	business_unit_name = models.CharField(max_length=30)
	prime_sub = models.CharField(max_length=5)
	contract_type = models.CharField(max_length=3)
	role_type = models.CharField(max_length=20)
	percent = models.DecimalField(max_digits=3, decimal_places=0)
	rate = models.DecimalField(max_digits=5, decimal_places=2)
	status = models.CharField(max_length=30)
	probability = models.DecimalField(max_digits=3, decimal_places=0)
	forecasted_total_hours = models.DecimalField(max_digits=4, decimal_places=0)
	forecasted_total_revenue = models.DecimalField(max_digits=8, decimal_places=2)
	risk_adjusted_total_revenue = models.DecimalField(max_digits=8, decimal_places=2)
	def __unicode__(self):
		fc = str(self.year) + ' ' + str(self.month) + ' ' + str(self.quarter) + ' ' + str(self.workdays) + ' ' + str(self.person)
		fc += ' ' + str(self.labor_category) + ' ' + str(self.project_name) + ' ' + str(self.client_name) + ' '
		fc += str(self.industry_name) + ' ' + str(self.sector_name) + ' ' + str(self.service_area_name) +  ' '
		fc += str(self.business_unit_name) + ' ' + str(self.prime_sub) + ' ' + str(self.contract_type) + ' ' 
		fc += str(self.role_type) + ' ' + str(self.percent) + ' ' + str(self.status) + ' ' + str(self.probability)
		fc += ' ' + str(self.forecasted_total_hours) + ' ' + str(self.forecasted_total_revenue) + ' ' + str(self.risk_adjusted_total_revenue)
		return fc

class ResourceProb(models.Model):
	year = models.DecimalField(max_digits=4, decimal_places=0)
	month = models.PositiveIntegerField()
	labor_category = models.CharField(max_length=100)
	cnt = models.DecimalField(max_digits=4, decimal_places=2)