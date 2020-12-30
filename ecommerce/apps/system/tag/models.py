from django.db import models
from django.db.models.signals import pre_save, post_save
from django.urls import reverse
from ecommerce.apps.system.products.utility import unique_slug_generator
from ecommerce.apps.system.products.models import Product




class Tag (models.Model):
    title  = models.CharField(max_length=120)
    slug   = models.SlugField()
    timestamp = models.DateTimeField()
    active = models.BooleanField(default=True)
    products = models.ManyToManyField(Product, blank=True)
    
    def __str__(self):
        return self.title
    
    
#this is the method to handle pre_save
def tag_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
pre_save.connect(tag_pre_save_receiver, sender=Tag)
