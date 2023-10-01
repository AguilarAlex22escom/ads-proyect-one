from django.db import models
from modelcluster.models import ClusterableModel
from wagtail.admin.panels import FieldPanel
from wagtail.api import APIField
from wagtail.api.v2.views import BaseAPIViewSet
from wagtail.api.v2.filters import OrderingFilter, FieldsFilter
#Creación de clases

class Place(ClusterableModel):
    name = models.CharField(
        default="Sin nombre",
        max_length=32,
        null=True,
        verbose_name="",
    )
    desc = models.TextField(
        default="Sin descripción",
        max_length=64,
        null=True
    )

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Edificio"
        verbose_name_plural = "Edificios"

class Users(ClusterableModel):
    OPTIONS_GENDER = (
        ("MAN","Hombre"),
        ("WOMAN","Mujer"),
        ("HELICOPTERO DE GUERRA","Tanque táctico"),
    )
    OPTIONS_MARITAL_STATUS = (
        ("MARRIED","Casado/Casada/Quesadilla"),
        ("SINGLE","Soltero/Soltera/Soltere"),
        ("WIDOWER","Viudo/Viuda/Natasha"),
    )
    OPTIONS_ROL = (
        ("SUPERINTENDENT","Super-intendente"),
        ("DIRECTOR","Director"),
        ("RESIDENT","Residente"),
        ("SUPERVISOR","Supervisor"),
    )
    name = models.CharField(
        max_length=32,
        null=False,
    )
    last_name = models.CharField(
        max_length=32,
        null=False,
    )
    maternal_last_name = models.CharField(
        max_length=32,
        null=False,
    )
    rfc = models.CharField(
        max_length=13,
        null=False,
        unique=True,
    )
    email = models.CharField(
        max_length=32,
        null=False,
    )
    birthdate = models.DateField(
        null=False,
    )
    gender = models.CharField(
        max_length=32,
        choices=OPTIONS_GENDER,
        default="Patata",
    )
    marital_status = models.CharField(
        max_length=32,
        choices=OPTIONS_MARITAL_STATUS,
        default="Aceite de oliva",
    )
    phone = models.CharField(
        max_length=10,
        null=False,
    )
    clabe = models.CharField(
        max_length=32,
        null=False,
    )
    salary = models.IntegerField(
        default=0,
        null=False,
    )
    rol = models.CharField(
        max_length=32,
        choices=OPTIONS_ROL,
        default="Sin definir",
    )
    filter_backends = [
        FieldsFilter,
        OrderingFilter
    ]
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"