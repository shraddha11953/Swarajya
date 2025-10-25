# helpinghand/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import HelpOffer, HelpRequest
from .forms import HelpOfferForm, HelpRequestForm

def home(request):
    return render(request, 'helpinghand/home.html')

@login_required
def submit_offer(request):
    if request.method == 'POST':
        form = HelpOfferForm(request.POST, request.FILES)
        if form.is_valid():
            offer = form.save(commit=False)
            offer.user = request.user
            offer.save()
            return redirect('helpinghand:view_offers')
    else:
        form = HelpOfferForm()
    return render(request, 'helpinghand/submit_offer.html', {'form': form})

@login_required
def submit_request(request):
    if request.method == 'POST':
        form = HelpRequestForm(request.POST, request.FILES)
        if form.is_valid():
            req = form.save(commit=False)
            req.posted_by = request.user
            req.save()
            return redirect('helpinghand:view_requests')
    else:
        form = HelpRequestForm()
    return render(request, 'helpinghand/submit_request.html', {'form': form})

@login_required
def view_offers(request):
    offers = HelpOffer.objects.all().order_by('-date') 
    #offers = HelpOffer.objects.all().order_by('-submitted_at')
    return render(request, 'helpinghand/view_offers.html', {'offers': offers})

@login_required
def view_requests(request):
    requests = HelpRequest.objects.all().order_by('-submitted_at')
    return render(request, 'helpinghand/view_requests.html', {'requests': requests})

@login_required
def my_offers(request):
    offers = HelpOffer.objects.filter(user=request.user)
    return render(request, 'helpinghand/my_offers.html', {'offers': offers})

@login_required
def my_requests(request):
    requests = HelpRequest.objects.filter(posted_by=request.user)
    return render(request, 'helpinghand/my_requests.html', {'requests': requests})

@login_required
def admin_dashboard(request):
    if not request.user.is_superuser:
        return redirect('index')
    offers = HelpOffer.objects.all()
    requests = HelpRequest.objects.all()
    return render(request, 'helpinghand/admin_dashboard.html', {
        'offers': offers,
        'requests': requests,
    })
