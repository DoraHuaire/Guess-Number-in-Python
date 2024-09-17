import random

number_random = random.randint(1,100)
player = None

print("¡Bienvenido a Guess the Number!, tú y la computadora intentarán adivinar el número correcto")

while player != number_random:
  print("\n----Round: player 1----")
  player = int(input("Escribe un número entero: "))
   
  if player < number_random:
    print("Demasiado bajo, vuelve a intentarlo") 
  elif player > number_random:
    print("Demasiado alto, vuelve a intentarlo") 
  else:
    print("Felicidades, adivinaste el número correcto")
    continue

  computer_random = random.randint(1,100)
  print("\n----Round: Computer----")
  print(f"La computadora elige: {computer_random}") 

  if computer_random < number_random:
    print("Demasiado bajo, vuelve a intentarlo")  
  elif computer_random > number_random:
    print("Demasiado alto, vuelve a intentarlo") 
  else:
    print("Ganó la computadora") 
    break

 


