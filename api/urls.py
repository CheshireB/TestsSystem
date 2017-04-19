from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'v0/$', views.subjects),
    url(r'v0/get$', views.static),
    url(r'v0/ntest$', views.newtemp),
    url(r'v0/test$', views.temp),
    url(r'v0/answer$', views.answer),
    url(r'v0/solve$', views.solve),
    url(r'v0/getinfosubject$', views.getinfosubject),
    url(r'v0/getinfostest$', views.getinfostest),
]