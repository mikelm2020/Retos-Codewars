def get_sum(a,b):
    value = 0
    if a == b:
        return a
    else:
        if a < b:
            for digit in range(a,b + 1):
                value += digit
        else:
            for digit in range(b,a + 1):
                value += digit
        return value


        



def run():
    print(get_sum(1,0))



if __name__ == '__main__':
    run()
