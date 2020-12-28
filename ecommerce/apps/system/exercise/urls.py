from django.conf.urls import url
from .views import(
    home_view,
    contact_page,
    login_page,
    ) 


urlpatterns = [
    url(r'^$',home_view),
    url(r'^contact/$',contact_page, name="contact"),
    url(r'^login/$',login_page, name="login")

]
