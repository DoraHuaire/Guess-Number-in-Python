# Guess the Number Game 🧙‍♀️💻🧙‍♂️

Este proyecto es un juego interactivo llamado Guess the Number, desarrollado. El objetivo del juego es que el jugador y la computadora intenten adivinar un número secreto entre 1 y 100, turnándose para hacer sus suposiciones.

![gif-juego](src/assets/images/juego.gif)

## 1. Requisitos

* Python 3 o superior
* Biblioteca unittest (incluida en la instalación estándar de Python)

***

## 2. Funciones en Python

Una parte fundamental de este proyecto fue entender y aplicar funciones en Python. A lo largo del código utilicé varias funciones para organizar las diferentes partes del juego. Algunas de las más importantes fueron:

* def guess_number(player_assumptions, computer_assumptions): Esta función gestiona los turnos entre el jugador y la computadora, comparando sus suposiciones con el número secreto.
* def check_number(chosen_number, secret_number): Aquí se utiliza la lógica condicional para verificar si la suposición es correcta, demasiado alta o demasiado baja.
* def number_random(): Genera un número aleatorio usando la función randint() del módulo random.

## 3. Manejo de excepciones

Aprendí a manejar errores potenciales usando el bloque try-except para asegurar que el juego no se detuviera si el jugador ingresaba un valor no válido:

![imagen-excepciones](src/assets/images/excepciones.png)

## 4. Listas de datos

Utilicé listas para almacenar las suposiciones realizadas tanto por el jugador como por la computadora. Esto me ayudó a hacer un seguimiento de los números que ya se habían adivinado durante el juego:

![imagen-listas](src/assets/images/listas.png)

## 5. Condicionales y bucles

El uso de bucles while y condicionales if-else fue esencial para controlar el flujo del juego. Aprendí a cambiar los turnos entre el jugador y la computadora, y a finalizar el juego cuando alguien adivinaba correctamente:

![vista-condiciones](src/assets/images/condiciones.png)

## 6. Pruebas unitarias con unittest

Desarrollé pruebas para validar el comportamiento de las funciones usando la biblioteca unittest. Aprendí a usar mocking para simular entradas y comprobar el comportamiento del juego.

* Usé @patch para simular las entradas del jugador.

## 7. Funciones Principales

* guess_number(): Controla los turnos del jugador y la computadora.
* check_number(): Compara la suposición con el número secreto.
* number_random(): Genera un número aleatorio entre 1 y 100.
* number_player(): Captura y valida el input del jugador.
* number_computer(): Genera la suposición de la computadora.
* start_game(): Inicia y gestiona el ciclo del juego.

## 6. Modularización

Dividí el código en funciones más pequeñas y reutilizables para hacerlo más legible y fácil de mantener. Esto me ayudó a comprender la importancia de la modularización en la programación.