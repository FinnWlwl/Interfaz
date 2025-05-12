#============================================================================================================#
#                                          DISEÑO VENTANA: PRINCIPAL                                         #
#============================================================================================================#
"""
Descripción:
Este script es el más importante del programa, pues contiene la ventana principal y la lógica de la misma.
Está dividido por secciones, cada una con su respectiva función, para facilitar la lectura y comprensión del 
código. Para agregar la lógica de lectura de datos, se debe modificar el código en las secciones de 
configuración de la gráfica y la tabla. Además si se quieren agregar funcionalidades extra, estas deben
ubicarse en la sección de métodos adicionales.
Actualmente los botones no poseen lógica, pero se pueden agregar en la sección de configuración de botones.
"""

#============================================================================================================#
#                                      IMPORTACIÓN DE LIBRERÍAS                                              #
#============================================================================================================#
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import sys

import util.generic as utl
from util.read_serial import ReadSerial

from config import (
    COLOR_BARRA_SUPERIOR, 
    COLOR_MENU_LATERAL, COLOR_MENU_CURSOR_ENCIMA, 
    COLOR_CUERPO_PRINCIPAL, 
    COLOR_BTN_START, COLOR_BTN_PAUSE, COLOR_BTN_STOP, COLOR_BTN_HOME, COLOR_BTN_BORRAR, 
    COLOR_BTN_EXPANDIR, COLOR_BTN_UNIDADES,
    COLOR_LETRAS_BTN_SUPERIORES, COLOR_LETRAS_BTN_INFERIORES)

from forms.main.panels.delete import DeleteDesign
from forms.main.panels.info_design import InfoDesign
from forms.main.panels.unidades import UnidadesDesign
from forms.main.panels.settings import SettingsDesign
from forms.main.panels.lateral_panel import toggle_panel

#============================================================================================================#
#                                      INICIO DE LA VENTANA PRINCIPAL                                        #
#============================================================================================================#
class NuevaVentana():
    def __init__(self):
        self.color_grafica = "black"  # Color inicial de la gráfica

        self.configurar_ventana()
        self.configurar_frames()
        self.configurar_barra_superior()
        self.configurar_menu_lateral()
        self.configurar_botones_superiores()
        self.configurar_grafica()
        self.configurar_tabla()
        self.configurar_botones_inferiores()
        
        self.serial_lectura = ReadSerial(self.ventana, self.actualizar_grafica)

        self.ventana.mainloop()  

#============================================================================================================#
#                                  CONFIGURACIÓN DE LA VENTANA PRINCIPAL                                     #
#============================================================================================================#
    def configurar_ventana(self):

        self.perfil = utl.leer_imagen("./images/logo.png", (125, 125))

        self.ventana = tk.Toplevel()
        self.ventana.title("Nueva Ventana")
        self.ventana.geometry("800x600")  
        self.ventana.state("zoomed")
        self.ventana.resizable(True, True)  #Modificar para poder maximizar y minimizar la ventana 
        self.ventana.configure(bg=COLOR_CUERPO_PRINCIPAL)
        self.ventana.iconbitmap("./images/icono_general.ico")
        
        self.ventana_expandida = None  # Controla si la ventana expandida está abierta

#============================================================================================================#
#                                CONFIGURACIÓN DE LOS FRAMES DE LA VENTANA                                   #
#============================================================================================================#
    def configurar_frames(self):
        # Creación de frames
        self.barra_superior = tk.Frame(
        self.ventana, bg=COLOR_BARRA_SUPERIOR, height=50)
        self.barra_superior.pack(side=tk.TOP, fill='both')

        self.menu_lateral = tk.Frame(self.ventana, bg=COLOR_MENU_LATERAL, width=150)
        self.menu_lateral.pack(side=tk.LEFT, fill='both', expand=False)
        self.menu_lateral.pack_forget()
        
        self.cuerpo_principal = tk.Frame(
            self.ventana, bg=COLOR_CUERPO_PRINCIPAL)
        self.cuerpo_principal.pack(side=tk.RIGHT, fill='both', expand=True)

