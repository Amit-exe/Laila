import pyttsx3
import speech_recognition as sr
import datetime
from datetime import date
import wikipedia
import webbrowser
import os
import random
import sys
from tkinter import *
from tkinter import ttk
import tkinter 
import random 

root= Tk()
root.geometry("375x400")
root.minsize(375,400)
root.maxsize(375,400)
root.configure(bg="chocolate1")
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 160)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good evening!")

    speak(" I am Laila , press the listen button"
            "and  tell me  what can i do for you")

def wishingui():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Life is full of uncertainties." 
                "But there will always be a sunrise"
                "after every sunset. Good morning!")
    elif hour>=12 and hour<18:
        speak("May this beautiful afternoon fill" 
                "your heart boundless happiness and "
                "gives you new hopes to start yours"
                 "with. May you have lot of fun! Good "
                 "afternoon dear! ")
    else:
        speak("May the sun in your life never set,"
                "may it always rise high and "
                "above… good evening.")


gnLbl=ttk.Label(root, text="")
gnLbl.pack()


def takecommand(lbl):
    r = sr.Recognizer() 
    with sr.Microphone() as source:
        speak("Listening...")
        print("Listning...")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        speak("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
        lbl.config(text="user said:" +query)

    except Exception as e:
        print(e)
        print("say that again please....")
        speak("say that again please....")
        return "None"
    return query.lower()

def joke():
    jo= open("project\\jokes.txt",encoding="utf8").read().splitlines()
    j1=random.choice(jo)
    speak(j1)
    

def fact():
    fa= open("project\\facts.txt",encoding="utf8").read().splitlines()
    f1=random.choice(fa)
    speak(f1)
    

def a_fact(query):
    query=query.replace("tell me a fact about", "")
    query=query+ " facts"
    webbrowser.get().open("https://google.com/search?q=%s" % query)

wish()


def vid():
    video_folder = "videos"
    songs = os.listdir(video_folder)
    last = len(songs)
    no=random.randrange(0,last,1)
    speak("playing video")
    os.startfile(os.path.join(video_folder, songs[no]))

def music():
    song_folder = "music"
    songs = os.listdir(song_folder)
    last = len(songs)
    no=random.randrange(0,last,1)
    speak("playing music")
    os.startfile(os.path.join(song_folder, songs[no]))

def main():
        
        query = takecommand(gnLbl)
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak(f"According to wikipedia {results}")
        elif 'open youtube' in query:
            url = "youtube.com"
            webbrowser.get(chrome_path).open(url)
            speak("opening youtube")
        elif 'open google' in query:
            url = "google.com"
            webbrowser.get(chrome_path).open(url)
            speak("opening google")
        elif 'open amazon' in query:
            url = "amazon.com"
            webbrowser.get(chrome_path).open(url)
            speak("opening amazon")
        elif 'open flipkart' in query:
            url = "flipkart.com"
            webbrowser.get(chrome_path).open(url) 
            speak("opening flipkart")
        elif 'open facebook' in query:
            url = "facebook.com"
            webbrowser.get(chrome_path).open(url)
            speak("opening facebook")
        elif 'open instagram' in query:
            url = "instagram.com"
            webbrowser.get(chrome_path).open(url)
            speak("opening instagram")
        elif 'open reddit' in query:
            url = "reddit.com"
            webbrowser.get(chrome_path).open(url)
            speak("opening reddit")
        elif 'open twiter' in query:
            url = "twiter.com"
            webbrowser.get(chrome_path).open(url)
            speak("opening twiter")
        elif 'wish me' in query:
            wishingui()
        elif 'play music' in query:
            music()
        elif 'play video' in query:
            vid()
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f" the time is {strTime}")
            print(strTime)
        elif 'the date' in query:
            today=date.today()
            speak(f" the date is {today}")
            print(today)
        elif 'open photoshop' in query:
            speak("opening photoshop")
            app ="C:/Program Files/Adobe Photoshop CC 2018/Photoshop.exe"
            os.startfile(app)
        elif 'open pycharm' in query:
            speak("opening pyharm ide")
            app ="C:\\Program Files\\JetBrains\\PyCharm Community Edition 2019.2.4\\bin\\pycharm64.exe"
            os.startfile(app)
        elif 'open android studio' in query:
            speak("opening android studio")
            app ="C:\\Program Files\\Android\\Android Studio\\bin\\studio64.exe"
            os.startfile(app)
        elif 'open edge' in query:
            speak("opening edge")
            app ="C:\\Users\\AmitKushwaha\\Desktop\\Microsoft Edge"
            os.startfile(app)
        elif 'open store' in query:
            speak("opening store")
            app ="C:\\Users\\AmitKushwaha\\Desktop\\Microsoft Store"
            os.startfile(app)
        elif 'open paint' in query:
            speak("opening paint")
            app ="C:\\Users\\AmitKushwaha\\Desktop\\Paint 3D"
            os.startfile(app)
        elif 'open android studio' in query:
            speak("opening android studio")
            app ="C:\\Users\\AmitKushwaha\\Desktop\\Android Studio"
            os.startfile(app)
        elif 'open pubg' in query:
            speak("opening android studio")
            app ="C:\\Users\\AmitKushwaha\\Desktop\\PUBG LITE"
            os.startfile(app)
        elif 'a joke' in query:
            joke()
        elif 'random fact' in query:
            fact()
        elif 'a fact' in query:
            a_fact(query)
        elif "colour game" in query:
            colorgame()
        elif "close now" in query:
            speak("quitting... goodbye.....")
            sys.exit()


