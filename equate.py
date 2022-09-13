import math, simplebar as load

print ("Enter a, b, and c for equation ax^2+bx+c=0")
a = float(input("a="))
b = float(input("b="))
c = float(input("c="))
discr = b**2 - 4*a*c

if discr > 0:
 x1 = (-b + math.sqrt(discr))/(2*a)
 x2 = (-b - math.sqrt(discr))/(2*a)
 load.simplebar("Computing ...", "...............")
 print("The equation has 2 roots:\n x1=",x1,"\n","x2=",x2)

elif discr == 0:
 load.simplebar("Computing ...", "...............")
 x = (-b + math.sqrt(discr))/(2*a)
 print("The equation has 1 root:\nx=",x)

else:
 print("The equation has no roots!")

