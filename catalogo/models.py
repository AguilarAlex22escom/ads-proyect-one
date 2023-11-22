import pandas as pd
import inspect
import io
from datetime import datetime

from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from modelcluster.models import ClusterableModel

from rest_framework.renderers import JSONRenderer
from rest_framework.fields import Field

from wagtail.api.v2.views import PagesAPIViewSet
from wagtail.api import APIField
from wagtail.api.v2.views import BaseAPIViewSet
from wagtail.api.v2.filters import OrderingFilter, FieldsFilter


# Creación de clases


#########################
# Clase: Edificio       #
#########################
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


#########################
# Clase: Arch. Empleados#
#########################
class StaffFile(models.Model):
    file = models.FileField(
        blank=False,
        upload_to="media/doc/",
        verbose_name="Ingrese el documento para autollenar todos los formularios",
    )

    def __str__(self):
        return "Versión del proyecto: " + str(self.file)

    class Meta:
        verbose_name = "Archivo de empleados"
        verbose_name_plural = "Listado de archivos de empleados"


@receiver(pre_save, sender=StaffFile)
def CheckData(sender, instance, **kwargs):
    doc = instance.file
    with io.BytesIO(doc.read()) as fh:
        df = pd.read_excel(
            fh,
            sheet_name="Empleados",
            engine="odf",
        )
        if (
            "Nombre" in df.columns
            and "Apellido paterno" in df.columns
            and "Apellido materno" in df.columns
            and "RFC" in df.columns
            and "Correo" in df.columns
            and "Fecha de nacimiento" in df.columns
            and "Género" in df.columns
            and "Estado civil" in df.columns
            and "Número de teléfono" in df.columns
            and "CLABE Bancaria" in df.columns
            and "Salario" in df.columns
            and "Puesto de trabajo" in df.columns
        ) == False:
            raise Exception("Faltan")
        # raise Exception("Todas")


@receiver(post_save, sender=StaffFile)
def SaveData(sender, instance, **kwargs):
    doc = instance.file
    with io.BytesIO(doc.read()) as fh:
        df = pd.read_excel(
            fh,
            sheet_name="Empleados",
            engine="odf",
        )
        df.fillna("")
        for idx, row in df.iterrows():
            obj = Users()
            obj.name = str(row["Nombre"])
            obj.last_name = str(row["Apellido paterno"])
            obj.maternal_last_name = str(row["Apellido materno"])
            obj.rfc = str(row["RFC"])
            obj.email = str(row["Correo"])
            obj.birthdate = row["Fecha de nacimiento"]
            obj.gender = str(row["Género"])
            obj.marital_status = str(row["Estado civil"])
            obj.phone = str(row["Número de teléfono"])
            obj.clabe = str(row["CLABE Bancaria"])
            obj.salary = str(row["Salario"])
            obj.rol = str(row["Puesto de trabajo"])
            if (
                str(row["Género"]) == "Hombre" or str(row["Género"]) == "Mujer"
            ) == False:
                return
            if (
                str(row["Estado civil"]) == "Casado(a)"
                or str(row["Estado civil"]) == "Soltero(a)"
            ) == False:
                return
            if (
                str(row["Puesto de trabajo"]) == "Super-intendente"
                or str(row["Puesto de trabajo"]) == "Director"
                or str(row["Puesto de trabajo"]) == "Residente"
                or str(row["Puesto de trabajo"]) == "Supervisor"
            ) == False:
                return
            obj.save()


#########################
# Clase: Empleados      #
#########################
class Users(ClusterableModel):
    OPTIONS_GENDER = (
        ("Hombre", "Hombre"),
        ("Mujer", "Mujer"),
    )
    OPTIONS_MARITAL_STATUS = (
        ("Casado(a)", "Casado(a)"),
        ("Soltero(a)", "Soltero(a)"),
    )
    OPTIONS_ROL = (
        ("Super-intendente", "Super-intendente"),
        ("Director", "Director"),
        ("Residente", "Residente"),
        ("Supervisor", "Supervisor"),
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
        verbose_name="Fecha de nacimiento",
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
        OrderingFilter,
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"


class UsersAPIViewSet(BaseAPIViewSet):
    renderer_classes = [JSONRenderer]
    body_fields = BaseAPIViewSet.body_fields + [
        "name",
        "last_name",
        "maternal_last_name",
        "rfc",
        "email",
        "birthdate",
        "gender",
        "marital_status",
        "phone",
        "clabe",
        "salary",
        "rol",
    ]
    listing_default_fields = BaseAPIViewSet.listing_default_fields + [
        "name",
        "last_name",
        "maternal_last_name",
        "rfc",
        "email",
        "birthdate",
        "gender",
        "marital_status",
        "phone",
        "clabe",
        "salary",
        "rol",
    ]

    filter_backends = [
        FieldsFilter,
        OrderingFilter,
    ]

    name = "users"
    model = Users


@receiver(pre_save, sender=Users)
def CheckData(sender, instance, **kwargs):
    pass


@receiver(post_save, sender=Users)
def SaveData(sender, instance, **kwargs):
    pass


#########################
# Clase: Frente de obra #
#########################
class JobRole(ClusterableModel):
    name = models.CharField(
        max_length=32,
        default="",
        verbose_name="Nombre",
    )

    desc = models.TextField(
        max_length=512,
        default="",
        verbose_name="Descripcción del puesto de trabajo",
    )

    filter_backends = [FieldsFilter, OrderingFilter]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Frente de obra"
        verbose_name_plural = "Listado de frentes de obra"
