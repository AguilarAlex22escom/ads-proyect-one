from wagtail.snippets.views.snippets import SnippetViewSetGroup
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet

from catalogo.models import Place,Users,JobRole

from gobierno.models import Manager as GobManager
from gobierno.models import Overview as GobOverview
from gobierno.models import Material as GobMaterial
from gobierno.models import Building as GobBuilding

#########################
#        Catalogo       #
#########################
#Definiciones sobre el catalogo
class PlaceMenu(SnippetViewSet):
    model = Place

class UsersMenu(SnippetViewSet):
    model = Users

class JobRoleMenu(SnippetViewSet):
    model = JobRole

#########################
#        Gobierno       #
#########################
#Definiciones sobre el edificio de gobierno
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
#Definición del menú del edificio de gobierno
class GobMenu(SnippetViewSetGroup):
    menu_label = "E. Gobierno"
    items = [
        GobManagerMenu,
        GobMaterialMenu,
        GobBuildingMenu,
        GobOverviewMenu,
    ]

#Definición del menú catalogo
class CatalogoMenu(SnippetViewSetGroup):
    menu_label = 'Catálogo'
    menu_icon = 'folder-open-inverse'  
    items = [
        PlaceMenu,
        UsersMenu,
        JobRoleMenu,
    ]

register_snippet(CatalogoMenu)
register_snippet(GobMenu)