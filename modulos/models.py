from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

my_choices = (
    ("SI", "SI"),
    ("NO", "NO")
)

class Articulos(models.Model):
    articulo = models.CharField(max_length=255, unique=True)
    unidad = models.CharField(max_length=10, blank=True, null=True)
    costo_ars_sinajuste = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    costo_ars = models.DecimalField(max_digits=20, decimal_places=2)
    costo_usd = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    costo_eur = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    tipo = models.CharField(max_length=255)
    tipo_2 = models.CharField(max_length=255, blank=True, null=True)
    condicion_pago_dias = models.PositiveSmallIntegerField(blank=True, null=True)
    peso_kg = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    diametro_mm = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    asa = models.CharField(max_length=2, choices=my_choices, blank=True, null=True)
    consumo_g_cm2 = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    consumo_estandar = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    velocidad_aplicacion_u_h = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    createdon = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING) # to_sql() sobreescribe la definición de la tabla. Hay que reveer como subir el dataframe.

class RecursosHumanos(models.Model):
    apellido = models.CharField(max_length=255, null=True)
    nombre = models.CharField(max_length=255, null=True)
    puesto = models.CharField(max_length=30, null=True)
    costo_hora_total = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    costo_mensual_total = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    createdon = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)

class FinanzasParametros(models.Model):
    iibb_bsas = models.DecimalField(max_digits=4, decimal_places=2, blank=True)
    iibb_mza = models.DecimalField(max_digits=4, decimal_places=2, blank=True)
    hig_seg = models.DecimalField(max_digits=4, decimal_places=2, blank=True)
    costo_deuda = models.DecimalField(max_digits=4, decimal_places=2, blank=True)
    tasa_anual = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    costo_funcionamiento = models.DecimalField(max_digits=20, decimal_places=2, blank=True)
    perc_propio = models.DecimalField(max_digits=4, decimal_places=2, blank=True)
    perc_cliente = models.DecimalField(max_digits=4, decimal_places=2, blank=True)
    ventas_estimadas_propio = models.DecimalField(max_digits=20, decimal_places=2, blank=True)
    ventas_estimadas_cliente = models.DecimalField(max_digits=20, decimal_places=2, blank=True)
    compras_estimadas_propio = models.DecimalField(max_digits=20, decimal_places=2, blank=True)
    createdon = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)

class FinanzasParametrosForm(ModelForm):
    class Meta:
        model = FinanzasParametros
        fields = '__all__'

class ProduccionParametros(models.Model):
    gral_rotura_maquina = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    gral_rotura_horno = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    gral_malos_color_lavadero = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    gral_prod_mens_bsas = models.IntegerField(blank=True)
    gral_prod_mens_mza = models.IntegerField(blank=True)
    screen_cant_art = models.IntegerField(blank=True)
    screen_tpo_cambio = models.DecimalField(max_digits=4, decimal_places=2, blank=True)
    screen_medida = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    screen_fab_hora = models.IntegerField(blank=True)
    persmaq_maquinistas = models.IntegerField(blank=True)
    persmaq_horno = models.IntegerField(blank=True)
    persmaq_autoelevador = models.DecimalField(max_digits=3, decimal_places=2, blank=True) # Es un factor de utilización: toma valor entre 0 y 1
    persmaq_personal_asa = models.IntegerField(blank=True)
    persmaq_vel_calco = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    horno_vel_tejido_1 = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    horno_vel_tejido_2 = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    sopl_maquinistas = models.IntegerField(blank=True)
    sopl_operarios = models.IntegerField(blank=True)
    sopl_tpo_setup = models.DecimalField(max_digits=4, decimal_places=2, blank=True)
    sopl_perc_pint = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    sopl_perc_solv = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    sopl_perc_adit = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    sopl_rotura = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    sopl_lavadero = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    lav_limp_ser = models.IntegerField(blank=True)
    lav_limp_sopl = models.IntegerField(blank=True)
    ins_unid_film = models.IntegerField(blank=True)
    ins_unid_cinta = models.IntegerField(blank=True)
    dis_cant_bsas = models.IntegerField(blank=True)
    dis_cant_mza = models.IntegerField(blank=True)
    createdon = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)

class ProduccionParametrosForm(ModelForm):
    class Meta:
        model = ProduccionParametros
        fields = '__all__'

class SopleteadoParametros(models.Model):
    tipo_articulo = models.CharField(max_length=255, blank=True, default="-")
    consumo = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    velocidad = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    createdon = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)

