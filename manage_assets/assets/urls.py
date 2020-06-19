from django.urls import path, include, reverse
from assets.views import index, view_assets, create_asset


urlpatterns = [
    path('', index, name='home'),
    path('view_assets/', view_assets, name='assets'),
    path('create_asset/', create_asset, name='new_asset'),
]
