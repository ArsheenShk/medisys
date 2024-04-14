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
    print(name,username,email,dob,password)
    c.execute("insert into Doctor (name,username,email,dob,password) values(?,?,?,?,?)",(name,username,email,dob,password))
    print("Registration successful")
    conn.commit()
