from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
import webbrowser

class MyApp(App):

    def build(self):
        layout = FloatLayout()

        # Добавляем основные текстовые поля
        self.add_main_text_inputs(layout)

        # Добавляем текстовые поля с узкими окнами
        self.add_narrow_text_inputs(layout)

        # Устанавливаем параметры окна
        self.set_window_properties()

        return layout

    def add_main_text_inputs(self, layout):

        #Окно суммаризации
        self.text_input_down = TextInput(multiline=True, size_hint=(0.4, 0.2), pos_hint={'center_x': 0.325, 'center_y': 0.13})
        layout.add_widget(self.text_input_down)
        #КНОПКА SUM
        button30 = Button(text='Sum', size_hint=(0.04, 0.05), pos_hint={'center_x': 0.1, 'center_y': 0.2}, background_color=(1, 0.7, 0, 1))
        layout.add_widget(button30)
        #КНОПКА COG
        button30 = Button(text='Sog', size_hint=(0.04, 0.05), pos_hint={'center_x': 0.1, 'center_y': 0.15}, background_color=(1, 0.7, 0, 1))
        layout.add_widget(button30)
        #Итоговое окно
        self.text_input_down_yes = TextInput(multiline=True, size_hint=(0.3, 0.2), pos_hint={'center_x': 0.675, 'center_y': 0.13})
        layout.add_widget(self.text_input_down_yes)

        # ОКНО два
        self.text_input = TextInput(multiline=True, size_hint=(0.25, 0.5), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        layout.add_widget(self.text_input)

        # ОКНО один
        self.text_input_left = TextInput(multiline=True, size_hint=(0.25, 0.5), pos_hint={'center_x': 0.25, 'center_y': 0.5})
        layout.add_widget(self.text_input_left)

        # ОКНО ТРИ
        self.text_input_right = TextInput(multiline=True, size_hint=(0.25, 0.5), pos_hint={'center_x': 0.75, 'center_y': 0.5})
        layout.add_widget(self.text_input_right)

    def add_narrow_text_inputs(self, layout):
        # ОКНО УЗКОЕ НОМЕР ОДИН
        self.text_input_right1 = TextInput(multiline=True, size_hint=(0.25, 0.08), pos_hint={'center_x': 0.25, 'center_y': 0.8})
        layout.add_widget(self.text_input_right1)
        button4 = Button(text='Замок', size_hint=(0.15, 0.05), pos_hint={'center_x': 0.25, 'center_y': 0.87})
        button4.bind(on_press=self.freeze_text)
        layout.add_widget(button4)

        button7 = Button(text='Ключ', size_hint=(0.15, 0.05), pos_hint={'center_x': 0.25, 'center_y': 0.92})
        button7.bind(on_press=self.unfreeze_text)
        layout.add_widget(button7)

        # ОКНО УЗКОЕ НОМЕР ДВА
        self.text_input_right2 = TextInput(multiline=True, size_hint=(0.25, 0.08), pos_hint={'center_x': 0.5, 'center_y': 0.8})
        layout.add_widget(self.text_input_right2)
        button5 = Button(text='Замок', size_hint=(0.15, 0.05), pos_hint={'center_x': 0.5, 'center_y': 0.87})
        button5.bind(on_press=self.freeze_text)
        layout.add_widget(button5)

        button8 = Button(text='Ключ', size_hint=(0.15, 0.05), pos_hint={'center_x': 0.5, 'center_y': 0.92})
        button8.bind(on_press=self.unfreeze_text)
        layout.add_widget(button8)

        # Узкое окно номер ТРИ
        self.text_input_right3 = TextInput(multiline=True, size_hint=(0.25, 0.08), pos_hint={'center_x': 0.75, 'center_y': 0.8})
        layout.add_widget(self.text_input_right3)
        button6 = Button(text='Замок', size_hint=(0.15, 0.05), pos_hint={'center_x': 0.75, 'center_y': 0.87})
        button6.bind(on_press=self.freeze_text)
        layout.add_widget(button6)

        button9 = Button(text='Ключ', size_hint=(0.15, 0.05), pos_hint={'center_x': 0.75, 'center_y': 0.92})
        button9.bind(on_press=self.unfreeze_text)
        layout.add_widget(button9)

        # Добавляем кнопки, которые ссылка
        button1 = Button(text='Y-1', size_hint=(0.04, 0.05), pos_hint={'center_x': 0.35, 'center_y': 0.87}, background_color=(1, 0, 0, 1))
        button1.bind(on_press=self.open_link1)
        layout.add_widget(button1)

        button2 = Button(text='Y-2', size_hint=(0.04, 0.05), pos_hint={'center_x': 0.6, 'center_y': 0.87}, background_color=(1, 0, 0, 1))
        button2.bind(on_press=self.open_link2)
        layout.add_widget(button2)

        button3 = Button(text='Y-3', size_hint=(0.04, 0.05), pos_hint={'center_x': 0.85, 'center_y': 0.87}, background_color=(1, 0, 0, 1))
        button3.bind(on_press=self.open_link3)
        layout.add_widget(button3)

    def set_window_properties(self):
        Window.clearcolor = (0, 0, 0, 1)  # Устанавливаем черный цвет фона
        Window.size = (800, 600)  # Устанавливаем размер окна
        Window.title = 'My Kivy App'  # Устанавливаем заголовок окна
        # Window.set_icon('icon.png')  # Устанавливаем иконку окна

    def freeze_text(self, instance):
        parent = instance.parent
        for child in parent.children:
            if isinstance(child, TextInput) and child.pos_hint['center_x'] == instance.pos_hint['center_x']:
                if child.pos_hint['center_y'] < instance.pos_hint['center_y']:
                    child.readonly = True
                    break

    def unfreeze_text(self, instance):
        parent = instance.parent
        for child in parent.children:
            if isinstance(child, TextInput) and child.pos_hint['center_x'] == instance.pos_hint['center_x']:
                if child.pos_hint['center_y'] < instance.pos_hint['center_y']:
                    child.readonly = False
                    break

    def open_link1(self, instance):
        text = self.text_input_right1.text
        if text.startswith('http://') or text.startswith('https://'):
            webbrowser.open(text)

    def open_link2(self, instance):
        text = self.text_input_right2.text
        if text.startswith('http://') or text.startswith('https://'):
            webbrowser.open(text)

    def open_link3(self, instance):
        text = self.text_input_right3.text
        if text.startswith('http://') or text.startswith('https://'):
            webbrowser.open(text)

if __name__ == '__main__':
    MyApp().run()
