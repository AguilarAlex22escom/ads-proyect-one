from django.db import models
from modelcluster.models import ClusterableModel
from wagtail.api.v2.filters import OrderingFilter, FieldsFilter
#Creación de clases

class Place(ClusterableModel):
    name = models.CharField(
        default="Sin nombre",
        max_length=32,
        null=True,
        verbose_name="Nombre del edificio",
    )
    desc = models.TextField(
        default="Sin descripción",
        max_length=64,
        null=True,
        verbose_name="Notas adicionales",
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
        verbose_name="Nombre",
    )
    last_name = models.CharField(
        max_length=32,
        null=False,
        verbose_name="Apellido paterno",
    )
    maternal_last_name = models.CharField(
        max_length=32,
        null=False,
        verbose_name="Apellido materno",
    )
    rfc = models.CharField(
        max_length=13,
        null=False,
        unique=True,
        verbose_name="R.F.C.",
    )
    email = models.CharField(
        max_length=32,
        null=False,
        verbose_name="Correo eléctronico",
    )
    birthdate = models.DateField(
        null=False,
        verbose_name="Fecha de cumpleaños",
    )
    gender = models.CharField(
        max_length=32,
        choices=OPTIONS_GENDER,
        default="Patata",
        verbose_name="Género",
    )
    marital_status = models.CharField(
        max_length=32,
        choices=OPTIONS_MARITAL_STATUS,
        default="Aceite de oliva",
        verbose_name="Estado civil",
    )
    phone = models.CharField(
        max_length=10,
        null=False,
        verbose_name="Número de teléfono",
    )
    clabe = models.CharField(
        max_length=32,
        null=False,
        verbose_name="CLABE bancaria",
    )
    salary = models.IntegerField(
        default=0,
        null=False,
        verbose_name="Salario",
    )
    rol = models.CharField(
        max_length=32,
        choices=OPTIONS_ROL,
        default="Sin definir",
        verbose_name="Puesto de trabajo",
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