from django.shortcuts import render
from django.http import HttpResponse
import json
# import urllib2
import requests
from urllib.request import urlopen



# Create your views here.
api_key = 'cf2de7e0ee02e6d80927a32fa0ff9727'
reimagine_api_key = 'key=cf2de7e0ee02e6d80927a32fa0ff9727'
all_clients_api = 'http://api.reimaginebanking.com/accounts?type=Checking&'
transfer_api = 'http://api.reimaginebanking.com/accounts/%s/transfers?'
dr_s_id = '560f0205f8d8770df0ef9aa2'
user_name = '277roshan'


def index_view(request):
	return render(request, 'gringotts/base.html',{"key": api_key})


def all_clients_view(request):
	page = urlopen(all_clients_api + reimagine_api_key) 
	page = page.read()
	page = json.loads(page.decode())
	return HttpResponse(page)

def transfer(request):
	if request.POST:
		payee_id = request.POST['id']
		amount = int(request.POST['money'])
		url = transfer_api.format(payee_id) + reimagine_api_key
		transfer_details = {
		  "medium": "balance",
		  "payee_id": payee_id,
		  "amount" : amount
		}

		# create a transfer
		response = requests.post( 
			url, 
			data=json.dumps(transfer_details),
			headers={'content-type':'application/json'},
			)
		if response.status_code == 201:
			print (True)
			print('account created')
		else:
			print (response.status_code)
			print ('Not yet')
		return render(request, 'gringotts/base.html',{"key": api_key})


		


# http://api.reimaginebanking.com/accounts/rtyuuyt/transfers?key=73773e58efaba48db97f6f32c3f89f51
# page = urllib2.urlopen(data)
# page_read = page.read()
# page = json.loads(page_read)
#http://api.reimaginebanking.com/accounts/rtyuuyt/transfers?key=73773e58efaba48db97f6f32c3f89f51
