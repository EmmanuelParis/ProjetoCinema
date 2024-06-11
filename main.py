from PIL import Image
from os import system
from time import sleep
import validations as valid
import authentications as auth
import menus as menu
import movies as mov
import ticketManager as tck

users = [{
    'user' : 'emmanuel',
    'password' : '123',
    'age' : 18,
    'email' : 'emmanuelparis2005@gmail.com',
    'id' : False,
    'bank' : 100,
    'recognized' : True,
    'watched' : list()
    }]

movies = [{
    'title' : 'Interestelar: O Antes do Futuro',
    'genre' : 'Ficção Científica',
    'sinopse' :'Em "Interestelar: O Antes do Futuro", a humanidade está à beira do colapso quando estranhas distorções temporais começam a desfazer a realidade. Uma equipe heterogênea de exploradores é convocada para uma missão audaciosa: encontrar um novo lar para a humanidade. Navegando através de portais temporais e enfrentando perigos cósmicos, eles descobrem civilizações antigas e criaturas além da imaginação. No entanto, à medida que avançam, percebem que há algo mais sinistro em jogo - uma entidade cósmica ancestral que desafia as leis fundamentais do universo. Com o destino da humanidade em suas mãos, eles se veem em uma corrida contra o tempo e o espaço, lutando não apenas pela sobrevivência, mas pela própria essência da existência.',
    'ageRating' : '14',
    'duration' : '150',
    'hours' : '2',
    'minutes' : '30',
    'price'  : '25',
    'rating' : '99',
    'capacity' : 50,
    'chairs' : 50,
    'comments' : list(),
    'bought' : 0
},
          {
    'title' : 'Quebrando a Banca: O Tigrinho',
    'genre' : 'Comédia',
    'sinopse' :' Em "Quebrando a Banca: O Inimigo Agora é o Tigrinho", um grupo de amigos entusiastas de jogos de azar descobre uma nova casa de apostas clandestina conhecida como "O Tigrinho". Pensando ser apenas mais uma oportunidade de ganhar dinheiro fácil, eles mergulham de cabeça nos jogos oferecidos. No entanto, à medida que acumulam vitórias, percebem que algo está errado. O Tigrinho não joga limpo - ele manipula resultados e engana os jogadores para garantir seus lucros exorbitantes. Agora, os amigos se encontram em uma batalha desigual contra essa máquina gananciosa, lutando não apenas para recuperar o dinheiro perdido, mas também para expor as práticas corruptas do Tigrinho e proteger outros jogadores inocentes. Em uma trama repleta de suspense e reviravoltas, eles arriscam tudo em uma tentativa audaciosa de quebrar a banca e restaurar a justiça no mundo do jogo.',
    'ageRating' : '10',
    'duration' : '180',
    'hours' : '3',
    'minutes' : '0',
    'price'  : '30',
    'rating' : '88',
    'capacity' : 80,
    'chairs' : 80,
    'comments' : list(),
    'bought' : 0
}]

while True:
    system('cls')
    menu.title('MENU PRINCIPAL')
    action = menu.menu(['LogIn','Cadastro','Sair'])

    if action == 1:
        loggedIn = False
        user = auth.logIn(users)
        if user != None:
            loggedIn = True
        sleep(1.5)
        
        while loggedIn:
            if (user['recognized'] == True) and (user['id'] == False):
                    system('cls')
                    menu.title('MENU - CLIENTES')
                    print(f'\033[36mCarteira: R${round(user['bank'],2)}\033[m\n')
                    action = menu.menu(['Depositar Dinheiro', 'Catálogo', 'Comprar Ingresso', 'Avaliar Filmes', 'Ingressos Vendidos', 'LogOut'])
                    
                    if action == 1:
                        deposit = valid.valInt('\033[34mQuanto deseja depositar? \nR$ \033[m')
                        print('\033[33mGerando o QR Code para depósito...\033[m')
                        sleep(1)                
                        pix = Image.open("./pix.png")
                        pix.show()
                        user['bank'] += deposit
                        sleep(3)
                    
                    elif action == 2:
                        mov.catalogue(movies)
                        
                    elif action == 3:
                        mov.buyTicket(movies, users)
                    
                    elif action == 4:
                        mov.rateMovie(movies,users)
                    
                    elif action == 5:
                        tck.showBoughtTickets()
                    
                    elif action == 6:
                        auth.logOut(users)
                        loggedIn = False
                    
            else:
                
                    system('cls')
                    menu.title('MENU - ADMIN')
                    action = menu.menu(['Criar Filme', 'Buscar Filme', 'Atualizar Filme', 'Apagar Filme', 'Ingressos Vendidos', 'Feedback', 'Caixa','LogOut'])
                
                    if action == 1:
                        movies.append(mov.createMovie())
                        
                    elif action == 2:
                        mov.readMovie(movies)
                    
                    elif action == 3:
                        mov.updateMovie(movies)
                    
                    elif action == 4:
                        mov.deleteMovie(movies)
                        
                    elif action == 5:
                        tck.showBoughtTickets()  
                        
                    elif action == 6:
                        mov.showRating(movies)
                    
                    elif action == 7:
                        tck.showProfit(movies)
                    
                    elif action == 8:
                        auth.logOut(users)
                        loggedIn = False
                
            
    elif action == 2:
        users.append(auth.register(users))
        
    elif action == 3:
        print('\033[31mFinalizando o programa...\033[m')
        sleep(1.5)
        break