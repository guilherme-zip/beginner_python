
""" Construa um programa no qual um usuário informe a sua 
estatura em metros e o programa converta-a para centímetros. """
try:
    altura=float(input("Digite sua estatura em metros e veja a mágica:"))
    altura_cm = altura*100
    
    print (f"Dado que sua altura em metros é {altura}m em centimetros ela será {altura_cm}cm")
except ValueError:
    print("Veja se você está digitando correto,exemplo:\n Tenho 1,60 metros --> 1.60")
