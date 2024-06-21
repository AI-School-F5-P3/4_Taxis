import time
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