#============================================================================================================#
#                                    CONFIGURACIÓN DE LA BARRA SUPERIOR                                      #
#============================================================================================================#
    def configurar_barra_superior(self):
        # Botón del menú lateral
        self.buttonMenuLateral = tk.Button(self.barra_superior, text="\uf0c9", font=("FontAwesome", 12), #\uf0c9  uf061  uf142
                                           command=lambda: toggle_panel(self),
                                           bd=0, bg=COLOR_BARRA_SUPERIOR, fg=COLOR_CUERPO_PRINCIPAL)
        self.buttonMenuLateral.pack(side=tk.LEFT, padx=2)

        # Etiqueta de título
        self.labelTitulo = tk.Label(self.barra_superior, text="Nombre de prueba")
        self.labelTitulo.config(fg="#fff", font=(
            "Roboto", 15), bg=COLOR_BARRA_SUPERIOR, pady=10, width=16)
        self.labelTitulo.pack(side=tk.LEFT)
        
        # Etiqueta de información
        self.labelTitulo = tk.Label(
            self.barra_superior, text="servicio@ualn.mx")
        self.labelTitulo.config(fg="#fff", font=(
            "Roboto", 10), bg=COLOR_BARRA_SUPERIOR, padx=10, width=20)
        self.labelTitulo.pack(side=tk.RIGHT)  
        
#============================================================================================================#
#                                      CONFIGURACIÓN DEL MENÚ LATERAL                                        #
#============================================================================================================#        
    def configurar_menu_lateral(self):
        # Etiqueta de perfil
        self.labelPerfil = tk.Label(
            self.menu_lateral, image=self.perfil, bg=COLOR_MENU_LATERAL)
        self.labelPerfil.pack(side=tk.TOP, pady=20)

        # Configuración del menú lateral
        ancho_menu = 20
        alto_menu = 2
        font_awesome = font.Font(family='FontAwesome', size=15)

#============================================================================================================#
#                                      CONFIGURACIÓN DE LOS BOTONES                                          #
#============================================================================================================# 
        #------------------------------------ BOTONES MENÚ LATERAL ------------------------------------------#
        self.buttonSettings = tk.Button(self.menu_lateral)
        self.buttonInfo = tk.Button(self.menu_lateral)                    
        self.buttonExit = tk.Button(self.menu_lateral)

        buttons_info = [
             #Repuestos por si el ícono no funciona: (f085) (f0ad) (f1de) (f013)
            ("Ajustes", "\uf1de", self.buttonSettings, self.abrir_ajustes), 
            ("Info", "\uf05a", self.buttonInfo, self.abrir_panel_info),
            ("Salir", "\uf2f6", self.buttonExit, self.cerrar_programa)
        ]

        for text, icon, button, comando in buttons_info:
            self.personalizar_boton_menu(button, text, icon, font_awesome, ancho_menu, alto_menu, comando)

    #-------------------------------------- BOTONES SUPERIORES ----------------------------------------------#
    def configurar_botones_superiores(self):   
       # Botones y opciones de la barra superior
        self.btn_expandir = tk.Button(self.cuerpo_principal, text="Expandir", font=("Arial", 10,"bold"), 
                                      bg=COLOR_BTN_EXPANDIR, fg=COLOR_LETRAS_BTN_SUPERIORES, 
                                      command=self.abrir_grafica_expandida)
        self.btn_expandir.place(x=120, y=30, width=75, height=30)

        self.btn_unidades = tk.Button(self.cuerpo_principal, text="Unidades", font=("Arial", 10,"bold"), 
                                      bg=COLOR_BTN_UNIDADES, fg=COLOR_LETRAS_BTN_SUPERIORES, 
                                      command=self.abrir_unidades)
        self.btn_unidades.place(x=215, y=30, width=75, height=30)


        #------------------------------------- CASILLAS SUPERIORES ------------------------------------------#
        self.lined_var = tk.BooleanVar(value=False)  

        self.check_lines = tk.Checkbutton(self.cuerpo_principal, text="Líneas", variable=self.lined_var, 
                             command=self.toggle_lines, bg=COLOR_CUERPO_PRINCIPAL, font=("Arial", 10))
        self.check_lines.place(x=700, y=30, width=80, height=30)

        self.grid_var = tk.BooleanVar()
        self.check_grid = tk.Checkbutton(self.cuerpo_principal, text="Cuadrícula", variable=self.grid_var, 
                                         command=self.toggle_grid, 
                                         bg=COLOR_CUERPO_PRINCIPAL, font=("Arial", 10))
        self.check_grid.place(x=800, y=30, width=80, height=30)

    #---------------------------------------- BOTONES INFERIORES --------------------------------------------#
    def configurar_botones_inferiores(self):
        # Creación de botones inferiores
        btn_style = {
            "font": ("Arial", 12, "bold"),
            "bd": 2,
            "relief": "raised"
        }

        self.btn_inicio = tk.Button(self.cuerpo_principal, text="Inicio", 
                                    bg=COLOR_BTN_START, fg=COLOR_LETRAS_BTN_INFERIORES, **btn_style)
        self.btn_inicio.place(x=130, y=580, width=90, height=40)

        self.btn_pausa = tk.Button(self.cuerpo_principal, text="Pausa", 
                                   bg=COLOR_BTN_PAUSE, fg=COLOR_LETRAS_BTN_INFERIORES, **btn_style)
        self.btn_pausa.place(x=240, y=580, width=90, height=40)

        self.btn_parar = tk.Button(self.cuerpo_principal, text="Parar", 
                                   bg=COLOR_BTN_STOP, fg=COLOR_LETRAS_BTN_INFERIORES, **btn_style)
        self.btn_parar.place(x=350, y=580, width=90, height=40)

        self.btn_home = tk.Button(self.cuerpo_principal, text="Home  \uf015", font=("FontAwesome", 12,"bold"), 
                                        bd=2, bg=COLOR_BTN_HOME, fg=COLOR_LETRAS_BTN_INFERIORES, 
                                        width=8, height=1, relief="raised")
        self.btn_home.place(x=780, y=580, width=90, height=40)

        self.btn_delete = tk.Button(self.cuerpo_principal, text="Borrar  \uf2ed", font=("FontAwesome", 12,"bold"),  #\uf2ed  \uf1f8  \uf829 \uf82a
                                            bd=2, bg=COLOR_BTN_BORRAR, fg=COLOR_LETRAS_BTN_INFERIORES,
                                            command=self.confirmar_borrado,
                                            width=8, height=1, relief="raised")
        self.btn_delete.place(x=1210, y=580, width=90, height=40)

