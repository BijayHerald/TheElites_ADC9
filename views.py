from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.http import HttpResponse
from .forms import *
from django.core.files.storage import FileSystemStorage
# Create your views here.





def index_page(request):
    return render(request, 'mobile/index.html')


def view_add_product_form(request):
    return render(request,'mobile/add_product.html')

def product_list(request):
    categories = Product.objects.all()
    return render(request,'mobile/list.html',{
        'products': categories
    })


def product_list_search(request):
    products = Product.objects.filter(name=request.GET['productname'])
    print(products)

    return render(request,'mobile/list.html',{
        'products': products
    })







def product_image_view(request): 
  
    if request.method == 'POST': 

        get_img = request.FILES['image']
        fs = FileSystemStorage()
        image = fs.save(get_img.name, get_img)


        form = Product(name = request.POST['product_name'], Fullprice = request.POST['product_fullprice'],image =get_img , Discountprice = request.POST['product_discount_price'],) 
        form.save() 
    return HttpResponse("records saved.") 
    
  
def success(request): 
    return HttpResponse('successfully uploaded') 

