import os
import subprocess# Importar subprocces para ejecutar comandos del sistema, como abrir un archivo en el en el editor de texto predeterminado del sistema
import sys # Para evitar problemas de compatibilidad
import logging # Importamos este módulo, que proporciona una forma flexible de generar logs
from fare import Fare
from ride import Ride

# Verificar y crear la carpeta 'logs' si no existe
if not os.path.exists("logs"):
    os.makedirs("logs")

# Configurar el sistema de logging y establecer los parámetros
logging.basicConfig(
    level=logging.DEBUG, # Establece los niveles que se registrarán de mensajes, nivel DEBUG y superiores.
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', # Establece el formato de los mensajes de log
    handlers=[
        logging.FileHandler("logs/taximeter.log"), # Enviar los mensajes de log a un archivo lamado taximeter.log
    ]
)

# Definición de colores, estilos e iconos
BRIGHT_GREEN = "\033[92m"
ITALIC = "\033[3m"
BG_BLACK = "\033[40m"
RESET = "\033[0m"
TAXI = "\U0001F696"          # 🚖
FLAG = "\U0001F3C1"          # 🏁
GREEN_CIRCLE = "\U0001F7E2"  # 🟢
RED_CIRCLE = "\U0001F534"    # 🔴
CROSS_MARK = "\U0000274C"    # ❌
STAR = "\U00002B50"          # ⭐
DESTINATION_FLAG = "\U0001F3C1"  # 🏁
LOCATION_MARKER = "\U0001F4CD"   # 📍
CELEBRATION = "\U0001F389"       # 🎉
SMILE = "\U0001F600"     # 😀
THINKING = "\U0001F914"  # 🤔
EYE = "\U0001F441"  # 👁️
RED = "\033[31m"
WHITE = "\033[37m"  # Definición del color blanco
LOCK = "\U0001F512"  # 🔒

# Creamos la clase Taximetro en la que intanciaremos Tarifa y Carrera, y será en la que tendremos el menu de comandos del programa
class Taximeter:
    def __init__(self):       
        self.fare = Fare(0.02, 0.05)  # Tarifas por defecto en caso de entrada inválida       
        self.ride = Ride(self.fare) # Pasamos el precio de las tarifas a la clase Ride
        # Creamos un logger con el nombre de la clase actual, para identificar el origen de los mensajes de log
        self.logger = logging.getLogger(self.__class__.__name__)
        self.correct_password ='4taxis'

    def check_password(self, user_password):# Definición de la función 'check_password'
                                            # Comprueba si la contraseña introducida por el usuario, convertida a minúsculas
                                            # es igual a la contraseña correcta almacenada en el objeto, también convertida a minúsculas.
        if user_password.lower() == self.correct_password.lower():
            print(f"{CELEBRATION}Acceso concedido{CELEBRATION}")
            return True 
        else:
            print(f"Contraseña incorrecta. La contraseña ingresada fue:'{user_password}'")
            return False # Si la contraseña no es correcta, imprime un mensaje de error indicando la contraseña que se introdujo y devuelve False.
          
        # Instanciamos para que el user pueda cambiar la tarifa
       

    # Method for the welcome message and command menu
    def command_menu(self):
        self.logger.info("Mostrando el menú de comandos") 
        print(f"\n{BRIGHT_GREEN}{BG_BLACK} {TAXI} Bienvenido/a a 4TAXIS, su taxímetro digital {TAXI} {RESET}\n") 
        print(f" {ITALIC}Menú{RESET}\n")
        print(f"  'i' - {FLAG} Iniciar un nuevo viaje")
        print(f"  'u' - {THINKING} Actualizar tarifas del viaje") 
        print(f"  'm' - {GREEN_CIRCLE} Indicar que el taxi está en movimiento")
        print(f"  's' - {RED_CIRCLE} Indicar que el taxi está detenido")        
        print(f"  'f' - {LOCATION_MARKER} Terminar el viaje y mostrar la tarifa total")
        print(f"  'h' - {EYE}  Consultar el historial de viajes")
        print(f"  'e' - {CROSS_MARK} Salir del sistema\n")
       
    # Method to start a new ride
    def start_ride(self):
        self.ride.start()
    
    # Method to custom the fare
    def update_fares(self):
        try:
            custom_stop_fare = float(input("Ingrese la tarifa por segundo cuando el taxi está detenido: "))
            custom_movement_fare = float(input("Ingrese la tarifa por segundo cuando el taxi está en movimiento: "))
            self.fare.stop_fare = custom_stop_fare
            self.fare.movement_fare = custom_movement_fare
            print(f"\n{BRIGHT_GREEN}Tarifas actualizadas correctamente!{RESET} {custom_movement_fare}€ en movimiento y {custom_stop_fare}€ en pausa.")
        except ValueError:
            print(f"\n{RED_CIRCLE} Error: Por favor, introduzca un número válido.{RESET}")
    
    #Actualizar las tarifas desde la interfaz gráfica
    def update_fares_ttk(self,custom_movement_fare,custom_stop_fare):
        try:
            self.fare.stop_fare = custom_stop_fare
            self.fare.movement_fare = custom_movement_fare
            print(f"\n{BRIGHT_GREEN}Tarifas actualizadas correctamente!{RESET} {custom_movement_fare}€ en movimiento y {custom_stop_fare}€ en pausa.")
        except ValueError:
            print(f"\n{RED_CIRCLE} Error: Por favor, introduzca un número válido.{RESET}")

    # Method to change the state of the taxi (moving or stopped)
    def change_state(self, movement):
        self.ride.change_state(movement)
         
    # Method to finish the ride and show the total fare
    def end_ride(self):
        self.ride.finish_ride()

    # Method to show all the save rides    
    def show_rides_history(self):        
        log_file_path = os.path.abspath("logs/rides_history.txt")  # Ruta absoluta al archivo
        try:
            # Abrir el archivo "rides_history.txt" en modo lectura
            with open("logs/rides_history.txt", "r") as file:
                print(f"\n{EYE}{WHITE} Historial de carreras:{RESET}\n")
                # Imprime el contenido del historial de carreras
                print(file.read())

            # Abrir el archivo en el editor de texto predeterminado del sistema
            if sys.platform.startswith('win'):  # Comprobación para sistemas Windows
                os.startfile(log_file_path )
            elif sys.platform.startswith('linux') or sys.platform.startswith('darwin'):  # Comprobación para sistemas Unix/Linux/MacOS
                subprocess.Popen(['xdg-open', log_file_path ])
                
        except FileNotFoundError:
            # Si el archivo no existe, captura la excepción FileNotFoundError
            # Imprime un mensaje indicando que no hay historial de carreras
            print(f"\n{RED}{CROSS_MARK}Todavia no hay historial de carreras.{RESET}\n")


