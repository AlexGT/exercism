def convert(number):
    result_string = ''
    if number % 3 == 0:
        result_string += 'Pling'
    if number % 5 == 0:
        result_string += 'Plang'
    if number % 7 == 0:
        result_string += 'Plong'
    if not result_string:
        result_string += str(number)

    return result_string
