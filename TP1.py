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
    print("pares: ")
    res += 2 * sumatoria(a + 2 * h, b - h, h, 2,funcion)
    print("impares")
    res += 4 * sumatoria(a + h, b - h, h, 2,funcion)
    res = (h / 3) * res
    return res

def sumatoria(inicio, fin, h,salto,funcion):
    suma = 0
    while (inicio <= fin):
        print("Estoy en x",inicio)
        suma += calcular_funcion(funcion, inicio)
        inicio += h*salto
    return suma

# funcion con un numero
def calcular_funcion(funcion, numero):
    f = funcion.subs(x, numero)
    return f

    # Aca empieza el programa
# Definir la variable
x = symbols('x')
x0 = 2
xn = 4
funcion = 5*x**2+2*x-3
print("El resultado de trapecista es:",trapecista(x0, xn, funcion,8))
print("--------------")
print("El resultado de simpson es:",simpson(x0, xn, funcion,8))