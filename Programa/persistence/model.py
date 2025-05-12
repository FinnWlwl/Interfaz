#============================================================================================================#
#                                          MODELO: AUTH_USER                                                 #
#============================================================================================================#
"""
Descripción:
Este archivo define el modelo de la tabla 'auth_user' en la base de datos.
La clase Auth_User representa a un usuario con nombre de usuario y contraseña.
Este modelo se usa para registrar y autenticar usuarios dentro del sistema.
"""

#============================================================================================================#
#                                    IMPORTACIÓN DE LIBRERÍAS                                                #
#============================================================================================================#
from sqlalchemy import Column  # Para definir columnas de la tabla
from sqlalchemy import String, Integer  # Tipos de datos para las columnas
from sqlalchemy.orm import declarative_base  # Base para la creación de modelos (ORM)

#============================================================================================================#
#                                DEFINICIÓN DE LA CLASE BASE PARA MODELOS                                    #
#============================================================================================================#
Base = declarative_base()

#============================================================================================================#
#                                    MODELO DE USUARIO: AUTH_USER                                            #
#============================================================================================================#
class Auth_User(Base):
    __tablename__ = "auth_user" # Nombre de la tabla en la base de datos
    id = Column(Integer, primary_key=True, autoincrement=True) # ID único, clave primaria
    username = Column(String(150)) # Nombre de usuario (máx. 150 caracteres)
    password = Column(String(128)) # Contraseña (máx. 128 caracteres)

    def __repr__(self):
        #Representación técnica del objeto
        return f'auth_user({self.username}, {self.password})' 

    def __str__(self):
        #Representación legible del objeto (al imprimirlo).
        return self.username