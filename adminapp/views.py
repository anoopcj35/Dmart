from django.shortcuts import render,redirect
from.models import*
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from userapp.models import*



# Create your views here.
def admin(request):
    users=Register.objects.all().count()
    orders=Checkout.objects.all().count()
    products=Products.objects.all().count()
    category=Category.objects.all().count()
    return render(request,'adminindex.html',{'users':users,'orders':orders,'products':products,'category':category})

def productform(request):
    return render(request,'addproduct.html')

def categoryform(request):
    return render(request,'addcategory.html') 

def productdata(request):
    if request.method=='POST':
        proname=request.POST.get('pname')
        proprice=request.POST.get('pprice')
        proquantity=request.POST.get('pquantity')
        proimage=request.FILES['pimage']
        data=Products(productname=proname,productprice=proprice,productquantity=proquantity,productimage=proimage)
        data.save()
        return redirect('productform')
    
def categorydata(request):
    if request.method=='POST':
        catname=request.POST.get('cname')
        catdescription=request.POST.get('cdescrip')
        catimage=request.FILES['cimage']
        data=Category(categoryname=catname,categorydescription=catdescription,categoryimage=catimage)
        data.save()
        return redirect('categoryform')
    
def producttable(request):
    data=Products.objects.all()
    return render(request,'viewproduct.html',{'data':data})


def categorytable(request):
    data=Category.objects.all()
    return render(request,'viewcategory.html',{'data':data})


def productedit(request,id):
    data=Products.objects.filter(id=id)
    return render(request,'editproduct.html',{'data':data})


def categoryedit(request,id):
    data=Category.objects.filter(id=id)
    return render(request,'editcategory.html',{'data':data})

def productupdate(request,id):
    if request.method=="POST": 
        proname=request.POST.get('pname')
        proprice=request.POST.get('pprice')
        proquantity=request.POST.get('pquantity')
        proimage=request.FILES['pimage']
        try:
            proimage = request.FILES['pimage']
            fs = FileSystemStorage()
            file = fs.save(proimage.name, proimage)
        except MultiValueDictKeyError:
            file = Products.objects.get(id=id).productimage
        Products.objects.filter(id=id).update(productname=proname,productprice=proprice,productquantity=proquantity,productimage=file)
        return redirect('producttable')
        
def categoryupdate(request,id):
    if request.method=='POST':
        catname=request.POST.get('cname')
        catdescription=request.POST.get('cdescrip')
        catimage=request.FILES['cimage']
        try:
            catimage = request.FILES['cimage']
            fs = FileSystemStorage()
            file = fs.save(catimage.name, catimage)
        except MultiValueDictKeyError:
            file = Category.objects.get(id=id).categoryimage
        Category.objects.filter(id=id).update(categoryname=catname,categorydescription=catdescription,categoryimage=file)
        return redirect('categorytable')     

def productdelete(request,id):
    Products.objects.filter(id=id).delete()
    return redirect('producttable')


def categorydelete(request,id):
    Category.objects.filter(id=id).delete()
    return redirect('categorytable')

def adminlogin(request):
    return render(request,'login.html')

def adlogin(request):
    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['pass']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin')
        else:
            return render(request,'login.html', {'msg':'Sorry Invalid User Credentials'})
    else:
        return render(request,'login.html')


def adminlogout(request):
    return render(request,'logout.html')

def adlogout(request):
    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['pass']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin')
        else:
            return render(request,'logout.html', {'msg':'Sorry Invalid User Credentials'})
    else:
        return render(request,'logout.html')
    
def user_data(request):
    data1=Register.objects.all()
    return render(request,'userdata.html',{'data1':data1})

def order_data(request):
    data2=Checkout.objects.all()
    return render(request,'orders.html',{'data':data2})

def contact_data(request):
    data3=Contactdb.objects.all()
    return render(request,'contactdata.html',{'data':data3})