import validations as valid
def register():
    username = valid.valStr('Digite seu user: ')
    password = valid.valStr('Digite sua senha: ')
    email = valid.valEmail('Digite seu email: ')
    age = valid.valInt('Digite sua idade: ')
    id = valid.valInt('Qual o tipo de cadastro? \n[1] - Cliente \n[2] - Admin \nOpção: ')
    if id == 1:
        id = False
    else:
        id = True
    
    user = dict()
    user['name'] = username
    user['password'] = password
    user['email'] = email
    user['id'] = id
    user['bank'] = 0
    user['recognized'] = False
    return user

def logIn(recognized=False, users=list):
    while recognized != True:
        username = input('\033[34mDigite seu usuário: \033[m')
        if username.lower() == 'sair':
            break
        else:
            for user in users:
                if user['user'] == username:
                    password = input('\033[34mDigite sua senha: \033[m')
                    if user['password'] != password:
                        print('\033[31mUsuário ou Senha iválidos!\033[m')
                    else:
                        user['recognized'] = True
                        print('\033[32mVocê está logado!\033[m')
                        recognized = True
            if user['user'] != username:
                print('\033[31mUsuário não encontrado\033[m')
                
def logOut(recognized=True, users=list):
    logout = valid.valInt('\033[34mTem certeza que deseja deslogar? \n[1] - Sim \n[2] - Não \n\nOpção: \033[m')
    if logout == 1:
        for user in users:
            user['recognized'] = False