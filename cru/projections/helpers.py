from .models import Forecast
from xlrd import open_workbook, xldate_as_tuple
from django.conf import settings
import csv, requests, urllib2, datetime

def import_forecast():
	wb = open_workbook(settings.ROOT_PATH + '/2015 Excella Consolidated ARF Q1.xlsx')
	print 'hello'
	sheet = wb.sheets()[1]
	date_index = sheet.row_values(0).index('Month')
	workdays_index = sheet.row_values(0).index('Work Days')
	person_index = sheet.row_values(0).index('Person (Last, First)')
	labor_cat_index = sheet.row_values(0).index('Labor Category')
	project_index = sheet.row_values(0).index('Project')
	project_code_index = sheet.row_values(0).index('Project Code')
	client_index = sheet.row_values(0).index('Client')
	client_id_index = sheet.row_values(0).index('Client Id')
	industry_index = sheet.row_values(0).index('Industry')
	sector_index = sheet.row_values(0).index('Sector')
	service_area_index = sheet.row_values(0).index('Service Area')
	business_unit_index = sheet.row_values(0).index('Business Unit')
	prime_sub_index = sheet.row_values(0).index('Prime/Sub')
	contract_type_index = sheet.row_values(0).index('Contract Type')
	type_index = sheet.row_values(0).index('Type')
	percent_index = sheet.row_values(0).index('Percent')
	rate_index = sheet.row_values(0).index('Rate')
	status_index = sheet.row_values(0).index('Status')
	probability_index = sheet.row_values(0).index('Probability')
	forecasted_total_hours_index = sheet.row_values(0).index('Forecasted Total Hours')
	forecasted_total_revenue_index = sheet.row_values(0).index('Forecasted Total Revenue')
	risk_adjusted_total_revenue_index = sheet.row_values(0).index('Risk Adjusted Total Revenue')
	for rownum in range(1, sheet.nrows):
		row = sheet.row(rownum)
		if row[0].value == '':
			continue
		forecast = Forecast()
		date = row[date_index].value
		date_tuple = xldate_as_tuple(date, wb.datemode)
		correct_date_object = datetime.date(date_tuple[0], date_tuple[1], date_tuple[2])
		forecast.forecast_date = correct_date_object
		forecast.year = 2015
		forecast.month = 12
		forecast.quarter = 'Q1'
		forecast.workdays = row[workdays_index].value
		forecast.person = row[person_index].value
		forecast.labor_category = row[labor_cat_index].value
		forecast.project_name = row[project_index].value
		forecast.project_code = row[project_code_index].value
		forecast.client_name = row[client_index].value
		forecast.client_id = row[client_id_index].value
		forecast.industry_name = row[industry_index].value
		forecast.sector_name = row[sector_index].value
		forecast.service_area_name = row[service_area_index].value
		forecast.business_unit = row[business_unit_index].value
		forecast.prime_sub = row[prime_sub_index].value
		forecast.contract_type = row[contract_type_index].value
		forecast.role_type = row[type_index].value
		forecast.percent = row[percent_index].value
		forecast.rate = row[rate_index].value
		forecast.status = row[status_index].value
		forecast.probability = row[probability_index].value
		forecast.forecasted_total_hours = row[forecasted_total_hours_index].value
		forecast.forecasted_total_revenue = row[forecasted_total_revenue_index].value
		forecast.risk_adjusted_total_revenue = row[risk_adjusted_total_revenue_index].value
		forecast.save()