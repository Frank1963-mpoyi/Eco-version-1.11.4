from django.shortcuts import render, redirect
from ecommerce.apps.system.products.models import Product
from .models import Cart







# def cart_create(user=None):
#     cart_obj = Cart.objects.create(user=None)
#     return cart_obj

def cart_home(request):
    template_name = "carts/home.html"
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    #=======receiver is handling this 
    # products = cart_obj.products.all()
    # total = 0
    # for x in products:
    #     total += x.price
    # cart_obj.total = total
    # cart_obj.save()
    
    context={
        "cart": cart_obj 
        }
    return render (request, template_name, context)

def cart_update(request):
    product_id = request.POST.get('product_id')
    if product_id is not None:
        try:
            product_obj = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return redirect("carts:home")       
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        if product_obj in cart_obj.products.all():
            card_obj.products.remove(product_obj)
        else:
            cart_obj.products.add(product_obj)# add products to manay to many field

    #return redirect(product_obj.get_absolute_url())
    return redirect("carts:home")# redirect to cart_home()




# def cart_home(request):
    # card_id = request.session.get("cart_id", None )# here to check if the cart id does already exists i have a cart id i dont have to create a new one
    # hey get the current cart id or saying None
    # if card_id is None: #and isinstance(cart_id, int) # mean whatever come in is an integer
        #print('create new cart')
        # card_obj = Cart.objects.create(user=None)
        # request.session['cart_id'] = cart_obj.id
        #request.session['card_id'] = 12 # after creation set it 
    # else:
    #     print('cart ID exists')
    #     print(card_id)
    #     cart_obj = Cart.objects.get(id=card_id)
    
    
    # template_name = "carts/home.html"
    # context = {}
    # return render(request, template_name, context )





# def cart_home(request):
    # print(request.session)# is there by default
    #print(dir(request.session))# gives you all the method in session
    # <django.contrib.sessions.backends.db.SessionStore object at 0x0423FBE0>
    # [30/Dec/2020 05:43:30] "GET /cart/ HTTP/1.1" 200 2920
    # 'session_key', 'set_expiry'
    #request.session.set_expiry(300) # mean after 5 minutes expire the session
    #request.session.session_key # you can store the seseion key and delete it later
    
    # key = request.session.session_key # when i login i will see the key for particular user, if you logout the key will be None, is where i can store object and some stuff
    # print(key)   
    
    # template_name = "carts/home.html"
    # context = {}
    # return render(request, template_name, context )