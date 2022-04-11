from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition 
from kivy.core.window import Window
import os
from kivy.properties import StringProperty
from kivy.lang import Builder
from posixpath import dirname
from kivy.core.text import LabelBase

Window.size = (414, 736)

Builder.load_file(os.path.join(dirname(__file__), 'Main.kv'))
Builder.load_file(os.path.join(dirname(__file__), 'Add.kv'))
Builder.load_file(os.path.join(dirname(__file__), 'OpMenu.kv'))
Builder.load_file(os.path.join(dirname(__file__), 'extra.kv'))
Builder.load_file(os.path.join(dirname(__file__), 'reg.kv'))
Builder.load_file(os.path.join(dirname(__file__), 'login.kv'))
Builder.load_file(os.path.join(dirname(__file__), 'AllTransactions.kv'))


class All(Screen):
    month = ' Марта'
    date = '9'
    amount = 3
    amount2 = 5
    def toTheMain(self):
        app = App.get_running_app()
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'Main'
    def toTheExtra(self):
        app = App.get_running_app()
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'Extra'

class Main(Screen):
    Username = 'Max'
    Currency = '$'
    Perriod = 'Март'
    Balance = 50000
    strBalance = str(Balance)
    cost = '-50 р'
    operation = 'Бутылка молока'
    space = '                                     ' 
    amount = 3
    amount2 = 5
    def toTheMain(self):
        app = App.get_running_app()
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'Main'
    def toTheAll(self):
        app = App.get_running_app()
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'All'
    def toTheOpMenu(self):
        app = App.get_running_app()
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'OpMenu'
    def toTheExtra(self):
        app = App.get_running_app()
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'Extra'
    def toTheAdd(self):
        app = App.get_running_app()
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'Add'

class Costs(Screen):
    pass

class OpMenu(Screen):
    cost = '-50 р'
    operation = 'Бутылка молока'
    space = '                                     ' 
    def toTheMain(self):
        app = App.get_running_app()
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'Main'
    def toTheAll(self):
        app = App.get_running_app()
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'All'
    def toTheOpMenu(self):
        app = App.get_running_app()
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'OpMenu'

        

class Login(Screen):
    def do_login(self, loginText, passwordText):
        app = App.get_running_app()
        app.username = loginText
        app.password = passwordText
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'Main'

    def toTheReg(self):
        app = App.get_running_app()
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'Reg'


    def resetForm(self):
        self.ids['login'].text = ""
        self.ids['password'].text = ""

class Reg(Screen):
    def do_reg(self, loginText, passwordText, password2Text, emailText):
        app = App.get_running_app()
        app.username = loginText
        app.password = passwordText
        app.password2 = password2Text
        app.email = emailText
        c1, c2, c3 = 0, 0, 0
        for i in emailText:
            if i == '@':
                c1 += 1
            elif i == '#' or i == '$' or i == '*':
                c3 += 1
        if c1 != 1 or c3 != 0 or passwordText != password2Text:
            self.manager.transition = SlideTransition(direction="left")
            self.manager.current = 'PnP2'
        else: 
            self.manager.transition = SlideTransition(direction="left")
            self.manager.current = 'Main'

class Add(Screen):
    def toTheMain(self):
        app = App.get_running_app()
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'Main'
    def addNewOp(self, costText, categoryText, dayText, monthText, yearText, nameText):
        app = App.get_running_app()
        app.cost = costText
        app.category = categoryText
        app.day = dayText
        app.month = monthText
        app.year = yearText
        app.name = nameText

class PnP2(Screen):
    def toTheReg(self):
        app = App.get_running_app()
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'Reg'

class Extra(Screen):
    def toTheMain(self):
        app = App.get_running_app()
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'Main'
    def toTheExtra(self):
        app = App.get_running_app()
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'Extra'

class MoneyCounterApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Login(name='Login'))
        sm.add_widget(Main(name='Main'))
        sm.add_widget(OpMenu(name='OpMenu'))
        sm.add_widget(All(name='All'))
        sm.add_widget(Costs(name='Costs'))
        sm.add_widget(Reg(name='Reg'))
        sm.add_widget(PnP2(name='PnP2'))
        sm.add_widget(Extra(name='Extra'))
        sm.add_widget(Add(name='Add'))
        return sm



if __name__ == "__main__":
    MoneyCounterApp().run()
