# 1. Cálculo de Expressões (0,2 ponto)
# Escreva um programa que peça ao usuário dois números inteiros x e y e calcule o seguinte:
# z = x + y * 2
# O programa deve exibir o resultado no formato:
# O resultado da expressão é: [resultado]

x = int(input("Digite o Primeiro valor: "))
y = int(input("Digite o Segundo Valor: "))
z = x + y * 2
print(f'O resultado da expressão é: {z}') 

# 2. Saudação Personalizada (0,2 ponto)
# Crie um programa que solicite o nome e a idade do usuário e exiba a seguinte mensagem:
# Olá, [nome]! Você tem [idade] anos.

nome = input("Informe o seu nome: ")
idade = int(input("Informe a sua idade: "))
print(f'Olá, {nome}! Você tem {idade} anos.')

# 3. Verificação de Condições Lógicas (0,2 ponto)
# Crie um programa que peça ao usuário três números inteiros (a, b e c).
# O programa deve verificar se a é menor que b E b é maior que c, OU se a + b é igual a c.
# Exiba uma das seguintes mensagens conforme o resultado:
# A condição é verdadeira!
# ou
# A condição é falsa!

a = int(input("Informe o Primeiro Nº Inteiro: "))
b = int(input("Informe o Segundo Nº Inteiro: "))
c = int(input("Informe o Terceiro Nº Inteiro: "))
if (a < b and b > c) or (a + b == c):
    print('A condição é verdadeira!')
else:
    print('Acondição é falsa')

# 4. Par ou Ímpar (0,2 ponto)
# Escreva um programa que peça ao usuário um número inteiro e determine se ele é PAR ou
# ÍMPAR.
# O programa deve exibir a mensagem correspondente:
# O número X é par.
# ou
# O número X é ímpar.

num = int(input("Informe um Nº Inteiro: "))
if num % 2 == 0:
    print(f'O número {num} é par')
else:
    print(f'O número {num} é ímpar')

# 5. Sistema de Desconto para Compras (0,2 ponto)
# Crie um programa que solicite ao usuário:
# - O valor unitário de um produto;
# - A quantidade comprada.
# O programa deve calcular o valor total da compra e aplicar um DESCONTO DE 10% caso o
# total seja maior ou igual a R$100,00.
# Se o desconto for aplicado, exiba:
# O total da compra com desconto é: R$ [valor_com_desconto]
# Caso contrário, exiba:
# O total da compra sem desconto é: R$ [valor_sem_desconto]

valor = float(input("Informe o valor do Produto: R$ "))
quant = int(input("Informe a quantidade comprada: "))
total = valor * quant
if (total >= 100):
    desconto = total * 0.10
    total = total - desconto
    print(f'O valor da compra com desconto é: R$ {total}')
else:
    print(f'O valor da compra sem o desconto é: R$ {total}')