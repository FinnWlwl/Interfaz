#============================================================================================================#
#                                               INICIO DE SESIÓN                                             #
#============================================================================================================#
"""
Descripción:
Este script construye la lógica del login de usuarios y el diseño de la ventana de inicio de sesión
usando Tkinter. Incluye validaciones de acceso y navegación hacia otras interfaces como el registro
o el panel principal.
"""

#============================================================================================================#
#                                       IMPORTACIÓN DE LIBRERÍAS                                             #
#============================================================================================================#
import tkinter as tk  # Librería base para interfaces gráficas
from tkinter import ttk, messagebox  # Widgets mejorados y cuadros de diálogo
from tkinter.font import BOLD  # Fuente en negrita

import util.generic as utl  # Funciones utilitarias (centrado, imagen, etc.)
import util.encoding_decoding as end_dec  # Cifrado y descifrado de contraseñas

# Navegación entre pantallas
import forms.register.register_designer as register_designer  # Diseño de la pantalla de registro
import forms.main.loading as master  # Pantalla principal (luego del login)

# Configuración visual
from config import (
    COLOR_FONDO_IZQUIEDO_LOGIN,
    COLOR_FONDO_DERECHO_LOGIN,
    COLOR_BTN_LOGIN,
    COLOR_TITULO_LOGIN,
    COLOR_REGISTRO_LOGIN,
    COLOR_LETRAS_LOGIN
)

# Modelo y acceso a base de datos
from persistence.model import Auth_User  # Modelo de usuario
from persistence.repository.auth_user_repository import AuthUserRepository  # Repositorio

#============================================================================================================#
#                               INICIALIZACIÓN DEL REPOSITORIO DE USUARIOS                                   #
#============================================================================================================#
auth_repository = AuthUserRepository()

#============================================================================================================#
#                                FUNCIÓN PARA VERIFICAR DATOS DE LOGIN                                       #
#============================================================================================================#
def verificar():
    global usuario, password_data, auth_repository

    if not usuario.get() or not password_data.get():
        messagebox.showerror(message="Por favor llena todos los campos", title="Mensaje")
        return 
       
    user_db: Auth_User = auth_repository.getUserByUserName(usuario.get())
    if(isUser(user_db)):
        isPassword(password_data.get(), user_db)

#============================================================================================================#
#                        FUNCIÓN PARA VERIFICAR SI EL USUARIO EXISTE                                         #
#============================================================================================================#
def isUser(user: Auth_User):
        status: bool = True
        if(user == None):
            status = False
            messagebox.showerror(
                message="El usuario no existe por favor registrese", title="Mensaje")            
        return status

#============================================================================================================#
#                      FUNCIÓN PARA VERIFICAR LA CONTRASEÑA DEL USUARIO                                      #
#============================================================================================================#
def isPassword(password: str, user: Auth_User):
        b_password = end_dec.decrypt(user.password)
        if(password == b_password):
            ventana_login.destroy()
            master.MasterPanel()
        else:
            messagebox.showerror(message="La contraseña no es correcta", title="Mensaje")

#============================================================================================================#
#                          FUNCIÓN PARA REDIRIGIR AL FORMULARIO DE REGISTRO                                  #
#============================================================================================================#
def userRegister():
    ventana_login.destroy()
    register_designer.RegisterDesigner()

#============================================================================================================#
#                              FUNCIÓN PARA MOSTRAR U OCULTAR CONTRASEÑA                                     #
#============================================================================================================#
def toggle_password():
    if mostrar_password_var.get():
        password_data.config(show="")  # Mostrar la contraseña
    else:
        password_data.config(show="*")  # Ocultar con asteriscos   

