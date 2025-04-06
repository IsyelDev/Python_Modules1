import random

random_heads = random.randint(0,1)

if random_heads == 0:
    print("PIEDRA")
else:
    print("PAPEL")

PI = 3.14151617

lista =[1,2,3,4,5]
lista.extend(lista)

print(lista)

friends = ["Alice" ,"Bob", "Charlie", "David", "Emanuel"]
numero = random.randint(0,len(friends)-1)
print(friends[numero])

escogido = random.choice(friends)
print(escogido)





elementos = ["piedra","papel","tijera"]

"""
while True:
    try:   
        user = input("Elige: piedra, papel o tijera (o 'salir' para terminar): ").lower()
 
        # Si el usuario elige "salir", se termina el bucle
        if user == "salir":
            print("¡Juego terminado!")
            break
        
        if user not in elementos:
            print("Error")
        else:
            cpu = random.choice(elementos)
            print(cpu)
        
            if user == cpu:
               print("Empate")
            elif(user=="papel"and cpu=="piedra" or user=="piedra"and cpu=="tijera" or user=="tijera"and cpu=="papel"):
               print("GANA USER")
            else:
               print("GANA CPU")
    except ValueError:
       print("INGRESA EL VALOR")

"""

numeros=[1,2,30,4,50,6456,7,8,90,100]

maximo=numeros[0]

for n in range(0,len(numeros)):
    if numeros[n] > maximo:
        maximo = numeros[n]

print(maximo)