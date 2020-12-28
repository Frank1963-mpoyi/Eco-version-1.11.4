from django.conf.urls import url
from .views import(
    home_view,
    contact_page,
    login_page,
    ) 

app_name="exercise"
urlpatterns = [
    url('home',home_view, name="home"),
    url(r'^contact/$',contact_page, name="contact"),
    url(r'^login/$',login_page, name="login")

]
# if there is app_name dont leave urls pattern blank