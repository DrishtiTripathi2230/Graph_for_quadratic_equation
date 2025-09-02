import numpy as np
import math
import matplotlib.pyplot as plt
print("quadratic equation : y = ax² + bx + c = 0 ")
print("Enter values for following constants : ")
a = float(input(" constant a: "))
b = float(input(" constant b: "))
c = float(input(" constant c: "))

D = ((b**2)-(4*a*c))

if D<0:
  print("No real roots, parabola won't touch x-axis")
  roots = []
elif D == 0:
  root = -b/(2*a)
  roots = [root]
else:  
  root1 = (-b+((D)**(0.5)))/(2*a)
  root2 = (-b-((D)**(0.5)))/(2*a)
  roots = [root1, root2]

#vertex
h = -b/(2*a)
k = a*h**2 + b*h + c
print("vertex: ", (h,k))

#work on graph

x = np.linspace(h-10,h+10, 400)
y = a*x**2 + b*x + c
plt.plot(x,y,label = f"{a}x²+ {b}x + {c}")
plt.axhline(0, color = 'black', linewidth = 0.8)
plt.axvline(0, color = 'black', linewidth = 0.8)

plt.scatter(h,k, color ='red', label = "vertex")
for r in roots:
  plt.scatter(r, 0, color = "green", label ="Root")

plt.title("Quadratic Equation Graph")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()


