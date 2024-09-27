import unittest
from src.main import check_number, guess_number, start_game, number_player
from unittest.mock import patch, Mock

mock = Mock()

class TestGuessTheNumber(unittest.TestCase):
    #check_number: el objetivo es validar el número dado por el jugador o computador es correcto, incorrecto o igual
    #recibe 2 parametros número dado por el computador o jugador y el número random
    #probar si el número es demasiado bajo
    def test_check_number_minor(self):
        result = check_number(chosen_number = 5, secret_number = 10)
        self.assertEqual(result, "Demasiado bajo, vuelve a intentarlo")
         
    #probar si el número es demasiado alto  
    def test_check_number_higher(self): 
        result = check_number(chosen_number = 10, secret_number = 5)
        self.assertEqual(result, "Demasiado alto, vuelve a intentarlo")
    
    #probar si el número es igual 
    def test_check_number_equal(self):
        result = check_number(chosen_number = 5, secret_number = 5)
        self.assertEqual(result, "\n----¡Felicidades! ¡Adivinaste el número correcto!----")
        
    #number_player: el objetivo es recibir un número entero por parte del jugador
    #no recibe parámetros y retorna nombre 
    #la función está diseñada para retornar unicamente enteros, si recibe un string debe convertirlo a número
    @patch('builtins.input')
    def test_number_player(self, mock_input):
        mock_input.side_effect = ["5"]
        result = number_player()
        self.assertEqual(result, 5)
        
    #si recibe un flotante, debe devolver none
    #debe retornar none
    @patch('builtins.input')
    def test_number_player_float(self, mock_input):
        mock_input.side_effect = ["3.34"]
        result = number_player()
        self.assertEqual(result, None)
    
    #si recibe un negativo
    #debe retornar none
    @patch('builtins.input')
    def test_number_player_negative(self, mock_input):
        mock_input.side_effect = ["-3"]
        result = number_player()
        self.assertEqual(result, None)
    
    #si recibe un número fuera del rango
    #debe retornar none
    @patch('builtins.input')
    def test_number_player_out_range(self, mock_input):
        mock_input.side_effect = ["101"]
        result = number_player()
        self.assertEqual(result, None)
    
    #si recibe un string
    @patch('builtins.input')
    def test_number_player_invalid_input(self, mock_input):
        mock_input.side_effect = ["hola"]
        result = number_player()
        self.assertEqual(result, None)
    
    #guess_number: captura los números y valida los turnos - jugador
    #definimos sus dos parámetros player_assumptions y computer_assumptions
    #realizamos el mock, del numero random y el número dado
    @patch("src.main.number_random")
    @patch("src.main.number_player")
    def test_player_winner(self, mock_number_random, mock_number_player): 
        mock_number_random.return_value = 5
        mock_number_player.return_value = 5
        result = guess_number([],[])
        self.assertEqual(result, "Jugador")
    
    #validamos si el jugador retorna None, el juego debe continuar
    @patch("src.main.number_player")
    @patch("src.main.number_random")
    def test_player_winner(self, mock_number_random, mock_number_player): 
        mock_number_random.return_value = 10
        mock_number_player.side_effect = [None,10]
        result = guess_number([],[])
        self.assertEqual(result, "Jugador") 
        
    #start_game
    #validamos si el reinicio del juego funciona
    @patch("src.main.guess_number")
    @patch("src.main.play_again")
    def test_start_game_out_range(self, mock_play_again, mock_guess_number):
        mock_play_again.return_value = False
        mock_guess_number.return_value = "Jugador"
        start_game()
        mock_guess_number.assert_called_once_with([], [])
        mock_play_again.assert_called_once()


if __name__ == '__main__':
    unittest.main()