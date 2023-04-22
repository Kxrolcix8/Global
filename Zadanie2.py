
z = str(input("Hej! Podaj wymyślone zdanie: "))
r = z.split()[::-1]
l = []
for i in r:
    l.append(i)
    
print(" ".join(l))




