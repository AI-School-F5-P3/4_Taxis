from pathlib import Path
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.icons import Emoji
from PIL import Image, ImageTk
from taximeter import Taximeter  # Importar la clase Taximeter

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


class App(ttk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.pack(fill=BOTH, expand=YES)     

        self.create_header()
        self.create_image()
        self.create_message_area()
        self.create_buttonbox()
        
        self.taximeter = Taximeter()  # Instanciar la clase Taximeter

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

            if self.taximeter.ride.in_ride:
                if self.taximeter.ride.in_movement:
                    self.console_label.config(text=f"Ya estamos en carrera.\n\nTaxímetro corriendo a {self.taximeter.fare.movement_fare}€ por segundo.",bootstyle=(INFO, INVERSE))
                else:
                    self.console_label.config(text=f"Ya estamos en carrera.\n\nTaxímetro corriendo a {self.taximeter.fare.stop_fare}€ por segundo.",bootstyle=(INFO, INVERSE))
            else:
                self.console_label.config(text=f"¡Hola! El taxi esta detenido.\n\nTaxímetro corriendo a {self.taximeter.fare.stop_fare}€ por segundo.",bootstyle=(INFO, INVERSE))
                self.taximeter.start_ride()  # Llama a start_ride
    
    def play_button_click(self):
        if self.taximeter.ride.in_ride: # Si esta en carrera
            self.pause_btn.config(bootstyle="DARK")  # Cambia el estilo del botón a verde
            self.move_btn.config(bootstyle="SUCCESS")  # Cambia el estilo del botón a oscuro
            self.start_btn.config(bootstyle="WARNING")  # Cambia el estilo del botón a amarillo
            self.stop_btn.config(bootstyle="DARK")  # Cambia el estilo del botón a oscuro

            if not self.taximeter.ride.in_movement:
                self.console_label.config(text=f"¡Vámonos! Taxi en movimiento.\n\nTaxímetro corriendo a {self.taximeter.fare.movement_fare}€ por segundo.")
            else:
                self.console_label.config(text=f"El taxi ya está en movimiento...\n\nTaxímetro corriendo a {self.taximeter.fare.movement_fare}€ por segundo.")
            
            self.taximeter.change_state(True)  # Llama a change_state
        else:
            self.console_label.config(text=f"\nEl viaje aún no se ha iniciado, llame a un taxi {RAISED_HAND}\n",bootstyle=(DANGER, INVERSE)) # Para controlar que no se mueve o se para sin haber iniciado la carrera
        
        
    def pause_button_click(self):      
        if self.taximeter.ride.in_ride: # Si esta en carrera
            self.pause_btn.config(bootstyle="SUCCESS")  # Cambia el estilo del botón a verde
            self.move_btn.config(bootstyle="DARK")  # Cambia el estilo del botón a oscuro
            self.start_btn.config(bootstyle="WARNING")  # Cambia el estilo del botón a amarillo
            self.stop_btn.config(bootstyle="DARK")  # Cambia el estilo del botón a oscuro

            if self.taximeter.ride.in_movement:
                self.console_label.config(text=f"Nos detenemos. El taxi está parado.\n\nTaxímetro corriendo a {self.taximeter.fare.stop_fare}€ por segundo.")
            else:
                self.console_label.config(text=f"El taxi ya está parado... ¿Qué hacemos ahora?\n\nTaxímetro corriendo a {self.taximeter.fare.stop_fare}€ por segundo.")
            self.taximeter.change_state(False)  # Llama a change_state
        else:
            self.console_label.config(text=f"El viaje aún no se ha iniciado, llame a un taxi {RAISED_HAND}",bootstyle=(DANGER, INVERSE)) # Para controlar que no se mueve o se para sin haber iniciado la carrera
        

    def stop_button_click(self):
        self.stop_btn.config(bootstyle="WARNING")  # Cambia el estilo del botón a verde
        self.pause_btn.config(bootstyle="DARK")  # Cambia el estilo del botón a verde
        self.move_btn.config(bootstyle="DARK")  # Cambia el estilo del botón a oscuro
        self.start_btn.config(bootstyle="DARK")  # Cambia el estilo del botón a amarillo

        if self.taximeter.ride.in_ride:
            self.taximeter.ride.finish_ride()  # Llama a change_state
            total_cost =  self.taximeter.ride.calculate_cost() # Calcula el costo total de la carrera
            self.console_label.config(text=f"{LOCATION_MARKER} Ha llegado a su destino.\n\nFinalizamos carrera. Coste total {round(total_cost, 2)}€",bootstyle=(SUCCESS, INVERSE))
        else:
            self.console_label.config(text=f"\nNo estamos en carrera... llame a un taxi {RAISED_HAND}\n",bootstyle=(DANGER, INVERSE)) # Para controlar que no se mueve o se para sin haber iniciado la carrera

                
    def exit_button_click(self):
        print(f"\n{BRIGHT_GREEN}{BG_BLACK} {SMILE} Gracias por viajar con 4TAXIS, su taxímetro digital {STAR}{STAR}{STAR}{STAR}{STAR} {RESET}\n") 
        print(f"Saliendo del sistema... \n")
        self.master.destroy()  # Cierra la aplicación

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
