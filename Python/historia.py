import time
def fim():
    print("")
    print("OBRIGADO POR JOGAR :)")
def intro():
    print("Bem Vindo ao jogo Labirinto do terror.")
    time.sleep(1)
    print("")
    print("Em uma noite sombria você estava caminhando pelo parque quando derrepente sentiu uma batida na cabeça e tudo ficou escuro.   ")
    time.sleep(1)
    
    print("")
    print("Você acorda em um labirinto onde a sangue pelas paredes, marcas de mãos, dentes e ossos pelo chão. Você ouve um barulho de gritos e vê em sua frente três caminhos")
    print("")
    
    time.sleep(1)
    iniciar_jogo()

def iniciar_jogo():
    print("")
    print("1.Caminho esquerda.")
    print("2.Caminho do meio.")
    print("3.Caminho da direita.")
    print("")
    
    escolha = input("Qual será sua escolha?:")   
    
    if escolha == '1':
        escolha_esquerda()    
    elif escolha == '2':
        escolha_meio()
    elif escolha == '3':
        escolha_direita()
    else:
        print("")
        print("vc morreu...Por não escolhar uma das opicoes")
        print("")
        fim()

def escolha_esquerda():
    print("Ao seguir pela esquerda você encontra uma criatura alta, magrela, preta como a escuridão, olhos esbugalhados e com dentes enormes.A criatura olha com seus olhos sedentos de sangue.")
    print("")
       
    time.sleep(2)
    
    print("")
    print("1.Para correr da criatura")
    print("2.para lutar com a criatura: ")
    print("")
 
    escolha = input("Qual sua Escolha?:")
    
    if escolha == '1':
        print("Você foi pego quando tentou correr a criatura mordeu sua cabeça com a boca babando e balançou até ela se soltar de seu pescoço. VOCÊ MORREU")
        fim()
    else:
        print("Você tenta acertar um soco na criatura que segura seu braço e o arranca...depois a criatura abre sua barriga e começa a comer suas tripas. VOCÊ MORREU")
        fim()

def escolha_meio():
    print("Indo pelo meio você sobe algumas escadas e chegando no final abre uma porta quando você abre se depara com um homem alto segurando um machado na mão direita e um corpo sem cabeça na esquerda... ele olha para você e solta o corpo... Você entra em desepero e começa a observar ao redor ao olhar para os lados você encontra uma janela e do lado oposto uma faca em cima da mesa...")
    print("")
       
    time.sleep(2)
    
    print("")
    print("1. Para pegar a faca")
    print("2. Correr para a janela ")
    print("")
 
    escolha = input("Qual sua Escolha?:")
    
    if escolha == '1':
        print("VocÊ rapidamente corre em direção a faca o homem tenta te acertar um golpe com o machado, mas você desvia ao pegar a faca você o acerta na perna... ele te empurra para longe fazendo você bater em uma parede e quebrar sua perna")
        print("")
        print("1. Continuar lutando")
        print("2. Correr para a janela ")
        print("")
        
        escolha = input("Qual sua escolha?: ")
        
        if escolha == '1':
            print("Mesmo com a perna quebrada você consegue se levantar e atacar novamente o homem... Ele tenta te acertar com o machado, mas você desvia e acerta um golpe no pescoço do homem... ele cai sangrando... Procurando pela casa você encontra um telefone e liga para a policia quando eles chegam investigam a residencia e enconram varias coisas macabras e descobrem que esse homem já era procurado a muito tempo por assassinato e ser membro de uma seita... após se recuperar no hospital você recebe uma recompensa por ajudar a policia com o ocorrido")
            fim()
        else:
            print("")
            print("Você desiste de lutar e tenta correr em direção a janela, mas você cai o homem sem piedade decepa suas duas pernas(Você desmaia por conta dos machucados)...Quando você acorda está pendurado pelos braços enquanto sangra até morrer.  ")
            fim()
        
    else:
        print("")
        print("Você corre em direção a janela o homem corre atrás de você, porém você é mais rapido e pula a janela quebrando tudo e se cortando você vê um portão alto e corre em direção a ele... o homem não parece mais te seguir... ao pular o portão você é atropelado por um carro... o motorista te ajuda e o leva para o hospital depois de uma semana você acorda, mas você não se lembra de nada além de ser atropelado")
        fim()

