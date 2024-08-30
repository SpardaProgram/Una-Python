from decimal import Decimal
import sys

""" Primeira questão """

boleto1 = float(input("Digite o primeiro boleto: "))
boleto2 = float(input("Digite o segundo boleto: "))
boleto3 = float(input("Digite o terceiro boleto: "))
boleto4 = float(input("Digite o quarto boleto: "))

salario_l = float(input("Digite o salário líquido disponível: "))

total = boleto1 + boleto2 + boleto3 + boleto4

print(f"O TOTAL DA FACADA É R${Decimal(total).quantize(Decimal(10)**-2)}")
print(f"SOBRARÁ UM TOTAL DE R${Decimal(salario_l-total).quantize(Decimal(10)**-2)}")

sys.exit(0)

""" Segunda questão """

boleto1 = float(input("Digite o primeiro boleto: "))
boleto2 = float(input("Digite o segundo boleto: "))
boleto3 = float(input("Digite o terceiro boleto: "))
boleto4 = float(input("Digite o quarto boleto: "))

salario_b = float(input("Digite o salário bruto disponível: "))
salario_l = salario_b * (1 - 0.14)

total = boleto1 + boleto2 + boleto3 + boleto4

print(f"O TOTAL DA FACADA É R${Decimal(total).quantize(Decimal(10)**-2)}")
print(f"O VALOR DO SALÁRIO LÍQUIDO SERÁ DE R${Decimal(salario_l).quantize(Decimal(10)**-2)}")
print(f"SOBRARÁ UM TOTAL DE R${Decimal(salario_l-total).quantize(Decimal(10)**-2)}")

sys.exit(0)