class Clientes(models.Model):
    cliente = models.CharField(max_length=255, unique=True)
    createdon = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)

class CotizadorSerigrafia(models.Model):
    # SERIGRAFIA # (19 campos - calidad no se usa)
    srg_quemado = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    srg_hh_cambio_screen = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    srg_hh_decoracion = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    srg_hh_horno = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    srg_mp_screen = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    srg_hh_screen_cop = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    srg_luz_gas = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    srg_mp_pintura = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    srg_sampista = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    srg_rot_impresion = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    srg_rot_horno = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    srg_lavado = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    srg_calco_vitrificable = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    srg_mp_cinta_stretch = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    srg_logistica = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    srg_mantenimiento = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    srg_calidad = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    srg_setup = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    srg_disenio_pelicula = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    # srg_costo_mp = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    # srg_costo_produccion = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    # srg_costo_funcionamiento = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    # srg_costo_total = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    # srg_costo_unitario_fab = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    # COATING # (9 campos)
    ctg_setup = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    ctg_hh_sopleteadora = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    ctg_luz_gas = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    ctg_mp_pintura = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    ctg_sampista = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    ctg_rotura = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    ctg_lavado = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    ctg_mp_cinta_stretch = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    ctg_mo_indirecta = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    # ctg_costo_mp = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    # ctg_costo_produccion = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    # ctg_costo_funcionamiento = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    # ctg_costo_total = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    # ctg_costo_unitario_fab = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    # GENERALES
    mp_articulo = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    codigo_caja = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    embalaje = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    transporte = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    costo_mp = models.DecimalField(max_digits=20, decimal_places=2, default = 0)
    costo_produccion = models.DecimalField(max_digits=20, decimal_places=2)
    costo_funcionamiento_articulo = models.DecimalField(max_digits=20, decimal_places=2, default = 0)
    costo_funcionamiento_decorado = models.DecimalField(max_digits=20, decimal_places=2, default = 0)
    costo_funcionamiento_total = models.DecimalField(max_digits=20, decimal_places=2, default = 0)
    costo_total = models.DecimalField(max_digits=20, decimal_places=2, default = 0)
    costo_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    costo_unitario_fab = models.DecimalField(max_digits=10, decimal_places=2, default = 0)
    costo_unitario_fab_articulo = models.DecimalField(max_digits=10, decimal_places=2, default = 0)
    costo_unitario_fab_decorado = models.DecimalField(max_digits=10, decimal_places=2, default = 0)
    costo_unitario_15 = models.DecimalField(max_digits=20, decimal_places=2, default = 0)
    costo_unitario_30 = models.DecimalField(max_digits=20, decimal_places=2, default = 0)
    costo_unitario_45 = models.DecimalField(max_digits=20, decimal_places=2, default = 0)
    costo_unitario_60 = models.DecimalField(max_digits=20, decimal_places=2, default = 0)
    createdon = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)

