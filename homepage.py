from tkinter import *
from PIL import ImageTk,Image
from tkcalendar import DateEntry
from tkinter import messagebox
from homepageDB import*
def message(l):
        choice,msg=l[0],l[1]
        if choice:
            messagebox.showinfo("Success",msg)
            return True
        else:
            messagebox.showerror("Error",msg)
            return False
def verify(aadhar,id):
    l = Patient_login(aadhar,id)
    if message(l):
        close_frame()
        show_info()

def close_frame():
    try:
        frame.destroy()
    except:
        print("Frame 1 error....")

def close_frame2():
    try:
        frame2.destroy()
    except:
        print("Frame 2 error....")
def new_frame():
    global frame
    frame=Frame(hp_window,height=660,width=990)
    frame.place(x=0,y=0)

    img = Image.open('frame_bg.jpg')  

    
    img=ImageTk.PhotoImage(img)
    # Create a label widget to display the image
    label = Label(frame, image=img)
    label.image = img  # reference to avoid garbage collection

    label.pack()

#TREATMENT FUNCTION
def treatment():
    new_frame()
    close_frame2()
    
    # frame.configure()
    close_bt=Button(frame,text="❌",cursor='hand2',font=('Montsterrat',12,'bold') ,relief=FLAT, bg="white",fg='red', command=close_frame)
    close_bt.place(x=880,y=30)
    
    #heading
    heading=Label(frame,text='PATIENT LOGIN',font=('Montsterrat',25,'bold'),bg='white',fg='lime green')
    heading.place(x=140,y=130)
    #name label
    label1= Label(frame,text="Aadhar No:",font=('Montsterrat',16,'bold'),bd=0,bg='white',fg='navy')
    label1.place(x=140,y=230)
    #name entry
    aadhar=Entry(frame,width=22,font=('Montsterrat',14),bd=1,bg='white',fg='navy')
    aadhar.place(x=140,y=260)
    #pateint ID label
    label2= Label(frame,text="PATIENT ID:",font=('Montsterrat',16,'bold'),bd=0,bg='white',fg='navy')
    label2.place(x=140,y=330)
    #patientID entry
    P_Id=Entry(frame,width=22,font=('Montsterrat',14),bd=1,fg='navy')
    P_Id.place(x=140,y=360)
    #login button
    loginbutton=Button(frame,width=19,bd=0,text='LOGIN',font=('Montsterrat',16,'bold'),
                        fg='white',bg='lime green',cursor='hand2',activeforeground='white',activebackground='lime green',
                        command=lambda:verify(aadhar.get(),P_Id.get()))
    loginbutton.place(x=135,y=430)

#VIEW RECORD FUNCTION
def view():
    new_frame()
    
    # frame.configure()
    close_bt=Button(frame,text="❌",cursor='hand2',font=('Montsterrat',12,'bold') ,relief=FLAT, bg="white",fg='red', command=close_frame)
    close_bt.place(x=880,y=30)
    
    #heading
    heading=Label(frame,text='PATIENT LOGIN',font=('Montsterrat',25,'bold'),bg='white',fg='lime green')
    heading.place(x=140,y=130)
    #name label
    label1= Label(frame,text="Aadhar No:",font=('Montsterrat',16,'bold'),bd=0,bg='white',fg='navy')
    label1.place(x=140,y=230)
    #name entry
    name=Entry(frame,width=22,font=('Montsterrat',14),bd=1,bg='white',fg='navy')
    name.place(x=140,y=260)
    #pateint ID label
    label2= Label(frame,text="PATIENT ID:",font=('Montsterrat',16,'bold'),bd=0,bg='white',fg='navy')
    label2.place(x=140,y=330)
    #patientID entry
    P_Id=Entry(frame,width=22,font=('Montsterrat',14),bd=1,fg='navy')
    P_Id.place(x=140,y=360)
    #login button
    viewbutton=Button(frame,width=19,bd=0,text='VIEW RECORD',font=('Montsterrat',16,'bold'),
                        fg='white',bg='lime green',cursor='hand2',activeforeground='white',activebackground='lime green',command=show_info)
    viewbutton.place(x=135,y=430)


#UPDATE RECORD FUNCTION
def update():
    new_frame()
    
    # frame.configure()
    close_bt=Button(frame,text="❌",cursor='hand2',font=('Montsterrat',12,'bold') ,relief=FLAT, bg="white",fg='red', command=close_frame)
    close_bt.place(x=880,y=30)
    
    #heading
    heading=Label(frame,text='PATIENT LOGIN',font=('Montsterrat',25,'bold'),bg='white',fg='lime green')
    heading.place(x=140,y=130)
    #name label
    label1= Label(frame,text="Aadhar No:",font=('Montsterrat',16,'bold'),bd=0,bg='white',fg='navy')
    label1.place(x=140,y=230)
    #name entry
    name=Entry(frame,width=22,font=('Montsterrat',14),bd=1,bg='white',fg='navy')
    name.place(x=140,y=260)
    #pateint ID label
    label2= Label(frame,text="PATIENT ID:",font=('Montsterrat',16,'bold'),bd=0,bg='white',fg='navy')
    label2.place(x=140,y=330)
    #patientID entry
    P_Id=Entry(frame,width=22,font=('Montsterrat',14),bd=1,fg='navy')
    P_Id.place(x=140,y=360)
    #login button
    updatebutton=Button(frame,width=19,bd=0,text='UPDATE RECORD',font=('Montsterrat',16,'bold'),
                        fg='white',bg='lime green',cursor='hand2',activeforeground='white',activebackground='lime green')
    updatebutton.place(x=135,y=430)





