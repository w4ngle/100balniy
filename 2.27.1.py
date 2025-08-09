f = open('2_27_A.txt')
a1 = []
a2 = []
for i in f:
    x, y = map(float, i.split())
    if y > 20 and x > 15:
        a1.append([x, y])
    else:
        a2.append([x, y])
b1 = 0  # мин расстояние от центральной точки до всех остальных
for i in range(len(a1)):
    c1 = 10**10  # мин расстояние от текущей точки до всех остальных
    for j in range(len(a1)):
        a = ((a1[j][0] - a1[i][0]) ** 2 + (a1[j][1] - a1[i][1]) ** 2) ** 0.5  # 0-это х, а 1- это у
        c1 += a
    if c1 > b1:
        b1 = c1
        a1x = a1[i][0]
        a1y = a1[i][1]
b2 = 0  # мин расстояние от центральной точки до всех остальных
for i in range(len(a2)):
    c2 = 10**10  # мин расстояние от текущей точки до всех остальных
    for j in range(len(a2)):
        a = ((a2[j][0] - a2[i][0]) ** 2 + (a2[j][1] - a2[i][1]) ** 2) ** 0.5
        c2 += a
    if c2 > b2:
        b2 = c2
        a2x = a2[i][0]
        a2y = a2[i][1]
print(a1x,a1y,a2x,a2y)
#print(len(a1),len(a2))
px = abs(int(a1x  * 10000))
py = abs(int(a2y  * 10000))
print(px, py)

