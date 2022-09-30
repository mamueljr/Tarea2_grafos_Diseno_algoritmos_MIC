# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
ADALBERTO EMMANUEL ROJAS PEREA
173374
DISEÑO DE ALGORITMOS MIC
TAREA 2 : LISTA DE ADYESENCIA
"""
#definir vertice
class V:
    def __init__(self, i):
        self.id=i
        self.repaso = False
        self.nivel = -1
        self.vecino = []
        
    def anadirVertice(self, ver):
        #verificar que no exista ya en la lista
        if not ver in self.vecino:
            self.vecino.appen(ver)
class G:
    def __init__(self):
        self.vertices = {}
        
    def nuevoVertice(self,ver):
        #verificar de nuevo que el vertice no exista en la lista
        if ver not in self.vertices:
            self.vertices[ver]= V(ver)
            
    def conectaArista(self, v1, v2):
        #crear grafica no direccionada
        #ver si existen los vertices
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].anadirVertice(v2)
            self.vertices[v2].anadirVertice(v1)
            
def main():
    g = G()
    lista= [0,1,2,3,4]
    for cada_vertice in lista:
        g.nuevoVertice(cada_vertice)
    
    lista = [0,1,1,2,2,3,3,4,4,0]
    for i in range(0, len(lista) - 1, 2):
        g.conectaArista(lista[1], lista[i+1])
    
    for v in g.vertices:
        print(v,g.vertices[v].vecino)

main()
    
            
            
            
                  
