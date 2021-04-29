from django.urls import path, include #include newly added
from django.conf import settings #I think I have to remove this
from django.conf.urls.static import static #I think I have to remove this as well 

from . import views

app_name = 'store'
urlpatterns = [
    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"), #changed the name and added include from a library
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name='update_item'),
    path('process_order/', views.processOrder, name="process_order"),
] #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)