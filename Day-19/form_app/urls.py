from django.urls import path
from form_app.views import product_list_page,home_page,add_product_page

urlpatterns = [
    path('',home_page,name= 'home' ),
    path('product-list/',product_list_page,name= 'product_list' ),
    path('add-product/',add_product_page,name= 'add_product' ),
]
