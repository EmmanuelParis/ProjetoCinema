import validations as valid

def line(tam = 40):
    return '=' * tam

def title(txt):
    print(line())
    print(txt.center(40))
    print(line())
    
def menu(list):
    c = 1
    for i in list:
        print(f'\033[33m{c}\033[m - \033[34m{i}\033[')
        c += 1
    opcao = valid.valInt('\033[32mOpção: \033[m')
    return opcao

def show(opitons):
    c = 1
    for i in opitons:
        print(f'\033[33m{c}\033[m - \033[34m{i}\033[')
        c += 1