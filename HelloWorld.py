def exchange(lst):
    if isinstance(lst[0], int) and isinstance(lst[1], int):
        a = str(lst[0])
        b = str(lst[1])
        new_one = int(a[:-1] + b[-1])
        new_two = int(b[:-1] + a[-1])
        return abs(new_two - new_one)
    else:
        return 'invalid elements'
def sorting_cards(cards):
    cards1 = []
    z = ['T', 'Q', 'J', 'K', 'A']
    for i in cards:
        if i not in z:
            cards1.append(int(i))
        else:
            if i == 'T':
                cards1.append(10)
            elif i == 'J':
                cards1.append(11)
            elif i == 'Q':
                cards1.append(12)
            elif i == 'K':
                cards1.append(13)
            elif i == 'A':
                cards1.append(14)
    cards2 = sorted(cards1)
    cards3 = []
    for i in cards2:
        if len(str(i)) < 2:
            cards3.append(str(i))
        else:
            if i == 10:
                cards3.append('T')
            elif i == 11:
                cards3.append('J')
            elif i == 12:
                cards3.append('Q')
            elif i == 13:
                cards3.append('K')
            elif i == 14:
                cards3.append('A')
    return cards3

# def check_password(s):
#     A = ['QWERTYUIOPASDFGHJKLZXCVBNM']
#     a = ['qwertyuiopasdfghjklzxcvbnm']
#     b = ['!@$%*.,?']
#     c = ['0123456789']
#     counta = countA = countb = countc = 0
#     for i in s:
#         if i in a:
#             counta += 1
#         elif i in A:
#             countA += 1
#         elif i in b:
#             countb += 1
#         elif i in c:
#             countc += 1
#         else:
#             return 'not valid'
#     return countc, counta, countb, countA
# print(check_password("")) # должно вернуть "not valid"
# print(check_password("password")) # должно вернуть "not valid"
# print(check_password("P1@p")) # должно вернуть "not valid"
# print(check_password("P1@pP1@p")) # должно вернуть "valid"
# print(check_password("P1@pP1@pP1@pP1@pP1@pP1@p")) # должно вернуть "not valid"
# print(check_password("Paaaaaa222!!!")) # должно вернуть "valid"
def sorted_people(a):
    b = []
    rost = []
    for i in range(len(a)):
        if a[i] == -1:
            b.append(i)
        else:
            rost.append(a[i])
    new_rost = sorted(rost)
    n = []
    c = 0
    for i in range(len(a)):
        if a[i] == -1:
            n.append(-1)
        else:
            elem = new_rost[c]
            n.append(elem)
            c += 1
    return n

def cats_and_mice(mapping, moves):
    if 'C' not in mapping or 'm' not in mapping:
        return 'We need two animals!'
    for i, line in enumerate(mapping.splitlines()):
        cat_index = line.find('C')
        mouse_index = line.find('m')
        if cat_index != -1:
            cat_position = (i, cat_index)
        if mouse_index != -1:
            mouse_position = (i, mouse_index)
    vertical_moves = abs(cat_position[0] - mouse_position[0]) * 3
    horizontal_moves = abs(cat_position[1] - mouse_position[1]) * 2
    if vertical_moves + horizontal_moves <= moves:
        return 'Caught!'
    else:
        return 'Run!'

def scramble(s, array):
    a = [i for i in range(len(array))]
    new = ''
    for i in range(len(a)):
        for j in range(len(array)):
            if i == array[j]:
                new += s[j]
    return new
