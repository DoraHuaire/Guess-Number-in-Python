import random

def guess_number():
    player_assumptions = [] 
    computer_assumptions = [] 
    number_random = random.randint(1, 100)
    turn = "Jugador"

    while True:
        print(f"\n----Round:{turn}----")
        
        if turn == "Jugador":
        # Llama a la función player para obtener el número del jugador
           number = player() 
           player_assumptions.append(number)
        # Llama a la función computer para obtener el número de la computadora
        else: 
           number = computer()  
           computer_assumptions.append(number)
        
        #Si el número es None, vuelve a intentarlo
        if number is None:
            continue
        
        if number < number_random:
            print("Demasiado bajo, vuelve a intentarlo") 
        elif number > number_random:
            print("Demasiado alto, vuelve a intentarlo")
        else:
            if turn == "Jugador":
              print("\n----¡Felicidades! ¡Adivinaste el número correcto!----")
              print(f"Estas fueron tus suposiciones {player_assumptions}")
            else: 
              print("\n----¡Felicidades! ¡Adivinaste el número correcto!----")
              print(f"Estas fueron tus suposiciones {computer_assumptions}")
            break
          
        # si el turno es jugador, entonces cambia a computador
        if turn == "Jugador":
           turn = "Computadora" 
        # de lo contrario si el turno es computador pasa a jugador
        else: 
           turn = "Jugador"
        
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

def play_again(): 
 restart_game = input("\n----¿Deseas jugar nuevamente? (sí/no): ----")

 if restart_game.lower() == 'sí' or restart_game.lower() == 'si':
    print("¡Genial! ¡Vamos a jugar nuevamente!")
    start_game()
 else:
    print("Gracias por jugar. ¡Hasta la próxima!")


def start_game():
    print("\n----¡Bienvenido a Guess the Number!----")
    print("Tú y la computadora intentarán adivinar el número correcto")
    
    #Llamamos los turnos
    guess_number()
    play_again()
     
start_game()