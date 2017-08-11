from django.conf.urls import include, url
from wx_app.views import index

urlpatterns = [
    url(r'^$',index)
]
