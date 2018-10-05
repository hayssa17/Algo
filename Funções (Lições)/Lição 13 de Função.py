#Lição 13  'Desconto'
def apresentação():
    print('Play')
    print('IaI ! de boa?')
    print('Olá! meu nome é Hayssa e seja bem-vindo ao meu programa!')
   
def número(V,D):
    print('Programa em execução...')
    r=(D*V)/100
    
    valor_pago=V-r
    print(valor_pago)
   
    
def fim():
     print('Obrigada por preferir esse programa')
     
   

apresentação()
    
valor=int(input('Digite o valor do produto:'))
desconto=int(input('Digite o valor do desconto á ser aplicado:'))


número(valor,desconto)


    
fim()