#============================================================================================================#
#                                      CONFIGURACIÓN DE LA GRÁFICA                                           #
#============================================================================================================# 
    def configurar_grafica(self):    
        # Inicializa listas vacías para cuando lleguen los datos reales desde Arduino
        self.x = []
        self.y = []

        # Crear la figura y la gráfica
        self.fig, self.ax = plt.subplots(figsize=(7, 5))
        self.fig.patch.set_facecolor(COLOR_CUERPO_PRINCIPAL)  # Ajustar el fondo de la figura
        self.ax.set_facecolor("white")  # Fondo blanco

        # Inicializa la gráfica sin lineas, para que se puedan activar con la casilla
        estilo = '-' if self.lined_var.get() else 'None'
        self.linea, = self.ax.plot([], [], linestyle=estilo, marker='o', color=self.color_grafica, label="Coordenadas")

        # Configurar los límites fijos según dimensiones máximas de la pieza
        self.ax.set_xlim(0, 15)
        self.ax.set_ylim(0, 6.5)

        # Configurar etiquetas y leyenda
        self.ax.set_xlabel("X (mm)")
        self.ax.set_ylabel("Y (mm)")
        self.ax.legend()
        self.ax.grid(self.grid_var.get())  # Sincroniza con la opción del grid
        self.ax.set_position([0.05, 0.1, 0.8, 0.9])  # [izquierda, abajo, ancho, alto]

        # Incrustar la gráfica en Tkinter
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.cuerpo_principal)
        self.canvas.get_tk_widget().config(bg=COLOR_CUERPO_PRINCIPAL, highlightthickness=0)  # Fondo del widget
        self.canvas.get_tk_widget().place(x=50, y=70, width=1000, height=500)
        self.canvas.draw()

