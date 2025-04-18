from django.shortcuts import render, redirect, get_object_or_404
from items.models import Item
from initialization.models import Configurations
from .models import Invoice, InvoiceItem, Credit_Note_Invoice, Credit_Note_InvoiceItem
from django.contrib import messages
from smartinvoice.utils import todaySi, calculate_unit_price_inclusive, safe_decimal, safe_float


def index(request):
    config = Configurations.objects.first()
    items = Item.objects.all().order_by('-id') or []

    if request.method == 'POST':
        if not config:
            messages.error(request, 'There Is No Configuration Setup Initialization')
            return render(request, "sales/index.html", {"items": items})
        print (request.POST)
        sale = request.POST
        item_names = sale.getlist('itemName[]')
        qtys = sale.getlist('qty[]')
        prices = sale.getlist('price[]')
        tax_amount = sale.getlist('tax_amount[]')
        rates = sale.getlist('rate[]')
        amounts = sale.getlist('amount[]')
        discount_rate = sale.getlist('discount_rate[]')
        discount_amount = sale.getlist('discount_amount[]')
        amounts = sale.getlist('amount[]')
        inclusive_amounts = sale.getlist('inclusive_amount[]')

        sale_items = []
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

                # expected_exclusive_amt = float(amounts[i]) or 0.00
                # expected_price = float(prices[i]) or 0.00

                vals = calculate_unit_price_inclusive(inclusive, rate, qty, dis_rate)

                # if vals["total_exclusive_amount"] != safe_decimal(expected_exclusive_amt):
                #     errors.append({
                #         "error": f"Exclusive Amount mismatch: {vals['total_exclusive_amount']} vs {expected_exclusive_amt}",
                #         "item name": itm.itemNm
                #     })

                # if vals["unit_price_exclusive"] != safe_decimal(expected_price):
                #     errors.append({
                #         "error": f"Unit Price mismatch: {vals['unit_price_exclusive']} vs {expected_price}",
                #         "item name": itm.itemNm
                #     })

                # calc_tax_amt = float(float(inclusive) - float(expected_exclusive_amt))
                # if vals["total_tax_amount"] != safe_decimal(calc_tax_amt):
                #     errors.append({
                #         "error": f"Tax Amount mismatch: {vals['total_tax_amount']} vs {calc_tax_amt}",
                #         "item name": itm.itemNm
                #     })

                inclusive_decimal = float(inclusive)
                tot_taxable_amt += inclusive_decimal
                tot_exclusive_amt += float(amounts[i])
                tot_tax_amt += tax_amt
                cash_dc_amt += dis_amt
                cash_dc_rt += dis_rate

                sale_items.append({
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
            sale_ = Invoice.objects.create(
                tpin=config.tpin,
                bhfId=config.bhfId,
                orgInvcNo=sale.get('orgInvcNo', ''),
                cisInvcNo=sale.get('cisInvcNo', ''),
                custTpin=sale.get('custTpin', ''),
                custNm=sale.get('custNm', ''),
                salesTyCd="N",
                rcptTyCd="S",
                pmtTyCd=sale.get('pmtTyCd', '01'),
                salesSttsCd=sale.get('salesSttsCd', '01'),
                cfmDt=todaySi(),
                salesDt=todaySi(),
                cnclReqDt=todaySi(),
                totItemCnt=len(item_names),
                totAmt=tot_exclusive_amt,
                totTaxblAmt=tot_taxable_amt,
                totTaxAmt=tot_tax_amt,
                cashDcRt=cash_dc_rt,
                cashDcAmt=cash_dc_amt,
                taxRtA= int(rate),
                prchrAcptcYn="Y",
                regrId="admin",
                regrNm="Admin",
                modrId="admin",
                modrNm="Admin",
                saleCtyCd="01",
                currencyTyCd=sale.get ('currencyTyCd', "ZMW"),
                exchangeRt=sale.get ('exchangeRt', "1.0")
            )

            for itm in sale_items:
                item = InvoiceItem.objects.create(**itm)
                sale_.itemList.add(item)

            sale_.save()
            return redirect('sale-info', sale_.id)
        except Exception as e:
            messages.error(request, f'There was an error saving the invoice: {e}')
            print(f"ERROR: {e}")

    return render(request, "sales/index.html", {"items": items})

def info(request, id):
    invoice = None
    try:
        invoice = get_object_or_404(Invoice, pk=id)
        if not invoice:
            return redirect("sales")
    except Exception as e:
        print(f"{e}")
    return render(request, "sales/info.html", {"sale": invoice})


def credit_note_list(request):
    invoices = []
    try:
        invoices = Credit_Note_Invoice.objects.all().order_by('-id')
    except Exception as e:
        print(f"{e}")
    return render(request, "sales/credit-notes.html", {"invoices": invoices})

def sales_list(request):
    invoices = []
    try:
        invoices = Invoice.objects.all().order_by('-id')
    except Exception as e:
        print(f"{e}")
    return render(request, "sales/sales-list.html", {"invoices": invoices})

def credit_note_info(request, id):
    invoice = []
    try:
        invoice = get_object_or_404(Credit_Note_Invoice, pk=id)
    except Exception as e:
        print(f"{e}")
    return render(request, "sales/credit-note-info.html", {"invoice": invoice})


def credit_note_new (request):
    items = Item.objects.all ().order_by ('-id')
    invoices = Invoice.objects.all ().order_by ('-id')
    try:
        pass
    except Exception as e:
        print(f"{e}")
    return render(request, "sales/credit-note-form.html", {"items": items, "invoices": invoices})
