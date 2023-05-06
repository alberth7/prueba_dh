def solution(N, A):
    vector_contador = [0] * N # inicializando vector contador con todos los valores en 0
    max_contador = 0 #inicializando contador maximo en 0
    aux_max_contador = 0 #inicializando contador auxiliar maximo en 0
    
    # recoriendo el "vector de enteros" 
    for k in A:
        if k == N + 1: # si A[K] = N + 1, entonces la operación K es el max counter
            aux_max_contador = max_contador
        else: # si A[K] = X, tal que 1 ≤ X ≤ N, entonces la operación K es increase(X)
            if vector_contador[k-1] < aux_max_contador:
                vector_contador[k-1] = aux_max_contador
            vector_contador[k-1] = vector_contador[k-1] + 1
            
            if vector_contador[k-1] > max_contador:
                max_contador = vector_contador[k-1]
        
        #Actulizando los valores del "vector de contadores"
        for i in range(N):
            if vector_contador[i] < aux_max_contador:
                vector_contador[i] = aux_max_contador
        
        print(vector_contador)

    return vector_contador

if __name__ == "__main__":
    '''
    Inicializando los valores de ejemplo
    '''
    N = 5 #longitud del "vector de contadores"
    M = 7 #longitud del "vector de enteros"
    A = [0] * M # creacion del "vector de enteros" con valores 0
    # Adicionando valores al "vector de enteros"
    A[0] = 1
    A[1] = 1
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 5
    A[6] = 5
    resultado = solution(N, A) # Enviando N y vector A a la funcion solucion y guardando el resultado
    print("<<<<< Resultado >>>>>>>")
    print(resultado)
    