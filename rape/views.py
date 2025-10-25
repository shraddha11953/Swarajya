# Create your views here.
from django.shortcuts import render, redirect
from .forms import RapeReportForm
from .models import RapeReport
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def home(request):
    return render(request, 'rape/home.html')


@login_required
def submit_rape_report(request):
    if request.method == 'POST':
        form = RapeReportForm(request.POST, request.FILES)
        if form.is_valid():
            report = form.save(commit=False)
            report.user = request.user
            report.save()
            return redirect('rape:my_rape_reports')
    else:
        form = RapeReportForm()
    return render(request, 'rape/submit_rape_report.html', {'form': form})

@login_required
def my_rape_reports(request):
    reports = RapeReport.objects.filter(user=request.user)
    return render(request, 'rape/my_rape_reports.html', {'reports': reports})

@login_required
def all_rape_reports_admin(request):
    if not request.user.is_superuser:
        return redirect('index')
    reports = RapeReport.objects.all()
    return render(request, 'rape/all_rape_reports.html', {'reports': reports})