class CosteoSerigrafia(models.Model):
    # GENERAL 1/2#
    createdon = models.DateTimeField(auto_now_add=True)
    cliente = models.ForeignKey(Clientes, on_delete=models.DO_NOTHING)
    proyecto = models.CharField(max_length=255, default=None, blank=True, null=True)
    tipo_2 = models.CharField(max_length=255, default = "-", blank=True, null=True)
    articulo = models.CharField(max_length=255)
    art_propio = models.BooleanField() # True "articulo propio", False "articulo de terceros"
    cant_unidades = models.IntegerField() # Unidades a producir
    # SERIGRAFIA #
    maquina_auto = models.BooleanField(blank=True, null=True) # True "automatica", False "manual"
    velocidad = models.IntegerField(blank=True, null=True)
    cant_personal = models.IntegerField(blank=True, null=True) # Cantidad de personas en maquina
    horno = models.IntegerField(blank=True, null=True) # Cantidad horno
    quemado = models.BooleanField(blank=True, null=True) # True "hay quemado", False "no hay quemado"
    disenio = models.BooleanField(blank=True, null=True) # True "nuevo", False "repetido"
    disenio_perc = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True) # Porcentaje de nuevo diseño
    tipo_decorado = models.CharField(max_length=255, blank=True, null=True) # Tinta Vitrificable, Tinta epoxi, Tinta UV, Calco Vitrificable
    cant_colores = models.IntegerField(blank=True, null=True) # Cant colores serigrafia
    pintura_1 = models.CharField(max_length=255, blank=True, null=True)
    dibujo_1 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    relieve_1 = models.CharField(max_length=255, blank=True, null=True)
    pintura_2 = models.CharField(max_length=255, blank=True, null=True)
    dibujo_2 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    relieve_2 = models.CharField(max_length=255, blank=True, null=True)
    pintura_3 = models.CharField(max_length=255, blank=True, null=True)
    dibujo_3 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    relieve_3 = models.CharField(max_length=255, blank=True, null=True)
    pintura_4 = models.CharField(max_length=255, blank=True, null=True)
    dibujo_4 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    relieve_4 = models.CharField(max_length=255, blank=True, null=True)
    pintura_5 = models.CharField(max_length=255, blank=True, null=True)
    dibujo_5 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    relieve_5 = models.CharField(max_length=255, blank=True, null=True)
    pintura_6 = models.CharField(max_length=255, blank=True, null=True)
    dibujo_6 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    relieve_6 = models.CharField(max_length=255, blank=True, null=True)
    pintura_7 = models.CharField(max_length=255, blank=True, null=True)
    dibujo_7 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    relieve_7 = models.CharField(max_length=255, blank=True, null=True)
    pintura_8 = models.CharField(max_length=255, blank=True, null=True)    
    dibujo_8 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    relieve_8 = models.CharField(max_length=255, blank=True, null=True)
    costo_calco = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    # COATING #
    ctg_cant_colores = models.IntegerField(blank=True, null=True)
    ctg_tipo = models.CharField(max_length=255, blank=True, null=True)
    ctg_cant_pasadas = models.IntegerField(blank=True, null=True) 
    ctg_color_1 = models.CharField(max_length=255, blank=True, null=True)
    ctg_cantidad_1 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ctg_color_2 = models.CharField(max_length=255, blank=True, null=True)
    ctg_cantidad_2 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ctg_color_3 = models.CharField(max_length=255, blank=True, null=True)
    ctg_cantidad_3 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ctg_color_4 = models.CharField(max_length=255, blank=True, null=True)
    ctg_cantidad_4 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ctg_color_5 = models.CharField(max_length=255, blank=True, null=True)
    ctg_cantidad_5 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ctg_color_6 = models.CharField(max_length=255, blank=True, null=True)
    ctg_cantidad_6 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    # GENERALES 2/2 #
    codigo = models.CharField(max_length=255, blank=True, null=True) # Código, Caja, Código + Caja
    embalaje = models.CharField(max_length=255, blank=True, null=True)
    muestra = models.BooleanField(blank=True, null=True) # True "si hay muestra", False "no hay muestra"
    transporte = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    com_ventas = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True, default=0)
    com_otras = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True, default=0)
    iibb_bsas = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True, default=0)
    iibb_mza = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True, default=0)
    hig_seg = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True, default=0)
    tipo_cotiz = models.CharField(max_length=255, default=0) # 1 "Serigrafia" , 2 "Coating", 3 "Serigrafia + Coating"
    cotizacion = models.ForeignKey(CotizadorSerigrafia, on_delete=models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)

class CosteoSerigrafiaForm(ModelForm):
    class Meta:
        model = CosteoSerigrafia
        fields = '__all__'

class CotizadorSerigrafiaForm(ModelForm):
    class Meta:
        model = CotizadorSerigrafia
        fields = '__all__'

class CotizadorHistoricoFilters(models.Model):
    fecha_desde = models.DateField(blank=True, null=True)
    fecha_hasta = models.DateField(blank=True, null=True)
    articulo = models.CharField(max_length=255, unique=True, blank=True, null=True)
    tipo_2 = models.CharField(max_length=255, blank=True, null=True)
    tipo_cotiz = models.CharField(max_length=255, default=0, blank=True, null=True) # 1 "Serigrafia" , 2 "Coating", 3 "Serigrafia + Coating"
    created_by = models.CharField(max_length=255, blank=True, null=True)
    cliente = models.CharField(max_length=255, blank=True, null=True)
    _id = models.IntegerField(blank=True, null=True)

class CotizadorHistoricoFiltersForm(ModelForm):
    class Meta:
        model = CotizadorHistoricoFilters
        fields = '__all__'

class NuevoClienteForm(ModelForm):
    class Meta:
        model = Clientes
        fields = ['cliente']