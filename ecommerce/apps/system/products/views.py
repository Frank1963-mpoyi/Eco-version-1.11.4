from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404

from  .models import Product
from ecommerce.apps.system.carts.models import Cart






# class ProductFeaturedListView(ListView):
    #template_name = 'products/list.html'
    
    # def get_queryset(self, *args, **kwargs):
        # request = self.request
        #return Product.objects.featured()
        # return Product.objects.all().featured()



# class ProductFeaturedDetailView(DetailView):
    # template_name = "products/featured-detail.html"
    # queryset = Product.objects.all().featured()
    
    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     return Product.objects.featured()


    
# def product_feature_detail_view(request, pk=None):
#     template_name = "products/featured-detail.html"
#     #obj = Product.objects.get(id=pk)
#     obj = get_object_or_404(Product, id=pk)
#     context={
#         'object': obj
#     }
#     return render(request, template_name, context)
        





class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'products/product-list.html'

# def product_list_view(request):
#     template_name = "products/product_list.html"
#     queryset = Product.objects.all()
#     context={
#         'object_list': queryset
#     }
#     return render(request, template_name, context)
        
        

 
    

class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = 'products/product_detail.html'
    context_object_name  = 'obj'
    
    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailSlugView, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj #context={"cart": cart_obj}
        return context
        
        
        
    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        #instance= get_object_or_404(Product, slug=slug)
        try:
            instance= Product.objects.get(slug=slug, active=True)
        except Product.DoesNotExist:
            raise Http404("Not found...")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug, activate=True)
            instance = qs.first()
        except:
            raise Http404("wowwwww")
        return instance
    
    
# def product_detail_view(request, pk=None,  *args, **kwargs):
#     template_name = "products/product_detail.html"
#     #obj = Product.objects.get(id=pk)
#     obj = get_object_or_404(Product, id = pk,  featured=True)
#     context={
#         'obj': obj
#     }
#     return render(request, template_name, context)
        

