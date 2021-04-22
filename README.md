# FizzBuzz
Introduction to Test-Driven Development (TDD) 
___

### Problem
Write a program which iterates the integers from 1 to 100.

- for multiples of 3, print `Fizz` instead of the number
- for multiples of 5, print `Buzz` instead of the number
- for numbers which are multiples of both 3 and 5, print `FizzBuzz`

Returns a concatenate string:
  `12Fizz4BuzzFizz78FizzBuzz11Fizz1314FizzBuzz1617Fizz19Buzz ... Buzz`


### Practical tips
1. Choose your preferred IDE (have python installed on your computer ^^, but java works also)
2. Create a directory : `FizzBuzz` or `git clone git@github.com:mleang/FizzBuzz.git`
3. Create a virtual environment if needed: `python -m venv tddvenv`
4. Activate it: `source tddvenv/bin/activate`
5. Create a test file : `test_fizz_buzz.py` with the following lines 

```python
import unittest

class TestFizzBuzz(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

if __name__ == '__main__':
    unittest.main()
```

6. 🔴 Run your test: `python -m unittest`  or  `python test_fizz_buzz.py`
7. 🔴 It fails, so you need to create your source code file: `fizz_buzz.py`
8. From the code file `fizz_buzz.py` import some functions in `test_fizz_buzz.py`: `from fizz_buzz import your_function`. If we run the test, it fails again because we haven’t defined methods yet
9. ✅ Write the minimum code to pass the test : write a method called `generate` in `fizz_buzz.py`
10. 🛠 If the test passes, refactor the code
11. 🔴 Write your second test, run it, it fails
12. ✅ Write the minimum code to pass the test
13. 🛠 If the test passes, refactor the code 
Recursively, repeat 🔴 ✅ 🛠