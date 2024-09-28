#AREA Y LONGITUD DE LA CIRCUNFERENCIA

a=float(input("Ingrese el valor del radio: "))

#El valor de pi hay que importarlo antes de usarlo

import math

area=math.pi*a**2
longitud=2*math.pi*a



print(f"El area del circulo es: {area:.2f}")
print(f"La longitud del circylo es: {longitud:.2f}")
