#Lição 2
def apresentação():
    print('Play')
    print('IaI ! de boa?')
    print('Esse programa é meu, eu sou Hayssa Gabrielly e seja bem vindo(a)!!')
    
def quem_é_vc():    
    print('Programa em execução')
    print('Gostaria de conhecer mais sobre você')
    nome=input('Qual é o seu nome:')
    print('Oh! nome maneiro!!')
    print('É um prazer te conhecer',nome)
    idade=int(input('Qual é a sua idade? :'))
    if idade>17:
        print('Oh! Quem diria você é maior de idade né! TRISTE!! Você não pode mais ir na piscina de bolhinhas.')
    else:
        print('Oh! Que maneiro, você ainda pode ir no MC donaits e pedir o lanche com brinquedo sem que ninguém te julgue!!')
    
def fim():
    print('Mas,agora tenho que ir')
    print('chau! chau!')
    
               


apresentação()

quem_é_vc()
 
fim()


