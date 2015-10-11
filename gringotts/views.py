from django.shortcuts import render
from django.http import HttpResponse
import httplib
import requests

# Create your views here.
def index_view(request):
	return render(request, 'gringotts/base.html')



		


