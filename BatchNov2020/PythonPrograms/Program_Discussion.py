num = 12345

def count_digit(num):
    length = len(str(num))
    print(length)

    total_digit = 0
    for i in str(num):
        total_digit = total_digit + 1
    print(total_digit)


def count_digit2(num):
    count_digit = 0
    while num > 0:
        num = num//10   #   123//10   = 12, 12//10 = 1
        count_digit += 1

    print(count_digit)

count_digit(num)

count_digit2(234567684787)