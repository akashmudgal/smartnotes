from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from datetime import datetime
def home(request: HttpRequest):
    return render(request,'home/welcome.html',{'today': datetime.today()})