from django.shortcuts import render,redirect
from form_app.models import ProductModel
from form_app.forms import ProductForm
# Create your views here.
def home_page(req):


    return render (req, 'home.html')

def product_list_page(req):
    product_data = ProductModel.objects.all()
    context ={
        'product_data' :product_data
    }
    return render(req, 'product_list.html',context)
def add_product_page(req):
    if req.method =="POST":
        form_data = ProductForm (req.POST, req.FILES)
        if form_data.is_valid():
            form_data.save()
            return redirect ('product_list')
#to show form
    form_data = ProductForm ()
    context = {
            'form_data' : form_data
        }
    return render (req,"add_product.html", context)
