import validations as valid
import menus as menu
import random

genres = ('Ação', 'Aventura', 'Drama', 'Comédia', 'Ficção Científica', 'Terror')
updateOptions = ('Título', 'Gênero', 'Sinopse', 'Faixa Etária', 'Duração', 'Preço do Ingresso', 'Sair')

def createMovie():
    global genres
    
    title = valid.valStr('\033[34mDigite o título do filme: \033[m')
    print('\033[33mEscolha o gênero do filme:')
    genre = menu.menu(genres)
    sinopse = valid.valStr('\033[34mDigite a sinopse do filme: \033[m')
    ageRating = valid.valInt('\033[34mDigite a faixa etária do filme: \033[m')
    duration = valid.valInt('\033[34mDigite a duração do filme (em minutos): \033[m')
    hours = int(duration) // 60
    minutes = int(duration) % 60
    price = valid.valInt('\033[34mDigite o valor do Ingresso: \033[m')
    capacity = valid.valInt('\033[34mDigite a capacidade da sala: \033[m')
    
    movie = dict()
    movie['title'] = title
    movie['genre'] = genres[genre-1]
    movie['sinopse'] = sinopse
    movie['ageRating'] = ageRating
    movie['duration'] = duration
    movie['hours'] = hours
    movie['minutes'] = minutes
    movie['price'] = price
    movie['rating'] = random.randint(1,100)
    movie['capacity'] = capacity
    movie['chairs'] = capacity
    movie['comments'] = list()
    movie['bought'] = 0
    return movie

def readMovie(movies=list):
    searchMovie = valid.valStr('\033[34mQual filme deseja buscar? \nFilme: \033[m')
    for movie in movies:
        if movie['title'] == searchMovie:
            menu.line()
            print(f'\033[36mTítulo do filme: \033[33m{movie['title']}\n\033[36mGênero do filme: \033[33m{movie['genre']}\n\033[36mSinopse do Filme: \033[33m{movie['sinopse']}\n\033[36mFaixa etária permitida: \033[33m{movie['ageRating']}\n\033[36mDuração: \033[33m{movie['hours']} Hora(s) e {movie['minutes']} Minuto(s)\n\033[36mPreço do ingresso: \033[33mR${movie['price']}\n\033[36mAprovação: \033[33m{movie['rating']}%\33[m')
            menu.line()
            input('Pressione qualquer tecla para continuar!')
            
def updateMovie(movies=list):
    global genres
    global updateOptions
    
    searchMovie = valid.valStr('\033[mQual filme deseja atualizar? \nFilme: \033[m')
    for movie in movies:
        if movie['title'] == searchMovie:
            print('\033[33mQual informação deseja atualizar?')
            update = menu.menu(updateOptions)
            if update == 1:
                print(f'\33[33mTítulo Atual: {movie['title']}\33[m')
                newTitle = valid.valStr('\33[34mDigite o novo título: \33[m')
                movie['title'] = newTitle
                print('\033[32mAlteração feita com sucesso!\033[m')
            elif update == 2:
                print(f'\33[33mGênero Atual: {movie['genre']}\33[m')
                print('\033[33mEscolha o gênero do filme:')
                newGenre = menu.menu(genres)
                movie['genre'] = genres[newGenre-1]
                print('\033[32mAlteração feita com sucesso!\033[m')
            elif update == 3:
                print(f'\33[33mSinopse Atual: {movie['sinopse']}\33[m')
                newSinopse = valid.valStr('\33[34mDigite a nova sinopse: \33[m')
                movie['sinopse'] = newSinopse
                print('\033[32mAlteração feita com sucesso!\033[m')
            elif update == 4:
                print(f'\33[33mFaixa Etária Atual: {movie['ageRating']}\33[m')
                newAgeRating = input('\33[34mDigite a nova faixa etária: \33[m')
                movie['ageRating'] = newAgeRating
                print('\033[32mAlteração feita com sucesso!\033[m')
            elif update == 5:
                print(f'\33[33mDuração Atual: {movie['duration']}\33[m')
                newDuration = input('\33[34mDigite a nova duração do filme: \33[m')
                newHour = int(newDuration) // 60
                newMinutes = int(newDuration) % 60
                movie['duration'] = newDuration
                movie['hours'] = newHour
                movie['minutes'] = newMinutes
                print('\033[32mAlteração feita com sucesso!\033[m')
            elif update == 6:
                print(f'\33[33mPreço do Ingresso Atual: {movie['price']}\33[m')
                newPrice = input('\33[34mDigite o novo preço do ingresso: \33[m')
                movie['price'] = newPrice
                print('\033[32mAlteração feita com sucesso!\033[m')
            elif update == 7:
                break
            else:
                print('\33[31mDigite uma opção válida!\33[m')
            input('Pressione qualquer tecla para continuar!')
            
