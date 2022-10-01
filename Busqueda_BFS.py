# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 18:15:52 2022

@author: Emmanuel
"""
#####################################################################
# ADALBERTO EMMANUEL ROJAS PEREA
# 173374
# Analisis y diseño de algoritmos MIC
#Busqueda en profundidad BFS

#Nota : para la siguiente tarea modifico el archivo para leer directamente 
#desde un archivo de texto 


arbol = {
  '0' : ['1','4'],
  '1' : ['0', '2','3','4'],
  '2' : ['1','3'],
  '3' : ['1','2','4'],
  '4' : ['0','3','1'],
  
}

visitado = [] # Lista vacia que contendra los nodos visitados
cola = []     # Lista vacia para poner los nodos en cola
# Creamos la funcion BFS
#El vertice tiene que ser el vertice raiz
def bfs(visitado, arbol, vertice):
  visitado.append(vertice)
  cola.append(vertice)
# Creamos un bucle para visitar cada nodo
 
  while cola:
    #quitamos el primer elemento que esta en la lista          
    m = cola.pop(0) 
    print (m, end = " ")
    
    for vecino in arbol[m]:
      if vecino not in visitado:
        visitado.append(vecino)
        cola.append(vecino)

 
print("---------------------------------------------------------")
print("----------------Busqueda en Anchura BFS------------------")
print("---------------------------------------------------------")
#LLamar a la funcion BFS, poniendo el vertice raiz
bfs(visitado, arbol, '0')