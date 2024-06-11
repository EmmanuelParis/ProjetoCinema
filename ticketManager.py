from matplotlib import pyplot as plt

def showBoughtTickets():
    movies = list()
    amount = list()
    
    with open('boughtTickets.txt','r') as controlTickets:
        c = 0
        for ticket in controlTickets:
            index = ticket.find(',')
            if ticket[:index] in movies:
                
                pass
            else:
                movies.append(ticket[:index])
                amount.append(ticket[index+1:-2])
            c += 1
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