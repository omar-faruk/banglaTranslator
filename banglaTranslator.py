from gi.repository import Gtk, GObject
import serial
import time
import goslate
translator=goslate.Goslate()

class TranslatorGUI:
		
	def __init__(self):
		builder = Gtk.Builder()
		builder.add_from_file("translate.glade")
		self.window = builder.get_object("messengerWindow")
		self.inputBox=builder.get_object("input_box")
		self.showBox=builder.get_object("receive_box")
		builder.connect_signals(self)

	def on_input_box_activate(self,inputBox):
		word=self.inputBox.get_text();
		lang='bn'
		ans=translator.translate(word,lang)
		self.showBox.set_text(ans)
		
	def mnu_quite_app(self, window):
		Gtk.main_quit()

if __name__ == '__main__':
    myTranslator = TranslatorGUI()
    myTranslator.window.connect("delete-event", Gtk.main_quit)
    myTranslator.window.show_all()
    Gtk.main()
