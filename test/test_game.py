import unittest
from src.main import check_number, guess_number, start_game
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
    
    #guess_number: captura los números y valida los turnos - jugador
    #definimos sus dos parámetros player_assumptions y computer_assumptions
    #realizamos el mock, del numero random y el número dado
    @patch("src.main.number_random")
    @patch("src.main.number_player")
    def test_player_winner(self, mock_number_random, mock_number_player): 
        mock_number_random.return_value = 5
        mock_number_player.return_value = 5
        result = guess_number(player_assumptions = [], computer_assumptions = [])
        self.assertEqual(result, "Jugador")
    
    #guess_number: captura los números y valida los turnos - jugador
    @patch("src.main.number_player")
    @patch("src.main.number_computer")
    @patch("src.main.number_random")
    def test_computer_winner(self, mock_number_random, mock_number_computer, mock_number_player): 
        mock_number_random.return_value = 5
        mock_number_computer.return_value = 5
        mock_number_player.return_value = 20
        result = guess_number(player_assumptions = [], computer_assumptions = [])
        self.assertEqual(result, "Computadora")
        
    #start_game: captura los números y valida los turnos - jugador
    @patch("src.main.guess_number")
    @patch("src.main.play_again")
    def test_start_game(self, mock_play_again, mock_guess_number):
        mock_guess_number.return_value = None
        mock_play_again.return_value = "si"
        result = start_game()
        mock_guess_number.assert_called_once_with([], [])  
        mock_play_again.assert_called()
        
        self.assertEqual(result, "si")
    

if __name__ == '__main__':
    unittest.main()