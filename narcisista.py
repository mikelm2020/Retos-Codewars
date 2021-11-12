def narcissistic(value):
    number_value = 0
    number_string = str(value)
    exponent = len(number_string)
    for number_char in number_string:
        digit = int(number_char)
        number_value += digit ** exponent
    if number_value == value:
        return True
    else:
        return False






def run():
    number = 153
    if narcissistic(number):
        print('Si es narcicista')
    else:
        print('No es narcicista')





if __name__ == '__main__':
    run()
