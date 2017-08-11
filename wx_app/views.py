from django.shortcuts import render

# Create your views here.

def index(request):
    dt = {}
    dt['name'] = 'no 1'
    return render(request, 'index.html', dt)
