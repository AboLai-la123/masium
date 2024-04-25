from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.pickers import MDDatePicker

KV = '''
MDFloatLayout:

    MDRaisedButton:
        text: "Open date picker"
        pos_hint: {'center_x': .5, 'center_y': .5}
        on_release: app.show_date_picker()
'''


class Test(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_string(KV)

    def on_save(self, instance, value, date_range):
        print(value)

    def on_cancel(self, instance, value):
        '''Events called when the "CANCEL" dialog box button is clicked.'''

    def show_date_picker(self):
        date_dialog = MDDatePicker(
            min_year=1900, max_year=2024
        )
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()


Test().run()