def fibonacciSuma(numero):
    fib_secuencia=[0,1]
    while len(fib_secuencia)<numero:
        fib_secuencia.append(fib_secuencia[-1]+fib_secuencia[-2])
        return sum(fib_secuencia)
    


numero_input = int(input("Por favor ingrese el numero input para ejecutar sucesion de fibonacci : "))

if  numero_input <= 0:
    print("Por favor ingrese un numero mayor a cero(0)")
else:
    resultado = fibonacciSuma(numero_input)
    print("La suma de los numeros:")
    print(numero_input)
    print("El output/resultado:")
    print(resultado)