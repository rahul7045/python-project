import backend
import sqlite3
from tkinter import *
from PIL import ImageTk, Image
import os
import tkinter.messagebox
from tkinter import messagebox



class Student:
	def __init__(self,root):
		self.root=root
		self.root.title("Hospital Management")
		self.root.geometry("1350x600+0+0")
		self.root.resizable(0,0)

		patid=StringVar()
		patfn=StringVar()
		patln=StringVar()
		patdob=StringVar()
		patage=StringVar()
		patgender=StringVar()
		patadd=StringVar()
		patmob=StringVar()
		patdr=StringVar()

		def iexit():
			iexit=tkinter.messagebox.askyesno("Hospital Management ","confirm Yes or no")
			if iexit>0:
				root.destroy()
			return

		def cleardata():
			self.txtpatid.delete(0,END)
			self.txtpatfn.delete(0,END)
			self.txtpatln.delete(0,END)
			self.txtpatage.delete(0,END)
			self.txtpatdr.delete(0,END)
			self.txtpatgender.delete(0,END)
			self.txtpatadd.delete(0,END)
			self.txtpatmob.delete(0,END)


	#***************************************************************Functions************************************************************************#

			
		def addd():
			if(len(patid.get())!=0):
				backend.add(patid.get(), patfn.get(),patln.get(),patdr.get(),patage.get(),patgender.get(),patadd.get() ,patmob.get(),patdr.get())
			messagebox.showinfo("information","Added Succesfully")  

		def create_window():
			newwin = Toplevel(root)
			newwin.geometry("1200x500+0+0")
			display1=Label(newwin,font=('arial',20),text="RAJESH SUPERSPECIALITY HOSPITAL",bg="green")
			display1.pack()
			
			con=sqlite3.connect("data.db")
			cur=con.cursor()
			cur.execute("SELECT * FROM data")
			rows=cur.fetchall()
			for row in rows:
				display77=Label(newwin,font=('arial',20),text=row)
				display77.pack()
				
			con.close()
		def create_window1():
			newwin1 = Toplevel(root)
			display1=Label(newwin1,font=('arial',20),text="RAJESH SUPERSPECIALITY HOSPITAL",bg="green")
			display1.pack()
			if(len(patfn.get()!=0)):
				display456=Label(newwin1,font=('arial',20),text=backend.search())
				display456.pack()
		def dele():
			if(len(patid.get()!=0)):
				backend.delete()


				
				
			








	#***************************************************************Frame************************************************************************#
		MainFrame=Frame(root,bg="cadet blue")
		MainFrame.grid()

		TitleFrame=Frame(MainFrame,bd=3,padx=34,pady=8,bg="white",relief=RIDGE)
		TitleFrame.pack(side=TOP)

		self.lbltit=Label(TitleFrame,font=('arial',47),text="RAJESH SUPERSPECIALITY HOSPITAL")
		self.lbltit.grid()

		ButtonFrame=Frame(MainFrame,bd=3,width=1350,height=70,padx=18,pady=10,bg="white",relief=RIDGE)
		ButtonFrame.pack(side=BOTTOM)

		DataFrame=Frame(MainFrame,bd=1,width=1300,height=400,padx=20,pady=20,bg="light blue",relief=RIDGE)
		DataFrame.pack(side=BOTTOM)

		DataleftFrame=LabelFrame(DataFrame,bd=1,width=1000,height=600,padx=20,bg="white",relief=RIDGE,font=('arial',20,'bold'),text="Patient information")
		DataleftFrame.pack(side=LEFT)

	#***************************************************************Labels and entry************************************************************************#

		self.lblpatid=Label(DataleftFrame,font=('arial',20),text="Patient id",padx=2,pady=2,bg="white")
		self.lblpatid.grid(row=0,column=0,sticky=W)
		self.txtpatid=Entry(DataleftFrame,font=('arial',20),textvariable=patid,width=39)
		self.txtpatid.grid(row=0,column=1)
		self.txtpatid.bind('<Return>', lambda e: self.txtpatfn.focus_set())

		self.lblpatfn=Label(DataleftFrame,font=('arial',20),text="First Name",padx=2,pady=2,bg="white")
		self.lblpatfn.grid(row=1,column=0,sticky=W)
		self.txtpatfn=Entry(DataleftFrame,font=('arial',20),textvariable=patfn,width=39)
		self.txtpatfn.grid(row=1,column=1)
		self.txtpatfn.bind('<Return>', lambda e: self.txtpatln.focus_set())

		self.lblpatln=Label(DataleftFrame,font=('arial',20),text="Patient Last Name",padx=2,pady=2,bg="white")
		self.lblpatln.grid(row=2,column=0,sticky=W)
		self.txtpatln=Entry(DataleftFrame,font=('arial',20),textvariable=patln,width=39)
		self.txtpatln.grid(row=2,column=1)
		self.txtpatln.bind('<Return>', lambda e: self.txtpatdr.focus_set())
			
		#self.lblpatdob=Label(DataleftFrame,font=('arial',20),text="date of birth",padx=2,pady=2,bg="blue")
		#self.lblpatdob.grid(row=3,column=0,sticky=W)
		#self.txtpatdob=Entry(DataleftFrame,font=('arial',20),textvariable=patdob,width=39)
		#self.txtpatdob.grid(row=3,column=1)

		self.lblpatdr=Label(DataleftFrame,font=('arial',20),text="Dr. Assigned",padx=2,pady=2,bg="white")
		self.lblpatdr.grid(row=3,column=0,sticky=W)
		self.txtpatdr=Entry(DataleftFrame,font=('arial',20),textvariable=patdr,width=39)
		self.txtpatdr.grid(row=3,column=1)


		self.lblpatage=Label(DataleftFrame,font=('arial',20),text="Patient age",padx=2,pady=2,bg="white")
		self.lblpatage.grid(row=4,column=0,sticky=W)
		#self.txtpatage=Entry(DataleftFrame,font=('arial',20),textvariable=patage,width=39)
		self.txtpatage=Spinbox(DataleftFrame,from_=0, to=100,font=('arial',20),textvariable=patage,width=38)
		self.txtpatage.grid(row=4,column=1)
		self.txtpatage.bind('<Return>', lambda e: self.txtpatgender.focus_set())
			
		self.lblpatgender=Label(DataleftFrame,font=('arial',20),text="gender",padx=2,pady=2,bg="white")
		self.lblpatgender.grid(row=5,column=0,sticky=W)
		self.txtpatgender=Spinbox(DataleftFrame,font=('arial',20),values=("NULL","Male","Female"),textvariable=patgender,width=38)
		self.txtpatgender.grid(row=5,column=1)
		

		self.txtpatgender.bind('<Return>', lambda e: self.txtpatadd.focus_set())
			
		self.lblpatadd=Label(DataleftFrame,font=('arial',20),text="address",padx=2,pady=2,bg="white")
		self.lblpatadd.grid(row=6,column=0,sticky=W)
		self.txtpatadd=Entry(DataleftFrame,font=('arial',20),textvariable=patadd,width=39)
		self.txtpatadd.grid(row=6,column=1)
		self.txtpatadd.bind('<Return>', lambda e: self.txtpatmob.focus_set())

		self.lblpatmob=Label(DataleftFrame,font=('arial',20),text="Mobile number",padx=2,pady=2,bg="white")
		self.lblpatmob.grid(row=7,column=0,sticky=W)
		self.txtpatmob=Entry(DataleftFrame,font=('arial',20),textvariable=patmob,width=39)
		self.txtpatmob.grid(row=7,column=1)

	

	#***************************************************************Buttons ************************************************************************#
		b1 = Button(ButtonFrame, text="Add New",font=('arial',15),bd=4,command=lambda:[addd(),cleardata()])
		b1.grid(row=0,column=0)

		b2 = Button(ButtonFrame, text="Display",font=('arial',15),bd=4,command=create_window)
		b2.grid(row=0,column=1)

		b3 = Button(ButtonFrame, text="Clear",font=('arial',15),bd=4,command=cleardata)
		b3.grid(row=0,column=2)

		b4 = Button(ButtonFrame, text="Delete",font=('arial',15),bd=4)
		b4.grid(row=0,column=3)

		#b5 = Button(ButtonFrame, text="Search",font=('arial',15),bd=4,command=create_window1)
		#b5.grid(row=0,column=4)

		#b7 = Button(ButtonFrame, text="Update",font=('arial',15) ,bd=4)
		#b7.grid(row=0,column=4)

		b6 = Button(ButtonFrame, text="Exit",font=('arial',15),bd=4,command=iexit)
		b6.grid(row=0,column=4)

if __name__=='__main__':
	root=Tk()
	application=Student(root)
	root.mainloop()




