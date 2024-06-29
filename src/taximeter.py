import logging # Importamos este módulo, que proporciona una forma flexible de generar logs
from fare import Fare
from ride import Ride


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
LOCK = "\U0001F512"  # 🔒


# Creamos la clase Taximetro en la que intanciaremos Tarifa y Carrera, y será en la que tendremos el menu de comandos del programa
class Taximeter:
    def __init__(self):
        # Instanciamos la clase Tarifa y le pasamos los parámetros de las tarifas establecidas
        self.fare = Fare(0.02, 0.05)
        # Instanciamos la clase Ride pasándole el parámetro Tarifa
        self.ride = Ride(self.fare)
        # Creamos un logger con el nombre de la clase actual, para identificar el origen de los mensajes de log
        self.logger = logging.getLogger(self.__class__.__name__)
        self.correct_password ='4taxis'

    # Definición de la función 'check_password'. Esta es una función de instancia, lo que significa que se aplica a un objeto específico de una clase.
   
    def check_password(self, user_password): # Comprueba si la contraseña introducida por el usuario, convertida a minúsculas,
                                             #es igual a la contraseña correcta almacenada en el objeto, también convertida a minúsculas.
        if user_password.lower() == self.correct_password.lower():
            print(f"{CELEBRATION}Acceso concedido{CELEBRATION}")
            return True  # Si la contraseña es correcta, imprime un mensaje de éxito y devuelve True.
        else:
            print(f"Contraseña incorrecta. La contraseña ingresada fue:'{user_password}'")
            return False
        # Si la contraseña no es correcta, imprime un mensaje de error indicando la contraseña que se introdujo y devuelve False.


    # Method for the welcome message and command menu
    def command_menu(self):
        self.logger.info("Mostrando el menú de comandos") 
        print(f"\n{BRIGHT_GREEN}{BG_BLACK} {TAXI} Bienvenido/a a 4TAXIS, su taxímetro digital {TAXI} {RESET}\n") 
        print(f" {ITALIC}Menú{RESET}\n")
        print(f"  'i' - {FLAG} Iniciar un nuevo viaje")
        print(f"  'm' - {GREEN_CIRCLE} Indicar que el taxi está en movimiento")
        print(f"  's' - {RED_CIRCLE} Indicar que el taxi está detenido")        
        print(f"  'f' - {LOCATION_MARKER} Terminar el viaje y mostrar la tarifa total")
        print(f"  'e' - {CROSS_MARK} Salir del sistema\n")
       
    # Method to start a new ride
    def start_ride(self):
        self.ride.start()
        
    # Method to change the state of the taxi (moving or stopped)
    def change_state(self, movement):
        self.ride.change_state(movement)
         
    # Method to finish the ride and show the total fare
    def end_ride(self):
        self.ride.finish_ride()

def main():
    taximeter = Taximeter()
    while True:                     # Este es un bucle infinito que se ejecuta hasta que se cumple una condición de salida.
        user_password = input(f"{LOCK} Ingrese la contraseña para desbloquear el sistema{LOCK}  ").strip()
                  # Solicita al usuario que ingrese una contraseña. La función 'strip()' se utiliza para eliminar los espacios en blanco al principio y al final.
        if taximeter.check_password(user_password): # Comprueba si la contraseña introducida por el usuario es correcta utilizando
                                                    # la función 'check_password' del objeto 'taximeter'.
            break # Si la contraseña es correcta, se rompe el bucle infinito con 'break'
        print("Contraseña incorrecta, por favor intentelo de nuevo")
    taximeter.command_menu()
    while True:
        command = input(f"Ingrese un comando:").strip().lower()
        if command == "i":
            taximeter.start_ride()
        elif command == "s":
            taximeter.change_state(False)
        elif command == "m":
            taximeter.change_state(True)
        elif command == "f":
            taximeter.end_ride()
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
