p10x = []
m1 = 52.5
v10x = [0.32, 0.31, 0.32, 0.32,0.32]
p1x = []
v1x = [-0.06,-0.06,-0.07,-0.06,-0.07]
p2x = []
m2 = 48
v2x = [0.1,0.09,0.1,0.1,0.1]
v = [0.13,0.15,0.14,0.15,0.14]
v1 = [0.14,0.21,0.22,0.24,0.3,0.31,0.4]
v2 = [0.38,0.5,0.54,0.6,0.67,0.68,0.8]
m = [1.66,2.51,3.36,4.21,5.06,5.91,6.76]
for i in range(5):
    p10x.append(m1 * v10x[i])
    p1x.append(m1 * v1x[i])
    p2x.append(m2 * v2x[i])
print('p1x', p1x)
print('p2x', p2x)
print('p10x', p10x)
dp = []
dw = []
for i in range(5):
    dp.append(((p1x[i] + p2x[i])/p10x[i]) - 1)
    dw.append(((m1*v1x[i]**2 + m2*v2x[i]**2)/ m1*v10x[i]**2)-1)
print('dp', dp)
print('dw',dw)
dpcherta = sum(dp)/5
dwcherta = sum(dw)/5
student = 2.77
Ep = 0
Ew = 0
for i in range(5):
    Ep += (dp[i] - dpcherta)**2
    Ew += (dw[i] - dwcherta)**2
deltadpcherta = student * (Ep/20)**0.5
deltadwcherta = student * (Ew/20)**0.5
print('deltadpcherta', deltadpcherta)
print('deltadwcherta', deltadwcherta)
p = [(m1 + m2) * v[i] for i in range(5)]
print('p', p)
dp9 = [p[i]/p10x[i] - 1 for i in range(5)]
print('dp9', dp9)
dwe = [((m1 + m2)*v2x[i]**2)/(m1*v10x[i]**2) - 1 for i in range(5)]
print('dwe', dwe)
dwt = -(m2)/(m1 + m2)
print('dwt', dwt)
x1 = 0.15
x2 = 0.8
g = 9.82
a = [(v2[i] - v1[i])**2/(2*(x2-x1)) for i in range(7)]
T = [m[i]*(g - a[i]) for i in range(7)]
print('a', a)
print('T', T)
E =0
for i in range(5):
    E += (dp[i] - dpcherta)**2
deltadpcherta = 2.77*(E/20)**0.5
epsilonp = deltadpcherta/ dpcherta
E =0
for i in range(5):
    E += (dw[i] - dwcherta)**2
deltadwcherta = 2.77*(E/20)**0.5
epsilonw = deltadwcherta/ dwcherta
print(dpcherta)
print(deltadpcherta)
print(epsilonp)
print(dwcherta)
print(deltadwcherta)
print(epsilonw)