#NEW PATEINT FUNCTION
def new_frame2():
    global frame2
    frame2=Frame(hp_window,height=660,width=990)
    frame2.place(x=0,y=0)
    img = Image.open('np_bg.jpg')  
 
    img=ImageTk.PhotoImage(img)
    # Create a label widget to display the image
    label = Label(frame2, image=img)
    label.image = img  # reference to avoid garbage collection

    label.pack()

def new_patient():
    new_frame2()

    close_bt=Button(frame2,text="❌",cursor='hand2',font=('Montsterrat',12,'bold') ,relief=FLAT, bg="white",fg='red', command=close_frame2)
    close_bt.place(x=900,y=55)
   
#heading
    heading2=Label(frame2,text='PATIENT DETAILS',font=('Montsterrat',25,'bold'),bg='white',fg='lime green')
    heading2.place(x=350,y=75)
##name entry
    #name label
    label3= Label(frame2,text="NAME OF THE PATIENT:",font=('Montsterrat',14,'bold'),bd=0,bg='white',fg='navy')
    label3.place(x=100,y=150)
    #name entry
    name2=Entry(frame2,width=22,font=('Montsterrat',14),bd=1,bg='white',fg='navy')
    name2.place(x=100,y=175)
    #dob label
    label4= Label(frame2,text="DATE OF BIRTH:",font=('Montsterrat',14,'bold'),bd=0,bg='white',fg='navy')
    label4.place(x=100,y=230)
    #dob entry
    dob=DateEntry(frame2, date_pattern='yyyy-mm-dd', firstweekday='sunday',
                        locale='en_US', width=20,font=('Montsterrat',14),bd=1,bg='white',fg='navy')
    dob.place(x=100,y=255)
     #address label
    label5= Label(frame2,text="ADDRESS:",font=('Montsterrat',14,'bold'),bd=0,bg='white',fg='navy')
    label5.place(x=100,y=310)
     #address entry
    add=Entry(frame2,width=22,font=('Montsterrat',14),bd=1,fg='navy')
    add.place(x=100,y=335)
    #phone label
    label6= Label(frame2,text="PHONE NO:",font=('Montsterrat',14,'bold'),bd=0,bg='white',fg='navy')
    label6.place(x=100,y=390)
    #phone entry
    phone=Entry(frame2,width=22,font=('Montsterrat',14),bd=1,fg='navy')
    phone.place(x=100,y=415)
    #EmailID
    label7= Label(frame2,text="EMAIL ID:",font=('Montsterrat',14,'bold'),bd=0,bg='white',fg='navy')
    label7.place(x=100,y=470)
    #email entry
    email_id=Entry(frame2,width=22,font=('Montsterrat',14),bd=1,fg='navy')
    email_id.place(x=100,y=495)
    
    #bloodgroup
    label8= Label(frame2,text="BLOOD GROUP:",font=('Montsterrat',14,'bold'),bd=0,bg='white',fg='navy')
    label8.place(x=600,y=150)
    #bg entry
    b_grp=Entry(frame2,width=22,font=('Montsterrat',14),bd=1,fg='navy')
    b_grp.place(x=600,y=175)
    #medicine name
    label9= Label(frame2,text="Aadhar No",font=('Montsterrat',14,'bold'),bd=0,bg='white',fg='navy')
    label9.place(x=600,y=230)
    #med  entry
    a_name=Entry(frame2,width=22,font=('Montsterrat',14),bd=1,fg='navy')
    a_name.place(x=600,y=255)
    # #total fee
    # label10= Label(frame2,text="TOTAL FEE:",font=('Montsterrat',14,'bold'),bd=0,bg='white',fg='navy')
    # label10.place(x=600,y=310)
    # #entry
    # total=Entry(frame2,width=22,font=('Montsterrat',14),bd=1,fg='navy')
    # total.place(x=600,y=335)
    #Next appointment
    # label11=Label(frame2,text="NEXT APPOINTMENT DATE:",font=('Montsterrat',14,'bold'),bd=0,bg='white',fg='navy')
    # label11.place(x=600,y=390)
    # #entry
    # next_date=Entry(frame2,width=22,font=('Montsterrat',14),bd=1,fg='navy')
    # next_date.place(x=600,y=415)
    #add pateint BUTTON
    addbutton=Button(frame2,width=19,bd=0,text='ADD PATIENT',font=('Montsterrat',16,'bold'),
                        fg='white',bg='lime green',cursor='hand2',activeforeground='white',activebackground='lime green',command=treatment)
    addbutton.place(x=620,y=480)

