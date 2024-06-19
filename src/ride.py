import time #Importamos el modulo time para trabajar con tiempo
from fare import Fare
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
        self.in_ride = True #Inicia la carrera
        self.time_start = time.time()  # Registra el tiempo de inicio de la carrera


    # Método Movimiento del Taxi (Parado/Movimiento) Cambiar los estados de parado o movimiento
    def change_state(self):
        if self.in_ride:
            current_time = time.time()
            if self.in_movement:  # Si el taxi está en movimiento
                self.time_in_movement += current_time - self.last_change  # Acumula el tiempo en movimiento
            else:
                self.time_stopped += current_time - self.last_change  # Acumula el tiempo parado
            self.in_movement = not self.in_movement  # Cambia el estado del taxi
            self.last_change = current_time  # Actualiza el momento del último cambio

    # Método para finalizar la carrera
    def finish_ride(self):
        if self.in_ride:
            self.calculate_cost()  # Calcula el costo total de la carrera
            self.in_ride = False  # Finaliza la carrera
            return self.fare.total_cost  # Retorna el costo total de la carrera
        else:
            return 0  # Si la carrera no ha empezado, retorna 0

    
    # Método para calcular el precio de la carrera
    def calculate_cost(self):
        if self.time_start and self.last_change:
            elapsed_time = time.time() - self.time_start  # Calcula el tiempo transcurrido
            if self.in_movement:
                self.time_in_movement += time.time() - self.last_change  # Acumula el tiempo en movimiento
            else:
                self.time_stopped += time.time() - self.last_change  # Acumula el tiempo parado
            
            self.fare.calculate_total_cost(self.time_stopped, self.time_in_movement)  # Calcula el costo total de la carrera