import os
os.environ['KIVY_IMAGE'] = 'pil'
# os.environ["KIVY_NO_CONSOLELOG"] = "1"
import kivy
kivy.require('2.1.0')
from kivy.config import Config
Config.set('graphics', 'width', '620')
Config.set('graphics', 'height', '280')
Config.set('graphics','resizable', False)
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

from kivy.app import App 
from kivy.core.window import Window
# Window.minimum_width, Window.minimum_height = (800, 600)
Window.clearcolor = (0.05, 0.1, 0.15, 1)
from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.filechooser import FileChooserListView
from modified_widget import *

class MainLayout(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        open_file_textinput = TextInput(size_hint=(None, None), size=(450, 30), pos=(60, 126))
        open_file_btn = Button(text="Open", size_hint=(None, None), size=(50, 30), pos=(510, 125))
        self.add_widget(open_file_btn)
        self.add_widget(open_file_textinput)

        content = BoxLayout(orientation='vertical')
        popup = Popup(content=content, 
            auto_dismiss=True, 
            size_hint=(0.6, 1),
            separator_height=0,
            separator_color=(0.9, 1, 1, 1),
            background_color=(41/255, 50/255, 70/255, 0.9),
            # title_font="assets/static/Nunito-Bold",
            title_size='16sp',
            title='')

        filerchooser_obj = FileChooserListView()
        content.add_widget(filerchooser_obj)

        def file_chooser_open_cb(i):
            filerchooser_obj.path = 'D:'+os.path.sep
            popup.open()
        open_file_btn.bind(on_release=file_chooser_open_cb)
        # popup.open()

        def print_loc(i):
            print(filerchooser_obj.path, filerchooser_obj.selection, filerchooser_obj.files)
            open_file_textinput.text = filerchooser_obj.path
            if filerchooser_obj.selection:
                open_file_textinput.text = filerchooser_obj.selection[0]
            popup.dismiss()

        choose_btn = Button(text="Load", size_hint_y=0.1)
        choose_btn.bind(on_release=print_loc)

        content.add_widget(choose_btn)


class Main_Window(App):
        def build(self):
            return MainLayout()


if __name__ == '__main__':
    Main_Window().run()