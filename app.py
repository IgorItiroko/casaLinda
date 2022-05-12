import json
class Login:
    def verificarLogin(usuario, senha):
        listaLogin = json.load(open('loginData.json', 'r'))
        for i in listaLogin:
            if usuario == format(i['usuario']) and senha == format(i['senha']):
                return True
        return False
    print(verificarLogin('teste1','teste2')) #return false
    print(verificarLogin('lucia','casalinda')) #return true