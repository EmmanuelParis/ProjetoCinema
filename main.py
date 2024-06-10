from PIL import Image
from os import system
from time import sleep
import validations as valid
import authentications as auth
import menus as menu
import movies as mov

users = [{
    'user' : 'emmanuel',
    'password' : '123',
    'age' : 18,
    'email' : 'emmanuelparis2005@gmail.com',
    'id' : False,
    'bank' : 0,
    'recognized' : False,
    'watched' : list()
    }]

movies = [{
    'title' : 'abc',
    'genre' : 'Ação',
    'sinopse' :'Filme massa',
    'ageRating' : '14',
    'duration' : '150',
    'hours' : '2',
    'minutes' : '30',
    'price'  : '25',
    'rating' : '99',
    'capacity' : 50,
    'chairs' : 50,
    'comments' : list()
},
          {
    'title' : 'filme2',
    'genre' : 'Comédia',
    'sinopse' :'RISOS',
    'ageRating' : '10',
    'duration' : '180',
    'hours' : '3',
    'minutes' : '0',
    'price'  : '30',
    'rating' : '88',
    'capacity' : 50,
    'chairs' : 50,
    'comments' : list()
}]

while True:
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
                    print(f'\033[36mCash: {round(user['bank'],2)}\033[m\n')
                    action = menu.menu(['Depositar Dinheiro', 'Catálogo', 'Comprar Ingresso', 'Avaliar Filmes', 'LogOut'])
                    
                    if action == 1:
                        deposit = valid.valInt('Quanto deseja depositar? \nR$')
                        print('Gerando o QR Code para depósito...')
                        sleep(1)                
                        pix = Image.open("./pix.png")
                        pix.show()
                        user['bank'] += deposit
                        sleep(3)
                    
                    elif action == 2:
                        mov.catalogue(movies)
                        
                    elif action == 3:
                        
                        pass
                    
                    elif action == 4:
                        
                        pass
                    
                    elif action == 5:
                        auth.logOut(users)
                        break
                    
            else:
                
                    system('cls')
                    menu.title('MENU - ADMIN')
                    action = menu.menu(['Criar Filme', 'Buscar Filme', 'Atualizar Filme', 'Apagar Filme', 'LogOut'])
                
                    if action == 1:
                        movies.append(mov.createMovie())
                        
                    elif action == 2:
                        mov.readMovie(movies)
                    
                    elif action == 3:
                        mov.updateMovie(movies)
                    
                    elif action == 4:
                        mov.deleteMovie(movies)
                        
                    elif action == 5:
                        auth.logOut(users)
                        break
                
            
    elif action == 2:
        users.append(auth.register(users))
        
    elif action == 3:
        print('\033[31mFinalizando o programa...\033[m')
        sleep(1.5)
        break