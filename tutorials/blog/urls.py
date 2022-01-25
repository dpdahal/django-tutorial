from django.urls import path, re_path, register_converter
from . import views
from . import urlcheck

register_converter(urlcheck.UrlCheck, 'newId')

urlpatterns = [
    path('', views.index, name='index'),
    path('about-us', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('news/<newId:id>', views.news)
    # re_path(r'^news/(?P<id>[0-5]{3})/$', views.news),

]
