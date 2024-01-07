def happy_new_year(seg: int):
    print(' ' * seg + '<>')
    for lvl in range(1, seg + 1):
        for i in range(0, lvl):
            print(' ' * (seg - i) + '/' + ' ' * 2 * i + chr(92))
        print(' ' * (seg - i - 1) + '/' + '_' * 2 * (i + 1) + chr(92))
    print(' ' * seg + '||')
def favourite_number() -> int:
    return 1
def sequence_element(n: int):
    return int((1 + (1 + 8*(n-1))**0.5)/2)
