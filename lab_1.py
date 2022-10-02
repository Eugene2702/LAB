import sys
q = []
while True:
    a = input()
    if a == "":
        break
    else:
        q.append(a)
if len(q) <= 2:
    print('error!')
    sys.exit()
mas = [int(x) for x in q]
mas.sort()

x = mas[-1]
b = mas[-2]
c = mas[-3]

def count(x, b, c):
    if x + b > c and x + c > b and b + c > x:
        p = (x+b+c)/2
        s = (p*(p-x)*(p-b)*(p-c))**0.5
        print(s)
    else:
        print('Такого треугольника не существует')
if x > 0 and b > 0 and c > 0:
    count(x, b, c)

