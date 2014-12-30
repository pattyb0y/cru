from django.http import HttpResponse, HttpResponseRedirect
from projections.helpers import import_forecast

def home(request):
	print 'hello'
	import_forecast()
