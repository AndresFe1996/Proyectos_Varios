# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 18:17:18 2022

@author: Home
"""

import string
import random

conteo=0
alfabeto=list(string.ascii_lowercase)
indices=[x for x in range(0,28)]
conteo=0
argumento=8 # toma el numero que se necesite y restar 1 (si la longitud es 15 entonces -1 es 14)

numeros=[i for i in range(0,100)]

palabras=""

while conteo <= argumento:
    conteo+=1 # inicia en 1
    val=random.randint(0,25) # trae un numero aleatorio entre el 0 y el 25 se quita la ñ
    letter=alfabeto[val] # el numero aleatorio busca se equivalencia en la lista de alfabeto
    palabras+=letter # asigna la letra en la palabra que se construye
    
print(palabras)