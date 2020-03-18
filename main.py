import kivy
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.image import Image, AsyncImage
from kivy.properties import StringProperty, ObjectProperty, ListProperty
import kivymd
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard, MDCardPost
from kivymd.uix.button import MDFillRoundFlatButton, MDRaisedButton
from kivy.uix.screenmanager import ScreenManager, Screen
import mysql.connector
from kivy.network.urlrequest import UrlRequest
from kivymd.toast import toast
from mysql.connector import errorcode
import time
import webbrowser as wb
from kivymd.uix.dialog import MDInputDialog, MDDialog
from kivymd.toast import toast
import datetime
import requests
import urllib


def popPic():
    show = UpPic()
    popup = Popup(title='Choose File', content=show, size_hint=(.95, .6))
    popup.open()

def get_id():
    show = LandId()
    popup = Popup(title='Enter Land ID', content=show, size_hint=(.95, None), height=150)
    popup.open()

class LandId(GridLayout):
    def printer(self):
        toast('Expressed interest in - '+self.ids.land_id.text + '\n We shall call you to know more about your order.')


class MyLabel(MDLabel):
    pass

class MyTitle(MDLabel):
    pass

class MyCard(MDCard):
    pass

class UpPic(GridLayout):
    url = 'http://127.0.0.1:8000/upload/'

    try:
        def upload(self, filepass, filename):
            print(str(filename))
            try:
                requests.post('http://127.0.0.1:8000/upload/', filepass)
            except:
                toast('Could not upload file')
    except:
        toast('unable to upload')
        '''

    def upload(self, filepass, filename):
        try:
            UrlRequest('http://127.0.0.1:8000/upload/', on_success=suc, on_failure=fail,file_path=filepass, ca_file=filename, method='POST' )
        except:
            toast('No Internet Connection', duration =5.0)
    def suc(self):
        toast('Was successful')

    def fail(self):
        toast('Failed')
        '''

