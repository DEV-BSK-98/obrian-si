
from django.shortcuts import render, redirect
from .models import Purchase, LineItems
def index (request):
    if request.method == 'POST':
        try:
            purchase = Purchase.objects.create(
                # branch_name=request.POST.get('branch_name', '').strip(),
                # bhfId=request.POST.get('bhfId', '').strip(),
            )
            return redirect ("purchase-info",)
        except Exception as e:
            print(f"Error saving data: {str(e)}")
    return render (request, "purchases/index.html")

def info (request, id):
    purchases = Purchase.objects.filter (id=id).first ()
    if not purchases:
        return redirect ("purchases")

    return render (request, "purchases/info.html", {"purchases": purchases})