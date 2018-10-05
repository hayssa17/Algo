#Lição 10
def apresentação():
    print('Play')
    print('IaI ! de boa?')
    print('Olá! meu nome é Hayssa e seja bem-vindo ao meu programa!')
   
def número_e_palavra(y,p):
    print('Programa em execução...')
    while y > 0:
        print(p)
        y=y-1
    
    
def fim():
     print('Obrigada por preferir esse programa')
     
    
               


apresentação()
    
N=int(input('Digite um número:'))
palavra=input('Digite uma palavra:')
número_e_palavra(N,palavra)
    
fim()


