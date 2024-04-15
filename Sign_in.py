from login_db import*
from homepage import*

def close():
    try:
        login_window.destroy()
        print("login frame changed")
    except:
        pass
    
def home(username,password):
    l = dblogin(username,password)
    if message(l):
        close()
        homepage()

def goto_register(name,username,email,dob,password):
    l = dbregister(name,username,email,dob,password)
    if message(l):
        sign_in()



def sign_in(page=1):
    global login_window
    close()

    #tkinter class object created 
    #login_window is object of class tkinter
        
    login_window=Tk()
    login_window.title("Login")

    #background image
    img1=ImageTk.PhotoImage(file='bgimage.jpg')
    login_window.geometry('990x660')
    login_window.resizable(0,0)
    bglabel=Label(login_window,image=img1)
    bglabel.grid(row=0,column=0)
    

    def hide():
        openeye.config(file='view.png')
        password.config(show='*')
        eyebutton.config(command=show)

    def show():
        openeye.config(file='hidden.png')
        password.config(show='')
        eyebutton.config(command=hide)

    def hide2():
        openeye2.config(file='view.png')
        password2.config(show='*')
        eyebutton.config(command=show)

    def show2():
        openeye2.config(file='view.png')
        password2.config(show='')
        eyebutton.config(command=hide)

    if page==1:

        #heading
        heading=Label(login_window,text='LOGIN',font=('Montsterrat',30,'bold'),bg='white',fg='lime green')
        heading.place(x=670,y=130)

        # username label
        lb1 = Label(login_window,text="Username",font=('Montsterrat',12),bd=0,bg='white',fg='navy')
        lb1.place(x=610,y=200)

        #Entry_field using Entry class(USERNAME)
        username=Entry(login_window,width=22,font=('Montsterrat',14),bd=1,bg='white',fg='navy')
        username.place(x=610,y=220)
        
        #underline using frame
        f1=Frame(login_window,width=250,height=2,bg='lime green')
        f1.place(x=610,y=250)

        # Password Label
        lb2 = Label(login_window,text="Password",font=('Montsterrat',12),bd=0,bg='white',fg='navy')
        lb2.place(x=610,y=280)

        # Entry_field using Entry class(PASSWORD)
        password=Entry(login_window,width=20,font=('Montsterrat',14),bd=1,bg='white',fg='navy')
        password.place(x=610,y=300)

        f2=Frame(login_window,width=250,height=2,bg='lime green')
        f2.place(x=610,y=330)
        openeye=PhotoImage(file='view.png')
        eyebutton=Button(login_window,image=openeye,bd=0,bg='white',activebackground='white',cursor='hand2',command=hide)
        eyebutton.place(x=850,y=300)

        password.config(show='*')
        eyebutton.config(command=show)

        #Forget paasword
        forgetbutton=Button(login_window,text='Forgot Password?',command=lambda:sign_in(3),activebackground='white',cursor='hand2',
                            font=('Montsterrat',12),fg='navy',bd=0,bg='white',activeforeground='navy')
        forgetbutton.place(x=740,y=350)

        
        

        #Login Button
        loginbutton=Button(login_window,width=19,bd=0,text='Login',font=('Montsterrat',18,'bold'),
                        fg='white',bg='lime green',cursor='hand2',activeforeground='white',activebackground='lime green',
                        command=lambda:home(username.get(),password.get()))
        loginbutton.place(x=590,y=400)

        #orLabel
        orlabel=Label(login_window,text='OR',font=('Poppins',16),bg='white',fg='navy')
        orlabel.place(x=720,y=455)

        #new user registration
        new_userbutton=Button(login_window,width=19,bd=0,text='New User? Register',command=lambda:sign_in(2),font=('Montsterrat',18,'bold'),
                        fg='white',bg='lime green',cursor='hand2',activeforeground='white',activebackground='lime green')
        new_userbutton.place(x=590,y=500)

    elif page==2:

        #heading
        heading=Label(login_window,text='REGISTER',font=('Montsterrat',30,'bold'),bg='white',fg='lime green')
        heading.place(x=640,y=100)

        # name label
        lb1 = Label(login_window,text="Name",font=('Montsterrat',12),bd=0,bg='white',fg='navy')
        lb1.place(x=610,y=170)
        #Entry_field using Entry class(NAME)
        name=Entry(login_window,width=22,font=('Montsterrat',14),bd=1,bg='white',fg='navy')
        name.place(x=610,y=190)
        #underline using frame
        f1=Frame(login_window,width=250,height=2,bg='lime green')
        f1.place(x=610,y=220)

        # username label
        lb2 = Label(login_window,text="Username",font=('Montsterrat',12),bd=0,bg='white',fg='navy')
        lb2.place(x=610,y=230)
        #Entry_field using Entry class(USERNAME)
        username=Entry(login_window,width=22,font=('Montsterrat',14),bd=1,bg='white',fg='navy')
        username.place(x=610,y=250)
        #underline using frame
        f2=Frame(login_window,width=250,height=2,bg='lime green')
        f2.place(x=610,y=280)

        # Email Label 
        lb3 = Label(login_window,text="Email",font=('Montsterrat',12),bd=0,bg='white',fg='navy')
        lb3.place(x=610,y=300)
        # Entry_field using Entry class(Email)
        Email=Entry(login_window,width=22,font=('Montsterrat',14),bd=1,bg='white',fg='navy')
        Email.place(x=610,y=320)
        #underline using frame
        f3=Frame(login_window,width=250,height=2,bg='lime green')
        f3.place(x=610,y=350)

        # DOB Label
        lb4 = Label(login_window,text="Date of Birth",font=('Montsterrat',12),bd=0,bg='white',fg='navy')
        lb4.place(x=610,y=360)
        dob = DateEntry(login_window, date_pattern='yyyy-mm-dd', firstweekday='sunday',
                        locale='en_US', width=20,font=('Montsterrat',14),bd=1,bg='white',fg='navy')
        dob.place(x=610, y=380)
        #underline using frame
        f4=Frame(login_window,width=250,height=2,bg='lime green')
        f4.place(x=610,y=410)

        # Password Label 
        lb5 = Label(login_window,text="Password",font=('Montsterrat',12),bd=0,bg='white',fg='navy')
        lb5.place(x=610,y=420)
        # Entry_field using Entry class(PASSWORD)
        password=Entry(login_window,width=20,font=('Montsterrat',14),bd=1,bg='white',fg='navy')
        password.place(x=610,y=440)
        #underline using frame
        f5=Frame(login_window,width=250,height=2,bg='lime green')
        f5.place(x=610,y=470)
        openeye=PhotoImage(file='view.png')
        eyebutton=Button(login_window,image=openeye,bd=0,bg='white',activebackground='white',cursor='hand2',command=hide)
        eyebutton.place(x=840,y=440)

        #Register Button
        Registerbutton=Button(login_window,width=19,bd=0,text='Register',font=('Montsterrat',18,'bold'),
                        fg='white',bg='lime green',cursor='hand2',activeforeground='white',activebackground='lime green',
                        command=lambda:goto_register(name.get(),(username.get()).lower(),Email.get(),dob.get(),password.get()))
        Registerbutton.place(x=590,y=490)

        #backlogin Button
        backtologinbutton=Button(login_window,bd=0,text='Back to login',font=('Montsterrat',12,'bold'),command=lambda:sign_in(1),
                        fg='navy',bg='white',cursor='hand2',activeforeground='navy',activebackground='white')
        backtologinbutton.place(x=770,y=540)

    elif page==3:
        #heading
        heading=Label(login_window,text='RESET',font=('Montsterrat',30,'bold'),bg='white',fg='lime green')
        heading.place(x=660,y=110)

        # Email Label 
        lb6 = Label(login_window,text="Email",font=('Montsterrat',12),bd=0,bg='white',fg='navy')
        lb6.place(x=610,y=190)
        # Entry_field using Entry class(Email)
        Email=Entry(login_window,width=22,font=('Montsterrat',14),bd=1,bg='white',fg='navy')
        Email.place(x=610,y=215)
        #underline using frame
        f6=Frame(login_window,width=250,height=2,bg='lime green')
        f6.place(x=610,y=245)

        # DOB Label
        lb7 = Label(login_window,text="Date of Birth",font=('Montsterrat',12),bd=0,bg='white',fg='navy')
        lb7.place(x=610,y=265)
        dob = DateEntry(login_window, date_pattern='yyyy-mm-dd', firstweekday='sunday',
                        locale='en_US', width=20,font=('Montsterrat',14),bd=1,bg='white',fg='navy')
        dob.place(x=610, y=290)
        #underline using frame
        f7=Frame(login_window,width=250,height=2,bg='lime green')
        f7.place(x=610,y=325)

        # Password Label 
        lb8 = Label(login_window,text="New Password",font=('Montsterrat',12),bd=0,bg='white',fg='navy')
        lb8.place(x=610,y=345)
        # Entry_field using Entry class(PASSWORD)
        password=Entry(login_window,width=20,font=('Montsterrat',14),bd=1,bg='white',fg='navy')
        password.place(x=610,y=370)
        #underline using frame
        f8=Frame(login_window,width=250,height=2,bg='lime green')
        f8.place(x=610,y=400)
        openeye=PhotoImage(file='view.png')
        eyebutton=Button(login_window,image=openeye,bd=0,bg='white',activebackground='white',cursor='hand2',command=hide)
        eyebutton.place(x=840,y=370)

        #Re-enter Password
        lb9 = Label(login_window,text="Re-enter Password",font=('Montsterrat',12),bd=0,bg='white',fg='navy')
        lb9.place(x=610,y=420)
        # Entry_field using Entry class(PASSWORD)
        password2=Entry(login_window,width=20,font=('Montsterrat',14),bd=1,bg='white',fg='navy')
        password2.place(x=610,y=445)
        #underline using frame
        f9=Frame(login_window,width=250,height=2,bg='lime green')
        f9.place(x=610,y=475)
        openeye2=PhotoImage(file='view.png')
        eyebutton2=Button(login_window,image=openeye2,bd=0,bg='white',activebackground='white',cursor='hand2',command=hide2)
        eyebutton2.place(x=840,y=445)


        #Register Button
        Resetbutton=Button(login_window,width=19,bd=0,text='Reset',font=('Montsterrat',18,'bold'),
                        fg='white',bg='lime green',cursor='hand2',activeforeground='white',activebackground='lime green')
        Resetbutton.place(x=590,y=500)

       #backlogin Button
        backtologinbutton=Button(login_window,bd=0,text='Back to login',font=('Montsterrat',12,'bold'),command=lambda:sign_in(1),
                        fg='navy',bg='white',cursor='hand2',activeforeground='navy',activebackground='white')
        backtologinbutton.place(x=770,y=550)

    login_window.mainloop()

sign_in(1)