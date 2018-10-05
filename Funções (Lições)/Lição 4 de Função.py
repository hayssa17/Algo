#Lição 4
def apresentação():
    print('IaI ! de boa?')
    print('Esse programa é meu, eu sou Hayssa Gabrielly e seja bem vindo(a)!!')
    
def quem_é_vc(nome,idade):
    print('Gostaria de conhecer mais sobre você')
    
def fim():
    print('Mas,agora tenho que ir')
    
               

print('Inicio')
apresentação()
    
print('Programa em execução')

nome=input('qual é o seu nome:')
print('Oh! nome maneiro!!')
print('É um prazer te conhecer',nome)
idade=int(input('Qual é a sua idade? :'))
if idade>17:
    print('Oh! Quem diria você é maior de idade né! TRISTE!! Você não pode mais ir na piscina de bolhinhas.')
else:
    print('Oh! Que maneiro, você é menor de idade. Ainda pode ir no MC donaits e pedir o lanche com brinquedo sem que ninguém te julgue!!')
    
quem_é_vc(nome,idade)

    
fim()

print('chau! chau!')
