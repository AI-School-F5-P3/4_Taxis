# Importar Path para manipulación de rutas de archivos
from pathlib import Path

# Importar ttkbootstrap para estilos modernos de widgets tkinter
import ttkbootstrap as ttk

# Importar constantes de ttkbootstrap para estilos y configuraciones
from ttkbootstrap.constants import *

# Importar Emoji para usar iconos en la interfaz
from ttkbootstrap.icons import Emoji

# Importar PIL para manejo de imágenes
from PIL import Image, ImageTk

# Importar la clase Taximeter, que contiene la lógica del taxímetro
from taximeter import Taximeter

# Importar Toplevel de tkinter para crear nuevas ventanas
from tkinter import Toplevel

# Definición de colores e iconos
BRIGHT_GREEN = "\033[92m"
ITALIC = "\033[3m"
BG_BLACK = "\033[40m"
RESET = "\033[0m"

TAXI = "\U0001F696"          # 🚖
FLAG = "\U0001F3C1"          # 🏁
GREEN_CIRCLE = "\U0001F7E2"  # 🟢
RED_CIRCLE = "\U0001F534"    # 🔴
CROSS_MARK = "\U0000274C"    # ❌
STAR = "\U00002B50"          # ⭐
DESTINATION_FLAG = "\U0001F3C1"  # 🏁
LOCATION_MARKER = "\U0001F4CD"   # 📍
CELEBRATION = "\U0001F389"       # 🎉
SMILE = "\U0001F600"     # 😀
THINKING = "\U0001F914"  # 🤔
CRY = "\U0001F622"       # 😢
RAISED_HAND = "\U0000270B"  # ✋
MONEY_BAG = "\U0001F4B0"      # 💰 
DOLLAR_BILL = "\U0001F4B5"    # 💵


