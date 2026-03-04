"""
Programa que calcular o preço final a partir do número de camisas. Seu Tanaka definiu as se guintes regras de desconto:
• Até 5 camisas, desconto de 3%
• Acima de 5 camisas e até 10 camisas, desconto de 
5%; e 
• Acima de 10 camisas, desconto de 7%.
>>Task : Calcule e imprima o valor a ser pago,dado que o custo de uma camisa é R$12,50

"""
def calcDesconto(quanti_camisa,v_inicio):
    desconto1=v_inicio*0.03
    desconto2=v_inicio*0.05
    desconto3=v_inicio*0.07
    
    if quanti_camisa <=5:
        return v_inicio - desconto1  #3%
    elif 5< quanti_camisa <=10:
        return v_inicio - desconto2  #5%
    else:
        return v_inicio - desconto3 #7%

quanti_camisa=int(input('Digite o valor correspondente a quantidade de camisas que desejas comprar:'))
v_inicio = quanti_camisa * 12.50 #Valor a ser pago por unidade de camisa sem o desconto 
print(f"Você iria pagar {v_inicio:.2f}\nMas como decidiu levar {quanti_camisa} camisas pagará agora : R$ {calcDesconto(quanti_camisa,v_inicio):.2f}")