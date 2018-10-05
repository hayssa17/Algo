#lição 6

def apresentação():
    print('Olá! meu nome é Hayssa e seja bem-vindo ao meu programa!')

def número(A,B):
    print('Programa em execução!')
    R=A**B
    print(A,'*','*',B,'=',R)

def fim():
    print('Obrigada por preferir esse programa')


print('Play')

apresentação()

N1=int(input('Digite um número:'))
N2=int(input('Digite outro número:'))

número(N1,N2)

fim()
    
