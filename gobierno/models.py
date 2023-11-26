from django.db import models
from django.db.models.signals import pre_save, post_save

from django.core.validators import MinValueValidator, MaxValueValidator

from django.dispatch import receiver

from rest_framework.renderers import JSONRenderer
from rest_framework.fields import Field

from wagtail.api.v2.views import PagesAPIViewSet
from wagtail.api import APIField
from wagtail.api.v2.views import BaseAPIViewSet
from wagtail.api.v2.filters import OrderingFilter, FieldsFilter


#########################
# Clase: Archivo        #
#########################
class File(models.Model):
    file = models.FileField(
        blank=False,
        upload_to="media/doc/",
        verbose_name="Ingrese el documento para autollenar todos los formularios",
    )

    registration_date = models.DateField(
        blank=True,
        editable=False,
    )

    def __str__(self):
        return "Versión del proyecto: " + self.registration_date

    class Meta:
        verbose_name = "Archivo"
        verbose_name_plural = "Listado de archivos"


@receiver(pre_save, sender=File)
def CheckData(sender, instance, **kwargs):
    pass


@receiver(post_save, sender=File)
def SaveData(sender, instance, **kwargs):
    pass


#########################
# Clase: General        #
#########################
class General(models.Model):
    electrical_buget = models.IntegerField(
        blank=False,
        default=0,
        verbose_name="Presupuesto de la instalación eléctrica",
    )

    water_budget = models.IntegerField(
        blank=False,
        default=0,
        verbose_name="Presupuesto para instalación hidrica",
    )

    mobilary_budget = models.IntegerField(
        blank=False,
        default=0,
        verbose_name="Presupuesto para inmobiliario",
    )

    floor_budget = models.IntegerField(
        blank=False,
        default=0,
        verbose_name="Presupuesto para el suelo",
    )

    release_date = models.DateField(
        blank=False,
        verbose_name="Fecha estimada de entrega",
    )

    registration_date = models.DateField(
        blank=True,
    )

    filter_backends = [FieldsFilter, OrderingFilter]

    def __str__(self):
        return "Versión del proyecto: " + self.registration_date

    class Meta:
        verbose_name = "Registo de presupuesto"
        verbose_name_plural = "Listado de presupuestos"


class GeneralAPIViewSet(BaseAPIViewSet):
    # renderer_classes = [JSONRenderer]
    body_fields = BaseAPIViewSet.body_fields + [
        "electrical_buget",
        "water_budget",
        "mobilary_budget",
        "floor_budget",
        "release_date",
        "registration_date",
    ]
    listing_default_fields = BaseAPIViewSet.listing_default_fields + [
        "electrical_buget",
        "water_budget",
        "mobilary_budget",
        "floor_budget",
        "release_date",
        "registration_date",
    ]

    filter_backends = [FieldsFilter, OrderingFilter]

    name = "gobierno_general"
    model = General


#########################
# Clase: Manager        #
#########################
class Manager(models.Model):
    OPTIONS_ROL = (
        ("SUPERINTENDENT", "Super-intendente"),
        ("DIRECTOR", "Director"),
        ("RESIDENT", "Residente"),
        ("SUPERVISOR", "Supervisor"),
    )

    name = models.ForeignKey(
        "catalogo.Users",
        on_delete=models.CASCADE,
        verbose_name="Nombre",
    )

    job = models.ForeignKey(
        "catalogo.JobRole",
        on_delete=models.CASCADE,
        verbose_name="Puesto de trabajo",
    )

    rol = models.CharField(
        max_length=32,
        choices=OPTIONS_ROL,
        default="Sin definir",
        verbose_name="Nivel de jerarquía",
    )

    desc = models.TextField(
        max_length=512,
        default="",
        blank=True,
        verbose_name="Descripcción sobre el responsable",
    )

    filter_backends = [FieldsFilter, OrderingFilter]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Responsable"
        verbose_name_plural = "Listado de responsables"


