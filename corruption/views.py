from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CorruptionReportForm
from .models import CorruptionReport

def home(request):
    return render(request, 'corruption/home.html')

@login_required
def submit_report(request):
    if request.method == 'POST':
        form = CorruptionReportForm(request.POST, request.FILES)
        if form.is_valid():
            report = form.save(commit=False)
            report.user = request.user
            report.save()
            return redirect('my_reports')
    else:
        form = CorruptionReportForm()
    return render(request, 'corruption/submit_report.html', {'form': form})

@login_required
def my_reports(request):
    reports = CorruptionReport.objects.filter(user=request.user).order_by('-submitted_at')
    return render(request, 'corruption/my_reports.html', {'reports': reports})


@login_required
def all_reports_admin(request):
    print("User:", request.user.username)
    print("Is superuser:", request.user.is_superuser)

    if not request.user.is_superuser:
        return redirect('index')  # make sure this URL name exists
    reports = CorruptionReport.objects.all()
    return render(request, 'corruption/all_reports.html', {'reports': reports})

#@login_required
#def all_reports_admin(request):
    #if not request.user.is_superuser:
       # return redirect('index')
    #reports = CorruptionReport.objects.all()
   # return render(request, 'corruption/all_reports.html', {'reports': reports})