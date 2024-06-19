
from fare import Fare
from ride import Ride

# Create the Taximeter class where we'll instantiate Fare and Ride,
# and where we'll have the program's command menu
class Taximeter:
    def __init__(self):
        # Instantiate the Fare class with the established fare parameters
        self.fare = Fare(0.02, 0.05)
        # Instantiate the Ride class, passing it the Fare instance
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
    def start_ride(self):
        self.ride.start_ride()
        print("Ride started.")

    # Method to change the state of the taxi (moving or stopped)
    def change_state(self, moving):
        self.ride.change_state(moving)
        state = "moving" if moving else "stopped"
        print(f"Taxi is now {state}.")

    # Method to finish the ride and show the total fare
    def end_ride(self):
        total_fare = self.ride.end_ride()
        print(f"Ride finished. Total fare: {total_fare:.2f}€")

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