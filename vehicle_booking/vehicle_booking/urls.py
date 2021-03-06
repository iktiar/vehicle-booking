"""vehicle_booking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from rest_framework import routers
from vehicle.views import ListVehicles, ListDrivers, ListRequisitionTicketLogs, ListRequisitionTicketLogForAdmin
from django.contrib import admin

#router = routers.DefaultRouter()
#router.register(r'users', views.UserViewSet)
#router.register(r'groups', views.GroupViewSet)

#API using automatic URL routing.
# login urls for browsable API.

urlpatterns = [
    #url(r'^', include(router.urls)),

    url(r'^api/car-requisition-admin', ListRequisitionTicketLogForAdmin.as_view(), name='list_requisition_ticket_for_admin'),
    url(r'^api/car-requisition', ListRequisitionTicketLogs.as_view(), name='list_requisition_ticket'),
    url(r'^api/vehicle', ListVehicles.as_view(), name='list_vehicles'),
    url(r'^api/driver', ListDrivers.as_view(), name='list_drivers'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
]
