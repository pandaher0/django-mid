# Author:hxj
from django.urls import re_path

from booktest import views

app_name = 'booktest'

urlpatterns = [
    re_path('^index$', views.index),
    re_path('^static_test$', views.static_test),

    re_path('^show_upload$', views.show_upload),
    re_path('^upload_handle$', views.upload_handle),

    re_path('^show_areas(?P<pindex>\d*)/$', views.show_areas),

    re_path('^areas$', views.areas),
    re_path('^prov$', views.prov),
    re_path('^city$', views.city),
    re_path('^dis(\d+)$', views.dis),

]
