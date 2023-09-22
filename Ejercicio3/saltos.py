def min_jumps(x):
    jumps = 0

    while x > 0:
        if x == 1:
            x -= 1
        elif x % 2 == 0:
            x //= 2
        else:
            x -= 1
            
        jumps += 1

    return jumps

def main():
    # Numero de pruebas
    t = int(input("Ingrese el número de casos de prueba: "))

    if t < 0 or t > 1000:
        print("Eror al ingresar el numero de casos")
        t = 0

    # Ingreso del punto X
    for _ in range(t):
        x = int(input("Ingrese la posición deseada: "))
        
        if x < 0 or x > 106:
            print("La posicion X deeada no coincide con el enunciado")
            break
        
        jumps = min_jumps(x)
        print(jumps)
        
        

if __name__ == '__main__':
    main()