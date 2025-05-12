#============================================================================================================#
#                                          DISEÑO VENTANA: CARGA                                             #
#============================================================================================================#
"""
Descripción:
Este script crea una ventana de carga para una aplicación utilizando Tkinter.
"""

#============================================================================================================#
#                                      IMPORTACIÓN DE LIBRERÍAS                                              #
#============================================================================================================#
import tkinter as tk
from tkinter import ttk  # Importar para usar Combobox
import util.generic as utl
from config import COLOR_PANTALLA_CARGA
from forms.main.master import NuevaVentana

#============================================================================================================#
#                                  CONFIGURACIÓN DE LA VENTANA DE CARGA                                      #
#============================================================================================================#
class MasterPanel:
    def __init__(self):
        self.ventana = tk.Tk()                             
        self.ventana.title('Cargando...')
        self.ventana.geometry("800x600")  
        self.ventana.attributes("-fullscreen", True)  
        self.ventana.resizable(False, False)     

        self.ventana.iconbitmap("./images/icono_general.ico")

        logo = utl.leer_imagen("./images/Logo.png", (200, 200))
        label = tk.Label(self.ventana, image=logo, bg=COLOR_PANTALLA_CARGA)
        label.place(x=0, y=0, relwidth=1, relheight=1)

        self.ventana.after(500, self.abrir_nueva_ventana)  #1 segundo de espera
        self.ventana.mainloop()

#============================================================================================================#
#                                      ABRIR LA VENTANA PRINCIPAL                                            #
#============================================================================================================#
    def abrir_nueva_ventana(self):
        self.ventana.withdraw()  # Oculta la ventana de carga
        NuevaVentana()  
