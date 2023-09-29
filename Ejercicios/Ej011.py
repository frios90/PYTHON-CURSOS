print("Ejercicio 11Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su producto escalar.")

a =  (1,2,3)
b = (-1,0,2)

res = []
for i in range(3):
    res.append(a[i] * b[i])

print(sum(res))

producto_escalar = sum(x * y for x, y in zip(a, b))

print("El producto escalar entre a y b es:", producto_escalar)


a = (1, 2, 3)
b = (-1, 0, 2)
product = 0
for i in range(len(a)):
    product += a[i]*b[i]
print("El producto de los vectores" + str(a) + " y " + str(b) + " es " + str(product)) 
