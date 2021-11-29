lista_numeros=[29,20,16,28,18,23,6,27,23,27,24,8,30,7]
lista2=["mayor","menor","suma","promedio"]
lista_numeros.sort()
print (lista2[0],lista_numeros[-1])
print (lista2[1], lista_numeros[0])
print(lista2[2], sum(lista_numeros))
print(lista2[3], sum(lista_numeros)/len(lista_numeros))