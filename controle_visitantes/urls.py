from django.contrib import admin
from django.urls import path

from usuarios.views import index
from visitantes.views import  (
    registrar_visitante, informacoes_visitante
)


urlpatterns = [
    path("admin/", admin.site.urls),

    path(
        "",
        index,
        name="index",
    ),

    path(
        "registrar-visitante/",         # string que representa a url no navegador
        registrar_visitante,
        name="registrar_visitante",
    ),

    path(
        "visitantes/<int:id>/" ,                # variavel que será exibida no navegador com id de cada cliente
        informacoes_visitante,                       # função criada no arquivo views
        name="informacoes_visitante",        #mesmo nome da função
    )
]
