def generate(number_1: int) -> str:
	if (number_1 % 15 == 0):
		return "FizzBuzz"
	if (number_1 % 3 == 0):
		return "Fizz"
	if (number_1 % 5 == 0):
		return "Buzz"
	return str(number_1)


def generate_all_numbers(number_1: int, number_2: int) -> str:
	result = ""
	for number in range(number_1, number_2+1):
		result += generate(number)
	return result