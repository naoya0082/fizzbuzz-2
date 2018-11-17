def fizzbuzz_convert(num):
    if num % 15 == 0:
        return "FizzBuzz"
    if num % 3 == 0:
        return "Fizz"
    if num % 5 == 0:
        return "Buzz"

    return str(num)


for num in range(1, 101):
    print(fizzbuzz_convert(num))
