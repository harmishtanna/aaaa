from tkinter import *
from datetime import date
import random
import webbrowser
import speech_recognition as sr
import pyttsx3
import time
import os, win32com.client, winshell
#pyaudio pipwin sounddevice

global balance
global name
global mic
mic = False
balance=2500
name = 'Harmish'
root = Tk()
frame = Frame(root)
frame.pack()
root.configure(background = "#2a2b2d")
root.title("Botix")
window_size = "700x450"
send_p = PhotoImage(file = r"default_send.png")
send_b = PhotoImage(file = r"neon_send.png")
send_l = PhotoImage(file = r"blue_send.png")
send_q = PhotoImage(file = r"grey_send.png")
mic_p = PhotoImage(file = r"default_mic.png")
mic_b = PhotoImage(file = r"neon_mic.png")
mic_l = PhotoImage(file = r"blue_mic.png")
mic_q = PhotoImage(file = r"grey_mic.png")
#global image1
#image1 = PhotoImage(file = r"d:\Users\admin\Pictures\Saved Pictures\ll.png")
#txt box frame
txt_frame = Frame(root, bd=6, bg="#2a2b2d")
txt_frame.pack(expand=True, fill=BOTH)
#scroll bar for text box
txt_scroll = Scrollbar(txt_frame, bd=0)
txt_scroll.pack(fill=Y, side=RIGHT)
#Contain message
txt = Text(txt_frame, yscrollcommand=txt_scroll.set, bd=1, padx=6, pady=9,
	   relief=GROOVE, spacing3=8, width=10, height=1, wrap=WORD, state=DISABLED,
	   bg="#212121", fg="#FFFFFF")
txt.pack(expand=True, fill=BOTH, side=RIGHT)
txt_scroll.config(command = txt.yview)
#txt.see('end')
#txt.config(yscrollcommand=txt_scroll.set)
#frame for entry
e_frame = Frame(root, bd=1, bg="#2a2b2d")
e_frame.pack(side=LEFT, fill=BOTH, expand=True)
#user entry field
e = Entry(e_frame, bd=1, justify=LEFT, bg="#212121", fg="#FFFFFF", insertbackground="#FFFFFF")
e.pack(fill=X, padx=0, pady=14, ipady=3)
#send button frame
send_frame = Frame(root, bd=0, bg="#2a2b2d")
send_frame.pack(side=RIGHT, padx=1, pady=1)
mic_frame = Frame(root, bd=0, bg="#2a2b2d")
mic_frame.pack(side=LEFT, padx=5, pady=5)
txt.tag_configure("right", justify = "right")
e.focus()


#startup
path = os.path.join("E:\Backup","Botix.lnk")
print(os.getcwd())
targeted_path = os.getcwd()
target = fr"{targeted_path}\botix-frontend 8 jan.py"
icon = fr"{targeted_path}\botix-frontend 8 jan.py"
shell = win32com.client.Dispatch("WScript.Shell")
shortcut = shell.CreateShortCut(path)
shortcut.Targetpath = target
shortcut.IconLocation = icon
shortcut.save()

#SpeechRecognition
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',175)

#text-to-speech
def talk(text):
	txt.insert(END, text)
	engine.say(text)
	engine.runAndWait()

#speech-to-text
listener = sr.Recognizer()
def mic_listen():
	#with sr.Microphone() as source:
	#	print("listening...")
	#	audio = listener.record(source, duration=3)
	#	try:
	#		str = listener.recognize_google(audio)
	#		print(str)
	#	except:
	#		print("some error occurred!")
    try:
        with sr.Microphone() as source:
			#listener.adjust_for_ambient_noise(source)
            listener.adjust_for_ambient_noise(source)
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            print(command)
    except:
        pass

def mic_change():
	global mic
	if mic:
		mic=False
		talk("Mic is now off")
	else:
		mic=True
		talk("Mic is now on")


#txt.image_create(END, image = image1)
def onclick(event=None):
	send1()
