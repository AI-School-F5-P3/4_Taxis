# test_app.py

import pytest # type: ignore
from unittest.mock import MagicMock
from app import App  # Asegúrate de que el nombre del archivo que contiene la clase App es app.py
from taximeter import Taximeter
import ttkbootstrap as ttk # type: ignore
from tkinter import Toplevel

@pytest.fixture
def app_tkinter():
    """Fixture para configurar y limpiar la instancia de la App con un master simulado."""
    master = ttk.Window()
    app = App(master)
    yield app
    master.destroy()

def test_app_initialization(app_tkinter):
    """Probar la inicialización de la aplicación y la creación de la interfaz de autenticación."""
    assert app_tkinter.taximeter is not None
    assert isinstance(app_tkinter.taximeter, Taximeter)
    assert app_tkinter.password_frame.winfo_ismapped()

def test_check_password_correct(app_tkinter):
    """Probar la verificación de la contraseña correcta."""
    app_tkinter.taximeter.check_password = MagicMock(return_value=True)
    app_tkinter.password_entry.insert(0, "correct_password")
    app_tkinter.check_password()
    assert not app_tkinter.password_frame.winfo_ismapped()

def test_check_password_incorrect(app_tkinter):
    """Probar la verificación de la contraseña incorrecta."""
    app_tkinter.taximeter.check_password = MagicMock(return_value=False)
    app_tkinter.password_entry.insert(0, "incorrect_password")
    app_tkinter.check_password()
    error_labels = [child for child in app_tkinter.password_frame.winfo_children() if isinstance(child, ttk.Label) and "incorrecta" in child.cget("text")]
    assert len(error_labels) > 0

def test_create_main_interface(app_tkinter):
    """Probar la creación de la interfaz principal."""
    app_tkinter.create_main_interface()
    assert app_tkinter.console_label.winfo_ismapped()

def test_start_button_click(app_tkinter):
    """Probar el funcionamiento del botón de inicio."""
    app_tkinter.taximeter.ride = MagicMock()
    app_tkinter.taximeter.ride.in_ride = False
    app_tkinter.taximeter.fare = MagicMock()
    app_tkinter.taximeter.fare.stop_fare = 0.02
    app_tkinter.start_button_click()
    assert app_tkinter.console_label.cget("text") == "¡Hola! El taxi esta detenido.\n\nTaxímetro corriendo a 0.02€ por segundo."

def test_create_fares_window(app_tkinter):
    """Probar la creación de la ventana de tarifas."""
    app_tkinter.create_fares_window()
    assert isinstance(app_tkinter.fares_window, Toplevel)

def test_update_fares(app_tkinter):
    """Probar la actualización de las tarifas."""
    app_tkinter.create_fares_window()
    app_tkinter.movement_fare_entry.insert(0, "0.05")
    app_tkinter.stop_fare_entry.insert(0, "0.03")
    app_tkinter.taximeter.update_fares_ttk = MagicMock()
    app_tkinter.update_fares()
    app_tkinter.taximeter.update_fares_ttk.assert_called_with(0.05, 0.03)
    assert not app_tkinter.fares_window.winfo_ismapped()

def test_exit_button_click(app_tkinter):
    """Probar el funcionamiento del botón de salida."""
    app_tkinter.exit_button_click()
    assert not app_tkinter.master.winfo_exists()
