def result_points(g_result, scoring_data):
    points = [0] * len(g_result)
    
    for i, position in enumerate(g_result):
        if position <= len(scoring_data):
            points[i] = scoring_data[position - 1]
            
    return points

def result_champions(g_results, scoring_data):
    points = [0] * len(g_results[0])

    for g_result in g_results:
        g_points = result_points(g_result, scoring_data)
        points = [p + rp for p, rp in zip(points, g_points)]

    max_points = max(points)
    champions = [str(i + 1) for i, p in enumerate(points) if p == max_points]

    return champions

def main():
    file = open("./Ejercicio2/output.txt", "w")
    
    while True:
        print("Ingresar en la primera posicion el numero de carreras seguido de un espacio en blanco y luego el numero de pilotos")
        
        try:
            G, P = map(int, input().split())
        except:
            print("El dato a ingresar tiene que ser de tipo numerico")
            break
        
        if G == 0 and P == 0:
            break
        
        # Validacion de entrada
        if (G < 0 or G > 100):
            print("Ingreso de valores no reconocidos para las carreras")
            break

        if (P < 0 or P > 100):
            print("Ingreso de valores no reconocidos para los pilotos")
            break


        g_results = []
        for g in range(G):
            print(f"Ingresa el orden de llegada para la carrera numero {g + 1} de los pilotos separando por un espacio en blanco")
            
            try:
                g_result = list(map(int, input().split()))
            except:
                print("El dato a ingresar tiene que ser de tipo numerico")
                break
            
            g_results.append(g_result)

        print("Ingresa el numero de sistemas de puntuacion")
        
        try:
            S = int(input())
        except:
            print("El dato a ingresar tiene que ser de tipo numerico")
            break
        
        if (S < 0 or S > 10):
            print("Ingreso de valores no reconocidos para el sistema de puntuacion")
            break
        
        champions = []

        for s in range(S):
            print(f"Ingresa los puntos para los pilotos en el sistema de puntuacion {s + 1} dejando un espacio en blanco")
            
            try:
                scoring_data = list(map(int, input().split()))
            except:
                print("El dato a ingresar tiene que ser de tipo numerico")
                break
            
            K = scoring_data[0]
            scoring_data = scoring_data[1:]
            result = result_champions(g_results, scoring_data)
            champions.append(result)

        print("*" * 55)
        file.write("************************************************************************************" + "\n")
        for i, champ in enumerate(champions):
            champ_str = ' '.join(champ)
            print(f"Campeón(es) del sistema de puntuación {i + 1} = {champ_str}")
            file.write(f"Campeón(es) del sistema de puntuación {i + 1} = {champ_str}" + "\n")
        file.write("************************************************************************************" + "\n")
            
        
        print("*" * 55)
            
    file.close()

if __name__ == "__main__":
    main()
