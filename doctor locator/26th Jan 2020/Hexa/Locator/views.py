from django.shortcuts import render
from django.http import HttpResponse
from coordinate2city import reverseGeocode 
# Create your views here.

def home(request):
	return render(request,'Locator/tempLocator.html')


def hexa(request):
	if request.method == 'POST':
		getlat = request.POST["lat"]
		getlon = request.POST["lon"]
		print(getlat,getlon)
		coordinates =(getlat,getlon)
		reverseGeocode(coordinates)
	return render(request,'Locator/address.html')