from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql

def login_page():
    signup_window.destroy()
    import Signin
    
def clear():
    emailEntry.delete(0,END)
    usernameEntry.delete(0,END)
    passwordEntry.delete(0,END)
    confirmEntry.delete(0,END)
    check.set(0)
    
def connect_database():
    if emailEntry.get()=='' or usernameEntry.get()=='' or passwordEntry.get()=='' or confirmEntry.get()=='':
        messagebox.showerror('Error','All Fields are Required')
    elif passwordEntry.get() != confirmEntry.get():
        messagebox.showerror('Error','Password mismatch')
    elif check.get()==0:
        messagebox.showerror('Error','Please Accept Terms & Conditions')
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='vIJAYBW@321')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Database Connectivity Issue , Please Try Again')
            return
        
        try:
            query='create database PROJECTuserdata'
            mycursor.execute(query)
            query='use PROJECTuserdata'
            mycursor.execute(query)
            query='create table data(id int auto_increment primary key not null, email varchar(50),username varchar(100),password varchar (20))'
            mycursor.execute(query)
        except:
            mycursor.execute('use PROJECTuserdata')
            query='select * from data where username=%s'
            mycursor.execute(query,(usernameEntry.get()))
            row=mycursor.fetchone()
            if row != None:
                messagebox.showerror('Error','Username Already exists')
            else:    
                query='insert into data(email,username,password) values(%s,%s,%s)'
                mycursor.execute(query,(emailEntry.get(),usernameEntry.get(),passwordEntry.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Success','Registration is successful')
        clear()
        signup_window.destroy()
        import Signin

signup_window=Tk()
signup_window.title('Signup page')
signup_window.resizable(False,False)

background=ImageTk.PhotoImage(file='bg.jpg')
bgLabel=Label(signup_window,image=background)
bgLabel.grid()

frame=Frame(signup_window,bg='white')
frame.place(x=554,y=100)


heading=Label(frame,text='CREATE AN ACCOUNT',font=('Poppins',18,'bold'),bg='white',fg='firebrick1')
heading.grid(row=0,column=0,padx=10,pady=10)

emaillabel=Label(frame,text='Email',font=('Poppins',10,'bold'),bg='white',fg='firebrick1')
emaillabel.grid(row=1,column=0,sticky='w',padx=25,pady=(10,0))

emailEntry=Entry(frame,width=30,font=('Poppins',10,'bold'),bg='white',fg='firebrick1')
emailEntry.grid(row=2,column=0,sticky='w',padx=25)

usernamelabel=Label(frame,text='Username',font=('Poppins',10,'bold'),bg='white',fg='firebrick1')
usernamelabel.grid(row=3,column=0,sticky='w',padx=25,pady=(10,0))

usernameEntry=Entry(frame,width=30,font=('Poppins',10,'bold'),bg='white',fg='firebrick1')
usernameEntry.grid(row=4,column=0,sticky='w',padx=25)

passwordlabel=Label(frame,text='Password',font=('Poppins',10,'bold'),bg='white',fg='firebrick1')
passwordlabel.grid(row=5,column=0,sticky='w',padx=25,pady=(10,0))

passwordEntry=Entry(frame,width=30,font=('Poppins',10,'bold'),bg='white',fg='firebrick1')
passwordEntry.grid(row=6,column=0,sticky='w',padx=25)

confirmlabel=Label(frame,text='Confirm Password',font=('Poppins',10,'bold'),bg='white',fg='firebrick1')
confirmlabel.grid(row=7,column=0,sticky='w',padx=25,pady=(10,0))

confirmEntry=Entry(frame,width=30,font=('Poppins',10,'bold'),bg='white',fg='firebrick1')
confirmEntry.grid(row=8,column=0,sticky='w',padx=25)

check=IntVar()
termsandconditions=Checkbutton(frame,text='I agree to the terms & conditions',font=('Poppins',9,'bold'),bg='white',fg='firebrick1',activebackground='white',activeforeground='firebrick1',cursor='hand2',variable=check)
termsandconditions.grid(row=9,column=0,sticky='w',pady=10,padx=15)

signupButton=Button(frame,text='Signup',font=('Open sans',16,'bold'),fg='white',bg='firebrick1',activeforeground='firebrick1',activebackground='white',cursor='hand2',bd=0,width=10,command=connect_database)
signupButton.grid(row=10,column=0,pady=10)

alreadyaccount=Label(frame,text="Don't have an account?",font=('Poppins',9,'bold'),bg='white',fg='firebrick1')
alreadyaccount.grid(row=11,column=0,sticky='w',padx=25,pady=10)

newaccountButton=Button(frame,text='Log In',font=('Open sans',9,'bold underline'),fg='blue',bg='white',activeforeground='blue',activebackground='white',cursor='hand2',bd=0,command=login_page)
newaccountButton.place(x=170,y=355)


signup_window.mainloop()