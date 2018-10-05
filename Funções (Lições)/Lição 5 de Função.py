#lição 5

def apresentação():
    print('Olá! meu nome é Hayssa e seja bem-vindo ao meu programa!')

def números(a,b,c):
    print('Programa em execução')
    soma=a+b+c
    print(a,'+',b,'+',c,'=',soma)
    

def fim():
    print('Obrigada por preferir esse programa')



print('Play')
apresentação()

N1=int(input('Digite um número:' ))
N2=int(input('Digite um segundo número:'))
N3=int(input('Digite um terceiro número:'))

números(N1,N2,N3)



fim()
      
