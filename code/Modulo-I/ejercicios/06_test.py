x = [1,2,3]
y = [4,5,6]

a = [(px * qx) for px, qx in zip(x,y)]
print(a)

b = sum((px * qx) ** 2 for px, qx in zip(x,y))
print(b)
