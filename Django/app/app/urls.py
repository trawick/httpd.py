from django.conf.urls import url

import views

urlpatterns = [
    url(r'^cgivars/$', views.cgivars),
    url(r'^protected/$', views.protected),
    url(r'^sendfile/$', views.sendfile),
]
