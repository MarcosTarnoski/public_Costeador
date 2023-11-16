from django.contrib import admin
from modulos.models import Articulos, FinanzasParametros, RecursosHumanos, \
                           ProduccionParametros, Clientes, CosteoSerigrafia, \
                           CotizadorSerigrafia, SopleteadoParametros

# Register your models here.
admin.site.register(Articulos)
admin.site.register(FinanzasParametros)
admin.site.register(RecursosHumanos)
admin.site.register(ProduccionParametros)
admin.site.register(Clientes)
admin.site.register(CosteoSerigrafia)
admin.site.register(CotizadorSerigrafia)
admin.site.register(SopleteadoParametros)
