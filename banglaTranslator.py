#!/usr/bin/env python
# coding=utf-8

from gi.repository import Gtk, GObject
import serial 
import time
import goslate
import sqlite3
translator=goslate.Goslate()
connection = sqlite3.connect('dict.db')
sql = connection.cursor()
def insertToDB(word,meaning):
	sql.execute("INSERT INTO english(EN) VALUES(?)",(word,))
	sql.execute("INSERT INTO bangla(BN) VALUES(?)",(meaning,))
	connection.commit()
	return

def eng2bn(word):
	sql.execute('SELECT * FROM english WHERE EN=?', (word,))
	try:
		sn=int(sql.fetchone()[0])
		sql.execute("SELECT * FROM bangla WHERE SN=?", (sn,))
		meaning=sql.fetchone()[1]
		return meaning
	except TypeError:
		return "NotFound"

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
		word=word.lower()
		lang='bn'
		inputBox.set_text("")
		meaning=eng2bn(word)
		if(meaning=="NotFound"):
			try:
				meaning=translator.translate(word,lang)
				if(meaning!="NotFound" and meaning!=word):
					insertToDB(word,meaning)
			except:
				if(meaning=="NotFound"):
					meaning="অর্থ খুঁজে পাওয়া যায়নি , ইন্টারনেট  সংযোগ  নিশ্চিত করুন "
		self.showBox.set_text(meaning)
		
	def mnu_quite_app(self, window):
		Gtk.main_quit()

if __name__ == '__main__':
    myTranslator = TranslatorGUI()
    myTranslator.window.connect("delete-event", Gtk.main_quit)
    myTranslator.window.show_all()
    Gtk.main()
