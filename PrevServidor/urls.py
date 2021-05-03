from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from apps.advogado.views import AdvogadosViewSet, ListaAdvogadosByEscritorio
from apps.escritorios.views.viewSerializer import EscritorioViewSet
from apps.ferramentas.views import ConvMonViewSet, TetosPrevViewSet

rotas = routers.DefaultRouter()
rotas.register('advogados', AdvogadosViewSet, basename='Advogados')
rotas.register('escritorio', EscritorioViewSet, basename='Escritorio')
rotas.register('convMon', ConvMonViewSet, basename='ConversaoMonetaria')
rotas.register('tetosPrev', TetosPrevViewSet, basename='TetosPrevidenciarios')

urlpatterns = [
    path('', include('apps.escritorios.urls')),
    path('admin/', admin.site.urls),
    path('explorer-api/', include(rotas.urls)),
    path('explorer-api/escritorio/<int:pk>/advogado', ListaAdvogadosByEscritorio.as_view()),
]
