"""
 Funções são blocos de códigos reutilizáveis que permite encapsular tarefas específicas e serem executadas ao decorrer do código.
 I)     def function () ->Função sem parâmetro 
 II)    def function (parâmetro) ->Função com o parâmetro nome 
 III)   def function (*parâmetro) ->Função que permite inserir uma tupla 
 IV)    def function (**parâmetro) ->Função que permite inserir um dicionário 
 V)     lambda arg : expressão     ->Tipo de função "reduzida"
"""
""" #Calculadora de soma com a função def com a atribuição de tuplas 
def soma (*numeros):
    total =0
    for numero in numeros:
        total += numero
    return total 
print(soma(499,1,0.05))#Saída = 500,05 -> Somatório de todos os numeros da lista 
 """
""" #Calculadora de soma com a função def 
def soma(n1,n2):
    return n1+n2
n1=int(input("Digit um valor inteiro para n1:"))
n2=int(input("Digit um valor inteiro para n2:"))

print(soma(n1,n2)) """

#calculadora de soma com a função lambda
soma = lambda n1,n2:n1+n2 
n1=int(input("Digit um valor inteiro para n1:"))
n2=int(input("Digit um valor inteiro para n2:"))

print(soma(n1, n2))