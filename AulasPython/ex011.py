# Crie um programa que peça ao usuário diversos preços e, ao final, exiba a soma do preço.
# Obs: Considere 'diversos' com uma quantidade determinada pelo usuário.

soma = 0 # Inicia uma variável com o valor 0 para armazenar os valores que seram somados.
qtd = int(input('Quantidade? ')) # Solicta ao usuario a quantidade de vezes que o loop será executado.
qtd2 = qtd

while qtd > 0: # Condição do loop while (enquanto a qtd for maior que 0):
    preco = float(input('Preço? ')) # Solicita o preço ao usuário.
    soma += preco # Armazena os valores de preco na variavel soma
    qtd -= 1 # decrementa a quantidade da variavel qtd para chegar 
print(f'A soma dos preços é {soma:.2f}') #

print('Usando for:')
qtd = int(input('Informe a quantidade: '))
soma = 0
for i in range (qtd):
    preco = float(input('informe o preço: R$ '))
    soma += preco
print(soma/qtd)