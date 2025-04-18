# Crie um programa que peça ao usuario diversos preços e, ao final, exiba a media dos preços.
# Obs: Considere 'diversos' com uma quantidade determinada pelo usuário.

soma = 0
qtd = int(input('Quantidade? '))
qtd2 = qtd

while qtd > 0:
    preco = float(input('Preço? R$ '))
    soma += preco
    qtd -= 1
print(f'A media dos preços é: R$ {soma / qtd2}')