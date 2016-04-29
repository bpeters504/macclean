#!/usr/bin/python

import gi, re, os
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject, Gdk

## Simple GTK 3 application to remove seperating characters from MAC addresses
## style provider code taken from fcwu on GitHub https://gist.github.com/fcwu/5794494

class EntryWindow(Gtk.Window):

    def __init__(self):
        self.clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)

        Gtk.Window.__init__(self, title="Clean Your MAC")
        self.set_default_size(300,100)
        self.set_border_width(10)
        self.timeout_id = None

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        vbox.set_valign(Gtk.Align.START)
        hbox1 = Gtk.Box(spacing=6)
        hbox1.set_halign(Gtk.Align.START)

        hbox2 = Gtk.Box(spacing=6)
        hbox2.set_valign(Gtk.Align.START)
        vbox.pack_start(hbox1, False, False, 0)
        vbox.pack_end(hbox2, False, False, 0)
        self.add(vbox)

        self.entry_label = Gtk.Label()
        self.entry_label.set_text("MAC:")
        self.entry_label.set_size_request(10, 30)
        hbox1.pack_start(self.entry_label, False, False, 0)

        self.entry = Gtk.Entry()
        self.entry.set_width_chars(19)
        self.entry.set_has_frame(True)
        self.entry.connect("activate", self.submit_button_clicked)
        hbox1.pack_end(self.entry, False, False, 0)

        self.label = Gtk.Label()
        self.label.set_text("")
        self.label.set_width_chars(32)
        hbox2.pack_start(self.label, False, False, 0)

        submit_button = Gtk.Button.new_with_label("Clean")
        submit_button.connect("clicked", self.submit_button_clicked)
        hbox2.pack_end(submit_button, False, False, 0)


    def submit_button_clicked(self, submit_button):
        clean_mac = re.sub('[^0-9a-fA-F]+', '', self.entry.get_text())
        if len(clean_mac) != 12 :
            self.label.set_text("Invalid MAC!")
        else :
            self.label.set_text("Cleaned MAC Copied to clipboard")
            self.entry.set_text(clean_mac)
            self.clipboard.set_text(clean_mac, -1)

def main():

    def gtk_style():
        pwd = os.path.dirname(os.path.realpath(__file__))
        cssProvider = Gtk.CssProvider()
        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(),
            cssProvider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

    gtk_style()
    win = EntryWindow()
    win.connect("delete-event", Gtk.main_quit)
    win.set_name("EntryWindow")
    win.show_all()
    Gtk.main()


main()
