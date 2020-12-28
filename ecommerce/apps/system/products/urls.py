from django.conf.urls import url
from .views import (
    ProductListView,
    product_list_view,
    ProductDetailSlugView,
   # product_detail_view,
    ProductFeaturedListView,
    ProductFeaturedDetailView,
    #product_feature_detail_view,
    )


urlpatterns = [
    url(r'^product/$', product_list_view, name="product"),
    url(r'^product-fbv/$',ProductListView.as_view(), name="product-fbv"),
    url(r'^product/(?P<slug>[\w-]+)/$',ProductDetailSlugView.as_view(), name="product"),
    #url(r'^product-fbv/(?P<pk>\d+)/$',product_detail_view, name="product"),
    url(r'^featured/$',ProductFeaturedListView.as_view(), name="product-fbv"),
    url(r'^featured/(?P<slug>[\w-]+)/$',ProductFeaturedDetailView.as_view(), name="product"),
    #url(r'^featured-fbv/(?P<pk>\d+)/$',product_feature_detail_view, name="featured"),
]



