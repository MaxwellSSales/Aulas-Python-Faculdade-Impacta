# Crie um programa que exiba os cinco primeiros números naturais.

n = 0 

'''
Por quê? Precisamos de uma variável para acompanhar qual número natural estamos exibindo no momento. Inicializamos essa variável chamada n com o valor zero, pois queremos começar exibindo o primeiro número natural (considerando o zero como o primeiro neste caso). Essa variável atuará como um contador.
'''

while n < 5: # ... código dentro do loop ...
    '''
    Por quê? Queremos exibir os números um por um até chegar ao quinto número natural. O while é uma estrutura de repetição que permite executar um bloco de código repetidamente enquanto uma determinada condição1 (n < 5) for verdadeira.
    '''
    print(n)
    '''
    Por quê? Dentro do loop, a cada iteração, queremos mostrar o valor atual da variável n na tela. Essa é a ação principal do programa: exibir os números naturais.
    '''
    n += 1
    
    '''
    Por quê? Depois de exibir o valor atual de n, precisamos incrementá-lo em 1 para que, na próxima vez que o loop rodar, o próximo número natural seja exibido. O operador += é uma forma abreviada de escrever n = n + 1.
    '''
    
    
    print('Usando for')
    for x in range(5):
        print(x)