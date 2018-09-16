#!/usr/bin/env python
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Simple Notebook Example")
        self.set_border_width(3)

        self.vbox = Gtk.VBox(False, 3)
        self.notebook = Gtk.Notebook()
        self.load_file = Gtk.FileChooserButton("Choose Hex File")
        self.hbox = Gtk.HBox(False, 3)
        self.read_button = Gtk.Button("Read")
        self.write_button = Gtk.Button("Write")
        self.load_file.connect("selection-changed",self.on_file_selected)
        self.hbox.pack_start(self.read_button, False, True, 0)
        self.hbox.pack_end(self.write_button, False, True, 0)
        self.vbox.pack_start(self.load_file, False, True, 0)
        self.vbox.pack_start(self.hbox, False, True, 0)
        self.vbox.pack_start(self.notebook, False, True, 0)
        self.add(self.vbox)

        self.page1 = Gtk.Box()
        self.page1.set_border_width(10)
        self.page1.hbox = Gtk.HBox(False, 3)
        self.page1.label1 = Gtk.Label('00-01')
        self.page1.label2 = Gtk.Label('02-03')
        self.page1.hbox.pack_start(self.page1.label1, False, True, 0)
        self.page1.hbox.pack_start(self.page1.label2, False, True, 0)
        self.page1.add(self.page1.hbox)
#        self.page1.add(Gtk.Label('Default Page!'))
        self.notebook.append_page(self.page1, Gtk.Label('Flash'))

        self.page2 = Gtk.Box()
        self.page2.set_border_width(10)
        self.page2.add(Gtk.Label('A page with an image for a Title.'))
        self.notebook.append_page(self.page2, Gtk.Label('EEPROM'))

        self.page3 = Gtk.Box()
        self.page3.set_border_width(10)
        self.page3.add(Gtk.Label('Default Page!'))
        self.notebook.append_page(self.page3, Gtk.Label('Fuse Bits/Setting'))

    def on_file_selected(self, widget):
        self.hex_file = self.load_file.get_filename()

#    def on_button_clicked(self, widget):
#        print("Hello World")

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
