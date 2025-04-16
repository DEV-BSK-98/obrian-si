from django.shortcuts import render, redirect,get_object_or_404
from .models import Item

def index(request):
    if request.method == 'POST':
        try:
            item = Item.objects.create(
                itemNm=request.POST.get('itemNm', '').strip(),
                itemCd=request.POST.get('itemCd', '').strip(),
                itemClsCd=request.POST.get('itemClsCd', '').strip(),
                itemTyCd=request.POST.get('itemTyCd', '').strip(),
                orgnNatCd=request.POST.get('orgnNatCd', '').strip(),
                pkgUnitCd=request.POST.get('pkgUnitCd', '').strip(),
                qtyUnitCd=request.POST.get('qtyUnitCd', '').strip(),
                vatCatCd=request.POST.get('vatCatCd', '').strip(),
                iplCatCd=request.POST.get('iplCatCd', '').strip(),
                tlCatCd=request.POST.get('tlCatCd', '').strip(),
                exciseTxCatCd=request.POST.get('exciseTxCatCd', '').strip(),
            )
            return redirect('item-info', item.id)
        except Exception as e:
            print(f"Error saving item: {str(e)}")
    return render (request, "items/index.html")

def info (request, id):
    item = None
    try:
        item = get_object_or_404(Item, pk=id)
        if not item:
            return redirect ("items")
    except Exception as e:
        print (f"{e}")
    return render (request, "items/info.html", {"item": item})

def list (request):
    items = []
    objs = Item.objects.all ().order_by ('-id')
    if objs:
        items = objs
    return render (request, "items/list.html", {"items": items})