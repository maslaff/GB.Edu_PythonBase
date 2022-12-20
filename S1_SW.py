num = 5.03
dig = round(num*10 % 10)
print(dig if dig else "no")

print(str(num).split('.')[1][:1])