#============================================================================================================#
#                                 DISEÑO DE LA INTERFAZ DE LOGIN                                             #
#============================================================================================================#
def LoginDesigner():
    global ventana_login, usuario, password_data, mostrar_password_var

    #------------------------------------------- VENTANA PRINCIPAL ------------------------------------------#
    ventana_login = tk.Tk()
    ventana_login.title('Iniciar sesión')
    ventana_login.geometry('800x500')
    ventana_login.config(bg='#fcfcfc')
    ventana_login.resizable(width=0, height=0)
    utl.centrar_ventana(ventana_login, 800, 500)

    ventana_login.iconbitmap("./images/icono_inicial.ico")

    #------------------------------------------ CARGA DE IMAGEN (LOGO) --------------------------------------#
    logo = utl.leer_imagen("./images/logo.png", (200, 200))

    #------------------------------------------ FRAME IZQUIERDO (LOGO) --------------------------------------#
    frame_logo = tk.Frame(ventana_login, bd=0, width=300, relief=tk.SOLID, padx=10, pady=10,
                            bg=COLOR_FONDO_IZQUIEDO_LOGIN)
    frame_logo.pack(side="left",expand=tk.YES,fill=tk.BOTH)
    label = tk.Label( frame_logo, image=logo,bg=COLOR_FONDO_IZQUIEDO_LOGIN)
    label.place(x=0,y=0,relwidth=1, relheight=1)

    #------------------------------------------ FRAME DERECHO (FORMULARIO) ----------------------------------#
    frame_form = tk.Frame(ventana_login, bd=0, relief=tk.SOLID, bg=COLOR_FONDO_DERECHO_LOGIN)
    frame_form.pack(side="right", expand=tk.YES, fill=tk.BOTH)

    # Encabezado
    frame_form_top = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg='black')
    frame_form_top.pack(side="top", fill=tk.X)
    title = tk.Label(frame_form_top, text="Iniciar sesión", font=('Times', 30),
                     fg=COLOR_TITULO_LOGIN, bg=COLOR_FONDO_DERECHO_LOGIN, pady=30)
    title.pack(expand=tk.YES, fill=tk.BOTH)

    # Contenido del formulario
    frame_form_fill = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg=COLOR_FONDO_DERECHO_LOGIN)
    frame_form_fill.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)

    # Campo Usuario
    etiqueta_usuario = tk.Label(frame_form_fill, text="Usuario", font=('Times', 14),
                                fg=COLOR_LETRAS_LOGIN, bg=COLOR_FONDO_DERECHO_LOGIN, anchor="w")
    etiqueta_usuario.pack(fill=tk.X, padx=20, pady=5)
    usuario = ttk.Entry(frame_form_fill, font=('Times', 14))
    usuario.pack(fill=tk.X, padx=20, pady=10)

    # Campo Contraseña
    etiqueta_password = tk.Label(frame_form_fill, text="Contraseña", font=('Times', 14),
                                 fg=COLOR_LETRAS_LOGIN, bg=COLOR_FONDO_DERECHO_LOGIN, anchor="w")
    etiqueta_password.pack(fill=tk.X, padx=20, pady=5)
    password_data = ttk.Entry(frame_form_fill, font=('Times', 14), show="*")
    password_data.pack(fill=tk.X, padx=20, pady=10)

    # Check para mostrar contraseña
    mostrar_password_var = tk.BooleanVar()
    mostrar_password_check = tk.Checkbutton(frame_form_fill, text="Mostrar contraseña",
                                            variable=mostrar_password_var,
                                            bg=COLOR_FONDO_DERECHO_LOGIN, font=('Times', 12),
                                            command=toggle_password)
    mostrar_password_check.pack(pady=10, padx=20, anchor="e")

    # Botón Iniciar sesión
    boton_inicio = tk.Button(frame_form_fill, text="Iniciar sesión", font=('Times', 15, BOLD),
                             bg=COLOR_BTN_LOGIN, bd=0, fg="#fff", command=verificar)
    boton_inicio.pack(fill=tk.X, padx=20, pady=(25, 20))

    # Botón Registrar
    boton_registro = tk.Button(frame_form_fill, text="Registrar", font=('Times', 15, BOLD),
                               bg=COLOR_FONDO_DERECHO_LOGIN, bd=0, fg=COLOR_REGISTRO_LOGIN,
                               command=userRegister)
    boton_registro.pack(fill=tk.X, padx=0, pady=0)

    #------------------------------------------- USABILIDAD -------------------------------------------------#
    usuario.bind("<Return>", lambda event: password_data.focus_set())
    password_data.bind("<Return>", lambda event: boton_inicio.invoke())

    # Inicia el ciclo principal
    ventana_login.mainloop()