def escolha_direita():
    print("Você segue pela direita as paredes começam a ficar estreitos cada vez as paredes ficam mais proximas de você mais a frente você encontra um cachorro enorme que está dormindo, mas está bloqueando o caminho pelo chão está cheio de sangue e ossos e você pensa em uma possibilidade de pegar um dos ossos e tentar golpear o cachorro")
    print("")
       
    time.sleep(2)
    
    print("")
    print("1. Pegar o osso e atacar o cachorro ")
    print("2. Tentar passar com cuidado por cima do cachorro ")
    print("")
 
    escolha = input("Qual sua Escolha?: ")
    
    if escolha == '1':
        print("Você pega um dos ossos e acerta a cabeça do cachorro antes que ele reagisse você o acerta varias e varias vezes... o cachorro morre. Você segue o caminho e encontra uma porta... Após abrir você está em uma sala cheia de corpos humanos(Aparentemente os corpos eram usados para alimentar o cachorro)... ao sair dessa sala você vê um jardim com um grande portao feito de madeira ao tentar abrir ela está trancada... ")
        print("") 
        
        time.sleep(2)
    
        print("")
        print("1. Arrombar a porta")
        print("2. Pular a porta ")
        print("")
    
        escolha = input("Qual sua escolha? ")
        
        if escolha == '1':
            print("Você começa a chutar a porta... Depois de alguns chutes ela começa a ceder ao olhar para trás um homem alto está te observado pela janela... ele aparenta estar esperando algo(O cachorro)... porém nada aparece após mais chutes a porta se abre você consegue sair e pedir ajuda... mesmo contando sobre a historia não acreditam pensam que você está louco e você é internado.")
            print("")
            fim()
        else:
            print("")
            print("Você rapidamente pula o portão, mas ao cair do outro lado torce seu tornozelo você começa a andar mancando e pedindo por ajuda... um carro para e te socorre ao explicar a historia e o motorista ver seu ferimento ele o leva para o hospital mais proximo onde você é socorrido o motorista foi para delegacia para contar sobre o ocorrido... Um tempo depois você recebe a noticia que o dono da casa onde você estava  foi preso e foi descoberto inumeras coisas macabras em sua casa.")
            fim()
    
    else:
        
        print("")
        print("Você tenta passar sorrateiramente pelo cachorro, mas ele acaba acordando... você corre para escapar do cachorro e encontra uma porta...Após abrir rapidamente a porta você está em uma sala cheia de corpos humanos(Aparentemente os corpos eram usados para alimentar o cachorro)... ao sair dessa sala você vê um jardim com um grande portão feito de madeira ao tentar abrir ela está trancada...o cachorro está correndo em sua direção e você começa a se desesperar...")
        
    time.sleep(2)

    print("")
    print("1. Arrombar a porta")
    print("2. Pular a porta ")
    print("")
    
    escolha = input("Qual sua escolha? ")
        
    if escolha == '1':
        print("Você começa a chutar a porta... Depois de alguns chutes ela começa a ceder ao olhar para trás um homem alto está te observado pela janela... e o cachorro está se aproximando cada vez mais... você começa chutar a porta deseperado, mas é inutil o cachorro chega até você e morde sua perna... o homem que estava obsevando começa a andar em sua direção... o homem te arrasta novamente para dentro da sala cheia de corpos VOCÊ VIROU LANCHE DE CACHORRO")
        fim()
        
    else:
        print("")
        print("Você rapidamente pula o portão, mas ao cair do outro lado torce seu tornozelo você começa a andar mancando e pedindo por ajuda... o cachorro fica latindo muito... depois de um tempo um carro para, mas antes que o motorista sair do veiculo o homem com machado abre o portão e te ataca... ele acerta sua perna e quando foi te acertar outro golpe o motorista acerta um tiro fazendo ele cair já sem vida o cachorro corre acuado... o motorista te socorre e o leva para o hospital onde você é socorrido o motorista foi para delegacia para contar sobre o ocorrido... Um tempo depois você recebe a noticia que o dono da casa onde você estava  era um assassino procurado a muito tempo e que foi descoberto inumeras coisas macabras em sua casa... e o motorista que te socorreu ganhou uma recompensa.")
        fim()

intro()











