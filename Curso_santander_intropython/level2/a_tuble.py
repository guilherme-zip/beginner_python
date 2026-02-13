"""
Tupla ou intânicas do tipo "tuple" são etrutura que armazenam dados que serão imutáveis ao decorrer do código e são representadas por : t= (x,y,z)
"""
t = (10, 20, 30, 20, 40, 20)
print("tupla:",t),

tamanho = len(t)
print(f"A tupla possui {tamanho} elementos."),#Saber a quantidade total de elementos na tupla

numero = int(input("Digite um número para buscar na tupla: "))

try:
    indice = t.index(numero)#Saber o **índice** da primeira aparição da variável 
    print(f"O número {numero} está no índice {indice}."),
    quantidade = t.count(numero)#Saber quantas vezes a variável foi apresentada 
    print(f"O número {numero} aparece {quantidade} vez na tupla."),

except ValueError:
    print(f"O número {numero} não está presente na tupla.Are you burro,man?")