def gran(z,e):
    a=e
    if(z>e):
        print(z,"Es major que",e)
        a=z
    elif(e>z):
        print(e,"Es major que",z)
    else:
        print(e,"y",z,"Es igual")
    return a
a=int(input("Numero 1"))
b=int(input("Numero 2"))
c=gran(a,b)
print("El major de",a,"1",b," es ",c)