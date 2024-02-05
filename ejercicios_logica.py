def suma_pares(numero):
    return sum(i for i in range(2, numero+1, 2))

# Ejemplo de uso
resultado = suma_pares(10)
print(resultado)






def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            print("No es primo", n, "es divisor")
            return False
        else:
            print("Es primo")
            return True

num=int(input())
es_primo(num)



def invertir_palabra(palabra):
    return palabra[::-1]

# Ejemplo de uso
resultado = invertir_palabra("Python")
print(resultado)


def fibonacci(n):
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib

# Ejemplo de uso
resultado = fibonacci(8)
print(resultado)



def contar_vocales(palabra):
    return sum(1 for letra in palabra if letra.lower() in 'aeiou')

# Ejemplo de uso
resultado = contar_vocales("Python")
print(resultado)
