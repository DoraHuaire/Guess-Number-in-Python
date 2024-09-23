import unittest
from src.main import check_number, number_player
from unittest.mock import patch

class TestGuessTheNumber(unittest.TestCase):
    #check_number: el objetivo es validar el número dado por el jugador o computador es correcto, incorrecto o igual
    #recibe 2 parametros número dado por el computador o jugador y el número random
    #probar si el número es demasiado bajo
    def test_check_number_minor(self):
        result = check_number(5,10)
        self.assertEqual(result, "Demasiado bajo, vuelve a intentarlo")
         
    #probar si el número es demasiado alto  
    def test_check_number_higher(self): 
        result = check_number(10,5)
        self.assertEqual(result, "Demasiado alto, vuelve a intentarlo")
    
    #probar si el número es igual 
    def test_check_number_equal(self):
        result = check_number(5,5)
        self.assertEqual(result, "\n----¡Felicidades! ¡Adivinaste el número correcto!----")
    
    #number_player: el objetivo es obtener el número del jugador mediante un input:
    #no tiene parámetros
    #debe recibir un entero
    def test_number_player(self):
    
""" from unittest import mock
from src.main import number_random """

""" class TestGuessNumber(unittest.TestCase):
    @mock.patch("main.number_random")
    def test_number_random(self, mock_response):
        mock_response.return_value = 3
        response = number_random()
        self.assertEqual (response, 3)
        self.assertNotEqual (response, 3.43) """

if __name__ == '__main__':
    unittest.main()