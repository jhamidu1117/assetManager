from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from assets.models import Asset
from assets.forms import CreateAssetForm

# Create your views here.


def index(request):
    return render(request, 'assets/home.html')


def view_assets(request):
    assets = Asset.objects.all()
    return render(request, 'assets/view_assets.html', {'assets': assets})


@login_required
def create_asset(request):
    if request.method == 'POST':
        form = CreateAssetForm(request.POST)
        if form.is_valid():
            asset = form.save()
            return redirect('home')
    else:
        form = CreateAssetForm()
    return render(request, 'assets/create_asset.html', {'form': form})