#============================================================================================================#
#                                   CONFIGURACIÓN DE LA TABLA DE DATOS                                       #
#============================================================================================================# 
    def configurar_tabla(self):
        # Título
        self.titulo_label = tk.Label(self.cuerpo_principal, text="Datos de la Gráfica", 
                                    font=("Arial", 16, "bold"), bg=COLOR_CUERPO_PRINCIPAL)
        self.titulo_label.place(x=1000, y=20, width=300, height=50)

        # Estilos
        style = ttk.Style()
        style.configure("Treeview", rowheight=53, font=("Arial", 13))
        style.configure("Treeview.Heading", font=("Arial", 14, "bold"), padding=(5, 5))

        # Frame y tabla
        self.tree_frame = tk.Frame(self.cuerpo_principal, bg=COLOR_CUERPO_PRINCIPAL)
        self.tree_frame.place(x=1000, y=70, width=300, height=450)

        self.tree = ttk.Treeview(self.tree_frame, columns=("N°", "X", "Y"), show="headings", height=15)

        columnas = [("N°", 40), ("X", 60), ("Y", 60)]
        for col, ancho in columnas:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=ancho, anchor="center")

        for i, (x, y) in enumerate(zip(self.x, self.y), start=1):
            self.tree.insert("", "end", values=(i, x, y))

        # Scrollbar
        scrollbar = ttk.Scrollbar(self.tree_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

#============================================================================================================#
#                                                                                                            #
#                                           MÉTODOS ADICIONALES                                              #
#                                                                                                            #
#============================================================================================================#
    #------------------------------------- ACTUALIZAR LA GRÁFICA --------------------------------------------#    
    def actualizar_grafica(self, nuevo_x, nuevo_y):
        """Agrega un nuevo punto a la gráfica y actualiza tanto la vista principal como la expandida."""
        self.x = np.append(self.x, nuevo_x)
        self.y = np.append(self.y, nuevo_y)

        # Actualizar gráfica principal
        self.linea.set_data(self.x, self.y)
        self.ax.relim()
        self.ax.autoscale_view()
        self.canvas.draw()

        # Actualizar tabla
        indice = len(self.x)  # o len(self.tree.get_children()) + 1
        self.tree.insert("", "end", values=(indice, nuevo_x, nuevo_y))

        # Actualizar gráfica expandida si está abierta
        if self.ventana_expandida and hasattr(self, 'linea_expandida'):
            self.linea_expandida.set_data(self.x, self.y)
            self.ax_expandido.relim()
            self.ax_expandido.autoscale_view()
            self.canvas_expandido.draw()

    #----------------------------- CONFIGURACIÓN DE LA GRÁFICA EXPANDIDA ------------------------------------# 
    def abrir_grafica_expandida(self):
        # Abre la gráfica en una ventana nueva si no está ya abierta
        if self.ventana_expandida and self.ventana_expandida.winfo_exists():
            self.ventana_expandida.lift()  # Traer la ventana al frente
            self.ventana_expandida.focus_force()  # Asegurar que reciba el foco
            return

        self.ventana_expandida = tk.Toplevel(self.ventana)
        self.ventana_expandida.title("Gráfica Expandida")
        self.ventana_expandida.geometry("900x700")
        self.ventana_expandida.configure(bg=COLOR_CUERPO_PRINCIPAL)  
        self.ventana_expandida.iconbitmap("./images/icono_general.ico")

        self.fig_expandida, self.ax_expandido = plt.subplots(figsize=(8, 6))
        self.fig_expandida.patch.set_facecolor(COLOR_CUERPO_PRINCIPAL)  # Ajustar el fondo de la figura
        self.ax_expandido.set_facecolor("white")
        
        # Crear la línea expandida con los datos actuales
        estilo = '-' if self.lined_var.get() else ' '
        self.linea_expandida, = self.ax_expandido.plot(
            self.x, self.y, linestyle=estilo, color=self.color_grafica, marker='o', label="Coordenadas"
        )
       
        # Ejes, etiquetas y grid
        self.ax_expandido.set_xlim(0, 15)
        self.ax_expandido.set_ylim(0, 6.5)
        self.ax_expandido.set_xlabel("X (mm)")
        self.ax_expandido.set_ylabel("Y (mm)")
        self.ax_expandido.legend()

         # Aplicar el estado actual de las opciones de grid
        self.ax_expandido.grid(self.grid_var.get())  # Aplicar estado del grid

        # Incrustar la gráfica en la ventana expandida
        self.canvas_expandido = FigureCanvasTkAgg(self.fig_expandida, master=self.ventana_expandida)
        self.canvas_expandido.get_tk_widget().config(bg=COLOR_CUERPO_PRINCIPAL, highlightthickness=0)
        self.canvas_expandido.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        self.canvas_expandido.draw()

        # Cerrar la ventana expandida con Esc
        self.ventana_expandida.bind("<Escape>", lambda event: self.ventana_expandida.destroy())

    def redibujar_expandida(self):
        if self.ventana_expandida:
            # No se usa clear() ni plot de nuevo
            estilo = '-' if self.lined_var.get() else ' '
            self.linea_expandida.set_linestyle(estilo)
            self.ax_expandido.grid(self.grid_var.get())
            self.canvas_expandido.draw()

#------------------------------------------ SINCRONIZAR GRID ------------------------------------------------# 
    def toggle_grid(self):
        """ Sincroniza el grid entre ambas gráficas. """
        self.ax.grid(self.grid_var.get())
        self.canvas.draw()
        if self.ventana_expandida:
            self.ax_expandido.grid(self.grid_var.get())
            self.canvas_expandido.draw()

    #-------------------------------------- LÍNEAS DE LA GRÁFICA --------------------------------------------# 
    def toggle_lines(self): #Activa o desactiva las líneas entre los puntos.
        estilo = '-' if self.lined_var.get() else 'None'
        self.linea.set_linestyle(estilo)

        # Actualizar leyenda principal
        if self.ax.legend_:
            self.ax.legend_.remove()
        self.ax.legend()

        self.canvas.draw()

        # Actualizar gráfica expandida si está abierta
        if self.ventana_expandida and hasattr(self, 'linea_expandida'):
            self.linea_expandida.set_linestyle(estilo)

            # Eliminar leyenda previa
            if self.ax_expandido.legend_:
                self.ax_expandido.legend_.remove()

            # Forzar la regeneración de la leyenda (siempre)
            self.ax_expandido.legend()

            self.canvas_expandido.draw()

    #----------------------------- CONFIGURACIÓN DE BOTONES MENÚ LATERAL ------------------------------------# 
    def personalizar_boton_menu(self, button, text, icon, font_awesome, ancho_menu, alto_menu, comando):
        button.config(text=f"  {icon}    {text}", anchor="w", font=font_awesome,
                      bd=0, bg=COLOR_MENU_LATERAL, fg="white", width=ancho_menu, height=alto_menu, 
                      command=comando)
        button.pack(side=tk.TOP)
        self.bind_hover_events(button)

    def bind_hover_events(self, button):
        # Asociar eventos Enter y Leave con la función dinámica
        button.bind("<Enter>", lambda event: self.on_enter(event, button))
        button.bind("<Leave>", lambda event: self.on_leave(event, button))

    def on_enter(self, event, button):
        # Cambiar estilo al pasar el ratón por encima
        button.config(bg=COLOR_MENU_CURSOR_ENCIMA, fg='white')

    def on_leave(self, event, button):
        # Restaurar estilo al salir el ratón
        button.config(bg=COLOR_MENU_LATERAL, fg='white')

    #------------------------------------- ABRIR PANEL DE AJUSTES -------------------------------------------# 
    def abrir_ajustes(self):
        def actualizar_color(color):
            self.color_grafica = color

            # Actualizar color en línea principal
            self.linea.set_color(color)
            self.ax.legend().set_visible(False)  # Ocultar leyenda para forzar actualización
            self.ax.legend()  # Volver a generar la leyenda
            self.canvas.draw()

            # Actualizar color en línea expandida (si existe)
            if hasattr(self, "linea_expandida"):
                self.linea_expandida.set_color(color)
                self.ax_expandido.legend().set_visible(False)
                self.ax_expandido.legend()
                self.canvas_expandido.draw()

        SettingsDesign(on_color_change=actualizar_color, color_actual=self.color_grafica)

    #--------------------------------------- ABRIR PANEL DE INFO --------------------------------------------# 
    def abrir_panel_info(self):           
        InfoDesign()

    #------------------------------------- ABRIR PANEL DE UNIDADES ------------------------------------------# 
    def abrir_unidades(self):           
        UnidadesDesign()
        

    #---------------------------------------- CERRAR PROGRAMA -----------------------------------------------# 
    def cerrar_programa(self):
        sys.exit()  # Cierra todo el proceso
    
    #---------------------------------------- BORRAR DATOS --------------------------------------------------#
    def confirmar_borrado(self):
        DeleteDesign()

