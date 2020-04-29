import matplotlib.pyplot as plt

a = 1
b = 2
c = 3
d = 5
coords = {
    'x': [],
    'y': [],
}

x = 0
while x <= 6:
    if x <= a:
        coords['y'].append(0)
    elif a <= x <= b:
        coords['y'].append((x - a) / (b - a))
    elif b <= x <= c:
        coords['y'].append(1)
    elif c <= x <= d:
        coords['y'].append((d - x) / (d - c))
    elif d <= x:
        coords['y'].append(0)
    else:
        print(x)
        raise ValueError

    coords['x'].append(x)
    x += 0.5

plt.plot(coords['x'], coords['y'])
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Корнєєв Артем (трапециевидная функція)')
plt.show()
