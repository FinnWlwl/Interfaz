#============================================================================================================#
#                                     CREACIÓN DE BASE DE DATOS                                              #
#============================================================================================================#
"""
Descripción:
Este script se encarga de crear la base de datos y sus tablas utilizando SQLAlchemy. Establece una conexión
con el motor SQLite y registra todos los modelos definidos en el proyecto. Si las tablas ya existen, no se
vuelven a crear.
"""

#============================================================================================================#
#                                   IMPORTACIÓN DE LIBRERÍAS                                                 #
#============================================================================================================#
import sqlalchemy as db  # Manejo flexible de bases de datos con SQLAlchemy
import persistence.model as mod  # Contiene la definición de los modelos (tablas)
from persistence.model import Auth_User  # Registro explícito del modelo Auth_User

#============================================================================================================#
#                                 CREACIÓN DEL MOTOR Y LAS TABLAS                                            #
#============================================================================================================#

engine = db.create_engine('sqlite:///db/login.sqlite', echo=True, future=True) # Crea el motor de conexión a la base de datos SQLite
mod.Base.metadata.create_all(engine) # Crea las tablas definidas en los modelos, si no existen aún