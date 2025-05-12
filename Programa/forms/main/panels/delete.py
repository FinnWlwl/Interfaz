#============================================================================================================#
#                                          DISEÑO VENTANA: BORRAR                                            #
#============================================================================================================#
"""
Descripción:
Este script crea una ventana de aviso para confirmar la eliminación de los datos de la tabla y gráfica.
"""

#============================================================================================================#
#                                      IMPORTACIÓN DE LIBRERÍAS                                              #
#============================================================================================================#
import tkinter as tk
import util.generic as util_ventana

#============================================================================================================#
#                                     INICIO DE VENTANA DE BORRADO                                           #
#============================================================================================================#
class DeleteDesign():
    ventana_aviso = None  # Variable de clase para controlar una sola instancia

    def __init__(self, ejecutar_borrado_callback):
        # Verificar si la ventana ya está abierta antes de crear una nueva
        if DeleteDesign.ventana_aviso and DeleteDesign.ventana_aviso.winfo_exists():
            DeleteDesign.ventana_aviso.lift()  # Traer la ventana al frente si ya existe
            return 

        self.ejecutar_borrado_callback = ejecutar_borrado_callback
        self.configurarVentana()
        self.construirWidget()
        self.ventana_aviso.mainloop()

#============================================================================================================#
#                                   CONFIGURACIÓN DE LA VENTANA DE AVISO                                     #
#============================================================================================================#
    def configurarVentana(self):   
        self.ventana_aviso = tk.Toplevel()  
        self.ventana_aviso.withdraw()  # Ocultar temporalmente la ventana         

        self.ventana_aviso.title('Confirmar borrado')
        self.ventana_aviso.iconbitmap("./images/icono_info.ico")
        w, h = 300, 150

        util_ventana.centrar_ventana(self.ventana_aviso, w, h)  # Centrar ventana

        self.ventana_aviso.resizable(False, False)  
        self.ventana_aviso.deiconify()  # Mostrar la ventana correctamente centrada

        self.ventana_aviso.protocol("WM_DELETE_WINDOW", self.on_close)
        DeleteDesign.ventana_aviso = self.ventana_aviso
        self.ventana_aviso.bind("<Escape>", lambda event: self.ventana_aviso.destroy())

#============================================================================================================#
#                                         DISEÑO DE LA VENTANA                                               #
#============================================================================================================#
    def construirWidget(self): 
        frame = tk.Frame(self.ventana_aviso, bg="white")
        frame.pack(expand=True, fill="both")

        label = tk.Label(frame, text="¿Estás seguro de que quieres borrar\ntodos los datos?", 
                         font=("Arial", 12), bg="white", justify="center")
        label.pack(pady=20)

        botones = tk.Frame(frame, bg="white")
        botones.pack()

        btn_si = tk.Button(botones, text="Sí", width=10, bg="#d32f2f", fg="white",
                           command=self.confirmar_borrado)
        btn_si.pack(side="left", padx=10)

        btn_no = tk.Button(botones, text="No", width=10, command=self.ventana_aviso.destroy)
        btn_no.pack(side="right", padx=10)

#============================================================================================================#
#                                   CONFIRMAR Y EJECUTAR BORRADO                                             #
#============================================================================================================#
    def confirmar_borrado(self):
        self.ventana_aviso.destroy()
        DeleteDesign.ventana_aviso = None
        self.ejecutar_borrado_callback()

#============================================================================================================#
#                                        CERRADO DE LA VENTANA                                               #
#============================================================================================================#
    def on_close(self):
        DeleteDesign.ventana_aviso = None
        self.ventana_aviso.destroy()
