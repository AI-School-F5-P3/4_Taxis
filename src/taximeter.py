from fare import Fare
from ride import Ride

# Definición de colores y estilos
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

BRIGHT_BLACK = "\033[90m"
BRIGHT_RED = "\033[91m"
BRIGHT_GREEN = "\033[92m"
BRIGHT_YELLOW = "\033[93m"
BRIGHT_BLUE = "\033[94m"
BRIGHT_MAGENTA = "\033[95m"
BRIGHT_CYAN = "\033[96m"
BRIGHT_WHITE = "\033[97m"

BOLD = "\033[1m"
DIM = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
BLINK = "\033[5m"
REVERSE = "\033[7m"
HIDDEN = "\033[8m"
STRIKETHROUGH = "\033[9m"

BG_BLACK = "\033[40m"
BG_RED = "\033[41m"
BG_GREEN = "\033[42m"
BG_YELLOW = "\033[43m"
BG_BLUE = "\033[44m"
BG_MAGENTA = "\033[45m"
BG_CYAN = "\033[46m"
BG_WHITE = "\033[47m"

BG_BRIGHT_BLACK = "\033[100m"
BG_BRIGHT_RED = "\033[101m"
BG_BRIGHT_GREEN = "\033[102m"
BG_BRIGHT_YELLOW = "\033[103m"
BG_BRIGHT_BLUE = "\033[104m"
BG_BRIGHT_MAGENTA = "\033[105m"
BG_BRIGHT_CYAN = "\033[106m"
BG_BRIGHT_WHITE = "\033[107m"

RESET = "\033[0m"

# Viajes y Transporte
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
        # Instanciamos la clase Tarifa y le pasamos los parámetros de las tarifas establecidas
        self.fare = Fare(0.02, 0.05)
        # Instanciamos la clase Ride pasándole el parámetro Tarifa
        self.ride = Ride(self.fare)

    # Method for the welcome message and command menu
    def command_menu(self):
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
            print(f"\n{BRIGHT_GREEN}{BG_BLACK} {SMILE} Gracias por viajar con 4TAXIS, su taxímetro digital {STAR}{STAR}{STAR}{STAR}{STAR} {RESET}\n") 
            print(f"Saliendo del sistema... \n")
            break
        else:
            print(f"{CELEBRATION} Unrecognized command. Please try again.")
            taximeter.command_menu()  # Show available commands again in case of an error

if __name__ == "__main__":
    main()

