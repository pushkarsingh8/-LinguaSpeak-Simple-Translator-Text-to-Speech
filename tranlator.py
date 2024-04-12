from tkinter import*
from tkinter import messagebox
import gtts
import playsound
from translate import Translator
import random
import string


window = Tk()
window.geometry("400x500")
window.title("Translator")
window.config(bg="light blue")

options = ["default","English","Hindi","German","Tamil","French","Spanish","Japanese"]


def optionss(selection):
    global language
    text2.delete(1.0,END)
    dictt = {
    "English": "en",
    "Hindi": "hi",
    "German": "de",
    "Tamil": "ta",
    "French": "fr",
    "Spanish": "es",
    "Japanese": "ja"
    }
   
    language =  dictt[selection]
    converted()
    



selected_option = StringVar(window)
selected_option.set(options[0])



def converted():
    
    global change_text

    

    try:
        textt = text1.get("1.0","end-1c")
        if not textt:
            
            messagebox.showerror("Error","Please enter something")
        else:   
            text2.delete(1.0,END)
            change = Translator(to_lang=language)
            change_text = change.translate(textt)
            button.config(text="Converted")
            print(change_text)
            text2.insert(1.0,change_text)
            
    except Exception as y:
        text1.delete(1.0,END)
        messagebox.showerror("Invalid","Please Enter valid detail")
    
    


def speaker():
    try:
        if  not change_text:
            messagebox.showerror("Error","Please click convert button  ")
        speak = gtts.gTTS(change_text,lang=language)
        d1 = random.choice(string.ascii_letters).lower()
        d2 = random.choice(string.ascii_letters).lower()
        d3 = random.choice(string.ascii_letters).lower()
        d4 = random.choice(string.ascii_letters).lower()
        ky = d1+d2+d3+d4
        sound = ky+".mp3"
        speak.save(sound)  
        playsound.playsound(sound)  
        



    except Exception as e:
        messagebox.showerror("Error","An error occured")
        
        
# menu = Menu(window)
# menu.configure(bg="light blue",fg="black")



lang = Label(window,text="Select lang:-",bg="light blue")
lang.place(x=176,y=194)

option_menu = OptionMenu(window,selected_option,*options,command=optionss)
option_menu.place(x=250,y=190)


title = Label(window,text="Translator",font=("bold",20,"underline"),fg="black",bg="light blue")
title.place(x=140,y=5)


detail = Label(window,text="Text:-",font=("bold",20),bg="light blue")
detail.place(x=20,y=100)

text1 = Text(window,height=5,width=20,bg="light blue")
text1.place(x=120,y=80)


detail1 = Label(window,text="Output:-",font=("bold",20),bg="light blue")
detail1.place(x=10,y=260)

text2 = Text(window,height=5,width=20,bg="light blue")
text2.place(x=120,y=240)

button = Button(window,text="Convert",font=("bold",15),command=converted,bg="light blue",fg="black")
button.place(x=160,y=380)

photo = PhotoImage(file="speak.png")
img_size = photo.subsample(22,22)
button = Button(window,image=img_size,font=20,height=20,width=20,command=speaker)
button.place(x=290,y=300)


















window.mainloop()





























