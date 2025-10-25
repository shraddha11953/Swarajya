from django.shortcuts import render,HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, 'swarajyam/dashboard.html')


# Create your views here.
def index(request):
    return render(request,'index.html')

def helping_hend(request):
    return render(request,'helping.html')

