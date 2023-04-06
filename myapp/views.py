from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp.models import ProductModel, User
#使用者登入
from django.contrib import auth 
from django.contrib.auth import authenticate
#註冊帳號時間
from datetime import datetime

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

def menu(request):
    # return HttpResponse("hello world")
    products = ProductModel.objects.all()
    productlist = []
    for i in range(1, 9):
        product = ProductModel.objects.get(id = i)
        productlist.append(product)
    return render(request, 'menu.html', locals())

def userlogin(request):
    message=""
    if request.method == "POST":
        username = request.POST['username']
        userPassword = request.POST['userPassword']
        print(username+" "+userPassword)
        user = authenticate(username=username, password=userPassword) #password(資料庫裡面名稱ID)=userPassword(取得HTML前端使用者輸入的資料)
        if user is not None:
            auth.login(request, user)
            return redirect('/index/')
        else:
            message = "登入失敗!"
            return render(request, 'userlogin.html', locals())
    else:
    # return HttpResponse("測試")
        useradd_success_status=False #成功登入狀態=False 
        return render(request, 'userlogin.html', locals())
    
def useradd(request):
    if request.method == "POST":
        username = request.POST['username']
        userPassword = request.POST['userPassword']
        userRePassword = request.POST['userRePassword']
        userPhone = request.POST['userPhone']
        userBirthday = request.POST['userBirthday']
        userEmail = request.POST['userEmail']

        # print(username+" "+userPassword+" "+userRePassword+" "+userPhone+" "+userBirthday+" "+userEmail)
        # print(type(userBirthday)) #<class 'str'>
      
        #判斷是否登入
        try:
            user=User.objects.get(username=username)  
        except:
            user=None
        
        if user!=None: #帳號如果設定過就跳回useradd.html
            print("帳號已建立")
            password_check=True #密碼檢查
            return render(request, "useradd.html",locals())  
        else:
            if userPassword != userRePassword: #密碼跟確認密碼不同時跳回useradd.html
                password_check=False
                return render(request, "useradd.html",locals())  
            else:
                print("可註冊")
                #儲存至資料庫
                user = User.objects.create_user(username, userEmail, userPassword)
                user.is_staff = False	# 工作人員狀態，設定True則可以登入admin後台
                user.is_active = True   # True該用戶可登入
                user.cPhone = userPhone
                userBirthday=datetime.strptime(userBirthday,'%Y-%m-%d') #取得HTML的資料後因是字串，所以還要轉成物件
                # print(type(userBirthday)) #<class 'datetime.datetime'>
                user.cBirthday = userBirthday
                user.save()
                useradd_success_status=True #註冊成功
                return render(request, "userlogin.html",locals())
    else:
        user=None #註冊帳號檢查
        password_check=True #密碼檢查
        return render(request, "useradd.html",locals()) 
    # return HttpResponse("測試")

def userlogout(request):
    auth.logout(request)
    return redirect('/index/')

def test(request):
    return render(request, 'test.html', locals())

