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


def create_patient_table(aadhar):
    str(aadhar)
    query=f'''CREATE TABLE IF NOT EXISTS P{aadhar} (
    id int PRIMARY KEY, 
    ttf TEXT NOT NULL,
    medicine TEXT NOT NULL,
    appointment TEXT NOT NULL,
    fees TEXT NOT NULL
    )'''
    c.execute(query)
    conn.commit()

def save_data(disease,medicine,next_date,fees,aadhar):
    query = "INSERT INTO P"+aadhar+" (ttf,medicine,appointment,fees) values (?,?,?,?)"
    try:
        c.execute(query,(disease,medicine,next_date,fees))
        conn.commit()
        return [True,"Data Saved Successful"]
    except:
        return [False,"Something went wrong please login again..."]

def get_dates(aadhar):
    query = "select appointment from P"+aadhar
    c.execute(query)
    tuple_list=c.fetchall()
    # print(dates)
    dates=[]
    
    for tp_i in tuple_list:
        dates.append(tp_i[0])
    conn.commit()

    return dates
# get_dates("123456789123")   

def get_data(aadhar,date):
    query="select * from P"+aadhar+" where appointment=?"
    c.execute(query,(date,))
    data=(c.fetchall())[0]
    print(data)
    conn.commit()
    return data
# get_data("123456789123","12-12-2025")   

def Patient_register(name,bloodG,dob,aadhar,address,phone,email):
    print(name,bloodG,dob,aadhar,address,phone,email)
    create_patient_table(aadhar)

    c.execute("select * from Patient where aadhar=?",(aadhar,))
    data = c.fetchone()
    if not data: 
        c.execute("insert into Patient (name,bloodG,dob,aadhar,address,phone,email) values(?,?,?,?,?,?,?)",(name,bloodG,dob,aadhar,address,phone,email))
        print("Registration successful")
        conn.commit()
        return [True,"Registration successful"]

    else:
        print("Patient Already Registered")
        return [True,"Patient Already Registered"]
    
# Patient_register('Dp',"B+","22-06-2002",'123456789123',"Jalgaon","1234567890","Dp@gmail.com")
def Patient_login(aadhar,id):
    print(aadhar)
    print(id)
    c.execute("select * from Patient where aadhar=? and id=?",(aadhar,id))
    data = c.fetchone()
    if data:
        print("Login")
        return [True,"Login Successful"]
    else:
        print("error")
        return[False,"Login Failed"]

# Patient_login("123456789123","1")


# create_patient_table(12333)
# c.execute("drop table ")
# conn.commit()