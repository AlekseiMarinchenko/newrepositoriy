def polynomial_evaluate(a, x):
    summ = 0
    for i in range(len(a)):
        summ += a[i]*x**i
    return summ



def polynomial_add(a, b):
    m = min(len(a), len(b))
    M = max(len(a), len(b))
    result = []
    for i in range(m):
        result.append(a[i] + b[i])
    if M == len(a) and M != m:
        for i in range(m, M):
            result.append(a[i])
    elif M == len(b) and M != m:
        for i in range(m, M):
            result.append(b[i])
    rr = result[::-1]
    for i in range(len(rr)):
        if rr[i] == 0:
            result = result[:-1]
        else:
            break
    if result == []:
        return [0]
    return result

def polynomial_derivative(a):
    result = []
    for i in range(len(a)):
        result.append(a[i] * i)
    res1 = result[::-1]
    while res1[0] == 0:
        res1 = res1[1:]
    result = res1[::-1]
    if result == [0]:
        return result
    return result[1:]

def polynomial_multiply(a, b):
    result = [0 for k in range(len(a) * len(b))]
    for i in range(len(a)):
        for j in range(len(b)):
            result[i+j] += a[i] * b[j]
    rr = result[::-1]
    for i in range(len(rr)):
        if rr[i] == 0:
             result = result[:-1]
        else:
             break
    return result

def polynomial_find_root(a):
    def polynomial_evaluate(a, x):
        summ = 0
        for i in range(len(a)):
            summ += a[i]*x**i
        return summ
    st_data = [i for i in range(-1000000, 1000001)]
    data = []
    for i in range(len(st_data)):
        data.append(st_data[i] * 0.0001)
    for i in range(len(data)):
        if polynomial_evaluate(a, data[i]) == 0:
            return data[i]


def polynomial_to_string(a):
    result = ''
    for i in reversed(range(len(a))):
        if i == 0:
            break
        if a[i] == 0:
            continue
        elif a[i] == 1:
            result += 'x' + '^' + str(i) + ' + '
        elif a[i] == -1:
            result += '-x' + '^' + str(i) + ' + '
        else:
            result += str(a[i]) + 'x' + '^' + str(i) + ' + '
    if a[0] != 0:
        result += str(a[0])
    else:
        result = result[:-3]
    return result.replace('+ -', '- ').replace('x^1', 'x')


import numpy
def polynomial_divide(a, b):
    mod = numpy.polydiv(a, b)[1]
    div = list(numpy.polydiv(a, b)[0])
    d = []
    for i in reversed(range(len(div))):
        d.append(div[i])
    m = []
    for i in reversed(range(len(mod))):
        m.append(mod[i])
    return d, m

def happy_new_year(seg: int):
    print(' ' * seg + '<>')
    for lvl in range(1, seg + 1):
        for i in range(0, lvl):
            if i == 0:
                str = ' ' * (seg - i) + '/' + ' ' * 2 * i + chr(92)
                print(str)
            else:
                igr = randint(i+1, 2*i+2)
                str = ' ' * (seg - i) + '/' + ' ' * 2 * i + chr(92)
                if igr > seg:
                    print(str[:igr] + '*' + str[igr + 1:])
                else:
                    print(str)
        print(' ' * (seg - i - 1) + '/' + '_' * 2 * (i + 1) + chr(92))
    print(' ' * seg + '||')
    return
