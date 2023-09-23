Y = [0.25, 0.35, 0.55, 0.75, 0.95]
Z = [2.93, 3.68, 5.87, 8.4, 10.88]
sigmaA = 0
E1 = 0
E2 = 0
a = 0
ch = 0
zn = 0
for i in range(5):
    ch += Z[i] * Y[i]
    zn += Z[i]** 2
a = ch/zn
print('a=', a)
for i in range(5):
    E1 += (Y[i]-a*Z[i])**2
    E2 += Z[i]**2
sigmaA = (E1/ (4*E2))**0.5
print('sigmaA=', sigmaA)
deltaAmaloe = 2*sigmaA
print('deltaAmaloe=', deltaAmaloe)
Epsilon_Alpha = deltaAmaloe/a
print('epsilon alpha v procentah', Epsilon_Alpha)
h0 = 180
h0sht = 180
x = 220
xsht = 1000
h = [190, 200,207,216,227]
hsht = [180,180,180,185,190]
sinus = []
for i in range(5):
    sinus.append(abs(((h0 - h[i]) - (h0sht - hsht[i]))/(xsht-x)))
print('sinus alpha', sinus)
t1sr = [1.52, 0.96,0.76,0.68,0.58]
t2sr = [4.9,3.3,2.6,2.3,1.98]
asr = []
for i in range(5):
    asr.append((2*(1 - 0.22))/ (t2sr[i]**2 - t1sr[i]**2))
print('asr', asr)
D = 0
E1 = 0
E2 = 0
for i in range(5):
    E1 += sinus[i]**2
    E2 += sinus[i]
D = E1 - (E2**2)/5
print('D', D)
gspb = 9.8195
deltax = 0.003
deltat = 0.07
deltaA = []
for i in range(5):
    deltaA.append(asr[i]*(((2*deltax**2)/Y[i]**2)+4*(((t1sr[i])*deltat)**2+((t2sr[i])*deltat)**2)/(t2sr[i]**2 - t1sr[i]**2)**2)**0.5)
print('deltaA', deltaA)
E1 = 0
E2 = 0
E3 = 0
E4 = 0
E5 = 0
B = 0
for i in range(5):
    E1 += asr[i]*sinus[i]
    E2 += asr[i]
    E3 += sinus[i]
    E4 += sinus[i]**2
    E5 += sinus[i]
B = (E1 - (E2 * E3)/5)/(E4 - (E5**2)/5)
print('B', B)
A = (E2 - B*E3)/5
print('A', A)
d = []
D = []
for i in range(5):
    d.append(asr[i]-(A+B*sinus[i]))
D = E4 - (E5**2)/5
print('d', d)
print('D', D)
sigmag = 0
e1 = 0
for i in range(5):
    e1 += d[i]**2
sigmag = 1.95
print('sigmag', sigmag)
deltag = 2*sigmag
print('deltag', deltag)
Epsilon_g = deltag/gspb
print('Epsilon g v procentah', Epsilon_g)
print('raznitca g', B - gspb)

