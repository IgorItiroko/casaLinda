import json
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

from estoque import Estoque


class LoginScreen(Screen):
    pass

class EstoqueScreen(Screen):
    pass

class AddScreen(Screen):
    pass

class windowManager(ScreenManager):
    pass

class EditScreen(ScreenManager):
    pass

sm = windowManager()
sm.add_widget(LoginScreen(name='login'))
sm.add_widget(EstoqueScreen(name='estoque'))
sm.add_widget(AddScreen(name='add'))
sm.add_widget(EditScreen(name='edit'))

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
                data["Produtos"][index]["Nome"],
                data["Produtos"][index]["Desc"],
                data["Produtos"][index]["Preco"],
                data["Produtos"][index]["Qtde"],
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
                ("Descrição", dp(61)),
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
            self.root.get_screen('edit').ids.error_label_edit.text = f'Para realizar alteracoes clicar no codigo'
            return False
    
    def editaDado(self, novoNome, novaDesc, novoPreco):
        dual = Estoque()
        deleteCod = self.codAlteracao
        try:
            if (dual.editarProduto(self.codAlteracao ,novoNome, novaDesc, float(novoPreco))):
                self.codAlteracao = 0
                

        

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
                return
            else:
                self.root.get_screen('add').ids.error_label_add.text = f'Dados fornecidos invalidos'
                return False
        except ValueError:
            self.root.get_screen('add').ids.error_label_add.text = f'O preco fornecido nao e um numero'
            return False

    def addScreen(self):
        self.root.current = 'add'
        return
MainApp().run()