send = Button(mic_frame,command=onclick, image = send_p, compound = RIGHT, highlightthickness = 0, relief=GROOVE, bd=0,
	      bg="#2a2b2d", fg="#FFFFFF", activebackground="#212121", activeforeground="#FFFFFF")
send.pack(side=RIGHT, ipady=3, ipadx=3)
mic = Button(mic_frame, image = mic_p, compound = CENTER, highlightthickness = 0, relief=GROOVE, bd=0,
	      bg="#2a2b2d", fg="#FFFFFF", activebackground="#212121", activeforeground="#FFFFFF")
mic.pack(side=LEFT, ipady=3, ipadx=3)
def color_theme_hacker():
	root.config(bg="#0F0F0F")
	txt_frame.config(bg="#0F0F0F")
	e_frame.config(bg="#0F0F0F")
	txt.config(bg="#0F0F0F", fg="#33FF33")
	e.config(bg="#0F0F0F", fg="#33FF33", insertbackground="#33FF33")
	send_frame.config(bg="#0F0F0F")
	send.config(bg="#0F0F0F", fg="#FFFFFF", activebackground="#0F0F0F", activeforeground="#FFFFFF", image = send_b)
	mic_frame.config(bg="#0F0F0F")
	mic.config(bg="#0F0F0F", fg="#FFFFFF", activebackground="#0F0F0F", activeforeground="#FFFFFF", image = mic_b)
def color_theme_grey():
	root.config(bg="#444444")
	txt_frame.config(bg="#444444")
	e_frame.config(bg="#444444")
	txt.config(bg="#4f4f4f", fg="#ffffff")
	e.config(bg="#4f4f4f", fg="#ffffff", insertbackground="#ffffff")
	send_frame.config(bg="#444444")
	send.config(bg="#444444", fg="#ffffff", activebackground="#4f4f4f", activeforeground="#ffffff", image = send_q)
	mic_frame.config(bg="#444444")
	mic.config(bg="#444444", fg="#FFFFFF", activebackground="#4f4f4f", activeforeground="#FFFFFF", image = mic_q)
def color_theme_blue():
	root.config(bg="#263b54")
	txt_frame.config(bg="#263b54")
	e_frame.config(bg="#263b54")
	txt.config(bg="#1c2e44", fg="#FFFFFF")
	e.config(bg="#1c2e44", fg="#FFFFFF", insertbackground="#FFFFFF")
	send_frame.config(bg="#263b54")
	send.config(bg="#263b54", fg="#FFFFFF", activebackground="#1c2e44", activeforeground="#FFFFFF", image = send_l)
	mic_frame.config(bg="#263b54")
	mic.config(bg="#263b54", fg="#FFFFFF", activebackground="#1c2e44", activeforeground="#FFFFFF", image = mic_l)
def color_theme_default():
	root.config(bg="#2a2b2d")
	txt_frame.config(bg="#2a2b2d")
	e_frame.config(bg="#2a2b2d")
	txt.config(bg="#212121", fg="#FFFFFF")
	e.config(bg="#212121", fg="#FFFFFF", insertbackground="#FFFFFF")
	send_frame.config(bg="#2a2b2d")
	send.config(bg="#2a2b2d", fg="#FFFFFF", activebackground="#212121", activeforeground="#FFFFFF", image = send_p)
	mic_frame.config(bg="#2a2b2d")
	mic.config(bg="#2a2b2d", fg="#FFFFFF", activebackground="#212121", activeforeground="#FFFFFF", image = mic_p)


def check():
	global balance
	if balance<1:
		talk("\nYour balance gone negative/null. Here's your 2500 extra cash to spend. Enjoy ;)")
		balance=0
		balance=balance+2500


def curr_date():
	sysdate=date.today()
	talk(sysdate)

def help():
	pass
#def reset_tabstop(event):
#       event.widget.configure(tabs=(event.width-17, "right"))

