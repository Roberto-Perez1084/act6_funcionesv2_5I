print("Mas sobre funciones")

def suma_ab(a,b):
    s=a+b
    return s
def res_ab(c,d):
    r=c-d
    return r
def mul_ab(e,f):
    m=e*f
    return m
def div_ab(g,h):
    d=g/h
    return d

print("Calculando suma")
n1=int(input("Ingresa el primer numero "))
n2=int(input("Ingresa el segundo numero "))
suma=suma_ab(n1,n2)
print(f"La suma de {n1} + {n2} es {suma}")

print("Calculando resta")
n3=int(input("Ingresa el primer numero "))
n4=int(input("Ingresa el segundo numero "))
resta=res_ab(n3,n4)
print(f"La resta de {n3} - {n4} es {resta}")

print("Calculando multiplicacion")
n5=int(input("Ingresa el primer numero "))
n6=int(input("Ingresa el segundo numero "))
multi=mul_ab(n5,n6)
print(f"La resta de {n5} × {n6} es {multi}")

print("Calculando division")
n7=int(input("Ingresa el primer numero "))
n8=int(input("Ingresa el segundo numero "))
divi=div_ab(n7,n8)
print(f"La resta de {n7} ÷ {n8} es {divi}")