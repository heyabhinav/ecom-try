from django.shortcuts import render
from . models import Product

# Create your views here.

def index(request):
    return render(request, 'index.html')
    
def dashboard(request):
    if request.method == "POST":
        product_name = request.POST["pname"]
        product_price = request.POST["price"]
        product_category = request.POST["category"]
        product_desc = request.POST["desc"]
        product_image = request.POST["pimage"]
        
        product = Product(product_name=product_name, price=product_price, desc=product_desc, image=product_image, category=product_category)
        
        product.save()
        return render(request, 'shop/dashboard.html')
    else:
        return render(request, 'shop/dashboard.html')