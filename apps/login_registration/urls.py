from django.conf.urls import url
from . import views
from models import *

urlpatterns = [
    url(r'^$', views.index),
    url(r'^welcome/(?P<user_id>\d+)$', views.welcome),
    url(r'^(?P<action>\w+)', views.process),
]