import validations as valid

def register(users=list):
    validado = True
    
    while validado:
        username = valid.valStr('\033[34mDigite seu user: \033[m')
        for user in users:
            if username == user['user']:
                print('\033[31mEste user já está sendo utilizado!\033[m') 
                validado = True
                break
        else:
            break
    
    
    password = valid.valStr('\033[34mDigite sua senha: \033[m')
    email = valid.valEmail('\033[34mDigite seu email: \033[m')
    
    while validado:
        age = valid.valInt('\033[34mDigite sua idade: \033[m')
        if age < 6 or age > 90:
            print('\033[31mIdade Inválida!\033[m')
            validado = True
        else:
            break
    
    accessType = valid.valInt('\033[34mQual o tipo de cadastro? \033[33m\n[1] - Cliente \n[2] - Admin \033[34m\nOpção: \033[m')
    if accessType == 1:
        accessType = False
    elif accessType == 2:
        accessType = True
    
    user = dict()
    user['user'] = username
    user['password'] = password
    user['email'] = email
    user['id'] = accessType
    user['bank'] = 0
    user['recognized'] = False
    user['watched'] = list()
    return user

def logIn(users=dict):
    recognized = False
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
                        return user
            if user['user'] != username:
                print('\033[31mUsuário não encontrado\033[m')
                
def logOut(users=list):
    logout = valid.valInt('\033[34mTem certeza que deseja deslogar? \n[1] - Sim \n[2] - Não \n\nOpção: \033[m')
    if logout == 1:
        for user in users:
            user['recognized'] = False