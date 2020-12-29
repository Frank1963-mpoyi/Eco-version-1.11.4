import random
import os
from django.db import models
from .utility import unique_slug_generator
# need to happen before the model save
from django.db.models.signals import pre_save, post_save
#pre_save mean before save in the database it must do something and we must create a method to handle that
from django.urls import reverse

# if we want to query this: Products.objects.all().featured
class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)
    
    def featured(self):
        return self.filter(featured=True, active=True)



class ProductManager(models.Manager):
    # with this queryset : Products.objects.featured
    # def featured(self):
    #     return self.get_queryset().filter(featured=True)
    
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)
    
    
    def all(self):
        return self.get_queryset().active()
    
    def featured(self):
        return self.get_queryset().featured()
    

    # def get_by_id(self, id):
    #     qs = self.get_queryset().filter(id=id)
    #     if qs.count() == 1:
    #         return qs.first()
    #     return none



class Product(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(default='hello', blank=True, unique=True)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20, null=True)
    image = models.ImageField(upload_to='products/', null=True, blank=True)# filefield is a standard field , dont put slash infront product
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    #we must let the model know about the change 
    objects = ProductManager()
    
    def get_absolute_url(self):
        #return "/product/{slug}/".format(slug=self.slug)
        #/product/{slug}/ not name in urlpattern
        return reverse("products:detail", kwargs={"slug":self.slug})
        # it doing the same thing than return above but here it use the name="detail" instead of url(r'^product/$',  )
        # mean the name detail is unique to the apps products beacause they can be the same name in different apps
    
    #this is for python 3    
    def __str__(self):
        return self.title
    
    #this is for python 2
    def __unicode__(self):
        return self.title

#this is the method to handle pre_save
def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
pre_save.connect( product_pre_save_receiver, sender=Product)