def main():
    taximeter = Taximeter()
    while True: # bucle infinito que Solicita al usuario que ingrese una contraseña. 
                #La función 'strip()' se utiliza para eliminar los espacios en blanco al principio y al final.
            user_password = input(f"{LOCK} Ingrese la contraseña para desbloquear el sistema{LOCK}  ").strip()
            if user_password.lower() == "salir":  # definimos variable de escape
                print("Saliendo del programa...")
                exit()  # Sale completamente del programa
            elif taximeter.check_password(user_password):
                break  # Si la contraseña es correcta, se rompe el bucle infinito con 'break'
            else: # Si la contraseña no es correcta, se imprime un mensaje de error y el bucle continúa
                print("Contraseña incorrecta, por favor inténtelo de nuevo")
    taximeter.command_menu()
    while True:
        command = input(f"Ingrese un comando:").strip().lower()
        if command == "i":
            taximeter.start_ride()
        elif command == "u":
            taximeter.update_fares()
        elif command == "s":
            taximeter.change_state(False)
        elif command == "m":
            taximeter.change_state(True)
        elif command == "f":
            taximeter.end_ride()
        elif command == "h":
            taximeter.show_rides_history()
        elif command == "e":
            taximeter.logger.info("Exiting the system.")  # Log de información cuando se sale del sistema
            print(f"\n{BRIGHT_GREEN}{BG_BLACK} {SMILE} Gracias por viajar con 4TAXIS, su taxímetro digital {STAR}{STAR}{STAR}{STAR}{STAR} {RESET}\n") 
            print(f"Saliendo del sistema... \n")
            break
        else:
            # Log de advertencia cuando se ingresa un comando no reconocido
            taximeter.logger.warning(f"Unrecognized command: {command}")              
            print(f"{CELEBRATION} Unrecognized command. Please try again.")
            taximeter.command_menu()  # Show available commands again in case of an error

if __name__ == '__main__':
    main()