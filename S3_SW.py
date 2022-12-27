a = "3*x**2+-12*x+6".split('+')
for i in a:
    b = i.split('*x')[0]
    print(b)
