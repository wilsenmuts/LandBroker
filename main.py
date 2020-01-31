import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang.builder import Builder
from kivy.uix.recycleview import RecycleView
from kivy.uix.popup import Popup
from kivy.config import Config
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.label import Label
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.properties import BooleanProperty
from PIL import *
import mysql.connector

Config.set('graphics', 'multisamples', '0')
Config.set('graphics','width', '300')
Config.set('graphics','Height', '600')



#*******************************************************************************************************************App instance Methods

def dismiss_popup(self):
    self._popup.dismiss()

def popPic():
    show = UpPic()
    popup = Popup(title='Choose File', content=show, size_hint=(.95, .6))
    popup.open()




#********************************************************************************************************************Pop Ups
class Erpop(GridLayout):
    pass

class UpPic(GridLayout):
    def upload(self, filepass, filename):
        print(filepass + ""+str(filename))
        naming = str(filename)
        ActivityScreen().change_state(filename)

class UpTitle(GridLayout):
    pass

class UpMap(GridLayout):
    pass

class Sucpop(GridLayout):
    pass

class TakePiC(GridLayout):
    pass




#******************************************************************************************************************Screens and Screen Manager
class ActivityScreen(Screen):
    #tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
    def UploadPic(self):
        popPic()


    def change_state(self, filename):
        self.ids.pictured.text=str(filename)
        print('stream')

    def show_dict(self):
        tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
        print(tinydict)
        try:
            conn= mysql.connector.connect(user ='wilson', password='12345',host= 'localhost', database='ugconn')
            cursor=conn.cursor()
            add_user =("SELECT reside, structure, brief from buyhouse")
            cursor.execute(add_user)
            #for val in cursor:
            #    print(val)
            self.ids.rv.data=[{'text': str(x)} for x in cursor]

            print("The connection was successful")
        except mysql.connector.Error as err:
            if err.errno== errorcode.ER_ACCESS_DENIED_ERROR:
                print('Invalid Login details')
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print('DATABASE MISSING')
            else:
                print(err)
            poperr()
        finally:
            conn.close()



#s**************************************************************************************************************RECYCLEVIEW EDITOR
class RV(RecycleView):
    def __init__ (self, **kwargs):
        super(RV, self).__init__ ( **kwargs)
        tinydict = {'name': ['john','Mark'],'code':6734, 'dept': 'sales'}
        self.data = [{'text': str(x)} for x in tinydict.values()]


class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior,RecycleBoxLayout):
    ''' Adds selection and focus behavior to the view. '''

class SelectableLabel(RecycleDataViewBehavior, Label):
    ''' Add selection support to the Label '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        return super(SelectableLabel, self).refresh_view_attrs(rv, index, data)

    def on_touch_down(self, touch):
        ''' Add selection on touch down '''
        if super(SelectableLabel, self).on_touch_down(touch):
            return True

        if self.collide_point( *touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of items in the view. '''
        self.selected = is_selected



class LoginScreen(Screen):
    pass

class ScreenMain(ScreenManager):
    pass

kv = Builder.load_file('landbroker.kv')

class LandBroker1App(App):
    def build(self):
        return kv

if __name__ == '__main__':
    LandBroker1App().run()