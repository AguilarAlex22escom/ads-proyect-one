from wagtail.api.v2.views import PagesAPIViewSet
from wagtail.api.v2.router import WagtailAPIRouter
from wagtail.images.api.v2.views import ImagesAPIViewSet
from wagtail.documents.api.v2.views import DocumentsAPIViewSet

from catalogo.models import UsersAPIViewSet as CatUsersAPI

from gobierno.models import GeneralAPIViewSet as GobGeneralAPI
from gobierno.models import ManagerAPIViewSet as GobManagerAPI
from gobierno.models import MaterialAPIViewSet as GobMaterialAPI
from gobierno.models import BuildingAPIViewSet as GobBuildingAPI
from gobierno.models import OverviewAPIViewSet as GobOverviewAPI
from gobierno.models import MetadataAPIViewSet as GobMetadataAPI


# Create the router. "wagtailapi" is the URL namespace
api_router = WagtailAPIRouter('wagtailapi')

# Add the three endpoints using the "register_endpoint" method.
# The first parameter is the name of the endpoint (such as pages, images). This
# is used in the URL of the endpoint
# The second parameter is the endpoint class that handles the requests
api_router.register_endpoint('pages', PagesAPIViewSet)
api_router.register_endpoint('images', ImagesAPIViewSet)
api_router.register_endpoint('documents', DocumentsAPIViewSet)
api_router.register_endpoint("general", GobGeneralAPI)
api_router.register_endpoint("manager", GobManagerAPI)
api_router.register_endpoint("material", GobMaterialAPI)
api_router.register_endpoint("building", GobBuildingAPI)
api_router.register_endpoint("overview", GobOverviewAPI)
api_router.register_endpoint("metadata", GobMetadataAPI)
api_router.register_endpoint("users", CatUsersAPI)