class ManagerAPIViewSet(BaseAPIViewSet):
    body_fields = BaseAPIViewSet.body_fields + [
        "name",
        "job",
        "rol",
        "desc",
    ]
    listing_default_fields = BaseAPIViewSet.listing_default_fields + [
        "name",
        "job",
        "rol",
        "desc",
    ]

    filter_backends = [FieldsFilter, OrderingFilter]

    name = "gobierno_manager"
    model = Manager


#########################
# Clase: Material       #
#########################
class Material(models.Model):
    OPTIONS_METHOD = (
        ("bulk", "Granel"),
        ("l", "Litros"),
        ("kg", "Kilogramos"),
        ("package", "Bultos/Costales"),
    )

    name = models.CharField(
        max_length=32,
        default="",
        blank=False,
        verbose_name="Nombre del material",
    )

    quantity = models.IntegerField(
        default=0,
        blank=False,
        verbose_name="Cantidad disponible",
    )

    price = models.IntegerField(
        default=0,
        blank=False,
        verbose_name="Precio unitario",
    )

    method = models.CharField(
        max_length=32,
        choices=OPTIONS_METHOD,
        blank=False,
        verbose_name="Tipo de venta",
    )

    desc = models.TextField(
        max_length=512,
        default="",
        blank=True,
        verbose_name="Descripcción del material",
    )

    filter_backends = [FieldsFilter, OrderingFilter]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Nota"
        verbose_name_plural = "Listado de notas"


class MaterialAPIViewSet(BaseAPIViewSet):
    body_fields = BaseAPIViewSet.body_fields + [
        "name",
        "quantity",
        "price",
        "method",
        "desc",
    ]
    listing_default_fields = BaseAPIViewSet.listing_default_fields + [
        "name",
        "quantity",
        "price",
        "method",
        "desc",
    ]

    filter_backends = [FieldsFilter, OrderingFilter]

    name = "gobierno_material"
    model = Material


#########################
# Clase: Materiales     #
#########################
class Ladrillo(models.Model):
    name = models.CharField(
        default="Ladrillo",
        max_length=16,
        editable=False,
        unique=True,
    )

    quantity = models.IntegerField(
        blank=False,
        default=0,
    )

    used = models.IntegerField(
        blank=True,
        default=0,
    )

    filter_backends = [FieldsFilter, OrderingFilter]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ladrillo"
        verbose_name_plural = "Listado de Ladrillos"


class LadrilloAPIViewSet(BaseAPIViewSet):
    body_fields = BaseAPIViewSet.body_fields + [
        "name",
        "quantity",
        "used",
    ]
    listing_default_fields = BaseAPIViewSet.listing_default_fields + [
        "name",
        "quantity",
        "used",
    ]

    filter_backends = [FieldsFilter, OrderingFilter]

    name = "gobierno_ladrillo"
    model = Ladrillo


#########################
class Mezcla(models.Model):
    name = models.CharField(
        default="Mezcla",
        max_length=16,
        editable=False,
        unique=True,
    )

    quantity = models.IntegerField(
        blank=False,
        default=0,
    )

    used = models.IntegerField(
        blank=True,
        default=0,
    )

    filter_backends = [FieldsFilter, OrderingFilter]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Mezcla"
        verbose_name_plural = "Listado de mezcla"


class MezclaAPIViewSet(BaseAPIViewSet):
    body_fields = BaseAPIViewSet.body_fields + [
        "name",
        "quantity",
        "used",
    ]
    listing_default_fields = BaseAPIViewSet.listing_default_fields + [
        "name",
        "quantity",
        "used",
    ]

    filter_backends = [FieldsFilter, OrderingFilter]

    name = "gobierno_mezcla"
    model = Mezcla


#########################
class Cable(models.Model):
    name = models.CharField(
        default="Cable",
        max_length=16,
        editable=False,
        unique=True,
    )

    quantity = models.IntegerField(
        blank=False,
        default=0,
    )

    used = models.IntegerField(
        blank=True,
        default=0,
    )

    filter_backends = [FieldsFilter, OrderingFilter]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Cable"
        verbose_name_plural = "Listado de cable"


