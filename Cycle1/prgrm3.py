import math
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
c=int(input("Enter the value of c:"))
d=b**2-4*a*c
if d<0:
    real=-b/2*a
    img=math.sqrt(abs(d)) / 2*a
    root1=complex(real,img)
    root2=complex(real,-img)
else:
    root1 = (-b + math.sqrt(d)) / (2*a)
    root2 = (-b - math.sqrt(d)) / (2*a)

print("Root1:",root1," and R1oot2: ",root2)