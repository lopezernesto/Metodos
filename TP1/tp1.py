from sympy import symbols
# Metodo del trapecista
#a y b son [a,b] de mi integral definida
def trapecista(a, b, funcion, n):
    h = (b - a) / n
    res = (calcular_funcion(funcion, a) + calcular_funcion(funcion, b) +
           2 * sumatoria(a + h, b - h, h, 1,funcion))
    res = (h / 2) * res
    return res


def simpson(a, b, funcion, n):
    h = (b - a) / n
    res = calcular_funcion(funcion, a) + calcular_funcion(funcion, b)
    res += 2 * sumatoria(a + 2 * h, b - h, h, 2,funcion)
    res += 4 * sumatoria(a + h, b - h, h, 2,funcion)
    res = (h / 3) * res
    return res

def sumatoria(inicio, fin, h,salto,funcion):
    suma = 0
    while (inicio <= fin):
        suma += calcular_funcion(funcion, inicio)
        inicio += h*salto
    return suma

# funcion con un numero
def calcular_funcion(funcion, numero):
    f = funcion.subs(x, numero)
    return f

#Aproximacion central
def aprox_central(matriz, num):
    matriz[num][num]
    return 1
def aproximar(matriz, num):
    #si hay elementos atras y adelante
    if((matriz[num-1][num-1] != None) & (matriz[num+1][num+1] != None)):
        #Si tanto para atras como para adelante hay una misma distancia
        if(matriz[num][0]-matriz[num-1][0]==matriz[num+1][0]-matriz[num][0]):
            return aprox_central(matriz, num)
        else:
            return aprox_adelante(matriz,num)
    else:
        if((matriz[num-1][num-1] != None) & (matriz[num-1][num-1]== None)):
            return aprox_adelante(matriz,num)
        else:
            if((matriz[num-1][num-1] == None) & (matriz[num-1][num-1]!=None)):
                return aprox_atras(matriz,num)
    # Aca empieza el programa
# Definir la variable
x = symbols('x')
x0 = 2
xn = 4
funcion = 5*x**2+2*x-3
matriz = [[2.0, 2.5,3.0,3.5,4.0],[0.2239,-0.0484,-0.2601,-0.3801,-0.387]]

print("El resultado de trapecista es:",trapecista(x0, xn, funcion,4))
print("--------------")
print("El resultado de simpson es:",simpson(x0, xn, funcion,4))