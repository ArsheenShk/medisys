import sqlite3


# Establishing connection to SQLite database
conn = sqlite3.connect('Hospital.db')
c = conn.cursor()

# Creating a table to store user information if it doesn't exist already
c.execute('''CREATE TABLE IF NOT EXISTS Doctor (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            dob TEXT NOT NULL,
            password TEXT NOT NULL
            )''')
conn.commit()

def dblogin(username,password):
    print(username)
    print(password)
    c.execute("select * from Doctor where username=? and password=?",(username,password))
    data = c.fetchone()
    if data:
        print("Login")
        return [True,"Login Successful"]
    else:
        print("error")
        return[False,"Login Failed"]

def dbregister(name,username,email,dob,password):
    
    if not(name and username and email and password ):
        return [False,"Please complete all feilds"]
    
    print(name,username,email,dob,password)

    c.execute("select * from Doctor where username=?",(username,))
    data = c.fetchone()
    if not data:
        c.execute("insert into Doctor (name,username,email,dob,password) values(?,?,?,?,?)",(name,username,email,dob,password))
        print("Registration successful")
        conn.commit()
        return [True,"Registration successful"]

    else:
        print("Doctor Already Registered")
        return [1,"Doctor Already Registered"]
    
def Reset_Password(Email, dob, password, password2):
    if not (Email and dob and password and password2):
        return [False, "Please complete all fields"]

    c.execute("SELECT * FROM Doctor WHERE email=? AND dob=?", (Email, dob))
    data = c.fetchone()

    if data:
        if password == password2:
            c.execute("UPDATE Doctor SET password=? WHERE email=? AND dob=?", (password, Email, dob))
            conn.commit()
            return [True, "Password reset successful"]
        else:
            return [False, "Passwords do not match"]
    else:
        return [False, "Incorrect email or date of birth"]