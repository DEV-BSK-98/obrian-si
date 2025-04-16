from django.shortcuts import render, redirect, get_object_or_404
from .models import Invoice, InvoiceItem, Credit_Note_Invoice, Credit_Note_InvoiceItem
import json

def index(request):
    if request.method == 'POST':

        try:
            sale = Invoice.objects.create(
                tpin=request.POST.get('tpin', '').strip(),
                bhfId=request.POST.get('bhfId', '').strip(),
                orgInvcNo=request.POST.get('orgInvcNo', 0),
                cisInvcNo=request.POST.get('cisInvcNo', '').strip(),
                custTpin=request.POST.get('custTpin', '').strip(),
                custNm=request.POST.get('custNm', '').strip(),
                salesTyCd=request.POST.get('salesTyCd', '').strip(),
                rcptTyCd=request.POST.get('rcptTyCd', '').strip(),
                pmtTyCd=request.POST.get('pmtTyCd', '').strip(),
                salesSttsCd=request.POST.get('salesSttsCd', '').strip(),
                cfmDt=request.POST.get('cfmDt'),
                salesDt=request.POST.get('salesDt'),
                stockRlsDt=request.POST.get('stockRlsDt') or None,
                cnclReqDt=request.POST.get('cnclReqDt') or None,
                cnclDt=request.POST.get('cnclDt') or None,
                rfdDt=request.POST.get('rfdDt') or None,
                rfdRsnCd=request.POST.get('rfdRsnCd') or None,
                totItemCnt=request.POST.get('totItemCnt') or 0,
                taxblAmtA=request.POST.get('taxblAmtA') or 0,
                taxAmtA=request.POST.get('taxAmtA') or 0,
                totTaxblAmt=request.POST.get('totTaxblAmt') or 0,
                totTaxAmt=request.POST.get('totTaxAmt') or 0,
                cashDcRt=request.POST.get('cashDcRt') or 0,
                cashDcAmt=request.POST.get('cashDcAmt') or 0,
                totAmt=request.POST.get('totAmt') or 0,
                prchrAcptcYn=request.POST.get('prchrAcptcYn') or 'N',
                remark=request.POST.get('remark', ''),
                regrId=request.POST.get('regrId', ''),
                regrNm=request.POST.get('regrNm', ''),
                modrId=request.POST.get('modrId', ''),
                modrNm=request.POST.get('modrNm', ''),
                saleCtyCd=request.POST.get('saleCtyCd') or '',
                lpoNumber=request.POST.get('lpoNumber') or None,
                currencyTyCd=request.POST.get('currencyTyCd') or 'ZMW',
                exchangeRt=request.POST.get('exchangeRt') or '1',
                destnCountryCd=request.POST.get('destnCountryCd') or '',
                dbtRsnCd=request.POST.get('dbtRsnCd') or '',
                invcAdjustReason=request.POST.get('invcAdjustReason') or ''
            )

            item_list_raw = request.POST.get('itemList', '[]')
            item_list = json.loads(item_list_raw)

            for item_data in item_list:
                InvoiceItem.objects.create(
                    invoice=sale,
                    itemSeq=item_data.get('itemSeq'),
                    itemCd=item_data.get('itemCd', ''),
                    itemClsCd=item_data.get('itemClsCd', ''),
                    itemNm=item_data.get('itemNm', ''),
                    bcd=item_data.get('bcd', ''),
                    pkgUnitCd=item_data.get('pkgUnitCd', ''),
                    pkg=item_data.get('pkg', 0),
                    qtyUnitCd=item_data.get('qtyUnitCd', ''),
                    qty=item_data.get('qty', 0),
                    prc=item_data.get('prc', 0),
                    splyAmt=item_data.get('splyAmt', 0),
                    dcRt=item_data.get('dcRt', 0),
                    dcAmt=item_data.get('dcAmt', 0),
                    isrccCd=item_data.get('isrccCd', ''),
                    isrccNm=item_data.get('isrccNm', ''),
                    isrcRt=item_data.get('isrcRt', 0),
                    isrcAmt=item_data.get('isrcAmt', 0),
                    vatCatCd=item_data.get('vatCatCd'),
                    exciseTxCatCd=item_data.get('exciseTxCatCd'),
                    tlCatCd=item_data.get('tlCatCd'),
                    iplCatCd=item_data.get('iplCatCd'),
                    vatTaxblAmt=item_data.get('vatTaxblAmt', 0),
                    vatAmt=item_data.get('vatAmt', 0),
                    exciseTaxblAmt=item_data.get('exciseTaxblAmt', 0),
                    tlTaxblAmt=item_data.get('tlTaxblAmt', 0),
                    iplTaxblAmt=item_data.get('iplTaxblAmt', 0),
                    iplAmt=item_data.get('iplAmt', 0),
                    tlAmt=item_data.get('tlAmt', 0),
                    exciseTxAmt=item_data.get('exciseTxAmt', 0),
                    totAmt=item_data.get('totAmt', 0),
                )

            return redirect('sale-info', sale.id)

        except Exception as e:
            print(f"Error saving sale: {str(e)}")
    return render(request, "sales/index.html")

def info(request, id):
    invoice = None
    try:
        invoice = get_object_or_404(Invoice, pk=id)
        if not invoice:
            return redirect("sales")
    except Exception as e:
        print(f"{e}")
    return render(request, "sales/info.html", {"invoice": invoice})


def credit_note_list(request):
    invoices = []
    try:
        invoices = Credit_Note_Invoice.objects.all().order_by('-id')
    except Exception as e:
        print(f"{e}")
    return render(request, "sales/credit-notes.html", {"invoice": invoices})

def credit_note_info(request, id):
    invoice = []
    try:
        invoice = get_object_or_404(Credit_Note_Invoice, pk=id)
    except Exception as e:
        print(f"{e}")
    return render(request, "sales/credit-note-info.html", {"invoice": invoice})


def credit_note_new(request, id):
    invoices = Invoice.objects.all ().order_by('-id')
    try:
        pass
    except Exception as e:
        print(f"{e}")
    return render(request, "sales/credit-note-new.html", {"invoices": invoices})
