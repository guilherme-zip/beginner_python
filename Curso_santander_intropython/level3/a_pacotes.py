"""
"Pakpage" são pastas no python para organizar melhor o código 
"""
from pacotes_python import modulo1
start =input("Welcome to calculator\nEscolha a operação de sua preferência: ")

if start in ("Soma","soma","+","sum"):
    op = "Soma"
    func= modulo1.soma
elif start in("Subtracao","Subtração","subtracao","subtração","-"):
    op="Subtracao"
    func=modulo1.subtra
elif start in("Divisão","Divisao","divisão","divisao","/"):
    op="Divisão"
    func=modulo1.dive
elif start in("Multiplicação","multiplicacao","Multiplicacao","multiplicação","*"):
    op="Multiplicação"
    func=modulo1.mult
else:
    print("Operação inválida")
    exit()
print("A operação que foi selecionada é :",op)

try:
    n1=int(input("Digite um número inteiro positivo:   "))
    n2=int(input("Digite outro número inteiro positivo:  "))
    if n1<0 or n2<0:
        raise ValueError("Informe um número inteiro positivo")
except ValueError as erro:
    print("Have a erro 😒:",erro)
    exit()

print("O resultadado de sua operação é:",func(n1,n2))


