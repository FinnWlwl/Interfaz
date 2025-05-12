#============================================================================================================#
#                                               MENÚ LATERAL                                                 #
#============================================================================================================# 
"""
Descripción:
Este script crea la ventana del menú lateral de la aplicación, mediante la función toggle_panel.
posteriormente al seleccionar el botón utilizando lambda, se ejecuta la función toggle_panel.
"""

#============================================================================================================#
#                                          MÉTODO: TOGGLE PANEL                                              #
#============================================================================================================# 
def toggle_panel(self):
    # Alternar visibilidad del menú lateral
    if self.menu_lateral.winfo_ismapped():
        # Ocultar el frame principal antes de modificarlo
        self.cuerpo_principal.pack_forget()
        self.menu_lateral.pack_forget()
        
        # Tamaño original de la pantalla
        self.ax.set_position([0.05, 0.1, 0.8, 0.9])  # [izquierda, abajo, ancho, alto]
        self.canvas.get_tk_widget().place(width=1000)
        self.canvas.draw()

        # Tamaño original de la tabla
        self.titulo_label.place(x=1000, width=300)
        self.tree_frame.place(x=1000, width=300)

        # Tamaño original de los botones superiores
        self.check_lines.place(x=700)
        self.check_grid.place(x=800)
        
        # Tamaño original de los botones inferiores
        self.btn_home.place(x=780)
        self.btn_delete.place(x=1210)

        # Volver a mostrar el frame principal
        self.cuerpo_principal.pack(side="right", fill="both", expand=True)

    else:
        # Ocultar el frame principal antes de modificarlo
        self.cuerpo_principal.pack_forget()
        self.menu_lateral.pack(side="left", fill="y")
        
        # Tamaño reducido de la pantalla
        self.ax.set_position([0.06, 0.1, 0.8, 0.9])  # [izquierda, abajo, ancho, alto]
        self.canvas.get_tk_widget().place(width=900)
        self.canvas.draw()

        # Tamaño reducido de la tabla
        self.titulo_label.place(x=850, width=250)
        self.tree_frame.place(x=850, width=250)

        # Tamaño reducido de los botones superiores
        self.check_lines.place(x=620)
        self.check_grid.place(x=720)

        # Tamaño reducido de los botones inferiores
        self.btn_home.place(x=710)
        self.btn_delete.place(x=1010)

        # Volver a mostrar el frame principal
        self.cuerpo_principal.pack(side="right", fill="both", expand=True)