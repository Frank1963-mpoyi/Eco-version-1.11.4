#from django.db.models import Q  // i want to put it in models to make model manager
from django.shortcuts import render
from django.views.generic import ListView
from ecommerce.apps.system.products.models import Product



class SearchProductListView(ListView):
    # queryset = Product.objects.all()
    template_name = 'search/view.html'  #search/view.html'
    
    #over write context
    def get_context_data(self, *args, **kwargs):
        context = super(SearchProductListView, self).get_context_data(*args, **kwargs)
        context['query'] = self.request.GET.get('q')
        return context
    
    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q', None)# name="q" from frontend
        if query is not None:
            # i want to cut this lookups and bring to model manager in models
            #lookups = Q(title__icontains=query) | Q(description__icontains=query)# can can also put directly to return but this is just a variable we made 
            # return Product.objects.filter(lookups).distinct()# if there is same product name in title and description it will return only one thing 
            return Product.objects.search(query) # imported from models.py
        # it means that if there is a query or user put a text 
        # return an object which the title have the name contain any of character user request
        return Product.objects.featured








#======================this one is not very great we must introduce lookup with Q=============
#class SearchProductListView(ListView):
    # queryset = Product.objects.all()
    #template_name = 'search/view.html'  #search/view.html'
    
    #over write context
    # def get_context_data(self, *args, **kwargs):
    #     context = super(SearchProductListView, self).get_context_data(*args, **kwargs)
    #     context['query'] = self.request.GET.get('q')
    #     return context
    
    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     method_dict = request.GET
        #query = method_dict.get('q', None)# name="q" from frontend
        #if query is not None:
            #return Product.objects.filter(title__icontains=query)
        # it means that if there is a query or user put a text 
        # return an object which the title have the name contain any of character user request
        #return Product.objects.featured

#========================================================    
# class SearchResultsView(ListView):
#     model = City
#     template_name = 'search_results.html'
    
#     def get_queryset(self): 
#         query = self.request.GET.get('q')
#         object_list = City.objects.filter(
#             Q(name__icontains=query) | Q(state__icontains=query)
#         )
#         return object_list

