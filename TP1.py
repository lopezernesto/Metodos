from sympy import symbols

# funcion con un numero


def calcular_funcion(funcion, numero):
    f = funcion.subs(x, numero)
    return f

# Metodo para la funcion de Simpson 1/3


def cantidad_equis(x0, xn, h):
    cont = 0
    x0 = x0+h
    while (x0 < xn):
        x0 += h
        cont += 1
    return cont


def trapecista(x0, xn, funcion):
    h = (xn-x0)/4
    cant = cantidad_equis(x0, xn, h)
    res = ((calcular_funcion(funcion, x0) +
            calcular_funcion(funcion, xn))+(2*sumatoria(x0+2*h, cant, h)))
    res = h/2*res
    return res


def sumatoria(inicio, fin, h):
    i = 1
    suma = 0
    while (i < fin):
        suma += calcular_funcion(funcion, inicio)
        print(suma)
        inicio += h
        i += 1
    return suma


def sumatoria_impares(inicio, fin, h):
    i = 1
    suma = 0
    while (i < fin):
        suma += calcular_funcion(funcion, inicio)
        inicio += 2*h
        i += 2
    return 1


    # Aca empieza el programa
funcion = "5x^2+2x-3"
# Definir la variable
x = symbols('x')
x0 = 2
xn = 4
funcion = 5*x**2+2*x-3
print(trapecista(x0, xn, funcion))