class CableAPIViewSet(BaseAPIViewSet):
    body_fields = BaseAPIViewSet.body_fields + [
        "name",
        "quantity",
        "used",
    ]
    listing_default_fields = BaseAPIViewSet.listing_default_fields + [
        "name",
        "quantity",
        "used",
    ]

    filter_backends = [FieldsFilter, OrderingFilter]

    name = "gobierno_cable"
    model = Cable


#########################
# Clase: Building       #
#########################
class Building(models.Model):
    name = models.CharField(
        max_length=32,
        blank=False,
        verbose_name="Nombre del plano",
    )

    blueprint = models.FileField(
        upload_to="gobierno/building/blueprints/",
        blank=False,
        verbose_name="Archivo de plano",
    )

    desc = models.TextField(
        max_length=1024,
        blank=False,
        verbose_name="Explicación detallada acerca del plano (Obligatorio)",
    )

    filter_backends = [FieldsFilter, OrderingFilter]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Plano"
        verbose_name_plural = "Listado de planos"


class BuildingAPIViewSet(BaseAPIViewSet):
    body_fields = BaseAPIViewSet.body_fields + [
        "name",
        "blueprint",
        "desc",
    ]
    listing_default_fields = BaseAPIViewSet.listing_default_fields + [
        "name",
        "blueprint",
        "desc",
    ]

    filter_backends = [FieldsFilter, OrderingFilter]

    name = "gobierno_building"
    model = Building


#########################
# Clase: Overview       #
#########################
class Overview(models.Model):
    name = models.CharField(
        max_length=32,
        default="",
        blank=False,
        verbose_name="Breve descripcción de la nota",
    )

    desc = models.TextField(
        max_length=512,
        default="",
        blank=True,
        verbose_name="Descripcción completa sobre la nota",
    )

    filter_backends = [FieldsFilter, OrderingFilter]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Nota"
        verbose_name_plural = "Listado de notas"


class OverviewAPIViewSet(BaseAPIViewSet):
    body_fields = BaseAPIViewSet.body_fields + [
        "name",
        "desc",
    ]
    listing_default_fields = BaseAPIViewSet.listing_default_fields + [
        "name",
        "desc",
    ]

    filter_backends = [FieldsFilter, OrderingFilter]

    name = "gobierno_overview"
    model = Overview


#########################
# Clase: Metadata       #
#########################
class Metadata(models.Model):
    name = models.CharField(
        max_length=32,
        blank=False,
        unique=True,
    )

    general_budget = models.IntegerField(
        default=0,
        blank=True,
    )

    material_budget = models.IntegerField(
        default=0,
        blank=True,
    )

    general_progress = models.IntegerField(
        default=0,
        blank=False,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100),
        ],
    )

    cimentacion_progress = models.IntegerField(
        default=0,
        blank=False,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100),
        ],
    )

    aplanado_progress = models.IntegerField(
        default=0,
        blank=False,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100),
        ],
    )

    electrica_progress = models.IntegerField(
        default=0,
        blank=False,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100),
        ],
    )

    hidrica_progress = models.IntegerField(
        default=0,
        blank=False,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100),
        ],
    )

    detalles_progress = models.IntegerField(
        default=0,
        blank=False,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100),
        ],
    )

    mobiliario_progress = models.IntegerField(
        default=0,
        blank=False,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100),
        ],
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Metadata"
        verbose_name_plural = "Metadatas"


class MetadataAPIViewSet(BaseAPIViewSet):
    body_fields = BaseAPIViewSet.body_fields + [
        "name",
        "general_progress",
        "general_budget",
        "material_budget",
        "cimentacion_progress",
        "aplanado_progress",
        "electrica_progress",
        "hidrica_progress",
        "detalles_progress",
        "mobiliario_progress",
    ]
    listing_default_fields = BaseAPIViewSet.listing_default_fields + [
        "name",
        "general_progress",
        "general_budget",
        "material_budget",
        "cimentacion_progress",
        "aplanado_progress",
        "electrica_progress",
        "hidrica_progress",
        "detalles_progress",
        "mobiliario_progress",
    ]

    filter_backends = [FieldsFilter, OrderingFilter]

    name = "gobierno_metadata"
    model = Metadata
