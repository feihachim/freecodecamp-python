"""
The Luhn algorithm, also known as the "modulus 10" or "mod 10" algorithm, is a simple checksum formula used to validate a variety of identification numbers, like credit card numbers. These are the steps to validate a number using the Luhn algorithm:

    - Starting from the right, and excluding the rightmost digit (the check digit), double the value of every other digit.
    - If the result of doubling a digit is greater than 9, sum the digits to get a single digit. Alternatively, you can subtract 9 from the result.
    - Take the sum of all the digits including the check digit.
    - If the sum of all the digits is a multiple of 10, then the number is valid; else it is not valid.

"""


def verify_card_number(card_number: str) -> str:
    numbers = [int(x) for x in card_number if x.isdigit()]
    print(numbers)
    i = len(numbers) - 2
    while i >= 0:
        numbers[i] = numbers[i] * 2
        i -= 2
    print(numbers)
    for i in range(len(numbers)):
        if numbers[i] > 9:
            numbers[i] -= 9
    print(numbers)
    total = 0
    for number in numbers:
        total += number
    print("total", total)
    if total % 10 == 0:
        return "VALID!"
    else:
        return "INVALID!"


verify_card_number("453914889")
verify_card_number("4111-1111-1111-1111")
verify_card_number("453914881")
verify_card_number("1234 5678 9012 3456")
