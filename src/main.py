import random

#Función para generar un número aleatorio
def number_random():
    return random.randint(1, 100)
     
#Definimos un función que gestiona el turno del jugador y la computadora
def guess_number(player_assumptions, computer_assumptions):
    secret_number = number_random()
    #iniciamor con el jugador
    turn = "Jugador"
    game_over = False

    while not game_over:
        print(f"\n----Round:{turn}----")
        #Llama a la función de computer y player para obtener sus números
        try:
            if turn == "Jugador":
              chosen_number = number_player() 
              if chosen_number is None:
                 print(f"Número inválido")
                 continue
              player_assumptions.append(chosen_number)
            else: 
              chosen_number = number_computer()  
              computer_assumptions.append(chosen_number)
    
            #Si el número está fuera de rango
            if not (1 <= chosen_number <= 100):
               print(f"Número inválido, debe estar entre 1 y 100.")
               continue
        
            #compara el número para ver si es el correcto
            result = check_number(chosen_number, secret_number)
            print(result)
        
            if chosen_number == secret_number:
               game_over = True
               if turn == "Jugador":
                  print(f"Estas fueron tus suposiciones: {player_assumptions}")
                  return "Jugador"
               else: 
                  print(f"Estas fueron tus suposiciones: {computer_assumptions}")
                  return "Computadora" 
            
            # si el turno es jugador, entonces cambia a computador
            if turn == "Jugador":
               turn = "Computadora" 
            # de lo contrario si el turno es computador pasa a jugador
            else: 
               turn = "Jugador"
     
        except Exception as e:
            print(f"Ocurrió un error inesperado: {str(e)}")
            continue 
      
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
        number = int(input("Escribe un número entero (entre 1 y 100): "))
        # Verificar el rango
        if 1 <= number <= 100:  
           return number
        else:
            print("\nEl número debe estar entre 1 y 100.")
            return None       
    except ValueError:
        print("Por favor ingresa un número entero válido.")
        return None  #Retorna None si el input no es un número válido

#Reiniciamos el juego, si el jugador quiere continuar
def play_again(): 
    restart_game = input("\n----¿Deseas jugar nuevamente? (sí/no): ----")

    if restart_game.lower() == 'sí' or restart_game.lower() == 'si':
       print("¡Genial! ¡Vamos a jugar nuevamente!")
       return True
    else:
       print("Gracias por jugar. ¡Hasta la próxima!")
       return False

#Definimos la función que de iniciar el juego con la bienvenida, llama a la ejecución del juego y a volver a jugar
def start_game():
    print("\n----¡Bienvenido a Guess the Number!---- \nTú y la computadora intentarán adivinar el número correcto")
   
    while True:
         #definimos las listas 
         player_assumptions = [] 
         computer_assumptions = [] 
    
         #iniciamos el juego
         winner = guess_number(player_assumptions, computer_assumptions)
         print(f"\nEl ganador es: {winner}")
    
         #Una vez terminado, damos la opción de reiniciar el juego
         if not play_again():
            break 

if __name__ == '__main__':
   start_game()
