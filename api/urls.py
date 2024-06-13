from django.urls import path
from .views import *
urlpatterns = [
    path('items',items,name='items'),
    path('suppliers',suppliers, name="suppliers" ),
    path('suppliers/<int:id>', supplier, name='supplier'),
    path('items/<int:id>', item, name='item')
]