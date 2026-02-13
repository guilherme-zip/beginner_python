conjunto=set()#aqui você acabou de criar um set vazio 

conjunto.add(1)#saída = {1}
conjunto.add('João')
conjunto.add('pera')
conjunto.add(5900)
#Saída = {1,João,pera,5900}
conjunto.discard('pera')#remove pera do conjunto e a saída fica : {1, 5900, 'João'}
print(conjunto)

