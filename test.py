from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
from tkcalendar import DateEntry
import sqlite3



# Establishing connection to SQLite database
conn = sqlite3.connect('user_database.db')
c = conn.cursor()

# Creating a table to store user information if it doesn't exist already
c.execute('''CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            dob TEXT NOT NULL,
            password TEXT NOT NULL
            )''')
conn.commit()

def show_popup(message):
    messagebox.showinfo("Information", message)

def sign_in(page=1):
    global login_window, name, username, email, dob, password, email_reset, dob_reset, password_reset, password2_reset, password2
    try:
        login_window.destroy()
        print("login frame changed")
    except:
        pass

    login_window = Tk()
    login_window.title("Login")

    img1 = ImageTk.PhotoImage(file='bgimage.jpg')
    login_window.geometry('990x660')
    login_window.resizable(0, 0)
    bglabel = Label(login_window, image=img1)
    bglabel.grid(row=0, column=0)

    def hide():
        openeye.config(file='view.png')
        password.config(show='*')
        eyebutton.config(command=show)

    def show():
        openeye.config(file='hidden.png')
        password.config(show='')
        eyebutton.config(command=hide)

    # def hide2():
    #     openeye2.config(file='view.png')
    #     password2.config(show='*')
    #     eyebutton.config(command=show)

    # def show2():
    #     openeye2.config(file='view.png')
    #     password2.config(show='')
    #     eyebutton.config(command=hide)

    if page == 1:
        heading = Label(login_window, text='LOGIN', font=('Montsterrat', 30, 'bold'), bg='white', fg='lime green')
        heading.place(x=670, y=130)

        lb1 = Label(login_window, text="Username", font=('Montsterrat', 12), bd=0, bg='white', fg='navy')
        lb1.place(x=610, y=200)

        username = Entry(login_window, width=22, font=('Montsterrat', 14), bd=1, bg='white', fg='navy')
        username.place(x=610, y=220)

        f1 = Frame(login_window, width=250, height=2, bg='lime green')
        f1.place(x=610, y=250)

        lb2 = Label(login_window, text="Password", font=('Montsterrat', 12), bd=0, bg='white', fg='navy')
        lb2.place(x=610, y=280)

        password = Entry(login_window, width=20, font=('Montsterrat', 14), bd=1, bg='white', fg='navy')
        password.place(x=610, y=300)

        f2 = Frame(login_window, width=250, height=2, bg='lime green')
        f2.place(x=610, y=330)
        openeye = PhotoImage(file='view.png')
        eyebutton = Button(login_window, image=openeye, bd=0, bg='white', activebackground='white', cursor='hand2',
                           command=hide)
        eyebutton.place(x=850, y=300)

        password.config(show='*')
        eyebutton.config(command=show)

        forgetbutton = Button(login_window, text='Forgot Password?', command=lambda: sign_in(3),
                              activebackground='white', cursor='hand2', font=('Montsterrat', 12), fg='navy', bd=0,
                              bg='white', activeforeground='navy')
        forgetbutton.place(x=740, y=350)

        loginbutton = Button(login_window, width=19, bd=0, text='Login', font=('Montsterrat', 18, 'bold'),
                             fg='white', bg='lime green', cursor='hand2', activeforeground='white',
                             activebackground='lime green', command=login_user)
        loginbutton.place(x=590, y=400)

        orlabel = Label(login_window, text='OR', font=('Poppins', 16), bg='white', fg='navy')
        orlabel.place(x=720, y=455)

        new_userbutton = Button(login_window, width=19, bd=0, text='New User? Register', command=lambda: sign_in(2),
                                font=('Montsterrat', 18, 'bold'),
                                fg='white', bg='lime green', cursor='hand2', activeforeground='white',
                                activebackground='lime green')
        new_userbutton.place(x=590, y=500)

    elif page == 2:
        heading = Label(login_window, text='REGISTER', font=('Montsterrat', 30, 'bold'), bg='white', fg='lime green')
        heading.place(x=640, y=100)

        lb1 = Label(login_window, text="Name", font=('Montsterrat', 12), bd=0, bg='white', fg='navy')
        lb1.place(x=610, y=170)
        name = Entry(login_window, width=22, font=('Montsterrat', 14), bd=1, bg='white', fg='navy')
        name.place(x=610, y=190)
        f1 = Frame(login_window, width=250, height=2, bg='lime green')
        f1.place(x=610, y=220)

        lb2 = Label(login_window, text="Username", font=('Montsterrat', 12), bd=0, bg='white', fg='navy')
        lb2.place(x=610, y=230)
        username = Entry(login_window, width=22, font=('Montsterrat', 14), bd=1, bg='white', fg='navy')
        username.place(x=610, y=250)
        f2 = Frame(login_window, width=250, height=2, bg='lime green')
        f2.place(x=610, y=280)

        lb3 = Label(login_window, text="Email", font=('Montsterrat', 12), bd=0, bg='white', fg='navy')
        lb3.place(x=610, y=300)
        email = Entry(login_window, width=22, font=('Montsterrat', 14), bd=1, bg='white', fg='navy')
        email.place(x=610, y=320)
        f3 = Frame(login_window, width=250, height=2, bg='lime green')
        f3.place(x=610, y=350)

        lb4 = Label(login_window, text="Date of Birth", font=('Montsterrat', 12), bd=0, bg='white', fg='navy')
        lb4.place(x=610, y=360)
        dob = DateEntry(login_window, date_pattern='yyyy-mm-dd', firstweekday='sunday',
                        locale='en_US', width=20, font=('Montsterrat', 14), bd=1, bg='white', fg='navy')
        dob.place(x=610, y=380)
        f4 = Frame(login_window, width=250, height=2, bg='lime green')
        f4.place(x=610, y=410)

        lb5 = Label(login_window, text="Password", font=('Montsterrat', 12), bd=0, bg='white', fg='navy')
        lb5.place(x=610, y=420)
        password = Entry(login_window, width=20, font=('Montsterrat', 14), bd=1, bg='white', fg='navy')
        password.place(x=610, y=440)
        f5 = Frame(login_window, width=250, height=2, bg='lime green')
        f5.place(x=610, y=470)
        openeye = PhotoImage(file='view.png')
        eyebutton = Button(login_window, image=openeye, bd=0, bg='white', activebackground='white', cursor='hand2',
                           command=hide)
        eyebutton.place(x=840, y=440)

        Registerbutton = Button(login_window, width=19, bd=0, text='Register', font=('Montsterrat', 18, 'bold'),
                                fg='white', bg='lime green', cursor='hand2', activeforeground='white',
                                activebackground='lime green',
                                command=register_user)
        Registerbutton.place(x=590, y=490)

        backtologinbutton = Button(login_window, bd=0, text='Back to login', font=('Montsterrat', 12, 'bold'),
                                   command=lambda: sign_in(1),
                                   fg='navy', bg='white', cursor='hand2', activeforeground='navy',
                                   activebackground='white')
        backtologinbutton.place(x=770, y=540)

    elif page == 3:
        heading = Label(login_window, text='RESET', font=('Montsterrat', 30, 'bold'), bg='white', fg='lime green')
        heading.place(x=660, y=110)

        lb6 = Label(login_window, text="Email", font=('Montsterrat', 12), bd=0, bg='white', fg='navy')
        lb6.place(x=610, y=190)
        email_reset = Entry(login_window, width=22, font=('Montsterrat', 14), bd=1, bg='white', fg='navy')
        email_reset.place(x=610, y=215)
        f6 = Frame(login_window, width=250, height=2, bg='lime green')
        f6.place(x=610, y=245)

        lb7 = Label(login_window, text="Date of Birth", font=('Montsterrat', 12), bd=0, bg='white', fg='navy')
        lb7.place(x=610, y=265)
        dob_reset = DateEntry(login_window, date_pattern='yyyy-mm-dd', firstweekday='sunday',
                              locale='en_US', width=20, font=('Montsterrat', 14), bd=1, bg='white', fg='navy')
        dob_reset.place(x=610, y=290)
        f7 = Frame(login_window, width=250, height=2, bg='lime green')
        f7.place(x=610, y=325)

        lb8 = Label(login_window, text="New Password", font=('Montsterrat', 12), bd=0, bg='white', fg='navy')
        lb8.place(x=610, y=345)
        password_reset = Entry(login_window, width=20, font=('Montsterrat', 14), bd=1, bg='white', fg='navy')
        password_reset.place(x=610, y=370)
        f8 = Frame(login_window, width=250, height=2, bg='lime green')
        f8.place(x=610, y=400)
        openeye = PhotoImage(file='view.png')
        eyebutton = Button(login_window, image=openeye, bd=0, bg='white', activebackground='white', cursor='hand2',
                           command=hide)
        eyebutton.place(x=840, y=370)

        lb9 = Label(login_window, text="Re-enter Password", font=('Montsterrat', 12), bd=0, bg='white', fg='navy')
        lb9.place(x=610, y=420)
        password2_reset = Entry(login_window, width=20, font=('Montsterrat', 14), bd=1, bg='white', fg='navy')
        password2_reset.place(x=610, y=445)
        f9 = Frame(login_window, width=250, height=2, bg='lime green')
        f9.place(x=610, y=475)
        openeye2 = PhotoImage(file='view.png')
        # eyebutton2 = Button(login_window, image=openeye2, bd=0, bg='white', activebackground='white', cursor='hand2',
        #                     command=hide2)

        eyebutton2 = Button(login_window, image=openeye2, bd=0, bg='white', activebackground='white', cursor='hand2',
                            command=hide)
        eyebutton2.place(x=840, y=445)

        Resetbutton = Button(login_window, width=19, bd=0, text='Reset', font=('Montsterrat', 18, 'bold'),
                             fg='white', bg='lime green', cursor='hand2', activeforeground='white',
                             activebackground='lime green',
                             command=reset_password)
        Resetbutton.place(x=590, y=500)

        backtologinbutton = Button(login_window, bd=0, text='Back to login', font=('Montsterrat', 12, 'bold'),
                                   command=lambda: sign_in(1),
                                   fg='navy', bg='white', cursor='hand2', activeforeground='navy',
                                   activebackground='white')
        backtologinbutton.place(x=770, y=550)

    login_window.mainloop()

