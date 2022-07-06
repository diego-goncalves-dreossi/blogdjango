from django.urls import path,include
from . import views

urlpatterns = [
    path('cadastro/', views.CadastroView.as_view(), name='cadastro')
]

# Login
# login e templates/registration/login.html se conectam com url path('contas/',include('django.contrib.auth.urls')),
# de blog.urls e com do blog.settings. É uma funcionalidade do próprio Django.
# # django.contrib.auth.urls
# Quando o login for efetuado com sucesso
# LOGIN_REDIRECT_URL = 'pagina_inicial'
# Deslogar
# LOGOUT_REDIRECT_URL = 'pagina_inicial'

