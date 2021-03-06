from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from apps.advogado.views import AdvogadosViewSet, ListaAdvogadosByEscritorio, AdvogadosConfirmacaoViewSet, AuthPrevClient
from apps.escritorios.views.viewSerializer import EscritorioViewSet
from apps.ferramentas.views import ConvMonViewSet, TetosPrevViewSet
from apps.informacoes.views import IndicadoresViewSet

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="NewPrev - Servidor",
      default_version='0.0.10',
      description="API Rest para consumo do programa Desktop NewPrev Cliente",
      terms_of_service="#",
      contact=openapi.Contact(email="newprev.projeto@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


rotas = routers.DefaultRouter()
rotas.register('advogados', AdvogadosViewSet, basename='Advogados')
rotas.register('escritorio', EscritorioViewSet, basename='Escritorio')
rotas.register('convMon', ConvMonViewSet, basename='ConversaoMonetaria')
rotas.register('tetosPrev', TetosPrevViewSet, basename='TetosPrevidenciarios')
rotas.register('indicadores', IndicadoresViewSet, basename='Indicadores')

urlpatterns = [
    path('', include('apps.escritorios.urls')),
    path('admin/', admin.site.urls),
    path('explorer/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/', include(rotas.urls)),
    path('api/escritorio/<int:pk>/advogado', ListaAdvogadosByEscritorio.as_view()),
    path('api/advogados/<int:pk>/confirmacao/', AdvogadosConfirmacaoViewSet.as_view()),
    path('api/advogados/auth/<str:login>', AuthPrevClient.as_view())
]
