from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        self.label = Label(text="Bonjour, Matthieu!")
        
        # Créez un bouton et liez la fonction on_button_press à l'événement 'on_press'
        self.button = Button(text="Appuyez-moi!")
        self.button.bind(on_press=self.on_button_press)
        
        # Utilisez un BoxLayout pour organiser le label et le bouton
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.label)
        layout.add_widget(self.button)
        
        return layout
    
    def on_button_press(self, instance):
        self.label.text = "Vous avez appuyé le bouton!"

if __name__ == '__main__':
    MyApp().run()
