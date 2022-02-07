'''O problema de Monty Hall, também conhecido por paradoxo de Monty Hall é um problema matemático e paradoxo que surgiu a partir de um concurso televisivo dos Estados Unidos 
chamado Let’s Make a Deal, exibido na década de 1970.
O jogo consistia no seguinte: Monty Hall, o apresentador, apresentava três portas aos concorrentes. 
Atrás de uma delas estava um prêmio (um carro) e, atrás das outras duas, dois bodes.
Na 1.ª etapa o concorrente escolhe uma das três portas (que ainda não é aberta);
Na 2.ª etapa, Monty abre uma das outras duas portas que o concorrente não escolheu, 
revelando que o carro não se encontra nessa porta e revelando um dos bodes;
Na 3.ª etapa Monty pergunta ao concorrente se quer decidir permanecer com a porta que escolheu no 
início do jogo ou se ele pretende mudar para a outra porta que ainda está fechada para então a abrir. 
Agora, com duas portas apenas para escolher — pois uma delas já se viu, na 2.ª etapa,
que não tinha o prêmio — e sabendo que o carro está atrás de uma das restantes duas,
o concorrente tem que tomar a decisão.'''


import os
from random import randint
os.system('cls')
p = [] 
print("Este é o LET´S MAKE A DEAL\nHá um prêmio em uma das 3 portas disponíveis.")    
def todas_portas():
    with open("todas_portas.txt","r") as arquivo:
        for linha in arquivo.read().splitlines():
            print(linha)
def ganhou():
    with open("ganhou.txt","r") as arquivo:
        for linha in arquivo.read().splitlines():
            print(linha)
def perdeu():
    with open("perdeu.txt","r") as arquivo:
        for linha in arquivo.read().splitlines():
            print(linha)
def porta1():
    with open("porta1.txt","r") as arquivo:
        for linha in arquivo.read().splitlines():
            print(linha)
def porta2():
    with open("porta2.txt","r") as arquivo:
        for linha in arquivo.read().splitlines():
            print(linha)
def porta3():
    with open("porta3.txt","r") as arquivo:
        for linha in arquivo.read().splitlines():
            print(linha)
         
def pergunta1(pergunta,min,max):
    while True:
        try:
            global a
            a = int(input(pergunta))
            if a < min or a > max:
                print(f"Valor não permitido. Você deve escolher uma porta entre {min} e {max}.")
            else:
                return a
        except Exception as e:
            print("O valor deve ser numérico.")

def pergunta2(pergunta,min,max):
    while True:
        try:
            global b
            b = int(input(pergunta))
            if b < min or b > max:
                print(f"Valor não permitido. Você deve escolher uma porta entre {min} e {max}.")
            else:
                return b
        except Exception as e:
            print("O valor deve ser numérico.")
            
def pergunta3(pergunta,min,max):
    while True:
        try:
            global c
            c = int(input(pergunta))
            if c < min or c > max:
                print(f"Valor não permitido. Você deve escolher uma porta entre {min} e {max}.")
            else:
                return c
        except Exception as e:
            print("O valor deve ser numérico.")

while True:
    jogar = input('Vamos jogar o "Let´s Make a Deal"? Pressione 1 para jogar ou qualquer tecla para sair.')
    if jogar != '1':
        break
    
    print('\nHá um prêmio atrás de uma das 3 portas. ')
    todas_portas() #chama a função que mostra os desenhos das portas
        
    pergunta1("ESCOLHE UMA PORTA: ",1,3)
    p.append(a) #adiciona o valor entrado pelo usuário na lista de portas
    print(f'\nBacana, você escolheu a porta {a}.')
    pergunta2(f'Agora vou deixar você escolher uma das portas que sobraram para retirar do jogo e escolher novamente.\nNo início do jogo suas chances eram 33,33% e agora serão de 50% !!!\nVAMOS CONTINUAR...RETIRE UMA PORTA: ',1,3)

    if a == 1 and b == 2:
        p.append(3)
        porta2()
    
    elif a == 1 and b == 3:
        p.append(2)
        porta3()
    elif a == 2 and b == 1:
        p.append(3)
        porta1()
    
    elif a == 2 and b == 3:
        p.append(1)
        porta3()

    elif a == 3 and b == 1:
        p.append(2)
        porta1()
        
    else:
        p.append(1)
        porta2()
    p.sort()
    x = p[0]
    y = p[1]
    
    porta_certa = randint(x,y)

    pergunta3("Deseja continuar com a porta que esolheu primeiro ou trocar? Escolha: ",1,3)

    if a == porta_certa:
        print('Você ganhou o prêmio!\n')
        ganhou()
    else:
        perdeu()
        print('\nO prêmio estava na porta',porta_certa)

sair = input('Precione qualquer tela para sair. ')
