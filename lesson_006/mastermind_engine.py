def number_in_numlist(number):
    numlist = []
    x = 1000
    for _ in range(0, 4):
        num_i = ((number // (x * 10)) * 10) - (number // x)
        x = x // 10
        if num_i < 0:
            num_i = num_i * (-1)
        numlist.append(num_i)
    return numlist


def get_number():
    import random
    n1 = random.randint(1, 9)
    while 1 > 0:
        n2 = random.randint(0, 9)
        if n2 != n1:
            break
    while 1 > 0:
        n3 = random.randint(0, 9)
        if n3 != n1 and n3 != n2:
            break
    while 1 > 0:
        n4 = random.randint(0, 9)
        if n4 != n1 and n4 != n2 and n4 != n3:
            break
    number = n1 * 1000 + n2 * 100 + n3 * 10 + n4
    return number


def check_number(number, true_number=1024):
    answer = {'bulls': 0, 'cows': 0}
    number = number_in_numlist(number)
    true_number = number_in_numlist(true_number)
    for i in range(4):
        checking_number = number[i]
        for j in range(4):
            correct_checking_number = true_number[j]
            if checking_number == correct_checking_number:
                if i == j:
                    answer['bulls'] += 1
                    break
                else:
                    answer['cows'] += 1
    return answer
