polynomial = list[int|float]
def monomial_to_string(coeff: float, d: int) -> str:
    if d == 0:
        return f'{coeff}'
    elif d == 1:
        return f'{coeff}x'
    return f'{coeff}x^{d}'
def to_string(p: polynomial):
    monomials = []
    for d in reversed(range(len(p))):  # идем по убыванию степеней
        monomials.append(monomial_to_string(p[d], d))
    result = ''
    for i in monomials:
        if i[0] != '0':
            result += i + ' + '
    result = result[:max(result.rfind('+'), result.rfind('-'))]
    if result[:2] == '1x':
        result = result[1:]
    return result.replace(' + -', ' - ').replace(' 1x', ' x').replace('-1x', '-x')
def to_latex(p: polynomial) -> str:
    c = to_string(p)
    b = ''
    flag = True
    for i in range(len(c) - 1):
        if c[i] == '0' and c[i + 1] == 'x':
            flag = False
        elif c[i] == '+' or c[i] == '-':
            flag = True
        if flag == True:
            b += c[i]
    b = b.replace(' + - ', ' - ').replace(' - + ', ' + ')
    return b

