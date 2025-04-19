from django.shortcuts import render, redirect, get_object_or_404
from .models import Imports
from django.contrib.auth.decorators import login_required

@login_required
def index (request):
    imports = []
    imps = Imports.objects.all ().order_by ('-id')
    if imps:
        imports = imps
    return render (request, "imports/index.html", {"imports": imports})

@login_required
def info (request, id):
    item = None
    try:
        item = get_object_or_404(Imports, pk=id)
        if not item:
            return redirect ("item")
    except Exception as e:
        print (f"{e}")
    return render (request, "imports/info.html", {"item": item})

@login_required
def pull (request):
    return redirect ("import-purchases")