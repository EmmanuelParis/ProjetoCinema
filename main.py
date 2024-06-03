from PIL import Image
from os import system
from time import sleep
import validations as valid
import authentications as auth
import menus as menu

users = [{
    'user' : 'emmanuel',
    'password' : '123',
    'age' : 18,
    'email' : 'emmanuelparis2005@gmail.com',
    'id' : False,
    'bank' : 0,
    'recognized' : False
    }]

movies = [{
    'title' : 'abc',
    'genre' : 'ação',
    'sinopse' :'Filme massa',
    'ageRating' : '14',
    'hours' : '2',
    'minutes' : '30',
    'price'  : '24.99',
    'rating' : '99%',
    'comments' : list()
}]



while True:
    menu.title('MENU PRINCIPAL')
    action = menu.menu(['Login','Cadastro','Sair'])

    if action == 1:
        for user in users:
            auth.logIn(user['recognized'],users)
            
        while True:
            if user['recognized'] == True and user['id'] == False:
                menu.title('MENU - CLIENTES')
                print(f'Cash: {round(user['bank'],2)}\n')
                action = menu.menu(['Depositar Dinheiro', 'Catálogo', 'Comprar Ingresso', 'Avaliar Filmes'])
                
                if action == 1:
                    deposit = valid.valInt('Quanto deseja depositar? \nR$')
                    print('Gerando o QR Code para depósito...')
                    sleep(1)                
                    pix = Image.open("./pix.jpg")
                    pix.show()
                    user['bank'] += deposit
                    sleep(3)
                
                elif action == 2:
                    pass
                
                elif action == 3:
                    pass
                
                elif action == 4:
                    auth.logOut(user['recognized'], users)
            else:
                break
                
            
    elif action == 2:
        users.append(auth.register())
        
    elif action == 3:
        print('\033[31mFinalizando o programa...\033[m')
        sleep(1.5)
        break