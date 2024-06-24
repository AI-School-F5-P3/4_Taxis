from fare import Fare
from ride import Ride

# Creamos la clase Taximetro en la que intanciaremos Tarifa y Carrera, y será en la que tendremos el menu de comandos del programa
class Taximeter:
    def __init__(self):
        # Instanciamos la clase Tarifa y le pasamos los parámetros de las tarifas establecidas
        self.fare = Fare(0.02, 0.05)
        # Instanciamos la clase Ride pasándole el parámetro Tarifa
        self.ride = Ride(self.fare)

    # Method for the welcome message and command menu
    def command_menu(self):
        print("Welcome to the digital taximeter system.")
        print("Available commands:")
        print("  'i' - Start a new ride")
        print("  's' - Indicate that the taxi is stopped")
        print("  'm' - Indicate that the taxi is moving")
        print("  'f' - Finish the ride and show the total fare")
        print("  'e' - Exit the system")
        
    # Method to start a new ride
    def startride(self):
        self.ride.start()
        
    # Method to change the state of the taxi (moving or stopped)
    def change_state(self, movement):
        print("status - ", movement), 
        self.ride.change_state(movement)
         
    # Method to finish the ride and show the total fare
    def end_ride(self):
        print("entrando en finish ride")
        self.ride.finish_ride()

def main():
    taximeter = Taximeter()
    taximeter.command_menu()
    while True:
        command = input("Enter a command: ").strip().lower()
        if command == "i":
            taximeter.start_ride()
        elif command == "s":
            taximeter.change_state(False)
        elif command == "m":
            taximeter.change_state(True)
        elif command == "f":
            taximeter.end_ride()
        elif command == "e":
            print("Exiting the system.")
            break
        else:
            print("Unrecognized command. Please try again.")
            taximeter.command_menu()  # Show available commands again in case of an error

if __name__ == "__main__":
    main()

