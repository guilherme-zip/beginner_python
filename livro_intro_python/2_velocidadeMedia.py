"""
Construa um programa que receba do usuário a variação do 
deslocamento de um objeto (em metros) e a variação do tempo 
percorrido (em segundo). Ao fim, o programa deve calcular a 
velocidade média, em m/s, do objeto 
"""
def vmCalculator(s_final,s_inicial,t_final,t_inicial):
    var_s = s_final - s_inicial 
    var_t = t_final - t_inicial 
    vm      = (var_s / var_t ) / 3.6
    return vm

print("Primeiro para calcular sua velocidade média precisamos saber de onde seu veículo PARTIU: \n")
s_inicial=float(input("Digite o *km* de partida: "))
t_inicial=float(input("Digite o *tempo(em horas)* de partida: "))
print(f"Depois de saber que o seu km de partida é {s_inicial} e no tempo {t_inicial};Precisamos do Km e o tempo em que se concluiu o tragéto:")

s_final=float(input("Digite o *km* final: "))
t_final=float(input("Digite o *tempo(em horas)* final: "))

print(f"O objejeto tem uma velocidade média de {vmCalculator(s_final,s_inicial,t_final,t_inicial)} m/s")