from fare import Fare
from ride import Ride

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

