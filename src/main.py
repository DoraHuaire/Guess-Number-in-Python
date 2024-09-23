import random

#Función para generar un número aleatorio
def number_random():
    return random.randint(1, 100)
     
#Definimos un función que gestiona el turno del jugador y la computadora
def guess_number(player_assumptions, computer_assumptions):
    secret_number = number_random()
    #iniciamor con el jugador
    turn = "Jugador"

    while True:
        print(f"\n----Round:{turn}----")
        #Llama a la función de computer y player para obtener sus números
        if turn == "Jugador":
           chosen_number = number_player() 
           player_assumptions.append(chosen_number)
        else: 
           chosen_number = number_computer()  
           computer_assumptions.append(chosen_number)
    
        #Si el número es None, vuelve a intentarlo
        if chosen_number is None:
            continue
        
        #compara el número para ver si es el correcto
        message = check_number(chosen_number, secret_number)
        print(message)
        
        if chosen_number == secret_number:
            if turn == "Jugador":
               print(f"Estas fueron tus suposiciones: {player_assumptions}")
            else: 
               print(f"Estas fueron tus suposiciones: {computer_assumptions}")
            break
        
        # si el turno es jugador, entonces cambia a computador
        if turn == "Jugador":
           turn = "Computadora" 
        # de lo contrario si el turno es computador pasa a jugador
        else: 
           turn = "Jugador"
      
pass

#Definimos una función que realice ejecute un if que compare si el número del jugador y de la computadora es el correcto o no
def check_number(chosen_number, secret_number):
    
    if chosen_number < secret_number:
       result = "Demasiado bajo, vuelve a intentarlo" 
    elif chosen_number > secret_number:
       result = "Demasiado alto, vuelve a intentarlo"
    else:
       result = "\n----¡Felicidades! ¡Adivinaste el número correcto!----"
    return result
           
# Definimos una función que genere el número random de la computadora    
def number_computer():
    computer_random = number_random()
    print(f"La computadora elige: {computer_random}") 
    return computer_random 


# Definimos una función que le pida al jugador su número con un input
def number_player():
    try:
        return int(input("Escribe un número entero (entre 1 y 100): "))
    except ValueError:
        print("Por favor ingresa un número entero válido.")
        return None  #Retorna None si el input no es un número válido


#Reiniciamos el juego, si el jugador quiere continuar
def play_again(): 
    restart_game = input("\n----¿Deseas jugar nuevamente? (sí/no): ----")

    if restart_game.lower() == 'sí' or restart_game.lower() == 'si':
       print("¡Genial! ¡Vamos a jugar nuevamente!")
       start_game()
    else:
       print("Gracias por jugar. ¡Hasta la próxima!")
    

#Definimos la función que de iniciar el juego con la bienvenida, llama a la ejecución del juego y a volver a jugar
def start_game():
    print("\n----¡Bienvenido a Guess the Number!----")
    print("Tú y la computadora intentarán adivinar el número correcto")
    
    #definimos las listas 
    player_assumptions = [] 
    computer_assumptions = [] 
    
    #iniciamos el juego
    guess_number(player_assumptions, computer_assumptions)
    
    #Una vez terminado, damos la opción de reiniciar el juego
    play_again()
     
start_game()

if __name__ == '__main__':
   start_game()