def send1():
	global balance
	global name
	#global image1
	#del image1
	send = e.get()
	if send.isspace() == True or len(send) == 0:
		return
	txt.configure(state=NORMAL)
	send = send.strip()
	txt.insert(END,"\n\t"+send+"\n", "right")
	txt.insert(END, "Botix> ")
	#txt.tag_add("start", "1.0", "end")
	#txt.tag_config("start", background="white", foreground="blue")
	txt.configure(state=NORMAL)
	#teemp = txt.index('image1')
	#txt.delete(teemp, END)
#       root.geometry('700x451')
	e.delete(0, END)
	e.insert (0, "")
	txt.yview(END)
#       txt.bind("<Configure>", reset_tabstop)
	send=send.lower()


#ASKTOM
	if send.startswith("asktom"):
		send = send[len("asktom "):]
		if send.isspace() == True or len(send) == 0:
			talk("Ask me your question after typing 'asktom'")
			txt.configure(state=DISABLED)
		else:
			no_list1=[0,1]
			n=random.choice(no_list1)
			if n==0:
				talk("Yes!! Thats true")
				txt.configure(state=DISABLED)
			else:
				talk("Nope")
				txt.configure(state=DISABLED)

#KILL
	elif send.startswith("kill"):
		send = send[len("kill "):]
		if send.isspace() == True or len(send) == 0:
			talk("Please enter the name of the person who do you want to kill after typing 'kill'")
		else:
			if send == name:
				talk("OK! You are Dead. And now i am being operated by a Ghost👻")
			else:
				no_list2=[1,2,3,4,5]
				n=random.choice(no_list2)
				if n==1:
					txt.insert(END, "After a long Day,"+name.capitalize()+" plops down on the couch with"+send.capitalize()+" and turns on the BIG Bang theory. After a sheldon cooper joke,",send.capitalize(),"laughs uncontrollably and they died. What a funny death they got💀")
				elif n==2:
					txt.insert(END, send.capitalize()+" dies from a swift kick to the Brain🤕")
				elif n==3:
					txt.insert(END, send.capitalize()+" drank a lot of coke, and died because of explosion. What the heck😑")
				elif n==4:
					txt.insert(END, send.capitalize()+" died from CoronaVirus!! Please maintain Social Distancin"+"")
				elif n==5:
					txt.insert(END, send.capitalize()+" fell down from that cliff while searching for pokemon in Pokemon GO game. Good job on keeping your nose in that stupid phone")

#ROAST
	elif send.startswith("roast"):
		send = send[len("roast "):]
		if send.isspace() == True or len(send) == 0:
			talk("Please enter the name of the person who do you want to roast after typing 'roast'")
		else:
			if send == name:
				talk("I should not roast my master. Thats my respect")
			else:
				no_list3=[1,2,3,4,5]
				n=random.choice(no_list3)
				if n==1:
					txt.insert(END, send.capitalize()+" is as useless as the 'ueue' in 'queue'🤭")
				elif n==2:
					txt.insert(END, send.capitalize()+" is so bad at gta 5 that he will get dnf even if he is alone in the race. Dumb.")
				elif n==3:
					txt.insert(END, "If i had a face like"+send.capitalize()+" I would shoot my creators!!")
				elif n==4:
					txt.insert(END, send.capitalize()+" must have been born on highway coz thats where most accidents happen")
				elif n==5:
					txt.insert(END, "If laughter is the best medicine "+send.capitalize()+"'s face must be curing the CoronaVirus!!")

