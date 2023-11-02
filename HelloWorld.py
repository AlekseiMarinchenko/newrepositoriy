def angle(a: point, b: point, c: point) -> float:
    a1 = a
    b1 = b
    c1 = c
    for i in a1:
        if i == 0:
            i = 1
    for i in b1:
        if i == 0:
            i = 1
    for i in c1:
        if i == 0:
            i = 1
    ab=[b[0]-a[0], b[1]-a[1]]
    lenght_ab=((ab[0]**2) + (ab[1]**2))**0.5
    bc=[c[0]-b[0], c[1]-b[1]]
    lenght_bc = ((bc[0]**2) + (bc[1]**2))**0.5
    cos = ((ab[0]*bc[0]) + (ab[1]*bc[1])) / (lenght_ab * lenght_bc)
    arc = math.acos(cos)
    ugol = math.degrees(arc)
    flagx = None
    flagy = None
    if (a1[0] <= 0) == (b1[0] <= 0) == (c1[0]<=0):
        flagx = True
    else:
        flagx = False
    if (a1[1] <= 0) == (b1[1] <= 0) == (c1[1]<=0):
        flagy = True
    else:
        flagy = False
    if flagy and flagx:
        return ugol
    return 180 - ugol
