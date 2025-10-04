from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Portfolio
from .forms import PortfolioForm

@login_required
def portfolio_list(request):
    portfolios = Portfolio.objects.filter(user=request.user)
    return render(request, "portfolio/portfolio_list.html", {"portfolios": portfolios})

@login_required
def portfolio_create(request):
    if request.method == "POST":
        form = PortfolioForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
            return redirect("portfolio_list")
    else:
        form = PortfolioForm()
    return render(request, "portfolio/portfolio_create.html", {"form": form})

@login_required
def portfolio_edit(request, pk):
    project = get_object_or_404(Portfolio, pk=pk, user=request.user)
    if request.method == "POST":
        form = PortfolioForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect("portfolio_list")
    else:
        form = PortfolioForm(instance=project)
    return render(request, "portfolio/portfolio_edit.html", {"form": form})

@login_required
def portfolio_delete(request, pk):
    project = get_object_or_404(Portfolio, pk=pk, user=request.user)
    if request.method == "POST":
        project.delete()
        return redirect("portfolio_list")
    return render(request, "portfolio/portfolio_delete.html", {"project": project})
