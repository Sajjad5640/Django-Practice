from django.urls import path
from form_app.views import home_page,product_list_page,add_product_page,product_detail_page,delete_product,edit_product_page

urlpatterns = [
    path('',home_page,name= 'home'),
    path('product-list/',product_list_page,name= 'product'),
    path('add-product/',add_product_page,name= 'add_product'),
    path('product-detail/<int:p_id>/',product_detail_page,name= 'product_detail'),
    path('delete-product/<int:p_id>/',delete_product,name= 'delete_product'),
    path('edit-product/<int:p_id>/',edit_product_page,name= 'edit_product'),
]