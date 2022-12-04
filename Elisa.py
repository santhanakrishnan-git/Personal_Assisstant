import random
from tkinter import *
from tkinter import messagebox
from datetime import datetime
from time import sleep as s
#Greet part
greet_input=['hi','hey','hello','hey hello','helo']
greet_responses=['Hi' ,'Yes','Yup!',"Hey Mate!"'Welcome!','Whatsup!',' Yes, Iam glad here to work for you!']


#Questions list to user
bot_qst=['Are you Want to Know Anything?',"Hmmm! Do You still Want to Know Anything ? If you don't Want please text 'Exit'"]

#lists
time_list=["whats the time now","hey, what is the time now","current time","time","what is the time now","tell the current time"]
date_list=["whats the today date","hey, what is the todays date","what is the todays date","current date","date","tell the current date"]
user_ans=['okie','okay','ok','cool','done','hmm','hm','mm','mmm','nice','well','good','wow','oh good','oh nice']
end_list=['quit','bye','ok bye','exit','bye bye']
total_list=time_list+date_list+user_ans+end_list

root=Tk()

#date and time
now = str(datetime.now())
print(now)
nowsplit = now.split()

def time():
    current_time = nowsplit[1]
    time_split=current_time.split('.')
    time_split.pop()
    t_edit=time_split[0]
    t_final=t_edit.split(':')
    return("Current Time : "+t_final[0]+'Hours '+t_final[1]+'Minutes '+t_final[2]+'Seconds\n')

def date():
    current_date = nowsplit[0]
    return("Current Date in Year-Month-Day : "+current_date)


def greeting(message):
    if message in greet_input:
        return random.choice(greet_responses)

def works(message):
    if(message in time_list):
        e.delete(0 , 'end')
        res = time()
        txt.insert(END,'\n'+bot_name+" : "+ res)
    elif(message in date_list):
        e.delete(0, 'end')
        res = date()
        txt.insert(END,'\n'+bot_name+" : "+ res+'\n')
    elif(message in user_ans):
        txt.insert(END,'\n' +bot_name+" : "+bot_qst[1]+"\n")
        e.delete(0, 'end')
    else:
        txt.insert(END,'\n'+bot_name+" : Sorry I Can't Do That!:(\n")
        e.delete(0,'end')
global bot_name
bot_name="Elisa"
def send(value):
    reply = "You : " + msg.get()
    input = msg.get().lower()
    txt.yview('end')
    txt.insert(END, "\n" + reply+'\n')
    if(greeting(input) != None):
        txt.insert(END, "\n" + bot_name +' : '+greeting(input)+"  "+bot_qst[0]+" \n")
        global bot_rep
        bot_rep=bot_qst[0]
        e.delete(0, 'end')
    elif(input in end_list)\
            :
        store=messagebox.askyesno(title="Exit Confirmation",message="Are You Sure ?")
        e.delete(0, 'end')
        if(store==True):
            messagebox.showinfo(title="Successfully Exited",message=bot_name+" : Bye Bye Take Care!")
            root.quit()
        else:
            txt.insert(END,'\n'+bot_name+" : Ok well! You Pressed No !! I think You like to chatting with me:) LOL\n")
            pass
    elif(input=='yes'):
        try:
            if((input == "yes") and (bot_rep in bot_qst)):
                txt.insert(END, '\n' + bot_name + " : Cool...! What do You Want to know? or Want to do?\n")
                e.delete(0,'end')
        except:
            txt.insert(END,'\n'+bot_name+" : OOPS! I Can't get you !")
            e.delete(0,'end')
    elif (input != None):
        try:
            if ((bot_rep in bot_qst) and (input in total_list)):
                works(input)
        except:
            txt.insert(END, '\n' + bot_name + " : OOPS! I Can't get you !")
            e.delete(0, 'end')
root.config(bg='white')
root.geometry('410x520')
root.title("ELISA")
root.iconbitmap(r'C:\Users\ELCOT\Downloads\log2.ico')

#scroll bar

scrollbar=Scrollbar(root)
scrollbar.place(x=388,y=26,height=450)

#chat window
txt=Text(root,bd=1,bg='lightblue',yscrollcommand=scrollbar.set,wrap=WORD,font=('Times new Roman',13),borderwidth=1)
txt.place(x=6,y=27,width=380,height=450)
label1=Label(root,text="Hi ! I'm Elisa Your Personal Assistant :)",bg='white',fg='blue',padx=2,pady=2,width=41,font=('Times new Roman',12))
label1.place(x=6.5,y=0)


scrollbar.config(command=txt.yview)
#message window
messageWindow=Text(root)

#button
button=Button(root,text='Send',command=send ,bd=2,bg='light grey',activebackground="white",font=("Times new Roman",15))
button.place(x=310,y=481,height=31,width=97)
msg=StringVar()
e=Entry(root, bd=1, bg="lightblue", font=('Times new Roman', 15), textvariable=msg)
e.bind('<Return>',send)
e.focus()
e.place(x=6,y=482,height=30,width=300)
root.mainloop()