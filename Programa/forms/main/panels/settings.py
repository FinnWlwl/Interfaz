#============================================================================================================#
#                                         DISEÑO VENTANA: AJUSTES                                            #
#============================================================================================================#
"""
Descripción:
Este script define la clase SettingsDesign, que crea una ventana de ajustes 
para seleccionar el color de la línea y los puntos en la gráfica.
"""

#============================================================================================================#
#                                      IMPORTACIÓN DE LIBRERÍAS                                              #
#============================================================================================================#
import tkinter as tk
from tkinter import ttk  # Importar para usar Combobox
import util.generic as util_ventana
from config import (COLOR_BTN_CERRAR, COLOR_BTN_GUARDAR, COLOR_LETRAS_BTN_GUARDAR_CERRAR, 
                    COLOR_BARRA_SUPERIOR, COLORES_GRAFICA, LISTA_COLORES)

#============================================================================================================#
#                                     INICIO DE VENTANA DE AJUSTES                                           #
#============================================================================================================#
class SettingsDesign():
    ventana_ajustes = None  # Variable de clase para controlar una sola instancia

    def __init__(self, on_color_change=None, color_actual="black"):
        self.on_color_change = on_color_change
        self.color_actual = color_actual

        # Verificar si la ventana ya está abierta antes de crear una nueva
        if SettingsDesign.ventana_ajustes and SettingsDesign.ventana_ajustes.winfo_exists():
            SettingsDesign.ventana_ajustes.lift()  # Traer la ventana al frente si ya existe
            return

        self.configurarVentana()
        self.construirWidget()

#============================================================================================================#
#                                     CONFIGURACIÓN DE LA VENTANA                                            #
#============================================================================================================# 
    def configurarVentana(self):   
        self.ventana_ajustes = tk.Toplevel()  
        self.ventana_ajustes.withdraw()  # Ocultar temporalmente la ventana         

        self.ventana_ajustes.title('Ajustes')
        self.ventana_ajustes.iconbitmap("./images/Icono_ajustes.ico")
        w, h = 325, 175      

        util_ventana.centrar_ventana(self.ventana_ajustes, w, h)  # Centrar ventana

        self.ventana_ajustes.resizable(False, False)  
        self.ventana_ajustes.deiconify()  # Mostrar la ventana correctamente centrada
            
            # Para limpiar la referencia cuando se cierre la ventana
        self.ventana_ajustes.protocol("WM_DELETE_WINDOW", self.on_close)

            # Guardamos la referencia en la variable de clase
        SettingsDesign.ventana_ajustes = self.ventana_ajustes

        self.ventana_ajustes.bind("<Escape>", lambda event: self.ventana_ajustes.destroy())
        
#============================================================================================================#
#                                         DISEÑO DE LA VENTANA                                               #
#============================================================================================================#
    def construirWidget(self):         
        # Etiqueta de título
        self.barra_superior = tk.Frame(
        self.ventana_ajustes, bg=COLOR_BARRA_SUPERIOR, height=1)
        self.barra_superior.pack(side=tk.TOP, fill='both') 

        self.labelTitulo = tk.Label(self.barra_superior, text="Ajustes de la gráfica")
        self.labelTitulo.config(fg="#fff", font=(
            "Roboto", 11, "bold"), bg=COLOR_BARRA_SUPERIOR, pady=5, width=16)
        self.labelTitulo.pack(side=tk.TOP)

        # Etiqueta de selección de color
        label_color = tk.Label(self.ventana_ajustes, text="Selecciona el color de la línea:")
        label_color.config(font=("Roboto", 11))
        label_color.pack(anchor="w", padx=20, pady=(10, 0))  # Este pady agrega espacio hacia arriba
        
        # Combobox para seleccionar color
        self.color_seleccionado = tk.StringVar()
        self.combobox_colores = ttk.Combobox(self.ventana_ajustes, textvariable=self.color_seleccionado, 
                                             values=LISTA_COLORES, state="readonly")
        self.combobox_colores.pack(anchor="w", padx=20, pady=5)

        # Invertimos el diccionario para buscar por color
        colores_inverso = {v: k for k, v in COLORES_GRAFICA.items()}
        color_nombre = colores_inverso.get(self.color_actual, "Negro")

        # Asignar como selección inicial
        self.color_seleccionado.set(color_nombre)

        # Frame para botones alineados a la derecha
        frame_botones = tk.Frame(self.ventana_ajustes)
        frame_botones.pack(side="bottom", fill="x", padx=10, pady=20)  
        
        # Botón Cerrar
        btn_cerrar = tk.Button(frame_botones, text="Cerrar", width=10, font=("TkDefaultFont", 9, "bold"), 
                               bg=COLOR_BTN_CERRAR, fg=COLOR_LETRAS_BTN_GUARDAR_CERRAR, command=self.ventana_ajustes.destroy)
        btn_cerrar.pack(side="right", padx=10)

        # Botón Guardar
        btn_guardar = tk.Button(frame_botones, text="Guardar", width=10, font=("TkDefaultFont", 9, "bold"), 
                                bg=COLOR_BTN_GUARDAR, fg=COLOR_LETRAS_BTN_GUARDAR_CERRAR, command=self.guardar_ajustes)
        btn_guardar.pack(side="right", padx=10)

        # Asociar eventos de teclado
        self.ventana_ajustes.bind("<Return>", lambda event: self.guardar_ajustes())  # Enter guarda
        self.ventana_ajustes.bind("<Escape>", lambda event: self.ventana_ajustes.destroy())  # Escape cierra

#============================================================================================================#
#                                        GUARDADO DE LA VENTANA                                              #
#============================================================================================================#
    def guardar_ajustes(self):
        color = COLORES_GRAFICA.get(self.color_seleccionado.get(), "black")
        
        if self.on_color_change:
            self.on_color_change(color)  # Ejecutar callback

        self.ventana_ajustes.destroy()

#============================================================================================================#
#                             MÉTODO PARA OBTENER EL COLOR SELECCIONADO                                      #
#============================================================================================================#
    def obtener_color(self):
        # Devuelve el color seleccionado en formato válido para matplotlib.
        return getattr(self, "color_resultado", "black")
    
#============================================================================================================#
#                                        CERRADO DE LA VENTANA                                               #
#============================================================================================================#
    def on_close(self):
        # Se ejecuta al cerrar la ventana, limpiando la referencia.
        SettingsDesign.ventana_ajustes = None
        self.ventana_ajustes.destroy()
