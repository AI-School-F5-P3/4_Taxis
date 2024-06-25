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


# Creamos la clase Taximetro en la que intanciaremos Tarifa y Carrera, y será en la que tendremos el menu de comandos del programa
class Taximeter:
    def __init__(self):
        # Preguntar al usuario si desea configurar tarifas personalizadas
        user_input = input("¿Desea configurar tarifas personalizadas? (s/n): ").strip().lower()
        if user_input == 's':
            # Si el usuario dice sí, solicitar las tarifas personalizadas
            try:
                custom_stop_fare = float(input("Ingrese la tarifa por segundo cuando el taxi está detenido: "))
                custom_movement_fare = float(input("Ingrese la tarifa por segundo cuando el taxi está en movimiento: "))
                self.fare = Fare(custom_stop_fare, custom_movement_fare)
            except ValueError:
                print("Entrada inválida, se aplicarán las tarifas por defecto.")
                self.fare = Fare(0.02, 0.05)  # Tarifas por defecto en caso de entrada inválida
        else:
            # Si el usuario dice no, usar las tarifas por defecto
            self.fare = Fare(0.02, 0.05)

        self.ride = Ride(self.fare)
        # Creamos un logger con el nombre de la clase actual, para identificar el origen de los mensajes de log
        self.logger = logging.getLogger(self.__class__.__name__)
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
            print(f"\n{BRIGHT_GREEN}Tarifas actualizadas correctamente!{RESET}")
        except ValueError:
            print(f"\n{RED_CIRCLE} Error: Por favor, introduzca un número válido.{RESET}")

    # Method to change the state of the taxi (moving or stopped)
    def change_state(self, movement):
        self.ride.change_state(movement)
         
    # Method to finish the ride and show the total fare
    def end_ride(self):
        self.ride.finish_ride()

def main():
    taximeter = Taximeter()
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

if __name__ == "__main__":
    main()

