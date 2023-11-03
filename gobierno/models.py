from django.db import models
from wagtail.api.v2.filters import OrderingFilter, FieldsFilter

class Manager(models.Model):
    OPTIONS_ROL = (
        ("SUPERINTENDENT","Super-intendente"),
        ("DIRECTOR","Director"),
        ("RESIDENT","Residente"),
        ("SUPERVISOR","Supervisor"),
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
    
    filter_backends = [
        FieldsFilter,
        OrderingFilter
    ]
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Responsable"
        verbose_name_plural = "Listado de responsables"

class Material(models.Model):
    OPTIONS_METHOD = (
        ("bulk","Granel"),
        ("l","Litros"),
        ("kg","Kilogramos"),
        ("package","Bultos/Costales"),
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

    filter_backends = [
        FieldsFilter,
        OrderingFilter
    ]
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Nota"
        verbose_name_plural = "Listado de notas"

class Building(models.Model):
    name = models.CharField(
        max_length=32,
        blank=False,
        verbose_name="Nombre del plano",
    )
    
    blueprint = models.FileField(
        upload_to='gobierno/building/blueprints/',
        blank=False,
        verbose_name="Archivo de plano",
    )

    desc = models.TextField(
        max_length=1024,
        blank=False,
        verbose_name="Explicación detallada acerca del plano (Obligatorio)",
    )

    filter_backends = [
        FieldsFilter,
        OrderingFilter
    ]
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Plano"
        verbose_name_plural = "Listado de planos"

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

    filter_backends = [
        FieldsFilter,
        OrderingFilter
    ]
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Nota"
        verbose_name_plural = "Listado de notas"