from wagtail.snippets.views.snippets import SnippetViewSetGroup
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet

from .models import Place,Users

class PlaceMenu(SnippetViewSet):
    model = Place

    # model = Place
    # base_url_path = ''
    # menu_label = 'Edificio'
    # menu_icon = ''
    # add_to_settings_menu = False
    # exclude_from_explorer = True
    # add_to_admin_menu = True

class UsersMenu(SnippetViewSet):
    model = Users
    # base_url_path = ''
    # menu_label = 'Usuarios'
    # menu_icon = ''
    # add_to_settings_menu = False
    # exclude_from_explorer = True
    # add_to_admin_menu = True

class CatalogoMenu(SnippetViewSetGroup):
    menu_label = 'Catálogo'
    menu_icon = 'folder-open-inverse'  
    items = (
        PlaceMenu,
        UsersMenu,
    )

register_snippet(CatalogoMenu)