import math, simplebar as load

def main():
 def ask_value(message):
  return float(input(message))
 def solv_square(a,b,c):
  def roots(d,a,b,c):
   def discr(a,b,c):
    return b**2 - 4*a*c
   d = discr(a,b,c)
   if d > 0:
    x1 = (-b + math.sqrt(d))/(2*a)
    x2 = (-b - math.sqrt(d))/(2*a)
    load.simplebar("  Computing roots:", ": ███████████████████ 100%")
    print("The equation has 2 roots:\n x1 =",x1,"\n","x2 =",x2)
   elif d == 0:
    x = (-b + math.sqrt(d))/(2*a)
    load.simplebar("  Computing the root:", ": ██████████████████ 100%")
    print("The equation has 1 root:\nx =",x)

   else:
    print("The equation has no roots!")
  roots("Results:\n",a,b,c)

# Driver
 print ("Enter a, b, and c for equation ax^2+bx+c=0")
 a = ask_value("a=")
 b = ask_value("b=")
 c = ask_value("c=")
 solv_square(a,b,c)

main()

