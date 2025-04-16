from django.shortcuts import render, redirect, get_object_or_404
from .models import Purchase, LineItems, Import_LineItems, Import_Purchase
from sales.models import Debit_Note_Invoice
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

def list_view (request):
    purchases = []
    objs = Purchase.objects.all ().order_by ('-id')
    if objs:
        purchases = objs
    return render (request, "purchases/list-purchases.html", {"purchases": purchases})


def import_list_view (request):
    purchases = []
    objs = Import_Purchase.objects.all ().order_by ('-id')
    if objs:
        purchases = objs
    return render (request, "purchases/list-import-purchases.html", {"purchases": purchases})


def info (request, id):
    purchases = Purchase.objects.filter (id=id).first ()
    if not purchases:
        return redirect ("new-purchases")

    return render (request, "purchases/info.html", {"purchases": purchases})


def import_info (request, id):
    purchases = Import_Purchase.objects.filter (id=id).first ()
    if not purchases:
        return redirect ("import-purchases")

    return render (request, "purchases/import-info.html", {"purchases": purchases})

def pull (request):
    return redirect ("imports")

def list_debit_note (request):
    invoices = []
    try:
        invoices = Debit_Note_Invoice.objects.all().order_by('-id')
    except Exception as e:
        print(f"{e}")
    return render(request, "purchases/debit-notes.html", {"invoice": invoices})

def debit_note_info(request, id):
    invoice = []
    try:
        invoice = get_object_or_404(Debit_Note_Invoice, pk=id)
    except Exception as e:
        print(f"{e}")
    return render(request, "purchases/debit-note-info.html", {"invoice": invoice})

