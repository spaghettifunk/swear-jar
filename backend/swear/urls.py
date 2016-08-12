from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^bravochecihaitentato/$', views.init, name='init'),
    url(r'^jar/$', views.update_jar, name='update')
]
