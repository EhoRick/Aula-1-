# Escreva um programa em Python que peça as seguintes informações:
# - Idade (um numero inteiro)
# - Altura em centímetros (um numero inteiro)
# - Tem autorização dos país? (uma string: "sim"ou "não")
#
# O programa deve exibir "Acesso Liberado!" se o visitante 
# puder andar no brinquedo, ou "Acesso Negado." caso contrário.
#
# Regra
# O visitante pode entrar se:
# - Tiver idade maior ou igual a 12 E altura maior ou igual a 140 OU
# - se tiver autorizacao igual a "sim".


Idade = int (input("Digite a Idade do Cidadão: "))
Altura =  int (input("Digite a Altura do Cidadão: "))
Autorização = input("Ele possuí a autorização?: ")

if Idade >= 12:
    situacao = "Liberado"

else:
    situacao = "Não Autorizado"


Altura_parque = 140

if Altura >= 140:
    situacao = "Liberado"
else:
    situacao = "Não Autorizado"


Autorização = "sim" or "nao" 

if Altura >= 140 and Idade >= 12 and Autorização == "sim" or Altura >= 140 and Idade < 12 and Autorização == "sim"or Altura < 140 and Idade <12 and Autorização == "sim" or Altura < 140 and Idade >= 12 and Autorização == "sim":
    print(f"Acesso permitido")   

 
else:
    print(f"Acesso Negado")
    


 
 
