#============================================================================================================#
#                                           REGISTRO DE USUARIOS                                             #
#============================================================================================================#
"""
Descripción:
Este script define la lógica para el registro de usuarios, así como el diseño de la interfaz gráfica
usando Tkinter. Incluye validaciones básicas, control de navegación y acceso a una base de datos SQLite.
"""

#============================================================================================================#
#                                       IMPORTACIÓN DE LIBRERÍAS                                             #
#============================================================================================================#
import tkinter as tk  # Librería base para interfaces gráficas
from tkinter import ttk, messagebox  # Widgets avanzados y cuadros de diálogo
from tkinter.font import BOLD  # Fuente en negrita

import util.generic as utl  # Funciones utilitarias (centrado de ventana, imagen, etc.)
import forms.login.login_design as login_design  # Diseño de la ventana de login

# Colores personalizados desde archivo de configuración
from config import (
    COLOR_FONDO_IZQUIERDO_REGISTER,
    COLOR_FONDO_DERECHO_REGISTER,
    COLOR_BTN_REGISTER,
    COLOR_TITULO_REGISTER,
    COLOR_REGRESAR_REGISTER,
    COLOR_LETRAS_REGISTER
)

# Manejo de usuarios y encriptación
from persistence.model import Auth_User  # Modelo de usuario
import util.encoding_decoding as end_dec  # Cifrado y descifrado de contraseñas
from persistence.repository.auth_user_repository import AuthUserRepository  # Repositorio de acceso a datos

#============================================================================================================#
#                              INICIALIZACIÓN DEL REPOSITORIO DE USUARIOS                                    #
#============================================================================================================#
auth_repository = AuthUserRepository()  # Instancia para manejar operaciones sobre usuarios

#============================================================================================================#
#                                FUNCIÓN PARA REGISTRAR UN NUEVO USUARIO                                     #
#============================================================================================================#
def register():
    # Verifica que todos los campos estén llenos
    if not usuario.get() or not password.get() or not confirmation.get():
        messagebox.showerror(message="Por favor llena todos los campos", title="Mensaje")
        return

    # Verifica que la contraseña y la confirmación coincidan
    if isConfirmationPassword():
        user = Auth_User()  # Crea un nuevo objeto usuario
        user.username = usuario.get()  # Asigna el nombre desde el campo de entrada
        user_db = auth_repository.getUserByUserName(usuario.get())  # Consulta si ya existe

        if not isUserRegister(user_db):  # Si el usuario no existe aún
            user.password = end_dec.encrypted(password.get())  # Encripta la contraseña
            auth_repository.insertUser(user)  # Inserta el usuario en la base de datos
            messagebox.showinfo(message="Se registró el usuario", title="Mensaje")  # Mensaje de éxito
            ventana_register.destroy()  # Cierra ventana actual
            login_design.LoginDesigner()  # Abre ventana de login

#============================================================================================================#
#                            FUNCIÓN PARA VALIDAR SI EL USUARIO YA EXISTE                                    #
#============================================================================================================#
def isUserRegister(user: Auth_User):
    status: bool = False
    if(user != None):  # Si el usuario fue encontrado
        status = True
        messagebox.showerror(message="El usuario ya existe", title="Mensaje")
    return status

#============================================================================================================#
#                         FUNCIÓN PARA VALIDAR QUE LAS CONTRASEÑAS COINCIDAN                                 #
#============================================================================================================#
def isConfirmationPassword():
    status: bool = True
    if(password.get() != confirmation.get()):  # Si las contraseñas no coinciden
        status = False
        messagebox.showerror(
            message="La contraseña no coincide, por favor verifica el registro",
            title="Mensaje"
        )
        password.delete(0, tk.END)  # Limpia campo contraseña
        confirmation.delete(0, tk.END)  # Limpia campo confirmación
    return status

#============================================================================================================#
#                                FUNCIÓN PARA REGRESAR A LA VENTANA LOGIN                                    #
#============================================================================================================#
def regresar():
    ventana_register.destroy()  # Cierra ventana de registro
    login_design.LoginDesigner()  # Abre la ventana de login

