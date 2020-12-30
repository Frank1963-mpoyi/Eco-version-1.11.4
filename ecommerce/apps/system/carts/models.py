from django.conf import settings # import settings
from django.db import models
from ecommerce.apps.system.products.models import Product
from django.db.models.signals import pre_save, post_save, m2m_changed



User = settings.AUTH_USER_MODEL # it going in user model in settings

# create model manager for cart_crete instead of doing it in views.py
class CardManager(models.Manager):
    #all the businesss logic is happening here instead of views.py
    def new_or_get(self, request):
        cart_id = request.session.get('cart_id', None)
        qs= self.get_queryset().filter(id=cart_id)  
        if qs.count() == 1:
            new_obj = False
            card_obj = qs.first() 
            if request.user.is_authenticated() and cart_obj.user is None:
                cart_obj.user = request.user
                cart_obj.save()       
        else:
            cart_obj = Cart.objects.new(user=request.user)
            new_obj = True
            # request.session['card_id'] = card_obj.id 
            return cart_obj, new_obj
        


    def new(self, user=None):
        user_obj = None
        if user is not None:
            if user.is_authenticated:
                user_obj = user
        return self.model.objects.create(user=user_obj)
        #return self.model.objects.create(user=user)

class Cart(models.Model):
    user =models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE) #blank and null any user can create a cart
    products =models.ManyToManyField(Product, blank=True) # blank=True i can have an ability to have a blank cart
    subtotal =models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    updated = models.DateTimeField(auto_now=True)#want to know when recently was updated
    timestamp = models.DateTimeField(auto_now_add=True)# want to know when the cart was created
    
    # let the class know about this card manager
    objects = CardManager()
    
    
    
    def __str__(self):
        return str(self.id)
    
    
    # no video for this part
    
def m2m_changed_cart_receiver(sender, instance, action, *args, **kwargs):
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        products = instance.products.all()
        total = 0
        for x in products:
            total += x.price
        if instance.subtotal != total:
            instance.subtotal = total
            instance.save()
m2m_changed.connect(m2m_changed_cart_receiver, sender=Cart.products.through)

def pre_save_cart_receiver(sender, instance, *args, **kwargs):
    if instance.subtotal > 0:
        instance.total = instance.subtotal + 10
    else:
        instance.total = 0.00
pre_save.connect(pre_save_cart_receiver, sender=Cart)