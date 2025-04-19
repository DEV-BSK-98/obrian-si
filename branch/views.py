from django.shortcuts import render, redirect
from .models import Branch
from django.contrib.auth.decorators import login_required

@login_required
def index (request):
    if request.method == 'POST':
        try:
            branch = Branch.objects.create(
                branch_name=request.POST.get('branch_name', '').strip(),
                bhfId=request.POST.get('bhfId', '').strip(),
            )
            return redirect ("branch-info", branch.id)
        except Exception as e:
            print(f"Error saving data: {str(e)}")
    return render (request, "branch/index.html")

@login_required
def list (request):
    branches = []
    objs = Branch.objects.all ().order_by ('-id')
    if objs:
        branches = objs
    return render (request, 'branch/list.html', {"branches": branches})

@login_required
def info (request, id):
    branch = Branch.objects.filter (id=id).first ()
    if not branch:
        return redirect ("branch")

    return render (request, "branch/info.html", {"branch": branch})