from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index_view(request):
	return HttpResponse("Hello subhay")






# page = urllib2.urlopen(data)
# page_read = page.read()
# page = json.loads(page_read)