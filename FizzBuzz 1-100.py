def fizzbuzz_convert(num):
    if num % 15 == 0:
        return "FizzBuzz"
    if num % 3 == 0:
        return "Fizz"
    if num % 5 == 0:
        return "Buzz"

    return str(num)


result = fizzbuzz_convert(1)
print(result)