def register_user():
    name_val = name.get()
    username_val = username.get()
    email_val = email.get()
    dob_val = dob.get()
    password_val = password.get()

    c.execute("INSERT INTO users (name, username, email, dob, password) VALUES (?, ?, ?, ?, ?)",
              (name_val, username_val, email_val, dob_val, password_val))
    conn.commit()
    show_popup("Registration successful!")
    print("User registered successfully!")

def login_user():
    username_val = username.get()
    password_val = password.get()

    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username_val, password_val))
    user = c.fetchone()

    if user:
        show_popup("Login successful!")
        print("Login successful!")
    else:
        show_popup("Invalid username or password!")
        print("Invalid username or password!")

def reset_password():
    email_reset_val = email_reset.get()
    dob_reset_val = dob_reset.get()
    new_password_val = password_reset.get()
    reenter_password_val = password2_reset.get()

    c.execute("SELECT * FROM users WHERE email=? AND dob=?", (email_reset_val, dob_reset_val))
    user = c.fetchone()

    if user:
        if new_password_val == reenter_password_val:
            c.execute("UPDATE users SET password=? WHERE email=?", (new_password_val, email_reset_val))
            conn.commit()
            show_popup("Password reset successful!")
            print("Password reset successful!")
        else:
            show_popup("Passwords do not match!")
            print("Passwords do not match!")
    else:
        show_popup("Invalid email or date of birth!")
        print("Invalid email or date of birth!")

# Start the GUI
sign_in(1)
