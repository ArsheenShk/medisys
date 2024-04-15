import sqlite3

conn = sqlite3.connect('patients.db')
c = conn.cursor()

# Creating a table to store user information if it doesn't exist already
c.execute('''CREATE TABLE IF NOT EXISTS Patient (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            bloodG TEXT NOT NULL,
            dob TEXT NOT NULL,
            aadhar TEXT NOT NULL,
            address TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT NOT NULL
            )''')
conn.commit()


def Patient_register(name,bloodG,dob,aadhar,address,phone,email):
    print(name,bloodG,dob,aadhar,address,phone,email)
    c.execute("select * from Patient where aadhar=?",(aadhar,))
    data = c.fetchone()
    if not data: 
        c.execute("insert into Patient (name,bloodG,dob,aadhar,address,phone,email) values(?,?,?,?,?,?,?)",(name,bloodG,dob,aadhar,address,phone,email))
        print("Registration successful")
        conn.commit()
        return [1,"Registration successful"]

    else:
        print("Patient Already Registered")
        return [1,"Patient Already Registered"]
    
# Patient_register('Dp',"B+","22-06-2002",'123456789123',"Jalgaon","1234567890","Dp@gmail.com")
def Patient_login(aadhar,id):
    print(aadhar)
    print(id)
    c.execute("select * from Patient where aadhar=? and id=?",(aadhar,id))
    data = c.fetchone()
    if data:
        print("Login")
        return [1,"Login Successful"]
    else:
        print("error")
        return[0,"Login Failed"]

# Patient_login("123456789123","1")

def create_patient_db(id):
    conn = sqlite3.connect(id+'.db')
    c = conn.cursor()

create_patient_db("123")