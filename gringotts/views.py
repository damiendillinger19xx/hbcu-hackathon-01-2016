from django.shortcuts import render, redirect
from django.http import HttpResponse
import json
import requests						# used for posting using a API

# ubuntu unblock this and block the following one line
# import urllib2.urlopen as urlopen

# others unblock this and block the above one line
from urllib.request import urlopen

_PAYER_ID = '560f0207f8d8770df0efa643'
reimagine_api_key = 'key=73773e58efaba48db97f6f32c3f89f51'
developer_api_key= '73773e58efaba48db97f6f32c3f89f51'
all_clients_api = 'http://api.reimaginebanking.com/accounts?'
transfer_api = 'http://api.reimaginebanking.com/accounts/%s/transfers?'
user_name = '277roshan'
final_list=[]
errors = []

def index_view(request):
	print ("in index:", errors)
	return render(request, 'gringotts/index.html', {"key": developer_api_key, 'error' : errors})


def all_clients_view(request):
	page = urlopen(all_clients_api + reimagine_api_key) 
	page = page.read()
	page = json.loads(page.decode())
	return HttpResponse(page)

def transfer(request):
	try:
		if (request.POST):
			payee_id = request.POST['id']
			amount = int(request.POST['money'])
			payload = {
			"medium":"balance",
			"amount":amount,
			"payee_id":payee_id,
			}
			url = 'http://api.reimaginebanking.com/accounts/%s/transfers?%s'%(_PAYER_ID, reimagine_api_key)
			response = requests.post( 
				url,
				data=json.dumps(payload),
				headers={'content-type':'application/json'},
				)
			if response.status_code == 201:
				print (True)
				print('transferred')
				transfers_url = 'http://api.reimaginebanking.com/accounts/%s/transfers?%s'%(_PAYER_ID, reimagine_api_key)
				page = urlopen(transfers_url) 
				page = page.read()
				page = json.loads(page.decode())
				payee = urlopen('http://api.reimaginebanking.com/accounts?key=73773e58efaba48db97f6f32c3f89f51') 
				payee = payee.read()
				payee = json.loads(payee.decode())
		
				payee_dict = {}
				for i in payee:
					payee_dict[i['_id']] = i['nickname']
				payee_pass_list= []
				for i in page:
					payee_pass_list.append((i["payee_id"],i["amount"]))			
				final_list=[]
				for i in payee_pass_list:
					final_list.append((payee_dict[i[0]],i[1]))
				final_list = final_list[-1::-1]
				
				return render(request, 'gringotts/transfer.html',{"payee_pass_list":final_list})
			else:
				error = ''
				error = 'error occured'
				print ('Not yet')
			return render(request, 'gringotts/index.html', {"payee_pass_list" : final_list, "error" : error})
	except ValueError:
		errors.append("Data input has errors, fix them and then resubmit")
		print ("in transfer:", errors)
		return redirect('gringotts:index')
		# return render(request, 'gringotts/index.html', {"error" : error})


# http://api.reimaginebanking.com/accounts/rtyuuyt/transfers?key=73773e58efaba48db97f6f32c3f89f51
# page = urllib2.urlopen(data)
# page_read = page.read()
# page = json.loads(page_read)
#http://api.reimaginebanking.com/accounts/rtyuuyt/transfers?key=73773e58efaba48db97f6f32c3f89f51
