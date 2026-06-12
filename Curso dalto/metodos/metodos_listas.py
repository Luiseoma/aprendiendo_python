#"list" crea una lista (es una función) pero no es muy usado, lo más común es usarlo para dejarla vacía

lista = list([10 , 29, 15, 4, 1999, 500])


#"len" devuelve cuantos elementos tiene la lista 

cantidad = len(lista)

#"APPEND" agrega elementos a la lista

lista.append(100)

#"insert" agrega un elemento a la lista en el indice especificado

lista.insert(4, 70 )

#"extend" agrega varios elementos a la lista

lista.extend([40, 35] )

#"pop" elimina un elemento de una lista, pide indice y devuelve valor

lista.pop(0) #-1 para eliminar el último -2 para eliminar el penúltimo

#"remove" remueve un elemento de una lista, pide valor

lista.remove(35)

#"clear" elimina todos los elementos de una lista

#lista.clear()

#"sort" ordena los elementos de forma ascendete (si utilizamos reverse=True los ordena en reversa)

lista.sort()

#"reverse" invierte los elementos de una lista

lista.reverse()

print(lista)

