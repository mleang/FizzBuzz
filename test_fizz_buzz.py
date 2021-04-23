import unittest
from fizz_buzz import generate, generate_all_numbers
class TestFizzBuzz(unittest.TestCase):
	def test_should_return_1_if_number_is_1(self):
		self.assertEqual(generate(1), "1")

	def test_should_return_2_if_number_is_2(self):
		self.assertEqual(generate(2), "2")

	def test_should_return_Fizz_if_number_is_3(self):
		self.assertEqual(generate(3), "Fizz")

	def test_should_return_Fizz_if_number_is_6(self):
		self.assertEqual(generate(6), "Fizz")

	def test_should_return_Buzz_if_number_is_5(self):
		self.assertEqual(generate(5), "Buzz")
	
	def test_should_return_Buzz_if_number_is_10(self):
		self.assertEqual(generate(10), "Buzz")

	def test_should_return_FizzBuzz_if_number_is_15(self):
		self.assertEqual(generate(15), "FizzBuzz")

	def test_should_return_FizzBuzz_if_number_is_30(self):
		self.assertEqual(generate(30), "FizzBuzz")

	def test_should_return_error_when_string(self):
		with self.assertRaises(TypeError):
			generate('Fizz')

	def test_should_return_12_if_numbers_are_1_and_2(self):
		self.assertEqual(generate_all_numbers(1, 2), "12")
	
	def test_should_return_12Fizz_if_numbers_are_1_to_3(self):
		self.assertEqual(generate_all_numbers(1, 3), "12Fizz")

	def test_should_return_12Fizz4BuzzFizz78FizzBuzz11Fizz1314FizzBuzz_if_numbers_are_1_to_15(self):
		self.assertEqual(generate_all_numbers(1, 15), "12Fizz4BuzzFizz78FizzBuzz11Fizz1314FizzBuzz")

if __name__ == '__main__':
	unittest.main()