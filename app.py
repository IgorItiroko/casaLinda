from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.datatables import MDDataTable
from kivy.uix.anchorlayout import AnchorLayout
from kivymd.uix.list import OneLineListItem
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.metrics import dp
import json

class LoginScreen(Screen):
    pass

class EstoqueScreen(Screen):
    pass

class windowManager(ScreenManager):
    pass

sm = windowManager()
sm.add_widget(LoginScreen(name='login'))
sm.add_widget(EstoqueScreen(name='estoque'))

class MainApp(MDApp):
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
            column_data=[
                ("Código", dp(12)),
                ("Nome", dp(25)),
                ("Descrição", dp(61)),
                ("Preço", dp(18)),
                ("Qtde", dp(15)),
            ],
            row_data= list
        )
        #self.data_tables.bind(on_row_press = self.row_press)
        self.root.get_screen('estoque').ids.data_layout.add_widget(self.data_tables) 

        return True


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


    def adicionaDado(self, instance_button: MDRaisedButton) -> None:
        
        

        return


MainApp().run()