class App(ttk.Frame):
    """
    Clase principal de la aplicación que representa la ventana principal
    de la interfaz gráfica de usuario (GUI) para el taxímetro digital.

    Hereda de ttk.Frame y utiliza ttkbootstrap para mejorar la apariencia
    de los widgets tkinter.

    Métodos:
        __init__(self, master):
            Constructor de la clase. Inicializa el marco y crea la interfaz de autenticación.
        create_password_interface(self):
            Crea la interfaz de usuario para la autenticación mediante contraseña.
        check_password(self):
            Verifica la contraseña ingresada y muestra la interfaz principal si es correcta.
        create_main_interface(self):
            Crea la interfaz principal de la aplicación después de la autenticación.
        create_header(self):
            Crea el encabezado de la aplicación con un mensaje de bienvenida y las instrucciones.
        create_image(self):
            Carga y muestra una imagen de fondo en la aplicación.
        create_message_area(self):
            Crea el área de mensajes para mostrar información al usuario.
        create_buttonbox(self):
            Crea la caja de botones para interactuar con la aplicación.
        start_button_click(self):
            Maneja la acción del botón de inicio.
        play_button_click(self):
            Maneja la acción del botón de reproducción.
        pause_button_click(self):
            Maneja la acción del botón de pausa.
        stop_button_click(self):
            Maneja la acción del botón de detención.
        logs_button_click(self):
            Maneja la acción del botón para ver los registros.
        fares_button_click(self):
            Maneja la acción del botón para actualizar las tarifas.
        exit_button_click(self):
            Maneja la acción del botón para salir de la aplicación.
        create_fares_window(self):
            Crea una ventana para actualizar las tarifas del taxímetro.
        cancel_fares(self):
            Maneja la acción de cancelar la actualización de tarifas.
        update_fares(self):
            Actualiza las tarifas del taxímetro con los valores ingresados.
    """

    def __init__(self, master):
        """
        Constructor de la clase. Inicializa el marco y crea la interfaz de autenticación.
        
        Args:
            master (tk.Tk): La ventana principal de tkinter.
        """
        super().__init__(master)
        self.pack(fill=BOTH, expand=YES)
        
        self.taximeter = Taximeter()  # Instanciar la clase Taximeter
        
        self.create_password_interface()

    def create_password_interface(self):
        """Crear la interfaz de autenticación"""
        
        self.create_image()
        self.password_frame = ttk.Frame(self, padding=50)
        self.password_frame.pack(expand=True)
        
        password_label = ttk.Label(self.password_frame, text="Contraseña", font=("Helvetica", 10))
        password_label.pack(pady=10)

        self.password_entry = ttk.Entry(self.password_frame, show="*", width=20, font=("Helvetica", 12))
        self.password_entry.pack(pady=10)
        
        button_frame = ttk.Frame(self.password_frame)
        button_frame.pack(pady=15)
        
        cancel_button = ttk.Button(
            button_frame, 
            text="Cancelar", 
            bootstyle=SECONDARY, 
            command=self.exit_button_click, 
            width=11,
            padding=(10, 5),
        )
        cancel_button.pack(side=LEFT, padx=5)

        submit_button = ttk.Button(button_frame, text="Enviar", bootstyle=SUCCESS, command=self.check_password,width=11,padding=(10, 5))
        submit_button.pack(side=LEFT, padx=5)

    def check_password(self):
        """Verificar la contraseña ingresada"""
        if self.taximeter.check_password(self.password_entry.get()):
            self.password_frame.pack_forget()  # Ocultar el frame de la contraseña
            self.create_main_interface()  # Crear la interfaz principal
        else:
            error_label = ttk.Label(self.password_frame, text="Contraseña incorrecta", font=("Helvetica", 12), foreground="red")
            error_label.pack(pady=10)
            
    def create_main_interface(self):
        """Crear la interfaz principal de la aplicación"""
        self.create_header()
        self.create_image()
        self.create_message_area()
        self.create_buttonbox()

    def create_header(self):
        """El encabezado de la aplicación"""
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES)

        welcome = ttk.Label(
            master=container,
            text="Bienvenido/a a 4TAXIS, su taxímetro digital", 
            padding=(50, 25, 50, 0),  # (left, top, right, bottom)
            font="-size 12",
            bootstyle=(DARK, INVERSE),
            anchor=CENTER 
        )
        welcome.pack(fill=X, expand=YES)

        instructions = ttk.Label(
            master=container,
            text="Pulse los botones inferiores para interactuar con la App", 
            padding=(50, 10, 50, 0),  # (left, top, right, bottom)
            font="-size 9",
            bootstyle=(DARK, INVERSE),
            anchor=CENTER 
        )
        instructions.pack(fill=X, expand=YES)

    def create_image(self):
        """Crear el marco para contener la imagen de fondo"""
        img_path = Path(__file__).parent / 'assets/mp_background.png'
        
        # Cargar la imagen usando PIL y redimensionarla
        image = Image.open(img_path)
        width, height = image.size
        new_width = 300
        new_height = int((new_width / width) * height)
        resized_image = image.resize((new_width, new_height), Image.LANCZOS)
        self.background_image = ImageTk.PhotoImage(resized_image)
        
        self.media = ttk.Label(
            self, image=self.background_image,
            padding=0,
            font="-size 12",
            bootstyle=(DARK, INVERSE),
            anchor=CENTER  
        )
        self.media.pack(fill=BOTH, expand=YES)

    def create_message_area(self):
        """Área para mensajes"""
        console_frame = ttk.Frame(self, padding=0)
        console_frame.pack(fill=X, expand=YES)

        self.console_label = ttk.Label(
            console_frame,
            text=f"\nLevante la mano para llamar a un taxi\n",
            padding=30,
            font="-size 10",
            bootstyle=(WARNING, INVERSE),
            anchor=CENTER,
            justify="center"
        )
        self.console_label.pack(fill=BOTH, expand=YES)
        
    def start_button_click(self):

        self.start_btn.config(bootstyle="SUCCESS")  # Cambia el estilo del botón a verde
        self.pause_btn.config(bootstyle="DARK")  # Cambia el estilo del botón a verde
        self.move_btn.config(bootstyle="DARK")  # Cambia el estilo del botón a oscuro
        self.stop_btn.config(bootstyle="DARK")  # Cambia el estilo del botón a oscuro
        self.fares_btn.config(bootstyle="DARK")
        self.logs_btn.config(bootstyle="DARK")

        if self.taximeter.ride.in_ride:
            if self.taximeter.ride.in_movement:
                self.console_label.config(text=f"Ya estamos en carrera.\n\nTaxímetro corriendo a {self.taximeter.fare.movement_fare}€ por segundo.", bootstyle=(INFO, INVERSE))
            else:
                self.console_label.config(text=f"Ya estamos en carrera.\n\nTaxímetro corriendo a {self.taximeter.fare.stop_fare}€ por segundo.", bootstyle=(INFO, INVERSE))
        else:
            self.console_label.config(text=f"¡Hola! El taxi esta detenido.\n\nTaxímetro corriendo a {self.taximeter.fare.stop_fare}€ por segundo.", bootstyle=(INFO, INVERSE))
            self.taximeter.start_ride()  # Llama a start_ride
    
    def play_button_click(self):
        if self.taximeter.ride.in_ride:  # Si está en carrera
            self.pause_btn.config(bootstyle="DARK")  # Cambia el color del botón
            self.move_btn.config(bootstyle="SUCCESS")
            self.start_btn.config(bootstyle="WARNING")
            self.stop_btn.config(bootstyle="DARK")
            self.fares_btn.config(bootstyle="DARK")
            self.logs_btn.config(bootstyle="DARK")

            if not self.taximeter.ride.in_movement:
                self.console_label.config(text=f"¡Vámonos! Taxi en movimiento.\n\nTaxímetro corriendo a {self.taximeter.fare.movement_fare}€ por segundo.")
            else:
                self.console_label.config(text=f"El taxi ya está en movimiento...\n\nTaxímetro corriendo a {self.taximeter.fare.movement_fare}€ por segundo.")
            
            self.taximeter.change_state(True)  # Llama a change_state
        else:
            self.console_label.config(text=f"\nEl viaje aún no se ha iniciado, llame a un taxi {RAISED_HAND}\n", bootstyle=(DANGER, INVERSE))  # Para controlar que no se mueve o se para sin haber iniciado la carrera
        
    def pause_button_click(self):      
        if self.taximeter.ride.in_ride:  # Si está en carrera
            self.pause_btn.config(bootstyle="SUCCESS")  # Cambia el collor del botón
            self.move_btn.config(bootstyle="DARK")
            self.start_btn.config(bootstyle="WARNING") 
            self.stop_btn.config(bootstyle="DARK")  
            self.fares_btn.config(bootstyle="DARK")
            self.logs_btn.config(bootstyle="DARK")

            if self.taximeter.ride.in_movement:
                self.console_label.config(text=f"Nos detenemos. El taxi está parado.\n\nTaxímetro corriendo a {self.taximeter.fare.stop_fare}€ por segundo.")
            else:
                self.console_label.config(text=f"El taxi ya está parado... ¿Qué hacemos ahora?\n\nTaxímetro corriendo a {self.taximeter.fare.stop_fare}€ por segundo.")
            self.taximeter.change_state(False)  # Llama a change_state
        else:
            self.console_label.config(text=f"El viaje aún no se ha iniciado, llame a un taxi {RAISED_HAND}", bootstyle=(DANGER, INVERSE))  # Para controlar que no se mueve o se para sin haber iniciado la carrera

    def stop_button_click(self):
        self.stop_btn.config(bootstyle="WARNING")  # Cambia el color del botón 
        self.pause_btn.config(bootstyle="DARK")  
        self.move_btn.config(bootstyle="DARK")  
        self.start_btn.config(bootstyle="DARK")
        self.fares_btn.config(bootstyle="DARK")
        self.logs_btn.config(bootstyle="DARK")

        if self.taximeter.ride.in_ride:
            self.taximeter.ride.finish_ride()  # Llama a change_state
            total_cost = self.taximeter.ride.calculate_cost()  # Calcula el costo total de la carrera
            self.console_label.config(text=f"{LOCATION_MARKER} Ha llegado a su destino.\n\nFinalizamos carrera. Coste total {round(total_cost, 2)}€", bootstyle=(SUCCESS, INVERSE))
        else:
            self.console_label.config(text=f"\nNo estamos en carrera... llame a un taxi {RAISED_HAND}\n", bootstyle=(DANGER, INVERSE))  # Para controlar que no se mueve o se para sin haber iniciado la carrera
                
    def exit_button_click(self):
        print(f"\n{BRIGHT_GREEN}{BG_BLACK} {SMILE} Gracias por viajar con 4TAXIS, su taxímetro digital {STAR}{STAR}{STAR}{STAR}{STAR} {RESET}\n") 
        print(f"Saliendo del sistema... \n")
        self.master.destroy()  # Cierra la aplicación

    def logs_button_click(self):
        self.logs_btn.config(bootstyle="INFO")
        self.fares_btn.config(bootstyle="DARK")
        self.stop_btn.config(bootstyle="DARK")
        self.taximeter.show_rides_history()
        self.console_label.config(text=f"\nHistorial de carreras abierto\n", bootstyle=(INFO, INVERSE))

    def fares_button_click(self):
        self.logs_btn.config(bootstyle="DARK")
        self.fares_btn.config(bootstyle="INFO")
        self.create_fares_window()

    def create_fares_window(self):
        """Crear una nueva ventana para actualizar las tarifas"""
        self.fares_window = Toplevel(self)
        self.fares_window.title("Actualizar Tarifas")

        ttk.Label(self.fares_window, text="Tarifa por Movimiento:", padding=20).grid(row=0, column=0)
        self.movement_fare_entry = ttk.Entry(self.fares_window)
        self.movement_fare_entry.grid(row=0, column=1, padx=50, pady=0)
        

        ttk.Label(self.fares_window, text="Tarifa por Parada:", padding=20).grid(row=1, column=0)
        self.stop_fare_entry = ttk.Entry(self.fares_window)
        self.stop_fare_entry.grid(row=1, column=1, padx=50, pady=0)

        # Crear un frame para centrar el botón
        button_frame = ttk.Frame(self.fares_window, padding=20)
        button_frame.grid(row=2, columnspan=2, pady=0)

        # Definir estilos para los botones con diferentes colores
        style = ttk.Style()
        style.configure(
            'Cancel.TButton',
            font=("Helvetica", 11),
            background='#CACFD4',  # Color de fondo para el botón Cancelar (gris)
            relief="flat",
            padding=(20, 10)
        )
        style.map(
            'Cancel.TButton',
            background=[('active', '#A9A9A9')]  # Color de fondo para el botón Cancelar al posicionarse (gris oscuro)
        )

        style.configure(
            'Update.TButton',
            font=("Helvetica", 11),
            background='#04B473',  # Color de fondo para el botón Actualizar (verde lima)
            relief="flat",
            padding=(20, 10)
        )
        style.map(
            'Update.TButton',
            background=[('active', '#029C63')]  # Color de fondo para el botón Actualizar al posicionarse (verde oscuro)
        )

        cancel_button = ttk.Button(
            button_frame, 
            text="Cancelar", 
            style='Cancel.TButton',  # Aplicar el estilo personalizado Cancel
            command=self.cancel_fares,  # Cerrar la ventana de tarifas
            width=8
        )
        cancel_button.pack(side=LEFT, padx=5)

        update_button = ttk.Button(
            button_frame, 
            text="Actualizar", 
            style='Update.TButton',  # Aplicar el estilo personalizado Update
            command=self.update_fares, 
            width=8
        )
        update_button.pack(side=LEFT, padx=5)

    def cancel_fares(self):
        self.fares_btn.config(bootstyle="DARK")
        self.fares_window.destroy()

    def update_fares(self):
        """Actualizar las tarifas del taxímetro"""
        try:
            movement_fare = float(self.movement_fare_entry.get())
            stop_fare = float(self.stop_fare_entry.get())

            self.taximeter.update_fares_ttk(movement_fare, stop_fare)
            self.fares_window.destroy()  # Cerrar la ventana de tarifas

            self.fares_btn.config(bootstyle="DARK")

            self.console_label.config(text=f"Tarifas actualizadas:\n\n{movement_fare}€ en movimiento y {stop_fare}€ en pausa.", bootstyle=(INFO, INVERSE))
        except ValueError:
            self.console_label.config(text=f"\nError: Por favor, ingrese valores válidos.\n", bootstyle=(DANGER, INVERSE))




    def create_buttonbox(self):
        """Crear la caja de botones con controles"""
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES)
        ttk.Style().configure('TButton', font="-size 20")

        self.start_btn = ttk.Button(
            master=container,
            text="\U0000270B",
            padding=20,
            bootstyle=DARK,
            command=self.start_button_click,  # Play
        )
        self.start_btn.pack(side=LEFT, fill=X, expand=YES)

        self.move_btn = ttk.Button(
            master=container,
            text=Emoji.get('black right-pointing triangle'),
            padding=20,
            bootstyle=DARK,
            command=self.play_button_click,  # Play
        )
        self.move_btn.pack(side=LEFT, fill=X, expand=YES)

        self.pause_btn = ttk.Button(
            master=container,
            text=Emoji.get('double vertical bar'),
            padding=20,
            bootstyle=DARK,
            command=self.pause_button_click,  # Pausa
        )
        self.pause_btn.pack(side=LEFT, fill=X, expand=YES)        

        self.stop_btn = ttk.Button(
            master=container,
            text=Emoji.get('black square for stop'),
            padding=20,
            bootstyle=DARK,
            command=self.stop_button_click,  # Stop
        )
        self.stop_btn.pack(side=LEFT, fill=X, expand=YES)          


        self.logs_btn = ttk.Button(
            master=container,
            text=Emoji.get('open file folder'),
            bootstyle=DARK,
            padding=20,
            command=self.logs_button_click,  # ver logs 
        )
        self.logs_btn.pack(side=LEFT, fill=X, expand=YES)   

        self.fares_btn = ttk.Button(
            master=container,
            text=DOLLAR_BILL,
            bootstyle=DARK,
            padding=20,
            command=self.fares_button_click,  # ver logs 
        )
        self.fares_btn.pack(side=LEFT, fill=X, expand=YES)  

        exit_btn = ttk.Button(
            master=container,
            text="\U0000274C",
            bootstyle=DARK,
            padding=20,
            command=self.exit_button_click,  # Salir
        )
        exit_btn.pack(side=LEFT, fill=X, expand=YES)         


if __name__ == '__main__':
    app = ttk.Window("4TAXIS", "litera")
    mp = App(app)
    app.mainloop()
