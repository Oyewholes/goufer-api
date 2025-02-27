from rest_framework_nested import routers
from pprint import pprint

from user.errand_boy_views import ErrandBoyViewset
from user.vendor_views import VendorViewSet
from .views import CategoryViewSet, ErrandBoyDocumentViewSet, LocationViewSet, ReviewsViewSet, SubCategoryViewSet, VendorDocumentViewSet

router = routers.DefaultRouter()

# Parent routers
router.register('categories', CategoryViewSet, basename='çollections')
router.register('location', LocationViewSet, basename='location')
router.register('vendors', VendorViewSet, basename='vendor')
router.register('errandboys', ErrandBoyViewset, basename='errandboy')



# Child routers
category_router = routers.NestedDefaultRouter(router, 'categories', lookup='category')
category_router.register('subcategory', SubCategoryViewSet, basename='category_subcategory')

vendor_router = routers.NestedDefaultRouter(router, 'vendors', lookup='vendor')
vendor_router.register('document', VendorDocumentViewSet, basename='vendor_document')

errand_boy_router = routers.NestedDefaultRouter(router, 'errandboys', lookup='errandboy')
vendor_router.register('document', ErrandBoyDocumentViewSet, basename='errandboy_document')




urlpatterns = router.urls + category_router.urls + vendor_router.urls + errand_boy_router.urls