#SUGGEST
	elif send.startswith("suggest"):
		send = send[len("suggest "):]
		if send.isspace() == True or len(send) == 0:
			talk("Please enter the category of what should i suggest after typing 'suggest'")
		else:
			engine.say("Here's what i found")
			engine.runAndWait()
			if 'songs' in send:
				txt.insert(END, "Here's what I found :-\n1. 'Rain On Me' by Lady Gaga\n2. 'Savage' by Megan Thee Stallion\n3. 'Savage Love' by Jawsh 685\n4. 'Toosie Slide' by Drake\n5. 'Dynamite' by BTS")
			elif 'food' in send:
				txt.insert(END, "Here's what I found :-\n1. 'Rogan Josh' - aromatic lamb curry\n2. 'Indian Chats' - Savoury snacks\n3. 'Vada Pav' - Indian Burger\n4. 'Vindaloo' - type of curry\n5. 'Pineapple Pizza' - Most hated by those who never tried")
			elif 'sport' in send:
				txt.insert(END, "Here's what I found :-\n1. Soccer/football\n2. Badminton\n3. Field Hockey\n4. Volleyball\n5. Basketball")
			elif 'video game' in send:
				txt.insert(END, "Here's what I found :-\n1. Doom Eternal\n2. Microsoft Flight Simulator\n3. Dark Souls 3\n4. The Witcher 3 : Wild Hunt\n5. Red Dead Redemption 2")
			else:
				webbrowser.open("https://www.google.com/search?client=?-b-d&q="+send)


# FLIP
	elif send.startswith("flip"):
		no_list4 = [0, 1]
		n = random.choice(no_list4)
		if n == 0:
			talk("Heads it is!")
		else:
			talk("Its Tails!")

# ROLL
	elif send.startswith("roll"):
		no_list5 = [1, 2, 3, 4, 5, 6]
		n = random.choice(no_list5)
		txt.insert(END, "You rolled " + str(n))
		engine.say("You rolled")
		engine.runAndWait()

# BAL
	elif send.startswith("bal"):
		txt.insert(END, "Your initial balance is " + str(balance))

# COINGame
	elif send.startswith("coin"):
		if 'head' in send:
			talk("You choosed Heads...")
			n1 = 0
			txt.insert(END, "\nFliping Coin...\n")
			no_list6 = [0, 1]
			n2 = random.choice(no_list6)
			if n1 == n2:
				time.sleep(3)
				txt.insert(END, "Congratulations!! You won 200 cash🎉")
				balance = balance + 200
			else:
				time.sleep(3)
				txt.insert(END, "You Lost! 100 cash is deducted")
				balance = balance - 100
		elif 'tail' in send:
			txt.insert(END, "You choosed Tails...")
			n1 = 1
			txt.insert(END, "\nFliping Coin...\n")
			no_list7 = [0, 1]
			n2 = random.choice(no_list7)
			if n1 == n2:
				time.sleep(3)
				txt.insert(END, "Congratulations!! You won 200 cash🎉")
				balance = balance + 200
			else:
				time.sleep(3)
				txt.insert(END, "You Lost! 100 cash is deducted")
				balance = balance - 100
		else:
			talk("Please choose your call (Heads or Tails) after typing 'coin'")
		check()

# BANK
	elif send.startswith("bank"):
		send = send[len("bank "):]
		if name == 'admin':
			txt.insert(END, "Balance Changed Successfully")
			balance = int(send)
			check()
		else:
			txt.insert(END, "You are not authorize to change your balance")
			check()

#help
	elif send.startswith("easter eggs"):
		help()
		txt.configure(state=DISABLED)

#Themes
	elif "theme" and "neon" in send:
		color_theme_hacker()
		talk("Theme changed to Neon")
		txt.configure(state=DISABLED)
	elif "theme" and "blue" in send:
		color_theme_blue()
		talk("Theme changed to Blue")
		txt.configure(state=DISABLED)
	elif "theme" and "grey" in send:
		color_theme_grey()
		talk("Theme changed to Grey")
		txt.configure(state=DISABLED)
	elif "theme" and "black" in send:
		color_theme_default()
		talk("Theme changed to Black")
		txt.configure(state=DISABLED)

#mic
	elif "mic" in send:
		if "on" in send:
			mic=True
			talk("Mic turned on")
			mic_listen()
		elif "off" in send:
			mic=False
			talk("Mic turned off")

	else:
		talk("Sorry, I did not understand.")
		txt.configure(state=DISABLED)
	txt.insert(END, "\n")
##txt.image_create(END, image=image1)
root.bind('<Return>', onclick)
root.geometry(window_size)
engine.say("Welcome, "+name+". Today's date is ")
engine.runAndWait()
curr_date()
root.title("Botix")
root.mainloop()
