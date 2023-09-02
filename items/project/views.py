from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . models import descri,wish,cart,checkout
from django.contrib.auth import login,logout,authenticate


def product(request):
    return render(request,'product.html')
def contact(request):
    return render(request,'contact.html')
def blog(request):
    return render(request,'blog.html')
def home(request):
    return render(request,'home-02.html')
def homes(request):
    return render(request,'home-03.html')
def shoping(request):
    return render(request,'shoping-cart.html')
def about(request):
    return render(request,'about.html')
def indexs(request):

    pro = descri.objects.all()
    pr = {
        'pro':pro
    }
    if request.user.is_active:
      
        kk = wish.objects.filter(userid = request.user).count()
        cartdetail = cart.objects.filter(userid =request.user).count()
        return render(request,'index.html',{'wished':kk,'pro':pro,'cart_info':cartdetail})
    else:
        return render(request,'index.html')




def index(request):
    if request.method == 'POST': 
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('createpassword')
        
        cust = User.objects.create_user(username = name, email = email, password = password)
        # print(name,email,password)
        cust.save()
        return redirect(indexs)
    return render(request,'signin.html')


def userlogin(request):
    if request.method == 'POST': 
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user:
            login(request,user)
            return redirect(indexs)
        else:
            return redirect(userlogin)
    return render(request,'login.html')

def userlogout(request):
    logout(request)
    return redirect(indexs)

def admineform(request):
    if request.method == 'POST':
        image = request.FILES['image']
        
        name = request.POST['pname']
        price = request.POST['pprice']
        description = request.POST['pdesp']

        ss = descri(photo = image, product_name = name, product_price = price, product_descrition = description)
        ss.save()    

        return HttpResponse('admin form successful')
    return render(request,'adminform.html')



def viewdetail(request):
    
    obj = descri.objects.get(id=1)

    print(obj.id,obj.product_name,'------')
    return JsonResponse({'data':obj})



def kkk(request):
    id_param = request.GET.get('id')  

    if id_param is not None:
        try:
            id_value = int(id_param)
            items = descri.objects.filter(id=id_value)
        except ValueError:
            items = []

    # If id_param is None or invalid, retrieve all items
    else:
        items = descri.objects.all()
        for i in items:
            print(i.photo,'----')
    data = [{'id': item.id, 'name': item.product_name, 'price': item.product_price, 'description':item.product_descrition,'photo':item.photo.url} for item in items]
    return JsonResponse({'items': data})
def iitem(request):
    return render(request,'jj.html')

def wished(request):
    id = request.user.id
    # print(request.user.id,'-----')

    kk = wish.objects.filter(userid = request.user).count()
    print(kk)
    return render(request,'wish.html',{'wished':kk})


def userwish(request):
    kk = wish.objects.filter(userid = request.user)
    for i in kk:
        print(i)
    return render(request,'wish.html',{'wished':kk})

def userwishlist(request):
   
    new_state = request.GET.get('state', False)
  
    return JsonResponse({'success': True})
        
    # return render(request,'jj.html')

def cart_info(request):
    id = request.user.id
    cartdetail = cart.objects.filter(userid =request.user).count()
    print(cartdetail)
    return render(request,'cartdetail.html',{'cart_info':cartdetail})

def cart_view(request):
    cartdetail = cart.objects.filter(userid =request.user)
    for i in cartdetail:
        print(i)
    return render(request,'cartdetail.html',{'cart_info':cartdetail})


def view_cart_details(request,id):
    # if request.method =="POST":
        # vv = descri.objects.get(id=product_id)
    product_id = 8
    userid = request.user.id
    size = request.POST.get('size')
    color = request.POST.get('color')
    quantity = request.POST.get('numproduct')
    print(id,userid,size,color,quantity,'------')
    return HttpResponse('-done-----')
        # detail = cart(size = size,color = color,quantity =quantity)
        # detail.save()

        
    # return render(request,"jj.html")


def checkoutdetail(request):
    checkout_order = checkout.objects.filter(userid = request.user)
    for i in checkout_order:
        print(i)
    return render(request,'shoping-cart.html',{"checkoutdetail":checkout_order})
