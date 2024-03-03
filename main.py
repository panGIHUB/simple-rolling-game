import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.colorpicker import ColorPicker
from kivy.uix.popup import Popup
import turtle

class TurtleDrawingTool(BoxLayout):
    def __init__(self, **kwargs):
        super(TurtleDrawingTool, self).__init__(**kwargs)

        self.screen = turtle.Screen()
        self.screen.title("Turtle Drawing Tool")
        self.screen.setup(width=800, height=600)

        self.t = turtle.Turtle()
        self.t.speed(0)

        self.prev_x = None
        self.prev_y = None

        self.orientation = "vertical"
        self.spacing = 10

        self.radius_label = Label(text="Radius:")
        self.add_widget(self.radius_label)
        self.radius_entry = TextInput()
        self.add_widget(self.radius_entry)

        self.draw_circle_btn = Button(text="Draw Circle")
        self.draw_circle_btn.bind(on_press=self.draw_circle)
        self.add_widget(self.draw_circle_btn)

        self.side_length_label = Label(text="Side Length:")
        self.add_widget(self.side_length_label)
        self.side_length_entry = TextInput()
        self.add_widget(self.side_length_entry)

        self.draw_square_btn = Button(text="Draw Square")
        self.draw_square_btn.bind(on_press=self.draw_square)
        self.add_widget(self.draw_square_btn)

        self.color_btn = Button(text="Choose Color")
        self.color_btn.bind(on_press=self.choose_color)
        self.add_widget(self.color_btn)

        self.pen_up_btn = Button(text="Pen Up")
        self.pen_up_btn.bind(on_press=self.toggle_pen)
        self.add_widget(self.pen_up_btn)

        self.clear_btn = Button(text="Clear Drawing")
        self.clear_btn.bind(on_press=self.clear_drawing)
        self.add_widget(self.clear_btn)

    def choose_color(self, instance):
        color_picker = ColorPicker()
        color_picker.bind(color=self.set_color)
        popup = Popup(title='Choose Color', content=color_picker, size_hint=(None, None), size=(400, 400))
        popup.open()

    def set_color(self, instance, value):
        self.t.color(value)

    def draw_circle(self, instance):
        try:
            radius = float(self.radius_entry.text)
            self.t.circle(radius)
        except ValueError:
            self.show_error("Invalid radius value!")

    def draw_square(self, instance):
        try:
            side_length = float(self.side_length_entry.text)
            for _ in range(4):
                self.t.forward(side_length)
                self.t.right(90)
        except ValueError:
            self.show_error("Invalid side length value!")

    def clear_drawing(self, instance):
        self.t.clear()

    def toggle_pen(self, instance):
        if self.t.isdown():
            self.t.penup()
            self.pen_up_btn.text = "Pen Down"
        else:
            self.t.pendown()
            self.pen_up_btn.text = "Pen Up"

    def show_error(self, message):
        popup = Popup(title='Error', content=Label(text=message), size_hint=(None, None), size=(300, 200))
        popup.open()

class DrawingToolApp(App):
    def build(self):
        return TurtleDrawingTool()

if __name__ == "__main__":
    DrawingToolApp().run()

