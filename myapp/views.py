from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import ProductModel

# Create your views here.
#建立首頁輪播圖片(跟資料庫互通資料)
def index(request):
    # return HttpResponse("hello world")
    products = ProductModel.objects.all()
    productlist = []
    for i in range(1, 5):
        product = ProductModel.objects.get(id = i)
        productlist.append(product)
    return render(request, 'index.html', locals())