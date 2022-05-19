from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
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

    def verificarLogin(self, user, password):
        listaLogin = json.load(open('loginData.json', 'r'))
        for i in listaLogin:
            if user == format(i['usuario']) and password == format(i['senha']):
                self.root.current = 'estoque'
                return True
            else:
                self.root.ids.error_label.text = f'Usuário e/ou senha incorretos'
                return False
        

MainApp().run()