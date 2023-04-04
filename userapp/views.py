from django.shortcuts import render,redirect
from adminapp.models import*
from django.db.models import Sum

from.models import*

# Create your views here.
def user(request):
    data=Category.objects.filter()
    return render(request,'userindex.html',{'data':data})

def uproducts(request):
    data=Products.objects.filter()
    return render(request,'userproducts.html',{'productdata':data})

def ucategories(request):
    data=Category.objects.filter()
    return render(request,'usercategories.html',{'categorydata':data})

def ucontact(request):
    return render(request,'contact.html')

def ureg(request):
    return render(request,'userregistration.html')

def ulogin(request):
    return render(request,'userlogin.html')

    
def regdata(request):
    if request.method=='POST':
        fnme=request.POST.get('fname')
        lnme=request.POST.get('lname')
        usn=request.POST.get('uname')
        psw=request.POST.get('pword')
        mobnum=request.POST.get('mnum')
        addr=request.POST.get('add')
        cty=request.POST.get('city')
        ste=request.POST.get('state')
        zipcde=request.POST.get('pincode')
        data=Register(firstname=fnme,lastname=lnme,username=usn,password=psw,mobilenumber=mobnum,address=addr,city=cty,state=ste,zipcode=zipcde)
        data.save()
        return redirect('ureg')
    


def memberlogin(request):
    if request.method == "POST":
        username_r = request.POST.get('user1')
        password_r = request.POST.get('pass1')
        if Register.objects.filter(username=username_r,password=password_r).exists():
            data = Register.objects.filter(username=username_r,password=password_r).values('firstname','lastname','mobilenumber','address','city','state','zipcode','id').first()
            request.session['ftname'] = data['firstname']
            request.session['ltname'] = data['lastname']
            request.session['menum'] = data['mobilenumber']
            request.session['addr'] = data['address']
            request.session['citty'] = data['city']
            request.session['sttate'] = data['state']
            request.session['ziipcode'] = data['zipcode']
            request.session['uid'] = data['id']
            return redirect('user')
        else:
            return render(request,'userlogin.html',{'msg':'Invalid Credentials'})
        

def memberlogout(request):
    del request.session['ftname']
    del request.session['ltname']
    del request.session['menum']
    del request.session['addr']
    del request.session['citty']    
    del request.session['sttate']
    del request.session['ziipcode']    
    del request.session['uid']
    return redirect('user') 

def uprodetails(request,id):
    data=Products.objects.filter(id=id)
    return render(request,'productdetails.html',{'prodata':data})

def userdata(request,id):
    if request.method=="POST":
        uid=request.session.get('uid')
        quant=request.POST.get("quantity")
        tot=request.POST.get("total")
        data=Cartdb(userid=Register.objects.get(id=uid),productid=Products.objects.get(id=id),quantity=quant,total=tot,status=0)
        data.save()
    return redirect('ucart')

def ucart(request):
    uid=request.session.get('uid')
    data=Cartdb.objects.filter(userid=uid)
    return render(request,'cart.html',{'cartdata':data})

def ucdelete(request,id):
    Cartdb.objects.filter(id=id).delete()
    return redirect('ucart')

def ucheckout(request):
    uid=request.session.get('uid')
    dat=Cartdb.objects.filter(userid=uid,status=0)
    data=Cartdb.objects.filter(userid=uid).aggregate(Sum('total'))
    return render(request,'checkout.html',{'dat':dat,'data':data})


def ucdata(request):
    if request.method=="POST":
        uid=request.session.get('uid')
        cartvar=Cartdb.objects.filter(userid=uid,status=0)
        for i in cartvar:
            data2=Checkout(userid=Register.objects.get(id=uid),cartid=Cartdb.objects.get(id=i.id))
            data2.save()
            Cartdb.objects.filter(id=i.id).update(status=1)
    return redirect("ucheckout")


def uabout(request):
    return render(request,'about.html')

def contactdata(request):
    if request.method=="POST":
        name1=request.POST.get('name')
        email1=request.POST.get('email')
        subject1=request.POST.get('subject')
        message1=request.POST.get('message')
        data=Contactdb(name=name1,email=email1,subject=subject1,messages=message1)
        data.save()
        return redirect('ucontact')
