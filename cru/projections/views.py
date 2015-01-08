from django.http import HttpResponse
from django.shortcuts import render

from projections.helpers import import_forecast, currency
from projections.models import Forecast
from django.db.models import Sum, Count

# Create your views here.
def index(request):

	#import_forecast()
	# Get the total revenue

	fc = Forecast.objects.aggregate(Sum('forecasted_total_revenue'))
	#print fc['forecasted_total_revenue__sum']
	fc_total_rev =  fc['forecasted_total_revenue__sum']
	fc = Forecast.objects.aggregate(Sum('risk_adjusted_total_revenue'))
	risk_adj_rev = currency(fc['risk_adjusted_total_revenue__sum'])
	fc = Forecast.objects.aggregate(Sum('forecasted_total_hours'))
	total_hrs = fc['forecasted_total_hours__sum']
	fc_avg_rate = currency(fc_total_rev/total_hrs)
	fc_total_rev = currency(fc_total_rev)

	# get projected revenue by sector
	fc_sector = Forecast.objects.values('sector_name').annotate(Sum('risk_adjusted_total_revenue')).annotate(Sum('forecasted_total_revenue'))
	#print 'Projected Revenue by Sector'
	# build drilldowns for each sector
	ra_drilldown = "series: ["
	tot_rev_drilldown = "series: ["
	for client in fc_sector:
		fc_client = Forecast.objects.filter(sector_name=client['sector_name']).values('client_name').annotate(Sum('risk_adjusted_total_revenue')).annotate(Sum('forecasted_total_revenue'))
		ra_drilldown += "{ id: 'drill_" + client['sector_name'] + "',"
		ra_drilldown += "data: ["
		tot_rev_drilldown += "{ id: 'drill_" + client['sector_name'] + "',"
		tot_rev_drilldown += "data: ["
		for i in fc_client:
			ra_drilldown += "['" + str(i['client_name']) + "'," + str(i['risk_adjusted_total_revenue__sum']) + "],"
			tot_rev_drilldown += "['" + str(i['client_name']) + "'," + str(i['forecasted_total_revenue__sum']) + "],"
		ra_drilldown = ra_drilldown[:-1]
		tot_rev_drilldown = tot_rev_drilldown[:-1]
		ra_drilldown += "]},"
		tot_rev_drilldown += "]},"
	ra_drilldown = ra_drilldown[:-1]
	tot_rev_drilldown = tot_rev_drilldown[:-1]
	ra_drilldown += "]"
	tot_rev_drilldown += "]"

	#	print str(i['sector_name']) + ' ' + str(currency(i['risk_adjusted_total_revenue__sum'])) + ' ' + str(currency(i['forecasted_total_revenue__sum']))

	
	# get projected revenue by industry
	#fc = Forecast.objects.values('industry_name').annotate(Sum('risk_adjusted_total_revenue')).annotate(Sum('forecasted_total_revenue'))
	#print 'Projected Revenue by Industry'
	#for i in fc:
	#	print str(i['industry_name']) + ' ' + str(currency(i['risk_adjusted_total_revenue__sum'])) + ' ' + str(currency(i['forecasted_total_revenue__sum']))

	# get projected revenue by project
	#fc = Forecast.objects.values('project_name').annotate(Sum('risk_adjusted_total_revenue')).annotate(Sum('forecasted_total_revenue'))
	#print 'Projected Revenue by Project'
	#for i in fc:
	#	print str(i['project_name']) + ' ' + str(currency(i['risk_adjusted_total_revenue__sum'])) + ' ' + str(currency(i['forecasted_total_revenue__sum']))

	# get resource TBD counts
	fc = Forecast.objects.filter(person__contains='TBD').values('labor_category', 'year', 'month').annotate(Sum('percent'))
	print 'TBD Resource counts'
	for i in fc:
		print str(i['year']) + '%' + str(i['month']) + '%' + i['labor_category'] + '%' + str(i['percent__sum']/100)

	# get resource counts
	#fc = Forecast.objects.values('labor_category', 'year', 'month').annotate(Count('labor_category'))
	#print 'All Resource Counts'
	#for i in fc:
	#	print str(i['year']) + ' ' + str(i['month']) + ' ' + i['labor_category'] + ' ' + str(i['labor_category__count'])

	# compare proposed rates to real rates to look for issues
	#fc = Forecast.objects.filter(contract_type='T&M').values('labor_category').annotate(Sum('forecasted_total_hours')).annotate(Sum('forecasted_total_revenue'))
	#print 'Projected Average Rate by Labor Category'
	#for i in fc:
	#	print str(i['labor_category']) + ' ' + currency(i['forecasted_total_revenue__sum'] / i['forecasted_total_hours__sum'])

	retVal = "Forecasted Total Revenue: " + fc_total_rev + "<br>Risk Adjusted Total Revenue: " + risk_adj_rev
	retVal += "<br>Forecasted Total Hours: " + str(total_hrs) + "<br>Projected Average Rate: " + fc_avg_rate

	print retVal 

	return render(request, 'projections/projections.html', 
		{'total_rev': fc_total_rev, 'risk_adj_rev': risk_adj_rev, 'total_hrs': total_hrs, 
		'fc_avg_rate': fc_avg_rate, 'fc_by_sector': fc_sector, 'ra_drilldown': ra_drilldown, 'tot_rev_drilldown': tot_rev_drilldown})