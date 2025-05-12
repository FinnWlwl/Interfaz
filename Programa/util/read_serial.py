#============================================================================================================#
#                                         LECTURA DEL PUERTO SERIAL                                          #
#============================================================================================================#
"""
Descripción:
Este módulo se encarga de leer datos desde un puerto serial utilizando la librería pyserial, también permite
detectar si el Arduino se encuentra conectado al puerto COM 5, hasta que este se conecte, sin embargo, si se
conecta y desconecta el Arduino es incapaz de reconectar la lectura sin reiniciar el programa.
"""

#============================================================================================================#
#                                      IMPORTACIÓN DE LIBRERÍAS                                              #
#============================================================================================================#
import serial

#============================================================================================================#
#                                           INICIO DEL SCRIPT                                                #
#============================================================================================================#
class ReadSerial:
    def __init__(self, ventana, callback):
        self.ventana = ventana
        self.callback = callback
        self.ser = None
        self.intentar_conectar()
    
    def intentar_conectar(self):
        try:
            self.ser = serial.Serial('COM5', 9600, timeout=1)
            print("[OK] Conectado a COM5")
            self.ventana.after(100, self.leer_datos_serial)
        except serial.SerialException as e:
            print("[ERROR] No se pudo abrir COM5. Reintentando...")
            self.ventana.after(1000, self.intentar_conectar)
    
    def leer_datos_serial(self):
        try:
            if self.ser and self.ser.in_waiting:
                linea = self.ser.readline().decode('utf-8').strip()
                x_str, y_str = linea.split(',')
                nuevo_x = float(x_str)
                nuevo_y = float(y_str)
                self.callback(nuevo_x, nuevo_y)
        except Exception as e:
            print("Error en lectura serial:", e)

        self.ventana.after(100, self.leer_datos_serial)


