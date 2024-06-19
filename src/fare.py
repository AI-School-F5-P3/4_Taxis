# Creamos la clase Tarifa que recibira los precios 
class Fare:
    # Constructor que tiene los parámetros de las tarifas stop y movement
    def __init__(self, stop_fare, movement_fare):
        self.stop_fare = stop_fare
        self.movement_fare = movement_fare

# OPCIONAL MÉTODO PARA MODIFICAR TARIFA