def deleteMovie(movies=list):
    searchMovie = valid.valStr('\033[34mQual filme deseja remover? \nFilme: \033[m')
    count = 0
    for movie in movies:
        if movie['title'] == searchMovie:
            del movies[count]
            print('\033[32mRemoção feita com sucesso!\033[m')
            input('Pressione qualquer tecla para continuar!')
        count += 1
        
def catalogue(movies=list):
    menu.title('FILMES')
    
    print('\33[34mQual filme deseja visualizar?\033[m')
    searchMovie = menu.showMovies(movies)
    for movie in movies:
        if searchMovie == movie['title']:
            menu.line()
            print(f'\033[36mTítulo do filme: \033[33m{movie['title']}\n\033[36mGênero do filme: \033[33m{movie['genre']}\n\033[36mSinopse do Filme: \033[33m{movie['sinopse']}\n\033[36mFaixa etária permitida: \033[33m{movie['ageRating']}\n\033[36mDuração: \033[33m{movie['hours']} Hora(s) e {movie['minutes']} Minuto(s)\n\033[36mPreço do ingresso: \033[33mR${movie['price']}\n\033[36mAprovação: \033[33m{movie['rating']}%\33[m')
            menu.line()
            input('Pressione qualquer tecla para continuar!')
            
def buyTicket(movies=list, users=list):
    menu.title('FILMES')
    
    print('\33[34mDe qual filme deseja comprar o ingresso?\033[m')
    searchMovie = menu.showMovies(movies)
    for movie in movies:
        if searchMovie == movie['title']:
            menu.title(movie['title'])
            print(f'\033[34mCapacidade da sala: \033[33m{movie['capacity']}\n\033[34mCadeiras Livres: \033[33m{movie['chairs']}\n')
            buy = valid.valInt(f'\033[34mQuantos ingressos deseja comprar? \033[33m[R${movie['price']}]\n\033[34mQuantidade: \033[m')
            if buy == 0:
                break
            for user in users:
                if user['recognized'] and user['bank'] >= int(movie['price'])*buy and buy <= int(movie['chairs']):
                    if buy <= int(movie['chairs']):
                        user['watched'].append(movie['title'])
                        user['bank'] -= buy*int(movie['price'])
                        movie['chairs'] -= buy
                        movie['bought'] += buy*int(movie['price'])
                        with open('boughtTickets.txt','a') as controlTickets:
                            controlTickets.write(f'{movie['title']},{buy}\n')
                        print('\033[32mCompra realizada com sucesso!\033[m')
                        input('Pressione qualquer tecla para continuar!')
                        break
                    else:
                        print('\033[31mNão é possível realizar a compra desta quantidade!\033[m')
                        input('Pressione qualquer tecla para continuar!')
                elif user['bank'] < int(movie['price'])*buy or buy > int(movie['chairs']):
                    print('\033[31mSaldo insuficiente!\033[m')
                    input('Pressione qualquer tecla para continuar!')
                    
def rateMovie(movies=list, users=list):
    menu.title('FILMES')
    
    print('\33[34mQual filme deseja avaliar?\033[m')
    searchMovie = menu.showMovies(movies)
    for movie in movies:
        if searchMovie == movie['title']:
            for user in users:
                if user['recognized'] and movie['title'] in user['watched']:
                    menu.title(movie['title'])
                    comment = valid.valStr('\033[34mDigite um comentário:\nComentário:  \033[m')
                    rate = valid.valInt('\033[34mDigite sua nota para esse filme [0-100]:\nNota: \033[m')
                    ratingPerUser = dict()
                    ratingPerUser['user'] = user['user']
                    ratingPerUser['comment'] = comment
                    ratingPerUser['rate'] = rate
                    movie['comments'].append(ratingPerUser)
                    print('\033[32mAvaliação registrada!\033[m')
                    input('Pressione qualquer tecla para continuar!')
            if movie['title'] not in user['watched']:
                print('\033[31mVocê não assistiu a este filme!\033[m')
                input('Pressione qualquer tecla para continuar!')

def showRating(movies=list):
    searchMovie = menu.showMovies(movies)
    for movie in movies:
        if searchMovie == movie['title']:
            menu.title(movie['title'])
            for i in movie['comments']:
                print(f'\033[34mUsuário: \033[33m{i['user']}\033[m')
                print(f'\033[34mComentário: \033[33m{i['comment']}\033[m')
                print(f'\033[34mAvaliação: \033[33m{i['rate']}\033[m')
                menu.line()
    input('Pressione qualquer tecla para continuar!')