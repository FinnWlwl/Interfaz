#============================================================================================================#
#                                       DISEÑO VENTANA: INFORMACIÓN                                          #
#============================================================================================================#
"""
Descripción:
Este script crea una ventana de información que muestra la versión del programa y los autores.
"""

#============================================================================================================#
#                                      IMPORTACIÓN DE LIBRERÍAS                                              #
#============================================================================================================#
import tkinter as tk
import util.generic as util_ventana
from config import COLOR_BARRA_SUPERIOR, COLOR_CUERPO_PRINCIPAL

#============================================================================================================#
#                                   INICIO DE VENTANA DE INFORMACIÓN                                         #
#============================================================================================================#
class InfoDesign():
    ventana_info = None  # Variable de clase para controlar una sola instancia

    def __init__(self):
        # Verificar si la ventana ya está abierta antes de crear una nueva
        if InfoDesign.ventana_info and InfoDesign.ventana_info.winfo_exists():
            InfoDesign.ventana_info.lift()  # Traer la ventana al frente si ya existe
            return 

        self.configurarVentana()
        self.construirWidget()
        
        self.ventana_info.mainloop()

#============================================================================================================#
#                                CONFIGURACIÓN DE LA VENTANA DE INFORMACIÓN                                  #
#============================================================================================================#
    def configurarVentana(self):   
        self.ventana_info = tk.Toplevel()  
        self.ventana_info.withdraw()  # Ocultar temporalmente la ventana         

        self.ventana_info.title('Información')
        self.ventana_info.iconbitmap("./images/icono_info.ico")
        w, h = 325, 175      

        util_ventana.centrar_ventana(self.ventana_info, w, h)  # Centrar ventana
        
        self.ventana_info.resizable(False, False)  
        self.ventana_info.deiconify()  # Mostrar la ventana correctamente centrada
        
        # Para limpiar la referencia cuando se cierre la ventana
        self.ventana_info.protocol("WM_DELETE_WINDOW", self.on_close)

        # Guardamos la referencia en la variable de clase
        InfoDesign.ventana_info = self.ventana_info

        self.ventana_info.bind("<Escape>", lambda event: self.ventana_info.destroy())

#============================================================================================================#
#                                         DISEÑO DE LA VENTANA                                               #
#============================================================================================================#
    def construirWidget(self):         
        self.ventana_info.labelVersion = tk.Label(self.ventana_info, text="Versión : 1.6")
        self.ventana_info.labelVersion.config(fg="#000000", font=("Roboto", 15), pady=10, width=20)
        self.ventana_info.labelVersion.pack()

        self.ventana_info.labelAutor = tk.Label(self.ventana_info, text="Autores:\n "
        "Diego Andrés Martínez Chávez\n "
        "Laura Ivonne López Rodríguez\n "
        "Jesús Alberto Soto Juárez\n "
        "Miguel Gerardo Castillo Ruiz\n")
        self.ventana_info.labelAutor.config(fg="#000000", font=("Roboto", 15), pady=20, width=25)
        self.ventana_info.labelAutor.pack()

#============================================================================================================#
#                                        CERRADO DE LA VENTANA                                               #
#============================================================================================================#
    def on_close(self):
        #Se ejecuta al cerrar la ventana, limpiando la referencia. 
        InfoDesign.ventana_info = None
        self.ventana_info.destroy()
