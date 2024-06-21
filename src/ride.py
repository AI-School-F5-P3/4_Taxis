from fare import Fare
from time import time

# Creamos la clase Carrera en la que se desarrollara la funcionalidad de todo el movimiento del Taxi
class Ride:
    # Constructor que recibirá el parámetro fare (stop_fare y movement_fare) cuando se instancie en la clase Taximetro
    def __init__(self, fare):
        self.fare = fare
        # Atributo para indicar si la carrera ha comenzado o no
        self.in_ride = False
        # Atributo para indicar ue empieza el movimiento(ya que la carrera siempre empieza parada)
        self.in_movement = False
        # Atributo para contabilizar el tiempo que esta parado, se inicializa en 0
        self.time_stopped = 0
        # Atributo para contabilizar el tiempo que esta en movimiento, se inicializa en 0
        self.time_in_movement = 0
        # Atributo para guardar el momento de tiempo de inicio de la carrera
        self.time_start = 0
        # Atributo que guarda el momento de tiempo del ultimo cambio que se realizó. Ej.: Parado/Movimiento
        self.last_change = 0


    # Método para iniciar Carrera (que incluye que el programa se mantenga a la espera)
    def start(self):
        pass


    # Método Movimiento del Taxi (Parado/Movimiento) Cambiar los estados de parado o movimiento
    def change_state(self):
        pass

    
    # OPCIONAL MÉTODOS PARA STOP, SEMÁFORO Y ATASCO


    # Método para finalizar la carrera
    def finish_ride(self):
         if self.in_ride:
            self.in_ride = False  # Finaliza la carrera
            total_cost =  self.calculate_cost() # Calcula el costo total de la carrera
            taxi_emoji = "\U0001F695"
            print(f"{taxi_emoji} Finalizamos carrera. Coste total {round(total_cost, 2)}€")
            # return self.fare.total_cost  # Retorna el costo total de la carrera
            
         else:
            print("No estamos en carrera")
            return 0  # Si la carrera no ha empezado, retorna 0


    # Método para calcular el precio de la carrera
    def calculate_cost(self):
        stop_cost = self.time_stopped * self.fare.stop_fare
        movement_cost = self.time_in_movement * self.fare.movement_fare
        return stop_cost + movement_cost
