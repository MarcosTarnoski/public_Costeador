from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("costeo_serigrafia/", views.costeo_serigrafia, name="costeo_serigrafia"),
    path("costeo_coating/", views.costeo_coating, name="costeo_coating"),
    path("compras/", views.compras, name="compras"),
    path("compras/detalle", views.compras_detalles, name="compras_detail"),
    path("rrhh/", views.rrhh, name="rrhh"),
    path("rrhh/detalle", views.rrhh_detalles, name="rrhh_detail"),
    path("finanzas/", views.finanzas, name="finanzas"),
    path("produccion/", views.produccion, name="produccion"),
    path("cotizaciones_hist/", views.cotizaciones_hist, name="cotizaciones"),
    # path("cotizaciones_hist/detail/<int:id>/", views.cotizaciones_hist_detail, name="cotizaciones_detail"),
    path('calcular-ganancia/', views.calcular_ganancia, name='calcular_ganancia'),
    path('nuevo_cliente/', views.nuevo_cliente, name='nuevo_cliente'),
    path("cotizacion_menu/", views.cotizacion_menu, name="cotizacion_menu"),
    path("cotizacion_form/<str:tipo_cotizacion>", views.cotizacion_form, name="cotizacion_form"),
    path('descargar_excel/', views.descargar_excel, name='descargar_excel'),
]