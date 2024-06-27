# test_taximeter.py


import pytest
from unittest.mock import patch, MagicMock
from taximeter import Taximeter
from fare import Fare
from ride import Ride

@pytest.fixture
def taximeter():
    return Taximeter()

def test_check_password_correct(taximeter):
    assert taximeter.check_password('4taxis') == True

def test_check_password_incorrect(taximeter):
    assert taximeter.check_password('wrongpassword') == False

def test_update_fares(taximeter):
    with patch('builtins.input', side_effect=['0.03', '0.06']):
        taximeter.update_fares()
    assert taximeter.fare.stop_fare == 0.03
    assert taximeter.fare.movement_fare == 0.06

def test_update_fares_invalid_input(taximeter, capsys):
    with patch('builtins.input', side_effect=['invalid', '0.06']):
        taximeter.update_fares()
    captured = capsys.readouterr()
    assert 'Error: Por favor, introduzca un número válido.' in captured.out

def test_start_ride(taximeter):
    ride_mock = MagicMock()
    taximeter.ride = ride_mock
    taximeter.start_ride()
    ride_mock.start.assert_called_once()

def test_change_state(taximeter):
    ride_mock = MagicMock()
    taximeter.ride = ride_mock
    taximeter.change_state(True)
    ride_mock.change_state.assert_called_once_with(True)

def test_end_ride(taximeter):
    ride_mock = MagicMock()
    taximeter.ride = ride_mock
    taximeter.end_ride()
    ride_mock.finish_ride.assert_called_once()

def test_show_rides_history_file_exists(taximeter, capsys):
    with patch('builtins.open', patch('builtins.open', MagicMock(return_value=iter(['Log entry'])))):
        with patch('os.path.exists', return_value=True):
            taximeter.show_rides_history()
    captured = capsys.readouterr()
    assert 'Historial de carreras:' in captured.out
    assert 'Log entry' in captured.out

def test_show_rides_history_file_not_exists(taximeter, capsys):
    with patch('builtins.open', side_effect=FileNotFoundError):
        taximeter.show_rides_history()
    captured = capsys.readouterr()
    assert 'Todavia no hay historial de carreras.' in captured.out
