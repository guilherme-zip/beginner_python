"""
Conjunto é uma estrutura de dados mutáveis e não ordenados que permite armazenar coleção de documentos únicos ,são definidos por { } ou criados com a função set()
"""
frutas ={"apple","pineple","banana","green apple"}
numeros = set([1,2,3,4])

frutas.add("pera") 
print(",".join(frutas)) #Saída {"apple","pineple","banana","green apple","pera"}
#",".join -->Faz com que o código retorne sem as chaves e áspas 

frutas.add("pera")
print(frutas)  # Imprime {"maçã", "banana", "laranja", "pera"}

frutas.remove("banana")
print(frutas)  # Imprime {"maçã", "laranja", "pera"}

frutas.discard("uva")
print(frutas)  # Imprime {"maçã", "laranja", "pera"}

frutas.clear()
print(frutas)  # Imprime set()