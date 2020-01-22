import sqlite3
con=sqlite3.connect("database35.db")
#con.execute("create table database35(PIN int primary key,NAME char(20),ACCOUNT_NO char(20),AMOUNT int);")
#con.execute("insert into database35(PIN,NAME,ACCOUNT_NO,AMOUNT)values(1111,'Mohit','8010092899',1000)")

#for i in data:
#    pin=i[0]
#    name=i[1]
#    acc_no=i[2]
#    amt=i[3]
#    print("PIN             :",i[0])
#    print("Name            :",i[1])
#    print("Account No.     :",i[2])
#    print("Amount          :",i[3])
con.commit()









def balance_enquiry():
    print("Balance Enquiry")
    root=Tk()
    root.title("ATM")
    f11=Canvas(root,bg="grey",bd=1,relief="solid",height=150,width=600)
    data=con.execute("select * from database35")
    for i in data:
        pin=i[0]
        name=i[1]
        acc_no=i[2]
        amt=i[3]
        #print("PIN         = ",i[0])
        #print("Name        = ",i[1])
        #print("Account No. = ",i[2])
        #print("Amount      = ",i[3])
    Label(f11,text="Name:       ",bg="grey",fg="black",borderwidth=1,relief="solid",width=14).place(x=180,y=30)
    Label(f11,text="Account No: ",bg="grey",fg="black",borderwidth=1,relief="solid",width=14).place(x=180,y=60)
    Label(f11,text="Amount:     ",bg="grey",fg="black",borderwidth=1,relief="solid",width=14).place(x=180,y=90)
    e1=Entry(f11,bd=1,relief="solid")
    e2=Entry(f11,bd=1,relief="solid")
    e3=Entry(f11,bd=1,relief="solid")
    Button(f11,bd=1,relief="solid",text="OK",bg="grey",fg="black",command=root.destroy).place(x=247,y=120)
    e1.insert(10,name)
    e2.insert(10,acc_no)
    e3.insert(10,amt)
    e1.place(x=281,y=30)
    e2.place(x=281,y=60)
    e3.place(x=281,y=90)
    f11.pack()
    root.mainloop()




def deposit():
    print("Deposit")
    data=con.execute("select * from database35")
    for i in data:
        amt=i[3]
    print(amt)
    root=Tk()
    root.title("ATM")
    dep1=IntVar()
    f2=Canvas(root,bg="grey",bd=1,relief="solid",height=130,width=600)
    Label(f2,text="Enter amount: ",bg="grey",fg="black",borderwidth=1,relief="solid",width=14).place(x=180,y=30)
    Entry(f2,bd=1,relief="solid",textvar=dep1).place(x=281,y=30)
    Button(f2,bd=1,relief="solid",text="Submit",bg="grey",fg="black",command=deposit_message).place(x=247,y=60)
    dep1=dep1.get()
    #con.execute("UPDATE database35 SET Amount = amt+dep1 where Pin = 1111")
    f2.pack()
    
    root.mainloop()

    

def deposit_message():
    
    from tkinter import messagebox
    messagebox.showinfo("Success","Deposit Successful")

    

    

def withdrawl():
    print("Withdrawl")
    data=con.execute("Select * from database35")
    for i in data:
        amt=i[3]
    print(amt)
    with1=IntVar()
    root=Tk()
    root.title("ATM")
    f3=Canvas(root,bg="grey",bd=1,relief="solid",height=130,width=600)
    Label(f3,text="Enter amount: ",bg="grey",fg="black",borderwidth=1,relief="solid",width=14).place(x=180,y=30)
    Entry(f3,bd=1,relief="solid",textvar=with1).place(x=281,y=30)
    Button(f3,bd=1,relief="solid",text="Submit",bg="grey",fg="black",command=receipt_initial).place(x=247,y=60)
    f3.pack()
    new_amt=amt+with1.get()
    #con.execute("update database35 set AMOUNT=new_amt where PIN=1111")
    root.mainloop()


def receipt_initial():
    root=Tk()
    root.title("ATM")
    f5=Canvas(root,bg="grey",bd=1,relief="solid",height=130,width=600)
    Label(f5,text="Do you want to print receipt???",bg="grey",borderwidth=1,relief="solid",width=28).place(x=180,y=30)
    Button(f5,bd=1,relief="solid",text="Yes",bg="grey",fg="black",command=receipt).place(x=200,y=60)
    Button(f5,bd=1,relief="solid",text="No",bg="grey",fg="black",command=withdrawl_message).place(x=350,y=60)
    f5.pack()
    root.mainloop()

    

