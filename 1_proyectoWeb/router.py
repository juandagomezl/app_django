from data_Api.viewsets import Datos_clientesViewset
from rest_framework import routers


router = routers.DefaultRouter()
router.register('datos_clientes', Datos_clientesViewset)


