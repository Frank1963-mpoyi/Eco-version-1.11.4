from django.conf.urls import url
# from ecommerce.apps.system.products.views import ProductListView
from .views import SearchProductListView




app_name= 'search'
urlpatterns = [
    
    url(r'^search/$',SearchProductListView.as_view(), name="query"),

]