#============================================================================================================#
#                              DISEÑO DE LA INTERFAZ DE REGISTRO                                             #
#============================================================================================================#
def RegisterDesigner():
    global ventana_register, usuario, password, confirmation

    #------------------------------------------ VENTANA PRINCIPAL -------------------------------------------#
    ventana_register = tk.Tk()
    ventana_register.title('Registro')
    ventana_register.geometry('800x500')
    ventana_register.config(bg='#fcfcfc')
    ventana_register.resizable(width=0, height=0)
    utl.centrar_ventana(ventana_register, 800, 500)
    ventana_register.iconbitmap("./images/icono_inicial.ico")

    #------------------------------------------- CARGA DE IMAGEN (LOGO) -------------------------------------#
    logo = utl.leer_imagen("./images/logo.png", (200, 200))

    #------------------------------------------- FRAME IZQUIERDO CON LOGO -----------------------------------#
    frame_logo = tk.Frame(ventana_register, bd=0, width=300, relief=tk.SOLID, padx=10, pady=10,
                          bg=COLOR_FONDO_IZQUIERDO_REGISTER)
    frame_logo.pack(side="left", expand=tk.YES, fill=tk.BOTH)
    label = tk.Label(frame_logo, image=logo, bg=COLOR_FONDO_IZQUIERDO_REGISTER)
    label.place(x=0, y=0, relwidth=1, relheight=1)

    #------------------------------------------ FRAME DERECHO DEL FORMULARIO --------------------------------#
    frame_form = tk.Frame(ventana_register, bd=0, relief=tk.SOLID, bg=COLOR_FONDO_DERECHO_REGISTER)
    frame_form.pack(side="right", expand=tk.YES, fill=tk.BOTH)

    #------------------------------------------ ENCABEZADO --------------------------------------------------#
    frame_form_top = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg='black')
    frame_form_top.pack(side="top", fill=tk.X)
    title = tk.Label(frame_form_top, text="Registro", font=('Times', 30),
                     fg=COLOR_TITULO_REGISTER, bg=COLOR_FONDO_DERECHO_REGISTER, pady=30)
    title.pack(expand=tk.YES, fill=tk.BOTH)

    #---------------------------------------- CAMPOS DEL FORMULARIO -----------------------------------------#
    frame_form_fill = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg=COLOR_FONDO_DERECHO_REGISTER)
    frame_form_fill.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)

    # Campo Usuario
    etiqueta_usuario = tk.Label(frame_form_fill, text="Usuario", font=('Times', 14),
                                fg=COLOR_LETRAS_REGISTER, bg=COLOR_FONDO_DERECHO_REGISTER, anchor="w")
    etiqueta_usuario.pack(fill=tk.X, padx=20, pady=5)
    usuario = ttk.Entry(frame_form_fill, font=('Times', 14))
    usuario.pack(fill=tk.X, padx=20, pady=10)

    # Campo Contraseña
    etiqueta_password = tk.Label(frame_form_fill, text="Contraseña", font=('Times', 14),
                                 fg=COLOR_LETRAS_REGISTER, bg=COLOR_FONDO_DERECHO_REGISTER, anchor="w")
    etiqueta_password.pack(fill=tk.X, padx=20, pady=5)
    password = ttk.Entry(frame_form_fill, font=('Times', 14), show="*")
    password.pack(fill=tk.X, padx=20, pady=10)

    # Campo Confirmación
    etiqueta_confirmation = tk.Label(frame_form_fill, text="Confirmación", font=('Times', 14),
                                     fg=COLOR_LETRAS_REGISTER, bg=COLOR_FONDO_DERECHO_REGISTER, anchor="w")
    etiqueta_confirmation.pack(fill=tk.X, padx=20, pady=5)
    confirmation = ttk.Entry(frame_form_fill, font=('Times', 14), show="*")
    confirmation.pack(fill=tk.X, padx=20, pady=10)

    #------------------------------------------ BOTONES -----------------------------------------------------#
    button_frame = tk.Frame(frame_form_fill, bg=COLOR_FONDO_DERECHO_REGISTER)
    button_frame.pack(fill=tk.X, padx=20, pady=10)

    registrar_btn = tk.Button(button_frame, text="Registrar", font=('Times', 15, BOLD),
                              bg=COLOR_BTN_REGISTER, bd=0, fg="#fff", command=register)
    registrar_btn.pack(side=tk.LEFT, expand=tk.YES, fill=tk.X, padx=5, pady=30)

    regresar_btn = tk.Button(button_frame, text="Regresar", font=('Times', 15, BOLD),
                             bg=COLOR_FONDO_DERECHO_REGISTER, bd=0, fg=COLOR_REGRESAR_REGISTER,
                             command=regresar)
    regresar_btn.pack(side=tk.LEFT, expand=tk.YES, fill=tk.X, padx=5, pady=30)

    #------------------------------------------- USABILIDAD -------------------------------------------------#
    usuario.bind("<Return>", lambda event: password.focus_set())  # Enter en usuario enfoca contraseña
    password.bind("<Return>", lambda event: confirmation.focus_set())  # Enter en contraseña enfoca confirmación
    confirmation.bind("<Return>", lambda event: registrar_btn.invoke())  # Enter en confirmación registra
    ventana_register.bind("<Escape>", lambda event: regresar())  # ESC regresa al login

    # Inicia el ciclo principal
    ventana_register.mainloop()