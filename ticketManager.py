from matplotlib import pyplot as plt

def showBoughtTickets():
    movies = list()
    amount = list()
    
    with open('boughtTickets.txt','r') as controlTickets:
        for ticket in controlTickets:
            index = ticket.find(',')
            movies.append(ticket[:index])
            amount.append(ticket[index+1:])
            
    if len(movies) == 0 or len(amount) == 0:
        print('Nenhum ingresso foi comprado!')
    else: 
        bars = plt.bar(movies, amount)
        
        plt.bar_label(bars, labels=amount)
        plt.box(False)
        plt.yticks([])
        plt.title('Ingressos Vendidos')
        plt.xlabel('Filmes')
        plt.ylabel('Quantidade de Ingressos')
        
        plt.show()
        
def showProfit(movies=list):
    profit = 0
    for movie in movies:
        print(f'\033[34mFilme: {movie['title']}\n\033[33mLucro: R${movie['bought']}\033[m')
        profit += int(movie['bought'])
        
    print(f'\n\033[34mO cinema lucrou no total: \033[33mR${profit}\033[m')
    input('Pressione qualquer tecla para continuar!')
    