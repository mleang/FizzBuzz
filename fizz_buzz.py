def generate(min_number: int, max_number:int) -> str:
	return evaluate_numbers(min_number, max_number)

def evaluate_numbers(min_number: int, max_number:int) -> str:
	result = ""
	while min_number <= max_number:
		result += evaluate_number(min_number)
		min_number += 1
	return result
	
def evaluate_number(number:int) -> str:
	if number % 15 == 0:
		return "FizzBuzz"
	if number % 3 == 0:
		return "Fizz"
	if number % 5 == 0:
		return "Buzz"
	return str(number)

