import random

def guess_number(player_name, choose_number):
    number_random = random.randint(1, 100)

    while True:
        print(f"\n----Round: {player_name}----")
        number = choose_number()  #Llama a la función para obtener el número en cada intento
        
        if number is None:
            continue  #Si el número es None, vuelve a intentarlo
        
        if number < number_random:
            print("Demasiado bajo, vuelve a intentarlo") 
        elif number > number_random:
            print("Demasiado alto, vuelve a intentarlo") 
        else:
            print("Felicidades, adivinaste el número correcto")
            break

def computer():
    computer_random = random.randint(1, 100)
    print(f"La computadora elige: {computer_random}") 
    return computer_random 

def player():
    try:
        return int(input("Escribe un número entero (entre 1 y 100): "))
    except ValueError:
        print("Por favor ingresa un número entero válido.")
        return None  #Retorna None si el input no es un número válido

def empezar_juego():
    print("\n----¡Bienvenido a Guess the Number!----")
    print("Tú y la computadora intentarán adivinar el número correcto")
    
    #Turno del jugador
    guess_number("Jugador", player)  #Pasamos la función "jugador" sin paréntesis
   
    #Turno de la computadora
    guess_number("Computadora", computer)  #Pasamos la función "computador" sin paréntesis

empezar_juego()