class ActivityScreen(Screen):
    a = StringProperty(None)
    b = StringProperty(None)
    p = StringProperty(None)
    uname = StringProperty(None)

    def UploadPic(self):
        popPic()

    def logout(self):
        self.manager.current='login'

    def change_state(self, filename):
        fname= str(filename)

    def printer(self, instance):
        get_id()

    def capture_text(self, instance, value):
        toast('you have input: ' + str(value))

    def on_enter1(self,instance, value):
        print('User pressed enter in', instance)
        toast('User pressed enter in:   ' + value.text)


    def show_more(self):
        self.ids.box.clear_widgets()
        cnx = mysql.connector.connect(user='wilson',password='12345', database='landbroker')
        cursor = cnx.cursor()
        query = ("SELECT id, reside, size, amount, mode_whole, mode_part, ownership, map_scan, distance FROM landbroker_sell WHERE is_active=True ")
        cursor.execute(query)
        for (id, reside, size, amount, mode_whole, mode_part, ownership, map_scan, distance) in cursor:
            '''
            card = MDCardPost(source="./black.jpg",tile_text=title, text_post="Date:"+str(date_as_is)+"\nAbout:"+about+"\nNotes:"+notes,card_size=(300,300) , with_image=True,callback=self.callback(value=self.isinstance.title_text), swipe=True)
            self.ids.box.add_widget(card,len(self.children))
            '''
            if mode_part is 1:
                mode='True'
            else:
                mode='False'
            a = str(id)
            layout = MDCard(orientation='horizontal', size_hint=(1,None), height=240, elevation=8)
            layout.add_widget(AsyncImage(source="http://127.0.0.1:8000/media/"+map_scan, keep_ratio= False, allow_stretch=True, size_hint=(.7,1)))
            layout1 = GridLayout(cols=1, padding=5)
            layout1.add_widget(MDLabel(text='Land ID:'+a))
            layout1.add_widget(MDLabel(text='Location: '+reside))
            layout1.add_widget(MDLabel(text='Size: '+size))
            layout1.add_widget(MDLabel(text='Amount: '+amount))
            layout1.add_widget(MDLabel(text='Ownership: '+ownership))
            layout1.add_widget(MDLabel(text='Distance: ' +distance))
            layout1.add_widget(MDLabel(text='Selling in Parts: ' +mode))
            layout1.add_widget( MDRaisedButton(text='Express Interest',md_bg_color=(.7, .2, .2, 1),size_hint_x=1, on_press=self.printer))
            layout.add_widget(layout1)
            #print(a +'\n'+ b + '\n'+p)

            self.ids.box.add_widget(layout,len(self.children))

        cursor.close()
        cnx.close()
        #card= MDCard(orientation='vertical', size_hint=(None, None), height=self.height/4, width= self.width/2.5, allow_stretch=True, keep_ratio=False, elevation= 6)
        #card.bind


    def to_top(self):
        self.ids.box.bar_pos_x='top'

    def submit_data(self):
        if self.ids.uname.text and self.ids.nin_no.text and self.ids.tel_no.text and self.ids.reside.text and self.ids.amount.text and self.ids.size.text:
            if self.ids.full:
                own='Full Ownership'
            if self.ids.rent:
                own='Rent'
            if self.ids.lease:
                own='lease'


            try:
                conn= mysql.connector.connect(user ='wilson', password='12345',host= 'localhost', database='landbroker')
                cursor=conn.cursor()
                add_investmoney=("INSERT INTO landbroker_sell (nin_no, reside,amount, size,id_card, title_scan, map_scan, mode_whole, mode_part, ownership, tel_no, is_active, date_box, distance, username_id  ) VALUES(%(nin_no)s, %(reside)s, %(amount)s, %(size)s, %(id_card)s, %(titlescan)s, %(mapscan)s, %(mode_whole)s, %(mode_part)s, %(ownership)s, %(tel_no)s,%(isactive)s ,%(date_box)s,%(distance)s, %(username_id)s)")
                user_data = {
                    'nin_no': self.ids.nin_no.text,
                    'tel_no': self.ids.tel_no.text,
                    'reside': self.ids.reside.text,
                    'amount':self.ids.amount.text,
                    'size':self.ids.size.text,
                    'id_card': 'landbroker/default.png',
                    'titlescan':'landbroker/default.png',
                    'mapscan':'landbroker/default.png',
                    'mode_whole':self.ids.wholly.active,
                    'mode_part':self.ids.Partly.active,
                    'ownership':own,
                    'date_box': datetime.datetime.now(),
                    'isactive':0,
                    'distance':'on road',
                    'username_id': self.ids.uname.text,
                }
                cursor.execute(add_investmoney, user_data)
                conn.commit()
                toast('success\n We will call within a week after confirming your ownership of sale.')
            except mysql.connector.Error as err:
                toast(str(err))
                print(str(err))
            finally:
                conn.close()
                self.ids.nin_no.text=''
                self.ids.tel_no.text=''
                self.ids.reside.text=''
                self.ids.amount.text=''
                self.ids.size.text=''
                self.ids.wholly.active= False
                self.ids.Partly.active=False
                self.ids.full.active = False
                self.ids.rent.active=False
                self.ids.lease.active= False
        else:
            toast('Incomplete Request')


class LoginScreen(Screen):
    def login(self):
        uname = self.ids.uname.text
        pswd = self.ids.pswd.text
        try:
            payload = {'username': uname, 'password': pswd}
            url = 'http://127.0.0.1:8000/api/auth/token/login/'
            p=requests.post(url, data=payload)
            if p:
                print(p.text)
                self.manager.current='activity'
                self.manager.get_screen('activity').ids.uname.text = uname

                toast("You have logged in.")
            else:
                toast('Invalid Details. Try Again')
        except:
            toast('No internet Connection')
        finally:
            self.ids.uname.text=''
            self.ids.pswd.text=''



    def signup(self):
        wb.open_new_tab('http://127.0.0.1:8000/register')


class RootScreen(ScreenManager):
    pass


class myApp(MDApp):
    def build(self):
        return

if __name__ =='__main__':
    myApp().run()