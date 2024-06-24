import unittest
from unittest.mock import MagicMock, patch
from taximeter import Taximeter

class TestTaximeter(unittest.TestCase):

    def setUp(self):
        # Parchear las clases Fare y Ride antes de cada prueba
        self.patcher_fare = patch('taximeter.Fare')
        self.patcher_ride = patch('taximeter.Ride')

        self.MockFare = self.patcher_fare.start()
        self.MockRide = self.patcher_ride.start()

        self.mock_fare_instance = self.MockFare.return_value
        self.mock_ride_instance = self.MockRide.return_value

        self.taximeter = Taximeter()

    def tearDown(self):
        self.patcher_fare.stop()
        self.patcher_ride.stop()

    def test_command_menu(self):
        # Redirigir la salida estándar a un StringIO para capturar la salida
        from io import StringIO
        import sys
        captured_output = StringIO()
        sys.stdout = captured_output

        self.taximeter.command_menu()
        sys.stdout = sys.__stdout__

        output = captured_output.getvalue().strip()
        expected_output = (
            "Welcome to the digital taximeter system.\n"
            "Available commands:\n"
            "  'i' - Start a new ride\n"
            "  's' - Indicate that the taxi is stopped\n"
            "  'm' - Indicate that the taxi is moving\n"
            "  'f' - Finish the ride and show the total fare\n"
            "  'e' - Exit the system"
        )
        self.assertEqual(output, expected_output)

    def test_start_ride(self):
        self.taximeter.start_ride()
        self.mock_ride_instance.start.assert_called_once()

    def test_change_state_to_moving(self):
        self.taximeter.change_state(True)
        self.mock_ride_instance.change_state.assert_called_once_with(True)

    def test_change_state_to_stopped(self):
        self.taximeter.change_state(False)
        self.mock_ride_instance.change_state.assert_called_once_with(False)

    def test_end_ride(self):
        # Redirigir la salida estándar a un StringIO para capturar la salida
        from io import StringIO
        import sys
        captured_output = StringIO()
        sys.stdout = captured_output

        self.taximeter.end_ride()
        sys.stdout = sys.__stdout__

        output = captured_output.getvalue().strip()
        expected_output = "entrando en finish ride"
        self.assertIn(expected_output, output)
        self.mock_ride_instance.finish_ride.assert_called_once()

if __name__ == '__main__':
    unittest.main()
