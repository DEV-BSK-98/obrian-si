from django.shortcuts import render, redirect, get_object_or_404
from .models import Purchase, LineItems, Import_LineItems, Import_Purchase
from sales.models import Debit_Note_Invoice
from items.models import Item
from initialization.models import Configurations
from django.contrib import messages
from smartinvoice.utils import todaySi, calculate_unit_price_inclusive, safe_decimal, safe_float
from django.contrib.auth.decorators import login_required

@login_required
def index (request):
    config = Configurations.objects.first()
    items = Item.objects.all().order_by('-id') or []
    if request.method == 'POST':
        if not config:
            messages.error(request, 'There Is No Configuration Setup Initialization')
            return render(request, "purchases/index.html", {"items": items})
        purchase_ = request.POST
        item_names = purchase_.getlist('itemName[]')
        qtys = purchase_.getlist('qty[]')
        prices = purchase_.getlist('price[]')
        tax_amount = purchase_.getlist('tax_amount[]')
        rates = purchase_.getlist('rate[]')
        amounts = purchase_.getlist('amount[]')
        discount_rate = purchase_.getlist('discount_rate[]')
        discount_amount = purchase_.getlist('discount_amount[]')
        amounts = purchase_.getlist('amount[]')
        inclusive_amounts = purchase_.getlist('inclusive_amount[]')
        purchase_items = []
        tot_taxable_amt = 0.00
        tot_tax_amt = 0.00
        tot_exclusive_amt = 0.00
        cash_dc_rt = 0.00
        cash_dc_amt = 0.00
        errors = []
        for i in range(len(item_names)):
            try:
                itm = Item.objects.filter(id=item_names[i]).first()
                if not itm:
                    errors.append({"error": "Item not found", "item id": item_names[i]})
                    continue

                inclusive = safe_float(inclusive_amounts[i])
                rate = safe_float(rates[i])
                dis_rate = safe_float(discount_rate[i])
                dis_amt = safe_float(discount_amount[i])
                tax_amt = safe_float(tax_amount[i])
                qty = safe_float(qtys[i])
                print (f"""
                    \n\n\n QTY: {qtys}
                    \n\n\n RATE: {rate}
                    \n\n\n inclusive: {inclusive}
                """)

                vals = calculate_unit_price_inclusive(inclusive, rate, qty, dis_rate)

                inclusive_decimal = float(inclusive)
                tot_taxable_amt += inclusive_decimal
                tot_exclusive_amt += float(amounts[i])
                tot_tax_amt += tax_amt
                cash_dc_amt += dis_amt
                cash_dc_rt += dis_rate

                purchase_items.append({
                    'itemSeq': i + 1,
                    'itemNm': itm.itemNm,
                    'itemCd': itm.itemCd,
                    'itemClsCd': itm.itemClsCd or "Each",
                    'bcd': itm.bcd or None,
                    'pkgUnitCd': itm.pkgUnitCd or "EA",
                    'pkg': 1.0,
                    'qtyUnitCd': itm.qtyUnitCd or "EA",
                    'qty': float(qty),
                    'prc': float(prices[i]),
                    'splyAmt': vals["total_exclusive_amount"],
                    'totAmt': float(inclusive),
                    'dcRt': dis_rate,
                    'dcAmt': dis_amt,
                    # 'isrccCd': "",
                    # 'isrccNm': "",
                    'vatCatCd': "A",
                    # 'exciseTxCatCd': "",
                    # 'tlCatCd': "",
                    # 'iplCatCd': "",
                    'isrcRt':0.00,
                    'isrcAmt':0.00,
                    'vatTaxblAmt': inclusive_decimal,
                    'vatAmt': tax_amt,
                    'exciseTaxblAmt':0.00,
                    'tlTaxblAmt':0.00,
                    'iplTaxblAmt':0.00,
                    'iplAmt':0.00,
                    'tlAmt':0.00,
                    'exciseTxAmt':0.00
                })
            except Exception as item_error:
                errors.append({"error": f"{item_error}", "item name": item_names[i]})

        if errors:
            messages.error(request, f'There are these Errors: {errors}')
            return render(request, "sales/index.html", {"items": items})

        try:
            purchase = Purchase.objects.create(
                tpin=config.tpin,
                bhfId=config.bhfId,
                spplrBhfId=purchase_.get('spplrBhfId', '') or "000",
                spplrInvcNo=purchase_.get('spplrInvcNo', ''),
                cisInvcNo=purchase_.get('cisInvcNo', ''),
                spplrTpin=purchase_.get('spplrTpin', ''),
                spplrNm=purchase_.get('spplrNm', ''),
                salesTyCd="N",
                rcptTyCd="S",
                pmtTyCd=purchase_.get('pmtTyCd', '01'),
                salesSttsCd=purchase_.get('salesSttsCd', '01'),
                cfmDt=todaySi(),
                salesDt=todaySi(),
                cnclReqDt=todaySi(),
                totItemCnt=len(item_names),
                totAmt=tot_exclusive_amt,
                totTaxblAmt=tot_taxable_amt,
                totTaxAmt=tot_tax_amt,
                taxRtA= int(rate),
                prchrAcptcYn="Y",
                regrId="admin",
                regrNm="Admin",
                modrId="admin",
                modrNm="Admin",
                saleCtyCd="1",
                currencyTyCd=purchase_.get ('currencyTyCd', "ZMW"),
                exchangeRt=purchase_.get ('exchangeRt', "1.0")
            )

            for itm in purchase_items:
                item = LineItems.objects.create(**itm)
                purchase.itemList.add(item)

            purchase.save()

            return redirect ("purchase-info", purchase.id)
        except Exception as e:
            print(f"Error saving data: {str(e)}")
    return render (request, "purchases/index.html",  {"items": items})

@login_required
def list_view (request):
    purchases = []
    objs = Purchase.objects.all ().order_by ('-id')
    if objs:
        purchases = objs
    return render (request, "purchases/list-purchases.html", {"purchases": purchases})

@login_required
def import_list_view (request):
    purchases = []
    objs = Import_Purchase.objects.all ().order_by ('-id')
    if objs:
        purchases = objs
    return render (request, "purchases/list-import-purchases.html", {"purchases": purchases})

@login_required
def info (request, id):
    purchase = Purchase.objects.filter (id=id).first ()
    if not purchase:
        return redirect ("new-purchases")

    line_items = purchase.itemList.all ()
    print (line_items)
    return render (request, "purchases/info.html", {"purchase": purchase})

@login_required
def import_info (request, id):
    purchases = Import_Purchase.objects.filter (id=id).first ()
    if not purchases:
        return redirect ("import-purchases")

    return render (request, "purchases/import-info.html", {"purchases": purchases})

@login_required
def pull (request):
    return redirect ("imports")

@login_required
def list_debit_note (request):
    invoices = []
    try:
        invoices = Debit_Note_Invoice.objects.all().order_by('-id')
    except Exception as e:
        print(f"{e}")
    return render(request, "purchases/debit-notes.html", {"invoice": invoices})

@login_required
def debit_note_info(request, id):
    invoice = []
    try:
        invoice = get_object_or_404(Debit_Note_Invoice, pk=id)
    except Exception as e:
        print(f"{e}")
    return render(request, "purchases/debit-note-info.html", {"invoice": invoice})

@login_required
def debit_note_new (request):
    items = Item.objects.all ().order_by ('-id')
    invoices = Purchase.objects.all ().order_by ('-id')
    try:
        # get invoice data
        pass
    except Exception as e:
        print(f"{e}")
    return render(request, "purchases/debit-note-form.html", {"items": items, "invoices": invoices})
