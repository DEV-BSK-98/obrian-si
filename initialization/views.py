from django.shortcuts import render, redirect
from .models import Configurations
from django.contrib.auth.decorators import login_required

@login_required
def index (request):
    check = Configurations.objects.all ()
    print (check)
    if check and len (check) > 0:
        return redirect ("initialization-info")
    if request.method == 'POST':
        try:
            taxpayer = Configurations.objects.create(
                tpin=request.POST.get('tpin', '').strip(),
                taxprNm=request.POST.get('taxprNm', '').strip(),
                bsnsActv=request.POST.get('bsnsActv', '').strip(),
                bhfId=request.POST.get('bhfId', '').strip(),
                bhfNm=request.POST.get('bhfNm', '').strip(),
                bhfOpenDt=request.POST.get('bhfOpenDt', '').strip(),
                prvncNm=request.POST.get('prvncNm', '').strip(),
                dstrtNm=request.POST.get('dstrtNm', '').strip(),
                sctrNm=request.POST.get('sctrNm', '').strip(),
                dvcid=request.POST.get('dvcid', '').strip(),
                vsdc_url=request.POST.get('vsdc_url', '').strip()
            )
            return redirect ("initialization-info")
        except Exception as e:
            print(f"Error saving data: {str(e)}")
    return render (request, "initialization/index.html")

@login_required
def info (request):
    config = Configurations.objects.all ().first ()
    if not config:
        return redirect ("initialization")

    return render (request, "initialization/info.html", {"config": config})