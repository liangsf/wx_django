#from django.http import HttpResponse

from django.shortcuts import render

def hello(request):
	#return HttpResponse("Hello World1! ");
	context = {}
	context['hello'] = 'hello liangsf!'
	return render(request, 'hello.html', context)
