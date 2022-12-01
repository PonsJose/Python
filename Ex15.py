def sumar_lista(a):
    sumatori=0
    for i in a:
        sumatori+=i
    return sumatori
def multiplicar_lista (lista):
    multiplicado=1
    for x in lista:
        multiplicado *= x
    return multiplicado
x = [1,2,3,4,5]
print ("La suma dels elements de la llista es: ",sumar_lista (x))
print ("La multiplicación dels elements de la llista es: ",multiplicar_lista (x))
