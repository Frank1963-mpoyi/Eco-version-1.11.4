from django.db import models



# if we want to query this: Products.objects.all().featured
class ProductQuerySet(models.query.QuerySet):
    def featured(self):
        return self.filter(featured=True)



class ProductManager(models.Manager):
    # with this queryset : Products.objects.featured
    # def featured(self):
    #     return self.get_queryset().filter(featured=True)
    
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)
    
    def features(self):
        return self.get_queryset().featured()
    

    # def get_by_id(self, id):
    #     qs = self.get_queryset().filter(id=id)
    #     if qs.count() == 1:
    #         return qs.first()
    #     return none



class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20, null=True)
    image = models.ImageField(upload_to='products/', null=True, blank=True)# filefield is a standard field , dont put slash infront product
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    #we must let the model know about the change 
    objects = ProductManager()
    
    
    
    #this is for python 3    
    def __str__(self):
        return self.title
    
    #this is for python 2
    def __unicode__(self):
        return self.title
