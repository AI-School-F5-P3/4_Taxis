# test_ride.py

import pytest
from unittest.mock import patch, MagicMock
import time
from ride import Ride
from fare import Fare

@pytest.fixture
def fare():
    return Fare(0.02, 0.05)

@pytest.fixture
def ride(fare):
    return Ride(fare)

def test_start_ride(ride, capsys):
    with patch('time.time', return_value=1000):
        ride.start()
        captured = capsys.readouterr()
        assert ride.in_ride is True
        assert ride.in_movement is False
        assert ride.time_stopped == 0
        assert ride.time_in_movement == 0
        assert "Empieza la carrera" in captured.out

def test_start_ride_already_started(ride, capsys):
    ride.in_ride = True
    ride.start()
    captured = capsys.readouterr()
    assert "El viaje ya había comenzado" in captured.out

def test_change_state_to_movement(ride, capsys):
    ride.in_ride = True
    ride.in_movement = False
    ride.last_change = 1000
    with patch('time.time', return_value=1010):
        ride.change_state(True)
        captured = capsys.readouterr()
        assert ride.in_movement is True
        assert ride.time_stopped == 10
        assert "¡Vámonos!" in captured.out

def test_change_state_to_stop(ride, capsys):
    ride.in_ride = True
    ride.in_movement = True
    ride.last_change = 1000
    with patch('time.time', return_value=1010):
        ride.change_state(False)
        captured = capsys.readouterr()
        assert ride.in_movement is False
        assert ride.time_in_movement == 10
        assert "Nos detenemos" in captured.out

def test_change_state_when_not_started(ride, capsys):
    ride.in_ride = False
    ride.change_state(True)
    captured = capsys.readouterr()
    assert "El viaje aún no se ha iniciado" in captured.out

def test_finish_ride(ride, capsys):
    ride.in_ride = True
    ride.time_stopped = 100
    ride.time_in_movement = 200
    ride.fare.stop_fare = 0.02
    ride.fare.movement_fare = 0.05
    with patch('time.time', return_value=1300):
        ride.finish_ride()
        captured = capsys.readouterr()
        assert "Coste total 12.00€" in captured.out

def test_finish_ride_when_not_started(ride, capsys):
    ride.in_ride = False
    ride.finish_ride()
    captured = capsys.readouterr()
    assert "No estamos en carrera" in captured.out

def test_calculate_cost(ride):
    ride.time_stopped = 100
    ride.time_in_movement = 200
    ride.fare.stop_fare = 0.02
    ride.fare.movement_fare = 0.05
    total_cost = ride.calculate_cost()
    assert total_cost == 12.0

def test_ride_logging(mocker, fare):
    logger_mock = mocker.patch('ride.logging.getLogger')
    ride = Ride(fare)
    assert logger_mock.called_once_with('Ride')

def test_finish_ride_logging(ride, mocker):
    ride.in_ride = True
    ride.time_stopped = 100
    ride.time_in_movement = 200
    ride.fare.stop_fare = 0.02
    ride.fare.movement_fare = 0.05
    logger_mock = mocker.patch.object(ride.logger, 'info')
    with patch('time.time', return_value=1300):
        ride.finish_ride()
    assert logger_mock.called

def test_start_logging(ride, mocker):
    logger_mock = mocker.patch.object(ride.logger, 'info')
    with patch('time.time', return_value=1000):
        ride.start()
    assert logger_mock.called_once_with("Ride started. Taxi is stopped.")
