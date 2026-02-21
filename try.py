from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical", padding=20, spacing=15)

        self.lbl = Label(text="Enter your comment:", font_size=22)

        self.txt = TextInput(
            hint_text="Type something...",
            font_size=20,
            size_hint=(1, 0.3)
        )

        btn = Button(
            text="Submit",
            font_size=22,
            size_hint=(1, 0.2)
        )
        btn.bind(on_press=self.submit_text)

        layout.add_widget(self.lbl)
        layout.add_widget(self.txt)
        layout.add_widget(btn)

        return layout

    def submit_text(self, instance):
        user_text = self.txt.text
        self.lbl.text = f"You typed: {user_text}"


if __name__ == "__main__":
    MyApp().run()
