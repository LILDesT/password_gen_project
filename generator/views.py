from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
	return render(request, 'generator/home.html')

def password(request):
	
	characters = list('abcdefghiklmnopqrstuvwxyz')
	num = list('0123456789')
	spec = list('!@#$%^&*()')

	if request.GET.get('uppercase'):
		characters.extend(list('ABCDEFGHIKLMNOPQRSTUVWXYZ'))

	if request.GET.get('special'):
		characters.extend(list('!@#$%^&*()'))

	if request.GET.get('numbers'):
		characters.extend(list('0123456789'))

	lenght = int(request.GET.get('lenght', '12'))

	thepassword = ''
	thepassword1 = ''
	thepassword2 = ''
	thepassword3 = ''

	for x in range(lenght):
		thepassword += random.choice(characters)
		thepassword1 += random.choice(num)
		thepassword2 += random.choice(spec)

	#if request.GET.get('numbers'):
	#	thepassword = thepassword1
	#if request.GET.get('special'):
	#	thepassword = thepassword2
	#if request.GET.get('numbers') and request.GET.get('special'):
	#	thepassword = thepassword1 + thepassword2
	#	for i in range(lenght):
	#		thepassword3 += random.choice(thepassword)
	#	thepassword = thepassword3

	
	return render(request, 'generator/password.html', {'password': thepassword})
