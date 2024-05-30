from django.shortcuts import render
from django.views.generic import ListView,DetailView
from products.models import Product,Category
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required


# Create your views here.

class ProductListView(ListView):
    model=Product

class ProductDetailView(DetailView):
    model=Product
    template_name="products/product_detail.html"
    context_object_name="product"

def RoyalCaninProducts(request):
    RoyalCaninproducts=Product.cm.RoyalCanin()
    return render(request,"products/product_brand.html",{"products":RoyalCaninproducts})


#---------------------------------------------------------------------


class CategoryDetailView(DetailView):
    model=Category
    template_name="category/category.html"
    context_object_name="category"
    slug_field="category_slug"

#--------------------------------------------------
#Search

def search(request):
    keyword=request.GET.get("keyword")
    products=Product.cm.all().filter(product_name__icontains=keyword)
    return render(request,"products/search.html",{"products":products})

@method_decorator(staff_member_required,name="dispatch")
class ProductCreateView(CreateView):
    model=Product
    fields="__all__"
    success_url="/product/product-admin/"

@method_decorator(staff_member_required,name="dispatch")
class ProductUpdateView(UpdateView):
    model=Product
    fields="__all__"
    success_url="/product/product-admin"

class ProductDeleteView(DeleteView):
    model=Product
    success_url="/products/product-admin"

@method_decorator(staff_member_required,name="dispatch")
class ProductAdminView(ListView):
    model=Product
    template_name="products/product_admin.html"