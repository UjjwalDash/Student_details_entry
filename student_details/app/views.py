from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'index.html')
def save(request):
    return render(request,'sumit.html')