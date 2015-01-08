from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from projections.helpers import import_forecast, currency
from projections.models import Forecast
from projections import views
from django.db.models import Sum, Count
from django.conf import settings

def home(request):
	print settings.BASE_DIR
	return render(request, 'index.html', {})