from django import template
from decimal import Decimal
import locale

register = template.Library()

@register.filter
def getattr_wrapper(obj, attr):
    return getattr(obj, attr)

@register.filter
def multiply(value_1, value_2):
    return round(value_1 * Decimal(value_2), 2)

@register.filter
def divide(value_1, value_2):
    return round(value_1 / Decimal(value_2), 2)

@register.filter
def cu_quince_dias(cu_fzas, cu_inicial):
    costo_deuda = cu_fzas/cu_inicial-1
    cu_fzas_corregido = cu_inicial*(1+costo_deuda/2)
    return round(cu_fzas_corregido, 2)

@register.filter
def format_currency(value):
    # Establecer la configuración regional
    locale.setlocale(locale.LC_ALL, 'es_AR')

    # Formatear el valor utilizando la configuración regional
    if isinstance(value, (Decimal)):
        formatted_value = locale.format_string('$%.2f', value, grouping=True)
        return formatted_value
    else:
        return value

@register.filter
def type(value):
    # Establecer la configuración regional
    return type(value)


@register.simple_tag
def precio_venta(cu_cl, cu_pr, dias, costo_deuda, \
                 margen_cl, margen_pr, com_otras, \
                 com_ventas, iibb_bsas, iibb_mza, \
                 hig_seg):
    
    if cu_pr == "":
        cu_pr = Decimal(0)
    
    if cu_cl == "":
        cu_cl = Decimal(0)

    margen_cl = Decimal(margen_cl)
    margen_pr = Decimal(margen_pr)

    precio_venta = cu_cl*margen_cl+cu_pr*margen_pr

    precio_venta_adj = precio_venta
    values_cargos = {
        "iibb_bsas":iibb_bsas,
        "iibb_mza":iibb_mza,
        "hig_seg":hig_seg,
        "com_ventas":com_ventas,
        "com_otras":com_otras
    }

    for value in values_cargos.values():
        if value:
            precio_venta_adj += precio_venta/Decimal(1-Decimal(value)/Decimal(100))-precio_venta
            # print(f"{value}: ", precio_venta/Decimal(1-Decimal(value)/Decimal(100)))
    
    # factor_dias: 15 días "2", 30 días "1", 45 días "1.5", 60 días "2"
    factores_dias = {
        "15":Decimal(2),
        "30":Decimal(1),
        "45":Decimal(1.5**(-1)),
        "60":Decimal(2**(-1))
    }

    if dias != 0:
        precio_venta_adj = precio_venta_adj*(1+costo_deuda/factores_dias[f"{dias}"])

    precio_venta_adj = format_currency(precio_venta_adj)

    return precio_venta_adj