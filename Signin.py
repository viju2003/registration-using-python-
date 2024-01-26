from tkinter import *
from PIL import ImageTk

#Functionality

def user_enter(event):
    if UsernameEntry.get()=='Username':
        UsernameEntry.delete(0,END)

def Pass_enter(event):
    if PasswordEntry.get()=='Password':
        PasswordEntry.delete(0,END)

def hide():
    openeye.config(file='closeye.png')
    PasswordEntry.config(show='*')
    eyeButton.config(command=show)
    
def show():
    openeye.config(file='openeye.png')
    PasswordEntry.config(show='')
    eyeButton.config(command=hide)
    
def Signup_page():
    login_window.destroy()
    import signup
        
# UI

login_window=Tk()
login_window.resizable(0,0) # for disable minimize button
login_window.title('Login Page') #title of window

bgImage=ImageTk.PhotoImage(file='bg.jpg')

bgLebel=Label(login_window,image=bgImage)
#bgLebel.place(x=0,y=0)
#bgLebel.grid(row=0,column=0) # using grid method
bgLebel.pack()

heading=Label(login_window,text='USER LOGIN',font=('Poppins',23,'bold'),bg='white',fg='firebrick1')
heading.place(x=610,y=110)

UsernameEntry=Entry(login_window,width=25,text='USER LOGIN',font=('Poppins',11),bd=0,fg='firebrick1')
UsernameEntry.place(x=585, y=200)
UsernameEntry.insert(0,'Username')

UsernameEntry.bind('<FocusIn>',user_enter) # bind is use for function like clik event

Frame1=Frame(login_window,width=250,height=2,bg='firebrick1').place(x=580,y=222) # Frame is use for underline

UsernameEntry.bind('<FocusIn>',user_enter)

PasswordEntry=Entry(login_window,width=25,text='Password',font=('Poppins',11),bd=0,fg='firebrick1')
PasswordEntry.place(x=585, y=260)
PasswordEntry.insert(0,'Password')

PasswordEntry.bind('<FocusIn>',Pass_enter)

Frame2=Frame(login_window,width=250,height=2,bg='firebrick1').place(x=580,y=282) 

openeye=PhotoImage(file='openeye.png')
eyeButton=Button(login_window,image=openeye,bd=0,bg='white',activebackground='white',cursor='hand2',command=hide)
eyeButton.place(x=800,y=250)

forgetButton=Button(login_window,text='Forgot Password?',bd=0,bg='white',activebackground='white',cursor='hand2',font=('Poppins',9,'bold'),fg='firebrick1',activeforeground='firebrick1')
forgetButton.place(x=715,y=295)

loginButton=Button(login_window,text='Login',font=('Open sans',16,'bold'),fg='white',bg='firebrick1',activeforeground='firebrick1',activebackground='white',cursor='hand2',bd=0,width=19)
loginButton.place(x=578,y=350)

orLable=Label(login_window,text='-------------- OR -------------',font=('Open Sans',16),fg='firebrick1',bg='white')
orLable.place(x=583,y=400)


facebook_logo=PhotoImage(file='facebook.png')
fbLable=Label(login_window,image=facebook_logo,bg='white')
fbLable.place(x=620,y=440)

Google_logo=PhotoImage(file='google.png')
GoogleLable=Label(login_window,image=Google_logo,bg='white')
GoogleLable.place(x=690,y=440)

twitter_logo=PhotoImage(file='twitter.png')
twitterLable=Label(login_window,image=twitter_logo,bg='white')
twitterLable.place(x=760,y=440)

signLable=Label(login_window,text='Dont have an account?',font=('Open Sans',9,'bold'),fg='firebrick1',bg='white')
signLable.place(x=590,y=500)

newaccountButton=Button(login_window,text='Create new one',font=('Open sans',9,'bold underline'),fg='blue',bg='white',activeforeground='blue',activebackground='white',cursor='hand2',bd=0,command=Signup_page)
newaccountButton.place(x=727,y=500)

login_window.mainloop()