global timeleft
timeleft=30
global score
score=0

def colorgame():
    colours = ['Red','Blue','Green','Pink','Black', 
           'Yellow','Orange','White','Purple','Brown'] 
    score = 0
    
  
    
    def startGame(event): 

        if timeleft == 30: 

            countdown() 

       
        nextColour() 
    
  
    def nextColour(): 
    
        global score 
         
    
        if timeleft > 0: 
        
            e.focus_set() 
    
            
            if e.get().lower() == colours[1].lower(): 

                score += 1
    
            
            e.delete(0, tkinter.END) 

            random.shuffle(colours) 

           
            label.config(fg = str(colours[1]), text = str(colours[0])) 

             
            scoreLabel.config(text = "Score: " + str(score)) 
    
    
      
    def countdown(): 
        global timeleft
        
    
         
        if timeleft > 0: 
        
            
            timeleft -= 1

           
            timeLabel.config(text = "Time left: "
                                   + str(timeleft)) 

            
            timeLabel.after(1000, countdown) 
    
    
                                           
    root = tkinter.Tk() 
    
    root.title("COLORGAME") 

    root.geometry("375x250") 
    
    instructions = tkinter.Label(root, text = "Type in the colour"
                            "of the words, and not the word text!", 
                                          font = ('Helvetica', 12)) 
    instructions.pack()  
    
    
    scoreLabel = tkinter.Label(root, text = "Press enter to start", 
                                          font = ('Helvetica', 12)) 
    scoreLabel.pack() 
    
    
    timeLabel = tkinter.Label(root, text = "Time left: " +
                  str(timeleft), font = ('Helvetica', 12)) 

    timeLabel.pack() 
    
    label = tkinter.Label(root, font = ('Helvetica', 60)) 
    label.pack() 
    
     
    e = tkinter.Entry(root) 
    
     
    root.bind('<Return>', startGame) 
    e.pack() 
    
    
    e.focus_set()

    rest=Button(root,text="reset",command=res,bg="purple",
                    fg="white",relief=RIDGE,borderwidth=3,pady=5,padx=5)
    rest.pack()



def res():
    global score
    global timeleft
    score=0
    timeleft=30




class ToolTipBase:

    def __init__(self, button):
        self.button = button
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0
        self._id1 = self.button.bind("<Enter>", self.enter)
        self._id2 = self.button.bind("<Leave>", self.leave)
        self._id3 = self.button.bind("<ButtonPress>", self.leave)

    def enter(self, event=None):
        self.schedule()

    def leave(self, event=None):
        self.unschedule()
        self.hidetip()

    def schedule(self):
        self.unschedule()
        self.id = self.button.after(1500, self.showtip)

    def unschedule(self):
        id = self.id
        self.id = None
        if id:
            self.button.after_cancel(id)

    def showtip(self):
        if self.tipwindow:
            return
        
        x = self.button.winfo_rootx() + 20
        y = self.button.winfo_rooty() + self.button.winfo_height() + 1
        self.tipwindow = tw = Toplevel(self.button)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        self.showcontents()

    def showcontents(self, text="Your text here"):
        # Override this in derived class
        label = Label(self.tipwindow, text=text, justify=LEFT,
                      background="#ffffe0", relief=SOLID, borderwidth=1,wraplength=10)
        label.pack()

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()


class ToolTip(ToolTipBase):

    def __init__(self, button, text):
        ToolTipBase.__init__(self, button)
        self.text = text

    def showcontents(self):
        ToolTipBase.showcontents(self, self.text)


class ListboxToolTip(ToolTipBase):

    def __init__(self, button, items):
        ToolTipBase.__init__(self, button)
        self.items = items

    def showcontents(self):
        listbox = Listbox(self.tipwindow, background="grey28",fg="white",width=50,height=1)
        listbox.pack()
        for item in self.items:
            listbox.insert(END, item)


frm= Frame(root,bg="grey20", pady=15,padx=30)
frm.pack(side=BOTTOM)
root.title("Laila your virtual assistant")
btn = Button(frm,text="wish", command=wishingui,bg="purple",fg="white",relief=RIDGE,borderwidth=5, )
tip1 = ListboxToolTip(btn, ["click here to get\n greetings"])
btn.grid(row=1,column=1,ipadx=5)
btn2 = Button(frm,text="Listen", command=main , bg="purple",fg="white",relief=RIDGE,borderwidth=5,)
tip2 = ListboxToolTip(btn2, ["click listen button to give command"])
btn2.grid(row=1,column=2)
btn4 = Button(frm,text="Joke", command=joke , bg="purple",fg="white",relief=RIDGE,borderwidth=5,)
tip4 = ListboxToolTip(btn4, ["click and ask for jokes"])
btn4.grid(row=1,column=4,ipadx=5)
btn5 = Button(frm,text="Video", command=vid , bg="purple",fg="white",relief=RIDGE,borderwidth=5,)
tip5 = ListboxToolTip(btn5, ["click to play videos"])
btn5.grid(row=1,column=5,pady=5,ipadx=5)
btn6 = Button(frm,text="music", command=music , bg="purple",fg="white",relief=RIDGE,borderwidth=5,)
tip6 = ListboxToolTip(btn6, ["click to play music"])
btn6.grid(row=1,column=3,pady=5,ipadx=5)
btn7 = Button(frm,text="game", command=colorgame , bg="purple",fg="white",relief=RIDGE,borderwidth=5,)
tip7 = ListboxToolTip(btn6, ["click to play game"])
btn7.grid(row=1,column=7,pady=5,ipadx=5)
root.mainloop()