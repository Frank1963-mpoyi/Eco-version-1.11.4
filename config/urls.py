
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    
    url(r'^carts/', include('ecommerce.apps.system.carts.urls')),
    url(r'^products/', include('ecommerce.apps.system.products.urls')),
    url(r'^search/', include('ecommerce.apps.system.search.urls')),
    url(r'^tag/', include('ecommerce.apps.system.tag.urls')),
    url(r'^admin/', admin.site.urls),
]
