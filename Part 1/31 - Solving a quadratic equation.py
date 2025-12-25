a = float(input("Value of a: "))
b = float(input("Value of b: "))
c = float(input("Value of c: "))

#(-b ± sqrt(b²-4ac))/(2a)
d = (b**2) - (4*a*c)
sol1 = (-b + sqrt(d)) / (2*a)
sol2 = (-b - sqrt(d)) / (2*a)

#ax²+bx+c
s1 = (a*sol1**2)+(b*sol1)+c
s2 = (a*sol2**2)+(b*sol2)+c

print(f"The roots are {sol1} and {sol2}")
