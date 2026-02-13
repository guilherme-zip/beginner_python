"""
Programa que determina o que você vai beber para comemorar a formatura:
->Alunos  menores de idade == todinho 
->Alunos adolescentes      == Vodca
->Alunos +30               == Whisky 

"""
idade=int(input("Digite sua idade que irei fazer uma previsão bem agora:"))

if idade >=17:
    print("Hoje na formatura irás tomar \n TODINHO") #\n pula linha 
elif idade >=18 and idade < 29:
    print("IIIIH,vai encher o coco de \n VODCA")
else :
    print("A idade chega para todos,vai de Whisky hoje,né?")