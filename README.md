# 4TAXIS

:grinning: ¡Te damos la bienvenida a 4TAXIS!

## Introducción

En respuesta al creciente desafío planteado por las empresas privadas de transporte, que están atrayendo a más clientes gracias a sus precios competitivos y mayor comodidad, el servicio de taxis ha decidido innovar tecnológicamente para recuperar y aumentar su clientela.

Tras un exhaustivo análisis, se identificó que una de las principales causas de la pérdida de clientes es el atraso tecnológico de los taxímetros actuales. Para abordar esta situación, se ha decidido desarrollar un prototipo de taxímetro digital que pueda ser implementado en toda la red de taxis.

El objetivo principal de este proyecto es modernizar el sistema de facturación existente y crear una solución eficiente y precisa para el cálculo de tarifas. Con esta modernización, buscamos no solo mejorar la experiencia del cliente, sino también optimizar el servicio y hacerlo más competitivo frente a las alternativas disponibles en el mercado.

**Objetivos del Proyecto**

- Proveer una solución eficiente para la gestión de carreras de taxis.

- Facilitar el cálculo de tarifas en tiempo real.

- Proporcionar una interfaz amigable para los conductores y usuarios.

Este proyecto representa un paso significativo hacia la modernización del servicio de taxis, asegurando que se mantenga relevante y competitivo en el entorno actual de transporte. 


## Tabla de Contenidos

- [Instalación](###instalación)
- [Inicio](###inicio)
- [Características](###características)
- [Extras](###extras)
- [Licencia](###licencia)


### 1. Instalación

    git clone https://github.com/AI-School-F5-P3/4_taxis.git


### 2. Inicio

Puedes iniciar la 4TAXIS en la interfaz grafica desde app.py o en la linea de comandos desde taximeter.py


### 3. Caracteristicas

**Bienvenida y Menú de Comandos:**
- Al iniciar el programa, se da la bienvenida y se muestra una lista de comandos, o una serie de botones, disponibles para el usuario.

**Inicio de Carrera:**
- Pulsando la tecla i o mediante el botón Hand de la interfaz gráfica.
- El programa empieza a calcular la tarifa y se asume que el taxi está inicialmente detenido.
        
**Movimiento del Taxi:**
- Pulsando la tecla m o mediante el botón Play de la interfaz gráfica.
- El taxi se mueve y el programa cambia la tarifa a 5 céntimos por segundo. 
        
**Pausa del Taxi:**
- Pulsando la tecla s o mediante el botón Pause de la interfaz gráfica.
- El taxi se ha detenido y el programa cambia la tarifa a 2 céntimos por segundo. 
     
**Fin de Carrera:**
- Pulsando la tecla e o mediante el botón Stop de la interfaz gráfica.
- Finaliza el cálculo de la tarifa y muestra el total acumulado en Euros.

**Salir del Programa:**
- Pulsando la tecla e o mediante el botón Exit de la interfaz gráfica.
- Permite al usuario salir del programa de manera segura.


### 4. Extras

- Al iniciar te pide la contraseña.
- El programa guarda en texto plano un registro histórico de carreras pasadas que se puede consultar.
- Los precios de la carrera se pueden configurar para adaptarse a la demanda actual.


### 5. Licencia

Puedes usarlo como quieras.