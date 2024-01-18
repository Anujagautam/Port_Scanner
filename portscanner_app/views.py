from django.shortcuts import render
from .scanner import scan_range


def scan(request):
    result = None

    if request.method == 'POST':
        start_ip = request.POST.get('start_ip')
        end_ip = request.POST.get('end_ip')
        result = scan_range(start_ip, end_ip)

    return render(request, 'portscanner_app/scan.html', {'result': result})
