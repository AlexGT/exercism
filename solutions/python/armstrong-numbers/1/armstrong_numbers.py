def is_armstrong_number(number):
    number_len = len(str(number))

    return number == sum(int(digit) ** number_len for digit in str(number))
