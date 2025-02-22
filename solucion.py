# Hola mundo
print("Hola mundo")
# Saludo y el nombre
nombre = input("Ingrese su nombre: ")
print(f"Hola, {nombre}")
# Edad
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Usted es mayor de edad.")
else:
    print("Usted no es mayor de edad.")
# Par o impar
numero = int(input("Ingrese un número entero: "))
if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")
# Suma
numero = int(input("Ingrese un número entero: "))
suma = 0
for i in range(1, numero + 1):
    suma += i
print(f"La suma de 1 hasta {numero} es: {suma}")