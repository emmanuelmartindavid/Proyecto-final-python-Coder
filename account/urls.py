from django.urls import path, include
from account.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('editar/usuario', editar_usuario, name="accountEditarUsuario"),
    path('login/', login_account, name="accountLogin"),
    path('registrar/', register_account, name="accountRegister"),
    path('logout/', LogoutView.as_view(template_name="account/logout.html"), name="accountLogout"),
]
