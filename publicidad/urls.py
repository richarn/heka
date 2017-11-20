from django.conf.urls import url
from publicidad.views import index, hotel
urlpatterns = [
    url(r'^$', hotel, name="hotel"),
]