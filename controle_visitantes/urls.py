from django.contrib import admin
from django.urls import path

from django.contrib.auth import views as auth_views

from dashboard.views import index

from visitantes.views import  (
    registrar_visitante, informacoes_visitante, finalizar_visita
)


urlpatterns = [
    path("admin/", admin.site.urls),

    path(
        "login/",                                               # Dominio Login
        auth_views.LoginView.as_view(           #Chamando a Variavel auth_view - View padrão do django 
            template_name="login.html"           # Atributo do template
        ),
        name="login"                                       #nome da URL login
    ),

    path(
        "logout/",
        auth_views.LogoutView.as_view(
            template_name="logout.html"
        ),
        name="logout"
    ),

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
    ),

    path(
        "visitantes/<int:id>/finalizar-visita/",  #nova url passando/ a string, id e o trecho final da url/
        finalizar_visita,  #função
        name="finalizar_visita"
    )
]
