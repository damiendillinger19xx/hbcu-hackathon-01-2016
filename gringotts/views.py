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
user_name = '277roshan'


def index_view(request):
	return render(request, 'gringotts/base.html',{"key":"73773e58efaba48db97f6f32c3f89f51"})


def all_clients_view(request):
	page = urlopen(all_clients_api + reimagine_api_key) 
	page = page.read()
	page = json.loads(page.decode())
	return HttpResponse(page)
	# return render(request, 'gringotts/index.html', {'items' : page[0]})


def transfer(request):
	if request.POST:
		person_id = request.POST['id']
		amount = int(request.POST['money'])
		payload = {
		  "type": "Savings",
		  "nickname": "test",
		  "rewards": 10000,
		  "balance": 10000,	
		}
		#url = 'http://api.reimaginebanking.com/accounts/%s/transfers?key=%s'%(person_id, reimagine_api_key)
		url = 'http://api.reimaginebanking.com/customers/{}/accounts?key={}'.format(person_id,reimagine_api_Key)
		print url
		response = requests.post( 
			url, 
			data=json.dumps(payload),
			headers={'content-type':'application/json'},
			)
		if response.status_code == 201:
			print True
			print('account created')
		else:
			print 'Not yet'

		return render(request, 'gringotts/base.html',{"key":"73773e58efaba48db97f6f32c3f89f51"}) 
	pass

		


# http://api.reimaginebanking.com/accounts/rtyuuyt/transfers?key=73773e58efaba48db97f6f32c3f89f51
# page = urllib2.urlopen(data)
# page_read = page.read()
# page = json.loads(page_read)
#http://api.reimaginebanking.com/accounts/rtyuuyt/transfers?key=73773e58efaba48db97f6f32c3f89f51