def receipt():
    root=Tk()
    root.title("ATM")
    print("Withdrawl\n 1000")
    f6=Canvas(root,bg="grey",bd=1,relief="solid",height=130,width=600)
    Label(f6,text="Withdrawl Successful !!",bg="grey",fg="black",borderwidth=1,relief="solid",width=20).place(x=180,y=30)
    Button(f6,bd=1,relief="solid",text="OK",bg="white",fg="black",command=submit).place(x=240,y=60)
    #con.execute("select ACCOUNT_NO from database35 where PIN=1111")
    f6.pack()
    root.mainloop()
    


def withdrawl_message():
    root=Tk()
    root.title("ATM")
    f4=Canvas(root,bg="grey",bd=1,relief="solid",height=130,width=600)
    Label(f4,text="Withdrawl Successful !!",bg="grey",fg="black",borderwidth=1,relief="solid",width=20).place(x=180,y=30)
    Button(f4,bd=1,relief="solid",text="OK",bg="white",fg="black",command=submit).place(x=240,y=60)

    f4.pack()
    root.mainloop()


    '''
    from tkinter import messagebox
    messagebox.showinfo("Success","Withdrawl Successful")
    '''





def pin_change():
    print("Pin change")
    root=Tk()
    root.title("ATM")
    pin1=IntVar()
    pin2=IntVar()
    pin3=IntVar()
    data=con.execute("select * from database35")
    for i in data:
        pin=i[0]
    f4=Canvas(root,bg="grey",bd=1,relief="solid",height=130,width=600)
    Label(f4,text="Old PIN: ",bg="grey",fg="black",borderwidth=1,relief="solid",width=14).place(x=180,y=30)
    Label(f4,text="New PIN: ",bg="grey",fg="black",borderwidth=1,relief="solid",width=14).place(x=180,y=48)
    Label(f4,text="Re-Enter PIN: ",bg="grey",fg="black",borderwidth=1,relief="solid",width=14).place(x=180,y=66)
    Entry(f4,bd=1,relief="solid",textvar=pin1).place(x=281,y=30)
    Entry(f4,bd=1,relief="solid",textvar=pin2).place(x=281,y=48)
    Entry(f4,bd=1,relief="solid",textvar=pin3).place(x=281,y=66)
    Button(f4,bd=1,relief="solid",text="Submit",bg="white",fg="black",width=16,command=pin_submit1).place(x=281,y=90)
    #data=con.execute("select * from database35")
    #con.execute("update database35 set PIN=? where PIN=?",[pin2.get(),pin1.get()])
    #print("abcd",pin)
    f4.pack()
    '''
    if pin2.get()==pin3.get() and pin==pin1.get():
        print("Possible")
        pin_submit1()
    else:
        print("Not possible")
        pin_submit2()'''
    root.mainloop()


def pin_submit1():
    #con.execute("update database35 set AMOUNT=new_amt where PIN=1111")
    from tkinter import messagebox
    messagebox.showinfo("PIN CHANGE","PIN Change Successful")

    
def pin_submit2():
    from tkinter import messagebox
    messagebox.showinfo("PIN CHANGE","PIN does not match")
    
          


def submit():
    pin_enter=ch.get()
    data=con.execute("select * from database35")
    for i in data:
        pin=i[0]
    print(pin)
    if int(pin_enter)==pin and len(pin_enter)==4:
        root=Tk()
        root.title("ATM")
        f=Canvas(root,bd=1,relief="solid",height=130,width=600)
        var1=IntVar()
        Radiobutton(f,text="Balance Enquiry",bg="grey",fg="black",borderwidth=1,relief="solid",command=balance_enquiry,value=1,width=14,variable=var1).place(x=180,y=30)
        Radiobutton(f,text="Deposit",bg="grey",fg="black",borderwidth=1,relief="solid",command=deposit,value=2,width=14,variable=var1).place(x=300,y=30)
        Radiobutton(f,text="Withdrawl",bg="grey",fg="black",borderwidth=1,relief="solid",command=withdrawl,value=3,width=14,variable=var1).place(x=180,y=70)
        Radiobutton(f,text="PIN Change",bg="grey",fg="black",borderwidth=1,relief="solid",command=pin_change,value=4,width=14,variable=var1).place(x=300,y=70)
        f.pack()
        root.mainloop()
    else:
        from tkinter import messagebox
        messagebox.showerror("ERROR!!","Invalid PIN\n Please Check")
    


from tkinter import *
root=Tk()
root.title("ATM")
#root.geometry('960x320')
ch=StringVar()
c1=Canvas(root,bd=1,relief="solid",height=360,width=920)
photo=PhotoImage(file="aaa.gif")
c1.create_image(920,360,image=photo,anchor=SE)
Label(c1,text="Enter PIN:",bg="white",fg="black",borderwidth=1,relief="solid",width=14).place(x=260,y=150)
Entry(c1,bd=1,relief="solid",textvar=ch,show='*').place(x=340,y=150)
Button(c1,bd=1,relief="solid",text="Submit",bg="white",fg="black",width=16,command=submit).place(x=300,y=180)
c1.pack()
root.mainloop()




