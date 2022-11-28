from rest_framework import routers
from api.views import CompanyViewSet, EmployeeViewSet
from django.urls import path,include


router = routers.DefaultRouter()
router.register(r'companies',CompanyViewSet)
router.register(r'employee',EmployeeViewSet)


urlpatterns = [
    path('', include(router.urls)),
]