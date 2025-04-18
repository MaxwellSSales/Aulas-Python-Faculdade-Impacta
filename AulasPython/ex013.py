# Crie um programa que exiba os n primeiros numeros naturais.
#Obs(1): Considere que n será um número dado pelo usuario.
#Obs(2): Exiba uma seguência descrecente.

n = int(input('n?'))
i = 0

while i < n:
    print(i)
    i += 1

num = int(input('Informe um número: '))
while num > 0:
    print(num)
    n-=1
    
print('Usando for')
num2 = int(input('Informe um número: '))
for x in range(num2, -1,-1):
    print(num2)