from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from assets.models import Asset


class CreateAssetForm(forms.ModelForm):

    class Meta:
        model = Asset
        fields = ('Tag', 'Serial_number', 'Manufacturer', 'asset_type')