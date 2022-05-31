import json
import kivy
import threading
from tkinter import Y

from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.list import OneLineListItem
from kivy.config import Config 
kivy.config.Config.set('graphics','resizable', False)
from estoque import Estoque
from financeiro import Financeiro



class LoginScreen(Screen):
    pass

class EstoqueScreen(Screen):
    pass

class AddScreen(Screen):
    pass

class EditScreen(Screen):
    pass

class FinanceiroScreen(Screen):
    pass

class AddFinanceiroScreen(Screen):
    pass

class LogsScreen(Screen):
    pass

class AddFinanceiroScreen(Screen):
    pass

class windowManager(ScreenManager):
    pass


sm = windowManager()
sm.add_widget(LoginScreen(name='login'))
sm.add_widget(EstoqueScreen(name='estoque'))
sm.add_widget(AddScreen(name='add'))
sm.add_widget(EditScreen(name='edit'))
sm.add_widget(FinanceiroScreen(name='financeiro'))
sm.add_widget(LogsScreen(name='logs'))
sm.add_widget(AddFinanceiroScreen(name='addFinanceiro'))


class MainApp(MDApp):
    codAlteracao = 0
    def build(self):
        sm = Builder.load_file('Screen.kv')

        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return sm


    def estoqueFunc(self):
        with open("estoque.json") as file:
            data = json.load(file)
        list = []
        for index in range(0, len(data["Produtos"])):
            produto = (
                data["Produtos"][index]["Cod"],
                "| " + str(data["Produtos"][index]["Nome"]),
                "| " + str(data["Produtos"][index]["Desc"]),
                "| " + str(data["Produtos"][index]["Preco"]),
                "| " + str(data["Produtos"][index]["Qtde"]),
                )
            list.append(produto)
        self.data_tables = MDDataTable(
            size_hint=(0.9, 0.8),
            use_pagination=True,
            rows_num=5,
            pagination_menu_pos = 'auto',
            column_data=[
                ("Código", dp(12)),
                ("Nome", dp(25)),
                ("Descrição",dp(61)),
                ("Preço", dp(18)),
                ("Qtde", dp(15)),
            ],
            row_data= list
        )
        self.data_tables.bind(on_row_press=self.on_row_press)
        self.root.get_screen('estoque').ids.data_layout.add_widget(self.data_tables) 
        return True

    def on_row_press(self, instance_table, instance_row):
        try:
            self.codAlteracao = int(instance_row.text)

            self.editScreen()
            return
        except ValueError:
            self.root.get_screen('estoque').ids.error_label_estoque.text = f'Para realizar alteracoes clicar no codigo'
            return False
    
    def editaDado(self, novoNome, novaDesc, novoPreco):
        dual = Estoque()
        try:
            if dual.editarProduto("Lucia" ,self.codAlteracao ,novoNome, novaDesc, float(novoPreco)):
                self.codAlteracao = 0
                self.root.current = 'estoque'
                self.estoqueFunc()
                return 
        except ValueError:
            self.root.get_screen('edit').ids.error_label_edit.text = f'Preco fornecido nao e um numero'
            return False

    def deletaDado(self):
        dual = Estoque()
        codDelete = self.codAlteracao
        if dual.excluirProduto(codDelete):
            self.root.current = 'estoque'
            self.root.get_screen('add').ids.nome.text = f''
            self.root.get_screen('add').ids.desc.text = f''
            self.root.get_screen('add').ids.preco.text = f''
            self.estoqueFunc()
            return
        print("lalala")
        return


    def editScreen(self):
        self.root.current = 'edit'
        return

    def verificarLogin(self, user, password):
        listaLogin = json.load(open('loginData.json', 'r'))
        for i in listaLogin:
            if user == format(i['usuario']) and password == format(i['senha']):
                self.root.current = 'estoque'
                self.estoqueFunc()
                return True
            else:
                self.root.get_screen('login').ids.error_label.text = f'Usuário e/ou senha incorretos'
                return False


    def adicionaDado(self, nome, desc, preco):
        dual = Estoque()
        try:
            if (dual.incluirProduto(nome, desc, float(preco))):
                self.root.current = 'estoque'
                self.root.get_screen('add').ids.nome.text = f''
                self.root.get_screen('add').ids.desc.text = f''
                self.root.get_screen('add').ids.preco.text = f''
                self.estoqueFunc()
                return
            else:
                self.root.get_screen('add').ids.error_label_add.text = f'Dados fornecidos invalidos ou produto ja adicionado'
                return False
        except ValueError:
            self.root.get_screen('add').ids.error_label_add.text = f'O preco fornecido nao e um numero'
            return False

    def addScreen(self):
        self.root.current = 'add'
        return

    def financeiroFunc(self):
        with open("financeiro.json") as file:
            data = json.load(file)
        list = []
        for index in range(0, len(data["Registros"])):
            financas = (
                data["Registros"][index]["Cod_Compra"],
                "| " + str(data["Registros"][index]["Cod_Produto"]),
                "| " + str(data["Registros"][index]["CompraVenda"]),
                "| " + str(data["Registros"][index]["Qtde"]),
                "| " + str(data["Registros"][index]["Valor_Uni"]),
                "| " + str(data["Registros"][index]["Data"]),
            )
            list.append(financas)
        self.data_tables = MDDataTable(
            size_hint=(0.9, 0.8),
            use_pagination=True,
            rows_num=5,
            pagination_menu_pos = 'auto',
            column_data=[
                ("Código Compra", dp(25)),
                ("Código Produto", dp(25)),
                ("Transação", dp(25)),
                ("Quantidade", dp(20)),
                ("Valor", dp(15)),
                ("Data", dp(20)),
            ],
            row_data= list
        )
        self.root.get_screen('financeiro').ids.data_layout_financeiro.add_widget(self.data_tables)
        return True

    def addFinanceiroScreen(self):
        self.root.current = 'addFinanceiro'
        return

    def adicionaFinanceiro(self, codProd, tipo, qtde, valor):
        dual = Financeiro()
        try:
            if (dual.adicionarFinanceiro(int(codProd), tipo, int(qtde), float(valor))):
                self.root.get_screen('addFinanceiro').ids.cod.text = f''
                self.root.get_screen('addFinanceiro').ids.tipo.text = f''
                self.root.get_screen('addFinanceiro').ids.valor.text = f''
                self.root.get_screen('addFinanceiro').ids.qtde.text = f''
                self.root.current = 'financeiro'
                self.financeiroFunc()
                return
            else:
                self.root.get_screen('addFinanceiro').ids.error_label_add_financeiro.text = f'Dados fornecidos invalidos'
                return False
        except ValueError:
            self.root.get_screen('addFinanceiro').ids.error_label_add_financeiro.text = f'Favor inserir uma quantidade e um valor em termos de numeros'
            return False

    def logsFunc(self):
        with open("logs.json") as file:
            data = json.load(file)
        list = []
        for index in range(0, len(data["Alteracoes"])):
            alter = (
                data["Alteracoes"][index]["Cod_Produto"],
                "| " + str(data["Alteracoes"][index]["Novo_Nome"]),
                "| " + str(data["Alteracoes"][index]["Nova_Desc"]),
                "| " + str(data["Alteracoes"][index]["Novo_Preco"]),
                "| " + str(data["Alteracoes"][index]["Autor_Alteracao"]),
            )
            list.append(alter)
        self.data_tables = MDDataTable(
            size_hint=(0.9, 0.8),
            use_pagination=True,
            rows_num=5,
            pagination_menu_pos = 'auto',
            column_data=[
                ("Código Produto", dp(25)),
                ("Novo Nome", dp(25)),
                ("Nova Descrição", dp(30)),
                ("Novo Preco", dp(25)),
                ("Autor da Alteracao", dp(30)),
            ],
            row_data= list
        )

        self.root.get_screen('logs').ids.data_layout_logs.add_widget(self.data_tables)
        return True

    def changeAdd(self):
        self.root.current = 'estoque'
        self.root.get_screen('add').ids.nome.text = f''
        self.root.get_screen('add').ids.desc.text = f''
        self.root.get_screen('add').ids.preco.text = f''
        return

    def changeEdit(self):
        self.root.current = 'edit'
        return
        
    def changeFinanceiro(self):
        self.root.current = 'financeiro'
        self.root.get_screen('addFinanceiro').ids.cod.text = f''
        self.root.get_screen('addFinanceiro').ids.tipo.text = f''
        self.root.get_screen('addFinanceiro').ids.valor.text = f''
        self.root.get_screen('addFinanceiro').ids.qtde.text = f''
        self.financeiroFunc()
        return

    def changeSair(self):
        self.root.current = 'login'
        self.root.get_screen('login').ids.user.text = f''
        self.root.get_screen('login').ids.password.text = f''
        return

    def changeEstoque(self):
        self.root.current = 'estoque'
        return

    def changeLogs(self):
        self.root.current = 'logs'
        self.logsFunc()
        return

MainApp().run()
