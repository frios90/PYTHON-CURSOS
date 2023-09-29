
print("EJ001 **********----------------------------------------------------------------")
monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
moneda = input("Introduce una divisa: ")
print(moneda)
print(moneda.title())
print(monedas.get(moneda.title(), "La divisa no está.")) 


monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
moneda = input("Introduce una divisa: ")
if moneda.title() in monedas:
    print(monedas[moneda.title()])
else:
    print("La divisa no está.")


print("EJ002 **********----------------------------------------------------------------")

