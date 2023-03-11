#ingreso de numeros
a=int(input("ingrese un numero : "))
b=int(input("ingrese un numero : "))
c=int(input("ingrese un numero : "))

#ordenamiento
lista = [a,b,c]
aux=0


for i in range (0, len(lista)):
    for j in range(i + 1, len(lista)):
        if(lista[i] > lista[j]):
            aux=(lista[i])
            lista[i]=(lista[j])
            lista[j]=(aux)



print(lista)