def show_info():
    new_frame2()

    close_bt=Button(frame2,text="❌",cursor='hand2',font=('Montsterrat',12,'bold') ,relief=FLAT, bg="white",fg='red', command=close_frame2)
    close_bt.place(x=900,y=55)
   
    #heading
    heading2=Label(frame2,text='PATIENT DETAILS',font=('Montsterrat',25,'bold'),bg='white',fg='lime green')
    heading2.place(x=350,y=75)
    ##name entry
    #name label
    label3= Label(frame2,text="TREATMENT TAKEN FOR:",font=('Montsterrat',14,'bold'),bd=0,bg='white',fg='navy')
    label3.place(x=100,y=150)
    #name entry
    disease=Entry(frame2,width=22,font=('Montsterrat',14),bd=1,bg='white',fg='navy')
    disease.place(x=100,y=175)
    #dob label
    # label4= Label(frame2,text="DATE OF BIRTH:",font=('Montsterrat',14,'bold'),bd=0,bg='white',fg='navy')
    # label4.place(x=100,y=230)
    # #dob entry
    # dob=DateEntry(frame2, date_pattern='yyyy-mm-dd', firstweekday='sunday',
    #                     locale='en_US', width=20,font=('Montsterrat',14),bd=1,bg='white',fg='navy')
    # dob.place(x=100,y=255)
    #  #address label
    # label5= Label(frame2,text="ADDRESS:",font=('Montsterrat',14,'bold'),bd=0,bg='white',fg='navy')
    # label5.place(x=100,y=310)
    #  #address entry
    # add=Entry(frame2,width=22,font=('Montsterrat',14),bd=1,fg='navy')
    # add.place(x=100,y=335)
    # #phone label
    # label6= Label(frame2,text="PHONE NO:",font=('Montsterrat',14,'bold'),bd=0,bg='white',fg='navy')
    # label6.place(x=100,y=390)
    # #phone entry
    # phone=Entry(frame2,width=22,font=('Montsterrat',14),bd=1,fg='navy')
    # phone.place(x=100,y=415)
    # #EmailID
    # label7= Label(frame2,text="EMAIL ID:",font=('Montsterrat',14,'bold'),bd=0,bg='white',fg='navy')
    # label7.place(x=100,y=470)
    # #email entry
    # email_id=Entry(frame2,width=22,font=('Montsterrat',14),bd=1,fg='navy')
    # email_id.place(x=100,y=495)
    
    # #bloodgroup
    # label8= Label(frame2,text="BLOOD GROUP:",font=('Montsterrat',14,'bold'),bd=0,bg='white',fg='navy')
    # label8.place(x=600,y=150)
    # #bg entry
    # b_grp=Entry(frame2,width=22,font=('Montsterrat',14),bd=1,fg='navy')
    # b_grp.place(x=600,y=175)
    # #medicine name
    # label9= Label(frame2,text="Aadhar No",font=('Montsterrat',14,'bold'),bd=0,bg='white',fg='navy')
    # label9.place(x=600,y=230)
    # #med  entry
    # a_name=Entry(frame2,width=22,font=('Montsterrat',14),bd=1,fg='navy')
    # a_name.place(x=600,y=255)
    
    savebutton=Button(frame2,width=19,bd=0,text='Save',font=('Montsterrat',16,'bold'),
                        fg='white',bg='lime green',cursor='hand2',activeforeground='white',activebackground='lime green',command=treatment)
    savebutton.place(x=620,y=480)
    

def homepage():
    global hp_window
    hp_window=Tk()
    hp_window.title("HomePage")
    hp_window.geometry('990x660')
    img2=ImageTk.PhotoImage(file='homepage-01.jpg')
    bglabel=Label(hp_window,image=img2)
    bglabel.grid(row=0,column=0)

    #BUTTONS
    treatmentbutton=Button(hp_window,text='Patient Treatment',activebackground='white',cursor='hand2',
                            font=('Montsterrat',20,'bold'),fg='white',bd=0,bg='lime green',activeforeground='LIME GREEN',
                            command=treatment)
    treatmentbutton.place(x=385,y=170)

    newbutton=Button(hp_window,text='NEW PATEINT',activebackground='white',cursor='hand2',
                            font=('Montsterrat',20,'bold'),fg='white',bd=0,bg='lime green',activeforeground='LIME GREEN',
                            command=new_patient)
    newbutton.place(x=420,y=250)

    viewbutton=Button(hp_window,text='VIEW RECORD',activebackground='white',cursor='hand2',
                            font=('Montsterrat',20,'bold'),fg='white',bd=0,bg='lime green',activeforeground='LIME GREEN',command=view)
    viewbutton.place(x=420,y=330)

    updatebutton=Button(hp_window,text='UPDATE RECORD',activebackground='white',cursor='hand2',
                            font=('Montsterrat',20,'bold'),fg='white',bd=0,bg='lime green',activeforeground='LIME GREEN',command=update)
    updatebutton.place(x=395,y=410)

    hp_window.mainloop()




