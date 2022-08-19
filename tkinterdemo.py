from tkinter import *
import mysql.connector
import tkinter.messagebox as msg
def create_conn():
    return mysql.connector.connect(
          host="localhost",
          user="root",
          password="",
          database="python_new",
          )
print(create_conn())
def insert_data():
    if e_fname.get()=="" or e_lname.get()=="" or e_email.get()=="" or e_mobile.get()=="":
      msg.showinfo("Insert Status","All Fields are Mandatory")
    else:
        conn=create_conn()
        cursor=conn.cursor()
        query="insert into emp(fname,lname,email,mobile) values(%s,%s,%s,%s)"
        args=(e_fname.get(),e_lname.get(),e_email.get(),e_mobile.get())
        cursor.execute(query,args)
        conn.commit()
        conn.close()
        e_fname.delete(0,'end')
        e_lname.delete(0,'end')
        e_email.delete(0,'end')
        e_mobile.delete(0,'end')
        msg.showinfo("insert Status","All data Inserted Succseefully")
def search_data():
    e_fname.delete(0,'end')
    e_lname.delete(0,'end')
    e_email.delete(0,'end')
    e_mobile.delete(0,'end')
    if e_id.get()=="":
        msg.showinfo("Search Status","Id is Mandatory For Search")
    else:
        conn=create_conn()
        cursor=conn.cursor()
        query="select * from emp where id=%s"
        args=(e_id.get(),)
        cursor.execute(query,args)
        row=cursor.fetchall()
        if row:
           for i in row:
              e_fname.insert(0,i[1])
              e_lname.insert(0,i[2])
              e_email.insert(0,i[3])
              e_mobile.insert(0,i[4])
        else:
            msg.showinfo("Search Status","No data Found")
        conn.close()
def clear_data():
    e_id.delete(0,'end')
    e_fname.delete(0,'end')
    e_lname.delete(0,'end')
    e_email.delete(0,'end')
    e_mobile.delete(0,'end')
    
def update_data():
    if e_fname.get()=="" or e_lname.get()=="" or e_email.get()=="" or e_mobile.get()=="" or e_id.get()=="":
        msg.showinfo("Update Status","All Fields are Mandatory")
    else:
        conn=create_conn()
        cursor=conn.cursor()
        query="update emp set fname=%s,lname=%s,email=%s,mobile=%s where id=%s"
        args=(e_fname.get(),e_lname.get(),e_email.get(),e_mobile.get(),e_id.get())
        cursor.execute(query,args)
        conn.commit()
        conn.close()
        e_id.delete(0,'end')
        e_fname.delete(0,'end')
        e_lname.delete(0,'end')
        e_email.delete(0,'end')
        e_mobile.delete(0,'end')
        msg.showinfo("Update Status","Data updated Successfully")
        
    

def delete_data():
    if  e_id.get()=="":
        msg.showinfo("Delete Status","ID is Mandatory")
    else:
        conn=create_conn()
        cursor=conn.cursor()
        query="delete from emp  where id=%s"
        args=(e_id.get(),)
        cursor.execute(query,args)
        conn.commit()
        conn.close()
        e_id.delete(0,'end')
        e_fname.delete(0,'end')
        e_lname.delete(0,'end')
        e_email.delete(0,'end')
        e_mobile.delete(0,'end')
        msg.showinfo("Delete Status","Data deleted Successfully")

    
root=Tk()
root.geometry("325x370")
root.title("My Tkinter Example")
root.resizable(width=False,height=False)







l_id=Label(root,text="ID")
l_id.place(x=50,y=50)

l_fname=Label(root,text="FIRST NAME")
l_fname.place(x=50,y=100)

l_lname=Label(root,text="LAST NAME")
l_lname.place(x=50,y=150)

l_email=Label(root,text="EMAIL")
l_email.place(x=50,y=200)

l_mobile=Label(root,text="MOBILE")
l_mobile.place(x=50,y=250)

e_id=Entry(root)
e_id.place(x=150,y=50)

e_fname=Entry(root)
e_fname.place(x=150,y=100)

e_lname=Entry(root)
e_lname.place(x=150,y=150)

e_email=Entry(root)
e_email.place(x=150,y=200)

e_mobile=Entry(root)
e_mobile.place(x=150,y=250)

insert=Button(root,text="INSERT",bg="black",fg="white",font=("Arial",10),command=insert_data)
insert.place(x=20,y=300)

search=Button(root,text="SEARCH",bg="black",fg="white",font=("Arial",10),command=search_data)
search.place(x=90,y=300)

update=Button(root,text="UPDATE",bg="black",fg="white",font=("Arial",10),command=update_data)
update.place(x=168,y=300)

delete=Button(root,text="DELETE",bg="black",fg="white",font=("Arial",10),command=delete_data)
delete.place(x=244,y=300)

clear=Button(root,text="CLEAR",bg="black",fg="white",font=("Arial",10),command=clear_data)
clear.place(x=130,y=330)
