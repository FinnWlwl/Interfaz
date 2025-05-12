#============================================================================================================#
#                                         DISEÑO VENTANA: UNIDADES                                           #
#============================================================================================================#
"""
Descripción:
Este archivo define la clase UnidadesDesign, que construye una ventana emergente (Toplevel) 
para permitir al usuario seleccionar un sistema de unidades actualmente no está integrado su
funcionamiento.
"""

#============================================================================================================#
#                                      IMPORTACIÓN DE LIBRERÍAS                                              #
#============================================================================================================#
import tkinter as tk
import util.generic as util_ventana
from config import (
    COLOR_BTN_CERRAR, COLOR_BTN_GUARDAR, COLOR_LETRAS_BTN_GUARDAR_CERRAR, COLOR_BARRA_SUPERIOR
)

#============================================================================================================#
#                                    INICIO DE VENTANA DE UNIDADES                                           #
#============================================================================================================#
class UnidadesDesign():
    ventana_unidades = None  # Variable de clase para controlar una sola instancia

    def __init__(self):
        # Verificar si la ventana ya está abierta antes de crear una nueva
        if UnidadesDesign.ventana_unidades and UnidadesDesign.ventana_unidades.winfo_exists():
            UnidadesDesign.ventana_unidades.lift()  # Traer la ventana al frente si ya existe
            return

        self.configurarVentana()
        self.construirWidget()
        
        self.ventana_unidades.mainloop()

#============================================================================================================#
#                                     CONFIGURACIÓN DE LA VENTANA                                            #
#============================================================================================================#
    def configurarVentana(self):   
        self.ventana_unidades = tk.Toplevel()  
        self.ventana_unidades.withdraw()  # Ocultar temporalmente la ventana         

        self.ventana_unidades.title('Unidades')
        self.ventana_unidades.iconbitmap("./images/icono_general.ico")
        w, h = 350, 200      

        util_ventana.centrar_ventana(self.ventana_unidades, w, h)  # Centrar ventana

        self.ventana_unidades.resizable(False, False)  
        self.ventana_unidades.deiconify()  # Mostrar la ventana correctamente centrada
        
        # Para limpiar la referencia cuando se cierre la ventana
        self.ventana_unidades.protocol("WM_DELETE_WINDOW", self.on_close)

        # Guardamos la referencia en la variable de clase
        UnidadesDesign.ventana_unidades = self.ventana_unidades

#============================================================================================================#
#                                         DISEÑO DE LA VENTANA                                               #
#============================================================================================================#
    def construirWidget(self):         
        # Etiqueta de título
        self.barra_superior = tk.Frame(
        self.ventana_unidades, bg=COLOR_BARRA_SUPERIOR, height=1)
        self.barra_superior.pack(side=tk.TOP, fill='both') 

        # Etiqueta de instrucción
        self.labelTitulo = tk.Label(self.barra_superior, text="Selecciona el sistema de unidades:")
        self.labelTitulo.config(fg="#fff", font=(
            "Roboto", 12, "bold"), bg=COLOR_BARRA_SUPERIOR, pady=5, width=50)
        self.labelTitulo.pack(side=tk.TOP)

        # Variable para almacenar la selección (por defecto en mm)
        self.unidad_seleccionada = tk.StringVar(value="mm")  

        # Opciones de unidades
        opciones = [("Milímetros", "mm"), ("Centímetros", "cm"), ("Pulgadas", "in")]
        
        for i, (texto, valor) in enumerate(opciones):
            rb = tk.Radiobutton(self.ventana_unidades, text=texto, variable=self.unidad_seleccionada, value=valor)
            rb.config(font=("Roboto", 12))
            
            # Solo al primer radiobutton le damos espacio hacia arriba
            if i == 0:
                rb.pack(anchor="w", padx=20, pady=(10, 0))  
            else:
                rb.pack(anchor="w", padx=20)

        # Frame para los botones alineados a la derecha
        frame_botones = tk.Frame(self.ventana_unidades)
        frame_botones.pack(side="bottom", fill="x", padx=10, pady=20)  # Más separación
  
        # Botón Cancelar
        btn_cancelar = tk.Button(frame_botones, text="Cancelar", width=10, font=("TkDefaultFont", 9, "bold"), 
                                 bg=COLOR_BTN_CERRAR, fg=COLOR_LETRAS_BTN_GUARDAR_CERRAR, 
                                 command=self.ventana_unidades.destroy)
        btn_cancelar.pack(side="right", padx=10)  # Botón antes de "Guardar"
        
        # Botón Guardar
        btn_guardar = tk.Button(frame_botones, text="Guardar", width=10, font=("TkDefaultFont", 9, "bold"), 
                                bg=COLOR_BTN_GUARDAR, fg=COLOR_LETRAS_BTN_GUARDAR_CERRAR, 
                                command=self.guardar_unidad)
        btn_guardar.pack(side="right", padx=10)  # Botón pegado a la derecha

        # Asociar eventos de teclado
        self.ventana_unidades.bind("<Return>", lambda event: self.guardar_unidad())  # Enter guarda
        self.ventana_unidades.bind("<Escape>", lambda event: self.ventana_unidades.destroy())  # Escape cierra

#============================================================================================================#
#                                        GUARDADO DE LA VENTANA                                              #
#============================================================================================================#
    def guardar_unidad(self):
        """ Función para manejar la acción de guardar (se programará la lógica después). """
        print(f"Unidad seleccionada: {self.unidad_seleccionada.get()}")
        self.ventana_unidades.destroy()

#============================================================================================================#
#                                        CERRADO DE LA VENTANA                                               #
#============================================================================================================#
    def on_close(self):
        """ Se ejecuta al cerrar la ventana, limpiando la referencia. """
        UnidadesDesign.ventana_unidades = None
        self.ventana_unidades.destroy()
