def valInt(txt):
    while True:
        try:
            n = int(input(txt))
            if n < 0:
                print('\033[31mErro: Por Favor, digite uma opção válida! \033[m')
                continue
        except(ValueError, TypeError):
            print('\033[31mErro: Por Favor, digite uma opção válida! \033[m')
            continue
        except(KeyboardInterrupt):
            print('\n\033[31mO usuário não digitou esse número \033[m')
            return 0
        else:
            return n
        
def valStr(txt):
    while True:
        try:
            n = input(txt)
            if n.isspace() or len(n) == 0:
                print('\033[31mErro: Por Favor, digite uma opção válida! \033[m')
                continue
        except(ValueError, TypeError):
            print('\033[31mErro: Por Favor, digite uma opção válida! \033[m')
            continue
        except(KeyboardInterrupt):
            print('\n\033[31mO usuário não digitou esse número \033[m')
            return 0
        else:
            return n
        
def valEmail(txt):
    while True:
        n = input(txt)
        if n.count('@') != 0 and len(n) > 3:
            return True
        else:
            print('\033[31mErro: Por Favor, digite um e-mail válido! \033[m')
            continue
