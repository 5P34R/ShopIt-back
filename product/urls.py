from importlib.resources import path
from nturl2path import url2pathname
from django.urls import path

from .views import Products

urlpatterns = [
    path('', Products.as_view())
]
