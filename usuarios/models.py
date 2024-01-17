from typing import Any
from django.db import models
from django.contrib.auth.models import(
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)

class UsuarioManager(BaseUserManager):

    def create_user(self, email, password = None):
        usuario = self.model(
            email = self.normalize_email(email)   # O metodo normalize evita que o cadastro do e-mail utilize caracteres maiuculos
        )

        usuario.is_active = True
        usuario.is_staff = False
        usuario.is_superuser = False

        if password:
            usuario.set_password(password)

        usuario.save()
        return usuario
        
    def create_superuser(self, email, password):
        usuario = self.create_user(
            email=self.normalize_email(email), # O metodo normalize evita que o cadastro do e-mail utilize caracteres maiuculos
            password=password,
        )

        usuario.is_active = True
        usuario.is_staff = True
        usuario.is_superuser = True

        usuario.set_password(password)

        usuario.save()

        return usuario


class Usuario(AbstractBaseUser, PermissionsMixin):
    
    email = models.EmailField(
        verbose_name="E-mail do usuário",
        max_length=194,
        unique=True,
    )
    
    is_active = models.BooleanField(
        verbose_name="Usuário está ativo",
        default=True,
    )

    is_staff = models.BooleanField(
        verbose_name="Usuário é da equipe de desenvolvimento",
        default=False,
    )

    is_superuser = models.BooleanField(
        verbose_name="Usuário é um superusuario",
        default=False,
    )

    USERNAME_FIELD = "email"

    objects = UsuarioManager()

class Meta:    # Meta dados 
    verbose_name = "Usuário"
    verbose_name = "Usuários"
    db_table = "usuario" # nome da tabela no banco de dados para representar 

    def __str__(self):  #retorna nesse metodo o email do usuario
        return self.email