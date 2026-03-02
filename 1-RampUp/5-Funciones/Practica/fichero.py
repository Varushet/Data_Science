# funciones.py
import math

def semanal(lista):
    dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    conversor = ""
    for n in lista:
        conversor += " " + dias[n]
    return conversor

def piramide(rango):
    lista = range(rango + 1)
    for n in lista:
        cono = range(n, 0, -1)
        print(*cono)

def calibre(n1, n2):
    if n1 == n2:
        return "Son iguales"
    elif n1 < n2:
        return f"{n2} es el más grande"
    else:
        return f"{n1} es el más grande"

def cuentaletras(texto, a):
    contador = 0
    for i in texto.lower():
        if i == a.lower():
            contador += 1
    return contador

def lexicoon(texto):
    diccionario = {}
    for a in texto:
        diccionario[a] = diccionario.get(a, 0) + 1
    return diccionario

def editar(lista, comando, elemento):
    if comando == "add":
        lista.append(elemento)
    elif comando == "remove":
        if elemento in lista:
            lista.remove(elemento)
    return lista

def arbitro(*palabras):
    return " ".join(palabras)

def area_cuadrado(lado):
    return lado ** 2

def area_triangulo(base, altura):
    return (base * altura) / 2

def area_circulo(radio):
    return math.pi * (radio ** 2)