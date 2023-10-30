import random

def choose_options():
  options = ("piedra", "papel", "tijera")
  user_option = input("Elige piedra, papel o tijera => ").lower()
  
  if not user_option in options:
    user_option = input("Esa opcion no es correcta, escoge una correcta  ").lower()
  
  computer_option = random.choice(options)  
  
  print("*" * 10)
  print("User option =>", user_option)
  print("Computer option =>", computer_option)
  return user_option, computer_option


def check_rules(user_option, computer_option, user_wins, computer_wins):
  if user_option == computer_option:
    print("Esto es un empate")
  elif user_option == "piedra" and computer_option == "tijera":
    print("Piedra gana a tijera")
    print("Ganaste :)")
    user_wins +=1
  elif user_option == "papel" and computer_option == "piedra":
    print("Papel gana a piedra")
    print("Ganaste :)")
    user_wins +=1
  elif user_option == "tijera" and computer_option == "papel":
    print("Tijera gana a papel")
    print("Ganaste :)")
    user_wins +=1
  elif computer_option == "piedra" and user_option == "tijera":
    print("Piedra gana a tijera")
    print("Perdiste :(")
    computer_wins += 1
  elif computer_option == "papel" and user_option == "piedra":
    print("Papel gana a piedra")
    print("Perdisre :(")
    computer_wins += 1
  else:
    print("Tijera gana a papel")
    print("Perdiste :(")
    computer_wins += 1

  return user_wins, computer_wins
  

def run_game():
  user_wins = 0
  computer_wins = 0
  rounds = 1
  while True:
    print("*" * 10)
    print("ROUND", rounds)
    print("*" * 10)
      
    print("User wins => ", user_wins)
    print("Computer wins => ", computer_wins)
    print("*" * 10)
    
    user_option, computer_option = choose_options()
    user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)
    if user_wins == 2:
      print("El Ganador es el usuario, GANASTE :)")
      break
      
    if computer_wins == 2:
      print("La computadora gano, PERDISTES :(")
      break  

    rounds += 1


run_game()