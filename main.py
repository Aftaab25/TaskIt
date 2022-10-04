# from email.mime import application
from cProfile import label
import gi
import sys

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw

class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        # Stuff

        self.set_default_size(600, 250)
        self.set_title("TaskIt")

        self.box1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.box2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.box3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        self.set_child(self.box1)
        self.box1.append(self.box2)
        self.box1.append(self.box3)

        self.button = Gtk.Button(label="Hello")
        self.box2.append(self.button)
        self.button.connect('clicked', self.hello)

    def hello(self, button):
        print("Hello")

class MyApp(Adw.Application):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        self.win = MainWindow(application=app)
        self.win.present()
    

app = MyApp(application_id="io.chromiumhead.TaskIt")
app.run(sys.argv)

# def on_activate(app):
#     win = Gtk.ApplicationWindow(application=app)
#     win.present()

# app = Gtk.Application()
# app.connect('activate', on_activate)

# app.run(None)
