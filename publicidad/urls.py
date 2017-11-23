from django.conf.urls import url
from publicidad.views import index, hotel, bodega, entretenimiento, santuario, restaurante,supermercado, \
publico, surtidor, bar, altagracia, sanvicente, churrasqueria_b, plazaTtefarina, petropar, brothers, santo_tomas, \
bacilica_caacupe
#se importan las funciones de las vistas
urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^hotel', hotel, name="hotel"),
    url(r'^bodega/', bodega, name="bodega"),
    url(r'^entretenimiento/', entretenimiento, name="entretenimiento"),
    url(r'^santuario/', santuario, name="santuario"),
    url(r'^restaurante/', restaurante, name="restaurante"),    
    url(r'^supermercado/', supermercado, name="supermercado"),
    url(r'^publico/', publico, name="publico"),
    url(r'^surtidor/', surtidor, name="surtidor"),
    url(r'^bar/', bar, name="bar"),
    url(r'^altagracia/', altagracia, name="altagracia"),
    url(r'^sanvicente/', sanvicente, name="sanvicente"),
    url(r'^churrasqueria_b/', churrasqueria_b, name="churrasqueria_b"),
    url(r'^plazaTtefarina/', plazaTtefarina, name="plazaTtefarina"),
    url(r'^petropar/', petropar, name="petropar"),
    url(r'^brothers/', brothers, name="brothers"),
    url(r'^santo_tomas/', santo_tomas, name="santo_tomas"),
    url(r'^bacilica_caacupe/', bacilica_caacupe, name="bacilica_caacupe"),            
]