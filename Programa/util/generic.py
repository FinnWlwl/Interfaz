#============================================================================================================#
#                                FUNCIONES AUXILIARES PARA INTERFAZ GRÁFICA                                  #
#============================================================================================================#
"""
Descripción:
Este módulo contiene funciones auxiliares para la manipulación de imágenes y la configuración de ventanas.
Facilita leer las imágenes usando la librería Pillow (PIL).
"""

#============================================================================================================#
#                                          IMPORTACIÓN DE LIBRERÍAS                                          #
#============================================================================================================#
from PIL import ImageTk, Image  # Librería Pillow para manipulación de imágenes

#============================================================================================================#
#                                                  FUNCIONES                                                 #
#============================================================================================================#
def leer_imagen(path, size): #Función para poder leer imágenes
        return ImageTk.PhotoImage(Image.open(path).resize(size)) #Abre la imagen y la redimensiona a un tamaño específico

def centrar_ventana(ventana,aplicacion_ancho,aplicacion_largo): #Función para centrar imágenes
    pantalla_ancho = ventana.winfo_screenwidth() #Obtiene el ancho de la pantalla
    pantalla_largo = ventana.winfo_screenheight() #Obtiene el largo de la pantalla
    x = int((pantalla_ancho/2) - (aplicacion_ancho/2)) #Calcula la posición x para centrar la ventana
    y = int((pantalla_largo/2) - (aplicacion_largo/2)) #Calcula la posición y para centrar la ventana
    return ventana.geometry(f"{aplicacion_ancho}x{aplicacion_largo}+{x}+{y}") #Coloca la ventana en la posición calculada