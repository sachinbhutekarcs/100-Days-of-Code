# Debug the following
for number in range(1, 101):
    # When number is divisible by 3 & 5, it should print FizzBuzz. So and should be used insted of or
    # if number % 3 == 0 or number % 5 == 0:
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    if number % 3 == 0:
        print("Fizz")
    if number % 5 == 0:
        print("Buzz")
    else:
        print([number])
