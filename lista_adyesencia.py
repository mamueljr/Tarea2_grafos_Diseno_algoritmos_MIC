#####################################################################
# ADALBERTO EMMANUEL ROJAS PEREA
# 173374
# Analisis y diseño de algoritmos MIC
# Definir funcion para insertar vertice a la lista de adyesencia

def insertar_vertice(lista, u, v):

    # Insertar vertice v a vertice u
    lista[u].append(v)
    return
'''
 Definir funcion para imprimir la lista de adyesencia,
 recibe como argumento el numero de vertices V
'''

def imprimir_lista(lista, V):

    for i in range(V):
        #Uso el parametro end para no dar el salto de linea y adjuntalo con los nodos
        print(i, end='')

        for j in lista[i]:
            print(' -> ' + str(j), end='')

        print()

    print()


# funcion principal
if __name__ == '__main__':
    # numero de vertices
    V = 5

    listaDelistaesencia = [[] for i in range(V)]

    # Insertar aristas en esta ocacion dejare los Vertices y aristas aqui en el codigo,
    # Para futuras trareas agrego codigo pare pedir numero de nodos y sus aristas
    insertar_vertice(listaDelistaesencia, 0, 1)
    insertar_vertice(listaDelistaesencia, 0, 4)
    insertar_vertice(listaDelistaesencia, 1, 0)
    insertar_vertice(listaDelistaesencia, 1, 2)
    insertar_vertice(listaDelistaesencia, 1, 3)
    insertar_vertice(listaDelistaesencia, 1, 4)
    insertar_vertice(listaDelistaesencia, 2, 1)
    insertar_vertice(listaDelistaesencia, 2, 3)
    insertar_vertice(listaDelistaesencia, 3, 1)
    insertar_vertice(listaDelistaesencia, 3, 2)
    insertar_vertice(listaDelistaesencia, 3, 4)
    insertar_vertice(listaDelistaesencia, 4, 0)
    insertar_vertice(listaDelistaesencia, 4, 1)
    insertar_vertice(listaDelistaesencia, 4, 3)

    # Imprimir la lista de Adyesencia
    print("---------------------------------------------------------")
    print("-------------- Lista de Adyesencia ----------------------")
    print("---------------------------------------------------------")
    print("NODO -vertice-> NODO ...")
    imprimir_lista(listaDelistaesencia, V)
