q = []
while True:
    a = input()
    if a == "":
        break
    else:
        q.append(a)
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
count(x,b,c)
