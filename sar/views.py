from django.shortcuts import render, redirect
from .models import SAR, SAR_Item
def index (request):
    if request.method == 'POST':
        try:
            sar = SAR.objects.create(
                # branch_name=request.POST.get('branch_name', '').strip(),
                # bhfId=request.POST.get('bhfId', '').strip(),
            )
            return redirect ("sar-info",)
        except Exception as e:
            print(f"Error saving data: {str(e)}")
    return render (request, "sar/index.html")

def info (request, id):
    sars = SAR.objects.filter (id=id).first ()
    if not sars:
        return redirect ("sars")

    return render (request, "sar/info.html", {"sars": sars})