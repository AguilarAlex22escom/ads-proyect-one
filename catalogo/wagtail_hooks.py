from wagtail.contrib.modeladmin.options import (
    ModelAdmin, ModelAdminGroup, modeladmin_register)

from .models import Place,Users

class PlaceMenu(ModelAdmin):
    model = Place
    base_url_path = ''
    menu_label = 'Edificio'
    menu_icon = ''
    add_to_settings_menu = False
    exclude_from_explorer = True
    add_to_admin_menu = True

class UsersMenu(ModelAdmin):
    model = Users
    base_url_path = ''
    menu_label = 'Usuarios'
    menu_icon = ''
    add_to_settings_menu = False
    exclude_from_explorer = True
    add_to_admin_menu = True

class CatalogoMenu(ModelAdminGroup):
    menu_label = 'Catálogo'
    menu_icon = 'folder-open-inverse'  
    items = (
        PlaceMenu,
        UsersMenu,
    )

modeladmin_register(CatalogoMenu)