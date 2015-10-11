from django.shortcuts import render
from django.http import HttpResponse
import json
# import urllib2
# import requests
from urllib.request import urlopen


# Create your views here.

reimagine_api_key = 'key=cf2de7e0ee02e6d80927a32fa0ff9727'
all_clients_api = 'http://api.reimaginebanking.com/accounts?type=Checking&'
transfer_api = 'http://api.reimaginebanking.com/accounts/%s/transfers?'


def index_view(request):
	return render(request, 'gringotts/base.html')


def all_clients_view(request):
	page = urlopen(all_clients_api + reimagine_api_key) 
	page = page.read()
	page = json.loads(page.decode())
	return HttpResponse(page)
	# return render(request, 'gringotts/index.html', {'items' : page[0]})


def transfer(request):
	pass
 	# if request.GET:
 	# 	payee_id = request.GET['id']
 	# 	transfer = transfer_api + reimagine_api_key
 	# 	page = urllib2.urlopen(transfer % (x))
 	# 	page_read = page.read()
 	# 	page = json.loads(page_read)
 	# return render(request, 'gringotts/base.html')

		


# 'http://api.reimaginebanking.com/accounts/%s/transfers?key=73773e58efaba48db97f6f32c3f89f51'
# page = urllib2.urlopen(data)
# page_read = page.read()
# page = json.loads(page_read)
