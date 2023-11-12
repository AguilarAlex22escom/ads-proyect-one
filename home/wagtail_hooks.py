from wagtail import hooks
from wagtail.snippets.views.snippets import SnippetViewSetGroup
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet

from catalogo.models import Place
from catalogo.models import Users
from catalogo.models import JobRole
from catalogo.models import StaffFile as CatStaffFile

from gobierno.models import File as GobFile
from gobierno.models import General as GobGeneral
from gobierno.models import Manager as GobManager
from gobierno.models import Overview as GobOverview
from gobierno.models import Material as GobMaterial
from gobierno.models import Building as GobBuilding


#########################
#        Catalogo       #
#########################
# Definiciones sobre el catalogo
class PlaceMenu(SnippetViewSet):
    model = Place


class UsersMenu(SnippetViewSet):
    model = Users
    menu_label = "Empleados"
    list_export = [
        'name',
        'birthdate',
    ]


class JobRoleMenu(SnippetViewSet):
    model = JobRole


class CatStaffFileMenu(SnippetViewSet):
    model = CatStaffFile
    menu_label = "Archivo de empleados"

#########################
#        Gobierno       #
#########################
# Definiciones sobre el edificio de gobierno
class GobFileMenu(SnippetViewSet):
    model = GobFile
    menu_label = "Subir documento"


class GobGeneralMenu(SnippetViewSet):
    model = GobGeneral
    menu_label = "Presupuestos"


class GobManagerMenu(SnippetViewSet):
    model = GobManager
    menu_label = "Responsables"


class GobMaterialMenu(SnippetViewSet):
    model = GobMaterial
    menu_label = "Materiales"


class GobBuildingMenu(SnippetViewSet):
    model = GobBuilding
    menu_label = "Construcción"


class GobOverviewMenu(SnippetViewSet):
    model = GobOverview
    menu_label = "Notas"


#########################
#         Menus         #
#########################
# Definición del menú del edificio de gobierno
class GobMenu(SnippetViewSetGroup):
    menu_label = "E. Gobierno"
    items = [
        GobFileMenu,
        GobGeneralMenu,
        GobManagerMenu,
        GobMaterialMenu,
        GobBuildingMenu,
        GobOverviewMenu,
    ]


# Definición del menú catalogo
class CatalogoMenu(SnippetViewSetGroup):
    menu_label = "Catálogo"
    menu_icon = "folder-open-inverse"
    items = [
        UsersMenu,
        CatStaffFileMenu,
    ]


register_snippet(CatalogoMenu)
register_snippet(GobMenu)


@hooks.register("construct_main_menu")
def hide_snippets_menu_item(request, menu_items):
    # for menu in menu_items:
    #     print(menu.name)
    # print(menu_items)
    menu_items[:] = [
        item
        for item in menu_items
        if item.name in ["images", "documents", "catalogo", "censos", "e-gobierno"]
    ]
    # menu_items[:] = [item for item in menu_items if item.name in ['images','documents','catalogo','censos','settings'] ]
