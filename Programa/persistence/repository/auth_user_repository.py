#============================================================================================================#
#                                  REPOSITORIO: AUTH_USER_REPOSITORY                                         #
#============================================================================================================#
"""
Descripción:
Este archivo define una clase repositorio para manejar operaciones con la tabla 'auth_user'.
Permite conectarse a la base de datos, obtener usuarios por nombre, insertar nuevos usuarios y 
borrar todos los registros de usuarios.
"""

#============================================================================================================#
#                                      IMPORTACIÓN DE LIBRERÍAS                                              #
#============================================================================================================#
import sqlalchemy as db  # Librería principal para trabajar con la base de datos
from sqlalchemy.orm import Session  # Permite manejar sesiones de consultas y transacciones
from persistence.model import Auth_User  # Modelo del usuario

#============================================================================================================#
#                                     CLASE: AUTH_USER_REPOSITORY                                            #
#============================================================================================================#
class AuthUserRepository():

    def __init__(self):
        # Crea el motor de conexión a la base de datos SQLite
        self.engine = db.create_engine('sqlite:///db/login.sqlite', echo=False, future=True)  

    def getUserByUserName(self, user_name: str):
        user: Auth_User = None  # Inicializa la variable que contendrá el usuario encontrado
        with Session(self.engine) as session:  # Abre una sesión con la base de datos
            # Realiza una consulta para buscar el primer usuario con el nombre indicado
            user = session.query(Auth_User).filter_by(username=user_name).first()  
        return user  # Retorna el usuario encontrado (o None si no existe)

    def insertUser(self, user: Auth_User):
        with Session(self.engine) as session:  # Abre una sesión con la base de datos
            session.add(user)  # Agrega el nuevo usuario a la sesión (preparado para inserción)
            session.commit()  # Confirma los cambios en la base de datos

    def clearUsers(self):
        with Session(self.engine) as session:  # Abre una sesión con la base de datos
            session.query(Auth_User).delete()  # Elimina todos los registros de la tabla 'auth_user'
            session.commit()  # Confirma los cambios en la base de datos