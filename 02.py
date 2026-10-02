# Crie um algoritmo que leia 3 valores (lados de um triângulo)
# Determine se forma um triângulo, e se formar verifique
# se é um equilátero, escaleno  isóceles.

lado1 = float (input("Digite o valor do lado 1 do triângulo:"))
lado2 = float (input("Digite o valor do lado 2 do triângulo:"))
lado3 = float (input ("Digite o valor do lado 3 do triângulo:"))

triângulo = (lado1 + lado2 >= lado3 and lado1 + lado3 >= lado2 and lado2 + lado3 >= lado1)
Não_triângulo = (lado1 + lado2 < lado3 and lado1 + lado3 < lado2 and lado2 + lado3 < lado1)

if triângulo:
    (lado1 + lado2 > lado3 and lado1 + lado3 >= lado2 and lado2 + lado3 >= lado1) == triângulo

else:
    situacao = Não_triângulo

if triângulo:
    (lado1 == lado2 == lado3) 
elif triângulo:
    (lado1 == lado2 !=lado3)

else:
    (lado1 != lado2 != lado3)

Equilátero = (lado1 == lado2 == lado3)
Escalêno = (lado1 == lado2 != lado3)
Isósceles = (lado1 != lado2 != lado3)


print(f"Equilátero: {Equilátero}")
print (f"Escaleno: {Escalêno}")
print (f"Isósceles {Isósceles}")


print(f"É um triângulo: {triângulo}")
print (f"Não é um triângulo: {Não_triângulo}")