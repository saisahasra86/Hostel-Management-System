from matplotlib.figure import Figure
import matplotlib.pyplot as plt 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from fpdf import FPDF
from tkPDFViewer import tkPDFViewer as kkk

from tkinter import *
import tkinter.messagebox as tmsg
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
from cryptography.fernet import Fernet

from databases.login import login

from databases.student_login_db import student_login_db
from databases.warden_login_db import warden_login_db
from databases.mess_manager_login_db import mess_manager_login_db
from databases.hostel_clerk_login_db import hostel_clerk_login_db

from databases.student_db import student_db
from databases.hostel_db import hostel_db
from databases.complaints_db import complaints_db
from databases.hostel_workers_db import hostel_workers_db
from databases.warden_db import warden_db
import os


dirn=os.path.dirname(__file__)
file = os.path.join(dirn,'AdmissionIDs.txt')


root = Tk()
root.title("hostel Management System")
root.geometry("1050x625")
root.resizable(0,0)
list_IDs=[]
file1 = open(file, 'r')
for line in file1.readlines():
	list_IDs.append(line.strip())

file1.close()
class home_page:

	@classmethod
	def pack_homepage(cls):

		cls.homepage = Frame(root, borderwidth=4, bg="light grey")
		cls.homepage.place(x=0,y=0,width=1050,height=625)

		file = os.path.join(dirn,'images/wood_background.jpg')
		cls.image = Image.open(file)
		cls.image = cls.image.resize((1050,625))
		cls.photo = ImageTk.PhotoImage(cls.image)
		cls.label = ttk.Label(cls.homepage, image = cls.photo)
		cls.label.pack(fill=BOTH, expand = YES)

		cls.title=Label(cls.homepage,text="Welcome!!",font=("times new roman",22),bg="light grey")
		cls.title.place(x=405,y=30)

		cls.title=Label(cls.homepage,text="hostel Management System, IIT Ropar",font=("times new roman",22,"bold","italic"),bg="light grey")
		cls.title.place(x=230,y=70)

		cls.title=Label(cls.homepage,text="You want to login as",font=("times new roman",20,"bold","italic"),bg="light grey")
		cls.title.place(x=340,y=140)

		cls.but0=Button(cls.homepage,text="Student",bg="Pale Turquoise", width=20,borderwidth=0,command= student_login.student_login_page)
		cls.but0.place(relx=0.45,rely=0.45,anchor=CENTER)

		cls.but1=Button(cls.homepage,text="Warden",bg="Pale Turquoise", width=20,borderwidth=0,command=warden_login.warden_login_page)
		cls.but1.place(relx=0.45,rely=0.55,anchor=CENTER)

		cls.but2=Button(cls.homepage,text="HMC Chairman",bg="Pale Turquoise", width=20,borderwidth=0,command=HMCChairman_login.HMCChairman_login_page)
		cls.but2.place(relx=0.45,rely=0.65,anchor=CENTER)

		cls.but3=Button(cls.homepage,text="Clerk",bg="Pale Turquoise", width=20,borderwidth=0,command=clerk_login.clerk_login_page)
		cls.but3.place(relx=0.45,rely=0.75,anchor=CENTER)

		cls.but4=Button(cls.homepage,text="Mess Manager",bg="Pale Turquoise", width=20,borderwidth=0,command=MessManager_login.MessManager_login_page)
		cls.but4.place(relx=0.45,rely=0.85,anchor=CENTER)

class student_login:
	
	@classmethod
	def student_login_page(cls):
		
		cls.loginStudent = Frame(root, borderwidth=4, bg="light grey")
		cls.loginStudent.place(x=0,y=0,width=1050,height=625)
		#cls.loginStudent.tkraise()
		file = os.path.join(dirn,'images/wood_background.jpg')
		cls.image = Image.open(file)
		cls.image = cls.image.resize((1050,625))
		cls.photo = ImageTk.PhotoImage(cls.image)
		cls.label = ttk.Label(cls.loginStudent, image = cls.photo)
		cls.label.pack(fill=BOTH, expand = YES)

		cls.back=Button(cls.loginStudent,text="<---",bg="Pale Turquoise", width=7,borderwidth=0,command=home_page.pack_homepage)
		cls.back.place(relx=0, rely=0.03,anchor="w")

		#username label and text entry box
		cls.usernameLabel = Label(cls.loginStudent, text="User Name",bg="Light coral",font=("Courier New",15,"bold"),fg="white").place(relx=0.35, rely=0.2,anchor=CENTER)
		cls.username=StringVar()
		cls.usernameEntry = Entry(cls.loginStudent, textvariable=cls.username).place(relx=0.5, rely=0.2,anchor=CENTER)  

		#password label and password entry box
		cls.passwordLabel = Label(cls.loginStudent,text="Password",bg="light grey").place(relx=0.35, rely=0.3,anchor=CENTER) 
		cls.password=StringVar() 
		cls.passwordEntry = Entry(cls.loginStudent, textvariable=cls.password, show='*').place(relx=0.5, rely=0.3,anchor=CENTER) 


		cls.but0=Button(cls.loginStudent,text="Login",bg="Pale Turquoise", width=20,borderwidth=0,command=cls.validate_login)
		cls.but0.place(relx=0.45, rely=0.4,anchor=CENTER)

		cls.but1=Button(cls.loginStudent,text="Sign up",bg="Pale Turquoise", width=20,borderwidth=0,command=cls.Sign_up_page)
		cls.but1.place(relx=0.45, rely=0.5,anchor=CENTER)

	@classmethod
	def validate_login(cls):
		#login validty chck
		#correct aythe student page open		

		cls.stulist = student_login_db.get_record_by_username(cls.username.get())

		if len(cls.stulist)!= 0:

			
			cls.login_stulist = login(cls.stulist[0][0], cls.stulist[0][1])
			cls.user_data = student_db.get_record_by_username(cls.stulist[0][0])
			cls.decrypted_password = cls.login_stulist.decrypt(cls.user_data[0][6])

			if(cls.decrypted_password == cls.password.get()):
				cls.user_data = student_db.get_record_by_username(cls.stulist[0][0])
				print(cls.user_data)
				cls.student_main()
			else:
				tmsg.showerror('ERROR', "Incorrect Username/Password !!!")
		else:
			tmsg.showerror('ERROR', "Incorrect Username/Password !!!")

	@classmethod
	def passs(cls,event):
		pass

	@classmethod
	def Sign_up_page(cls):

		cls.Student_signup = Frame(root, borderwidth=4, bg="light grey")
		cls.Student_signup.place(x=0,y=0,width=1050,height=625)

		file = os.path.join(dirn,'images/wood_background.jpg')
		cls.image = Image.open(file)
		cls.image = cls.image.resize((1050,625))
		cls.photo = ImageTk.PhotoImage(cls.image)
		cls.label = ttk.Label(cls.Student_signup, image = cls.photo)
		cls.label.pack(fill=BOTH, expand = YES)


		cls.back=Button(cls.Student_signup,text="<---",bg="Pale Turquoise", width=7,borderwidth=0,command=student_login.student_login_page)
		cls.back.place(relx=0, rely=0.03,anchor="w")

		cls.nameLabel = Label(cls.Student_signup, text="Name",bg="lightgrey").place(relx=0.35, rely=0.2,anchor=CENTER)
		cls.name=StringVar()
		cls.nameEntry = Entry(cls.Student_signup, textvariable=cls.name).place(relx=0.5, rely=0.2,anchor=CENTER)

		cls.usenameLabel = Label(cls.Student_signup, text="User Name",bg="lightgrey").place(relx=0.35, rely=0.3,anchor=CENTER)
		cls.usename=StringVar()
		cls.usenameEntry = Entry(cls.Student_signup, textvariable=cls.usename).place(relx=0.5, rely=0.3,anchor=CENTER) 

		cls.passwordsLabel = Label(cls.Student_signup,text="Password",bg="light grey").place(relx=0.35, rely=0.4,anchor=CENTER) 
		cls.passwords=StringVar() 
		cls.passwordsEntry = Entry(cls.Student_signup, textvariable=cls.passwords, show='*').place(relx=0.5, rely=0.4,anchor=CENTER) 


		cls.Addresslabel = Label(cls.Student_signup, text="Address",bg="lightgrey").place(relx=0.35, rely=0.5,anchor=CENTER)
		cls.T=Text(cls.Student_signup,width=25,bg="white",height=4)
		cls.T.place(relx=0.52, rely=0.55,anchor=CENTER) 
		

		cls.ContactLabel = Label(cls.Student_signup, text="Contact Number",bg="lightgrey").place(relx=0.35, rely=0.7,anchor=CENTER)
		cls.Contact=StringVar()
		cls.ContactEntry = Entry(cls.Student_signup, textvariable=cls.Contact).place(relx=0.5, rely=0.7,anchor=CENTER) 

		cls.addmission_idLabel = Label(cls.Student_signup,text="Addmission ID",bg="light grey").place(relx=0.35, rely=0.8,anchor=CENTER) 
		cls.addmission_id=StringVar() 
		cls.addmission_idEntry = Entry(cls.Student_signup, textvariable=cls.addmission_id).place(relx=0.5, rely=0.8,anchor=CENTER) 

		cls.but1=Button(cls.Student_signup,text="Sign up",bg="Pale Turquoise", width=20,borderwidth=0,command=cls.Add_details)
		cls.but1.place(relx=0.45, rely=0.9,anchor=CENTER)


	@classmethod
	def Add_details(cls):
		#database addition
		#HMC chairman

		name = cls.name.get()
		address = cls.T.get(1.0, "end-1c")
		contact_number = cls.Contact.get()
		username = cls.usename.get()
		password = cls.passwords.get()
		Addmission_ID=cls.addmission_id.get()

		if Addmission_ID in list_IDs:
			if(len(name.strip()) !=0 and  len(address.strip()) !=0  and len(contact_number.strip()) == 10 and len(username.strip()) != 0):
				if((len(password) >= 8) and ( not password.islower())):
		
					key = Fernet.generate_key().decode("utf-8")
					fernet_object = Fernet(key.encode("utf-8"))
					encrypted_password = fernet_object.encrypt(password.encode("utf-8"))

					student_db.insert_records((name,address,contact_number,username,password,key,'not alloted',0,0,'not alloted','not alloted')) 
					temptemp = student_db.get_record_by_username(username)

					student_login_db.insert_record((username,encrypted_password,temptemp[0][0]))
					tmsg.showinfo('KUDOS','Successful Signup!!!')
				else:

					tmsg.showerror('ERROR', 'Bad Password, Please make sure your password is at least 8 character long and has a caps letter')

			else:
				tmsg.showerror('ERROR','Few details empty, please fill all the details')

		else:
			tmsg.showerror('ERROR','Wrong Admission ID, please contact the Institute Administration')

	@classmethod
	def student_main(cls):

		cls.Student_main = Frame(root, borderwidth=4, bg="light grey")
		cls.Student_main.place(x=0,y=0,width=1050,height=625)

		file = os.path.join(dirn,'images/wood_background.jpg')
		cls.image = Image.open(file)
		cls.image = cls.image.resize((1050,625))
		cls.photo = ImageTk.PhotoImage(cls.image)
		cls.label = ttk.Label(cls.Student_main, image = cls.photo)
		cls.label.pack(fill=BOTH, expand = YES)


		cls.student_menu = Frame(cls.Student_main, borderwidth=4, bg="rosy brown")
		cls.student_display = Frame(cls.Student_main, borderwidth=4, bg="black")
		cls.student_menu.place(x=-2,y=-2,width=1050,height=30)
		cls.student_display.place(x=-3,y=28,width=1050,height=600)

		
		file = os.path.join(dirn,'images/wood_background.jpg')
		cls.image = Image.open(file)
		cls.image = cls.image.resize((1050,600))
		cls.photo = ImageTk.PhotoImage(cls.image)
		cls.label = ttk.Label(cls.student_display, image = cls.photo)
		cls.label.place(x=-3,y=-3,width=1048,height=600)

		cls.Make_Complaint=Button(cls.student_menu, text="Make Complaint",bg="Pale Turquoise", width=20,borderwidth=0,command=cls.make_complaint).grid(row=0,column=0,padx=10)
		cls.Clear_due=Button(cls.student_menu, text="Pay Dues",bg="Pale Turquoise", width=20,borderwidth=0,command=cls.clear_dues).grid(row=0,column=1,padx=10)
		cls.Profile=Button(cls.student_menu, text="Profile",bg="Pale Turquoise", width=20,borderwidth=0, command=cls.profile).grid(row=0,column=2,padx=10)
		cls.Logout=Button(cls.student_menu, text="Log Out",bg="Pale Turquoise", width=20,borderwidth=0, command=home_page.pack_homepage).grid(row=0,column=3,padx=10)

	@classmethod
	def make_complaint(cls):
		cls.student_makecomplaint = Frame(cls.Student_main, borderwidth=4, bg="black")
		cls.student_makecomplaint.place(x=-3,y=28,width=1050,height=600)

		file = os.path.join(dirn,'images/wood_background.jpg')
		cls.image = Image.open(file)
		cls.image = cls.image.resize((1050,600))
		cls.photo = ImageTk.PhotoImage(cls.image)
		cls.label = ttk.Label(cls.student_makecomplaint, image = cls.photo)
		cls.label.place(x=-3,y=-3,width=1048,height=600)

		cls.back_to_main=Button(cls.student_makecomplaint, text="Back to Homepage",bg="Pale Turquoise", width=20,borderwidth=0, command=cls.Back_To_Main).place(x=835,y=67)

		cls.complaint_box= Frame(cls.student_makecomplaint, borderwidth=4, bg="peach puff")
		cls.complaint_box.place(x=30,y=20,width=500,height=530)

		cls.title=Label(cls.complaint_box,text="Complaint Box",font=("times new roman",17,"bold","italic"),bg="peach puff")
		cls.title.place(x=155,y=65)

		cls.complaint=Text(cls.complaint_box,width=45,bg="white",height=10)
		cls.complaint.place(relx=0.5, rely=0.4,anchor=CENTER)

		cls.send_complaint=Button(cls.complaint_box, text="Send Complaint",bg="Pale Turquoise",height=2, width=20,borderwidth=0, command=cls.sends_complaint).place(x=155,y=337) 

		cls.ATR= Frame(cls.student_makecomplaint, borderwidth=4, bg="peach puff")
		cls.ATR.place(x=560,y=180,width=450,height=370)

		cls.title=Label(cls.ATR,text="Action Taken Report",font=("times new roman",17,"bold","italic"),bg="peach puff")
		cls.title.place(x=110,y=25)

		listbox1 = Listbox(cls.ATR,height=7,width=30,font=("Times new roman",13," "))
		listbox1.place(x=60,y=90)

	@classmethod
	def Back_To_Main(cls):
		cls.student_main()
	@classmethod
	def sends_complaint(cls):
		com = cls.complaint.get(1.0,"end-1c")
		stu_id=cls.user_data[0][0]
		stu_name=cls.user_data[0][1]
		hostel_name=cls.user_data[0][7]
		cls.hostel_list=hostel_db.get_record_by_name(hostel_name)
		war_nam=cls.hostel_list[0][9]
		cls.war_list=warden_db.get_records_by_name(war_nam)
		war_id=cls.war_list[0][0]
		complaints_db.insert_records((stu_id,stu_name,war_id,war_nam,hostel_name,com," "))
		tmsg.showinfo('KUDOS','Complaint has been registered!')
		pass
		
	@classmethod
	def clear_dues(cls):
		cls.student_clear_dues = Frame(cls.Student_main, borderwidth=4, bg="black")
		cls.student_clear_dues.place(x=-3,y=28,width=1050,height=600)

		file = os.path.join(dirn,'images/wood_background.jpg')
		cls.image = Image.open(file)
		cls.image = cls.image.resize((1050,600))
		cls.photo = ImageTk.PhotoImage(cls.image)
		cls.label = ttk.Label(cls.student_clear_dues, image = cls.photo)
		cls.label.place(x=-3,y=-3,width=1048,height=600)

		cls.pay_dues = Frame(cls.student_clear_dues, borderwidth=4, bg="peach puff")
		cls.pay_dues.place(x=200,y=90,width=410,height=400)

		cls.title=Label(cls.pay_dues,text="Your Due Amount",font=("times new roman",12,"bold"),bg="peach puff")
		cls.title.place(x=135,y=25)
		
		cls.MessChargesLabel = Label(cls.pay_dues, text="Mess Charges",bg="peach puff").place(x=5, y=75)
		cls.MessCharges=StringVar(value=cls.user_data[0][8])
		cls.MessChargesEntry = Entry(cls.pay_dues, textvariable=cls.MessCharges).place(x=200, y=75) 
		
		cls.othersChargesLabel = Label(cls.pay_dues, text="Other Charges",bg="peach puff").place(x=5, y=125)
		cls.othersCharges=StringVar(value=cls.user_data[0][9])
		cls.othersChargesEntry = Entry(cls.pay_dues, textvariable=cls.othersCharges).place(x=200, y=125) 

		cls.title=Label(cls.pay_dues,text="--------------------------------",font=("times new roman",12,"bold"),bg="peach puff")
		cls.title.place(x=180,y=145)

		cls.TotalChargesLabel = Label(cls.pay_dues, text="Total Charges",bg="peach puff").place(x=5, y=175)
		cls.TotalCharges=StringVar(value=(cls.user_data[0][8]+cls.user_data[0][9]))
		cls.TotalChargesEntry = Entry(cls.pay_dues, textvariable=cls.TotalCharges).place(x=200, y=175) 

		cls.note=StringVar()
		cls.note.set("*Note*")
		cls.TotalChargesEntry = Entry(cls.pay_dues,state=DISABLED ,width=7,textvariable=cls.note).place(x=5, y=275) 

		cls.title=Label(cls.pay_dues,text="Other Charges include amenities charge and room rent",font=("times new roman",10),bg="peach puff")
		cls.title.place(x=5,y=315)
		

		cls.pay_due=Button(cls.student_clear_dues, text="Pay due amount",bg="Pale Turquoise", width=20,borderwidth=0, command=cls.pays_due).place(x=700,y=250)
		cls.Go_back=Button(cls.student_clear_dues, text="Back to homepage",bg="Pale Turquoise", width=20,borderwidth=0, command=cls.student_main).place(x=700,y=290)
	@classmethod
	def pays_due(cls):
		cls.MessChargesEntry.delete(0,END)
		cls.othersChargesEntry.delete(0,END)
		cls.TotalChargesEntry.delete(0,END)
		student_db.update_mess_charge(0,cls.user_data[0][0])
		student_db.update_other_charge(0,cls.user_data[0][0])
		tmsg.showinfo('KUDOS','Successful Payment!!')
	
	@classmethod
	def profile(cls):
		cls.student_prof = Frame(cls.Student_main, borderwidth=4, bg="black")
		cls.student_prof.place(x=-3,y=28,width=1050,height=600)

		file = os.path.join(dirn,'images/wood_background.jpg')
		cls.image = Image.open(file)
		cls.image = cls.image.resize((1050,600))
		cls.photo = ImageTk.PhotoImage(cls.image)
		cls.label = ttk.Label(cls.student_prof, image = cls.photo)
		cls.label.place(x=-3,y=-3,width=1048,height=600)    
		pdf = FPDF('P', 'mm',(210,180))

		pdf_w=210
		pdf_h=297
		# Add a page
		pdf.add_page()

		pdf.set_xy(10.5, 10)
		file = os.path.join(dirn,'images/Indian_Institute_of_Technology_Ropar_logo.png')
		pdf.image(file, w = 30, h = 30)

		pdf.set_xy(20.0,8.0)
		pdf.set_font('Arial', 'B', 15)
		pdf.set_text_color(0, 0, 139)
		pdf.cell(w=210.0, h=40.0, align='C', txt="INDIAN INSTITUTE OF TECHNOLOGY Ropar", border=0)

		pdf.set_xy(85.0,32.0)
		pdf.set_font('Arial', 'B', 17)
		pdf.set_text_color(0, 0, 0)
		pdf.cell(w=210.0, h=40.0, align='L', txt="STUDENT PROFILE", border=0)

		pdf.set_xy(10.0,48.0)
		pdf.set_font('Times', 'B', 14)
		pdf.set_text_color(0, 0, 0)
		pdf.cell(w=210.0, h=40.0, align='L', txt="Name:", border=0)
		pdf.set_xy(40.0,48.0)
		pdf.cell(w=210.0, h=40.0, align='L', txt=cls.user_data[0][1], border=0)

		pdf.set_xy(10.0,58.0)
		pdf.cell(w=210.0, h=40.0, align='L', txt="Address:", border=0)
		pdf.set_xy(40.0,58.0)
		pdf.cell(w=210.0, h=40.0, align='L', txt=cls.user_data[0][2], border=0)

		pdf.set_xy(10.0,68.0)
		pdf.cell(w=210.0, h=40.0, align='L', txt="Contact:", border=0)
		pdf.set_xy(40.0,68.0)
		pdf.cell(w=210.0, h=40.0, align='L', txt=cls.user_data[0][3], border=0)

		pdf.set_xy(10.0,78.0)
		pdf.cell(w=210.0, h=40.0, align='L', txt="Username:", border=0)
		pdf.set_xy(40.0,78.0)
		pdf.cell(w=210.0, h=40.0, align='L', txt=cls.user_data[0][4], border=0)

		pdf.set_xy(10.0,88.0)
		pdf.cell(w=210.0, h=40.0, align='L', txt="Password:", border=0)
		pdf.set_xy(40.0,88.0)
		pdf.cell(w=210.0, h=40.0, align='L', txt=cls.user_data[0][5], border=0)

		pdf.set_xy(10.0,98.0)
		pdf.cell(w=210.0, h=40.0, align='L', txt="hostel Name:", border=0)
		pdf.set_xy(40.0,98.0)
		pdf.cell(w=210.0, h=40.0, align='L', txt=cls.user_data[0][7], border=0)

		pdf.set_xy(10.0,108.0)
		pdf.cell(w=210.0, h=40.0, align='L', txt="Room_no:", border=0)
		pdf.set_xy(40.0,108.0)
		pdf.cell(w=210.0, h=40.0, align='L', txt=cls.user_data[0][11], border=0)

		pdf.set_xy(10.0,118.0)
		pdf.cell(w=210.0, h=40.0, align='L', txt="Room_type:", border=0)
		pdf.set_xy(40.0,118.0)
		pdf.cell(w=210.0, h=40.0, align='L', txt=cls.user_data[0][10], border=0)

		pdf.output("Profile.pdf")

		v1 = kkk.ShowPdf()
		v2 = v1.pdf_view(cls.label, pdf_location = r"Profile.pdf",  width = 70, height = 30)
		v2.pack(pady= 10)


		cls.print=Button(cls.student_prof, text="Print Profile",bg="Pale Turquoise", width=20,borderwidth=0, command=cls.print_profile).place(x=450,y=540)
		

	@classmethod
	def print_profile(Cls):
		tmsg.showinfo('KUDOS','PDF downloaded!!')
		pass




class warden_login:

	@classmethod
	def warden_login_page(cls):
		cls.loginWarden = Frame(root, borderwidth=4, bg="light grey")
		cls.loginWarden.place(x=0,y=0,width=1050,height=625)

		file = os.path.join(dirn,'images/wood_background.jpg')
		cls.image = Image.open(file)
		cls.image = cls.image.resize((1050,625))
		cls.photo = ImageTk.PhotoImage(cls.image)
		cls.label = ttk.Label(cls.loginWarden, image = cls.photo)
		cls.label.pack(fill=BOTH, expand = YES)
		

		cls.back=Button(cls.loginWarden,text="<---",bg="Pale Turquoise", width=7,borderwidth=0,command=home_page.pack_homepage)
		cls.back.place(relx=0, rely=0.03,anchor="w")


		#username label and text entry box
		cls.usernameLabel = Label(cls.loginWarden, text="User Name",bg="lightgrey").place(relx=0.35, rely=0.2,anchor=CENTER)
		cls.username=StringVar()
		cls.usernameEntry = Entry(cls.loginWarden, textvariable=cls.username).place(relx=0.5, rely=0.2,anchor=CENTER)  

		#password label and password entry box
		cls.passwordLabel = Label(cls.loginWarden,text="Password",bg="light grey").place(relx=0.35, rely=0.3,anchor=CENTER) 
		cls.password=StringVar() 
		cls.passwordEntry = Entry(cls.loginWarden, textvariable=cls.password, show='*').place(relx=0.5, rely=0.3,anchor=CENTER) 


		cls.but0=Button(cls.loginWarden,text="Login",bg="Pale Turquoise", width=20,borderwidth=0,command=cls.validate_login)
		cls.but0.place(relx=0.45, rely=0.4,anchor=CENTER)

	@classmethod
	def validate_login(cls):
	    #login validty chck
	    #correct aythe warden page open

		# cls.warlist = warden_login_db.get_record_by_username(cls.username.get())

		# if len(cls.warlist)!= 0:

			
		# 	cls.login_warlist = login(cls.warlist[0][0], cls.warlist[0][1])
		# 	cls.user_data = student_db.get_record_by_username(cls.warlist[0][0])
		# 	cls.decrypted_password = cls.login_warlist.decrypt(cls.user_data[0][4])

		# 	if(cls.decrypted_password == cls.password.get()):
		# 		cls.user_data = warden_db.get_record_by_username(cls.warlist[0][0])
		# 		cls.warden_main()
		# 	else:
		# 		tmsg.showerror('ERROR', "Incorrect Username/Password !!!")
		# else:
		# 	tmsg.showerror('ERROR', "Incorrect Username/Password !!!")
		cls.warden_main()

	@classmethod
	def warden_main(cls):
		cls.Warden_main = Frame(root, borderwidth=4, bg="light grey")
		cls.Warden_main.place(x=0,y=0,width=1050,height=625)


		cls.warden_menu = Frame(cls.Warden_main, borderwidth=4, bg="light blue")
		cls.warden_display = Frame(cls.Warden_main, borderwidth=4, bg="black")
		cls.warden_menu.place(x=-3,y=-3,width=1055,height=30)
		cls.warden_display.place(x=-3,y=28,width=1055,height=600)

		
		file = os.path.join(dirn,'images/wood_background.jpg')
		cls.image = Image.open(file)
		cls.image = cls.image.resize((1050,600))
		cls.photo = ImageTk.PhotoImage(cls.image)
		cls.label = ttk.Label(cls.warden_display, image = cls.photo)
		cls.label.place(x=-3,y=-3,width=1048,height=600)

		cls.View_Occupancy=Button(cls.warden_menu, text="View Occupancy",bg="Pale Turquoise", width=20,borderwidth=0,command=cls.view_occupancy).grid(row=0,column=0,padx=10)
		cls.Hire_Fire_Workers=Button(cls.warden_menu, text="Hire/Fire Workers",bg="Pale Turquoise", width=20,borderwidth=0,command=cls.hire_fire_workers).grid(row=0,column=1,padx=10)
		cls.Solve_Complaint=Button(cls.warden_menu, text="Solve Complaint",bg="Pale Turquoise", width=20,borderwidth=0, command=cls.solve_complaint).grid(row=0,column=2,padx=10)
		# cls.Payment=Button(cls.warden_menu, text="Payment",bg="Pale Turquoise", width=20,borderwidth=0, command=cls.payment).grid(row=0,column=3,padx=10)
		cls.Request_Grant=Button(cls.warden_menu, text="Request Grant",bg="Pale Turquoise", width=20,borderwidth=0, command=cls.request_grant).grid(row=0,column=4,padx=10)
		cls.Logout=Button(cls.warden_menu, text="Log Out",bg="Pale Turquoise", width=20,borderwidth=0, command=home_page.pack_homepage).grid(row=0,column=5,padx=10)
		
	@classmethod
	def view_occupancy(cls):
		cls.warden_view_occupancy = Frame(cls.Warden_main, borderwidth=4, bg="black")
		cls.warden_view_occupancy.place(x=-3,y=28,width=1050,height=600)

		file = os.path.join(dirn,'images/wood_background.jpg')
		cls.image = Image.open(file)
		cls.image = cls.image.resize((1050,600))
		cls.photo = ImageTk.PhotoImage(cls.image)
		cls.label = ttk.Label(cls.warden_view_occupancy, image = cls.photo)
		cls.label.place(x=-3,y=-3,width=1048,height=600)
		
		cls.warden_view = Frame(cls.label, borderwidth=4, bg="black")
		cls.warden_view.place(x=150,y=50,width=550,height=450)

		fig = plt.figure(figsize = (4, 4),dpi =100)
		fig.suptitle("Room Occupancy", fontsize = 20)
	    # list of squares
		y = [0,100]
		y1 = [2,400]
		labels = ["occupied", "vacant"]
		explode = [0.1,0.1]

		plt.subplot(1,2,1)
		plt.title('Single Room')
		pie = plt.pie(y,  shadow=True, autopct='%1.1f%%')
		plt.legend(pie[0], labels, loc="upper left")
	    

		plt.subplot(1,2,2)
		plt.title('Double Room')
		pie1 = plt.pie(y1, labels=labels, explode=explode, shadow=True, autopct='%1.1f%%')
		plt.legend(pie1[0], labels, loc="upper left")
	    


		canvas = FigureCanvasTkAgg(fig,master = cls.warden_view)  
		# canvas.draw()
	  
		canvas.get_tk_widget().pack(fill=BOTH)

	@classmethod
	def hire_fire_workers(cls):
		cls.warden_hire_fire_workers= Frame(cls.Warden_main, borderwidth=4, bg="black")
		cls.warden_hire_fire_workers.place(x=-3,y=28,width=1050,height=600)

		file = os.path.join(dirn,'images/wood_background.jpg')
		cls.image = Image.open(file)
		cls.image = cls.image.resize((1050,600))
		cls.photo = ImageTk.PhotoImage(cls.image)
		cls.label = ttk.Label(cls.warden_hire_fire_workers, image = cls.photo)
		cls.label.place(x=-3,y=-3,width=1048,height=600)

		cls.pay_salaries=Button(cls.warden_hire_fire_workers, text="Pay Salaries",bg="Pale Turquoise", width=20,borderwidth=0, command=cls.pays_salary).place(x=835,y=67)


		cls.warden_fire_workers= Frame(cls.warden_hire_fire_workers, borderwidth=4, bg="peach puff")
		cls.warden_fire_workers.place(x=30,y=20,width=500,height=530)

		cls.warden_hire_workers= Frame(cls.warden_hire_fire_workers, borderwidth=4, bg="peach puff")
		cls.warden_hire_workers.place(x=560,y=180,width=450,height=370)


		cls.title=Label(cls.warden_hire_workers,text="Hire New Worker",font=("times new roman",22,"bold","italic"),bg="peach puff")
		cls.title.place(x=115,y=25)


		cls.title=Label(cls.warden_hire_workers,text="Worker Details",font=("times new roman",12,"bold"),bg="peach puff")
		cls.title.place(x=5,y=85)

		cls.NameWLabel = Label(cls.warden_hire_workers, text="Worker Name",bg="peach puff").place(x=5, y=125)
		cls.NameW=StringVar()
		cls.NameWEntry = Entry(cls.warden_hire_workers, textvariable=cls.NameW).place(x=200, y=125) 

		cls.SalaryWLabel = Label(cls.warden_hire_workers, text="Worker Daily Wage",bg="peach puff").place(x=5, y=165)
		cls.SalaryW=StringVar()
		cls.SalaryWEntry = Entry(cls.warden_hire_workers, textvariable=cls.SalaryW).place(x=200, y=165) 

		cls.hire_worker=Button(cls.warden_hire_workers, text="Hire Worker",bg="Pale Turquoise", width=20,borderwidth=0, command=exit).place(x=150,y=285)


		list=["Type","Attendant","Gardener"]
		cls.workertypelabel = Label(cls.warden_hire_workers, text="Woker Type",bg="peach puff").place(x=5,y=205)
		cls.workertypeEntry=ttk.Combobox(cls.warden_hire_workers,values=list)
		cls.workertypeEntry.current(0)
		cls.workertypeEntry.place(x=200,y=205) 
		cls.workertypeEntry.bind("<<ComboboxSelected>>",cls.passs)
	@classmethod
	def passs(cls):
		pass

	@classmethod
	def pays_salary(cls):
		tmsg.showinfo('KUDOS','Salary Payment done!')
	

	@classmethod
	def solve_complaint(cls):
		cls.warden_solve_complaint = Frame(cls.Warden_main, borderwidth=4, bg="black")
		cls.warden_solve_complaint.place(x=-3,y=28,width=1050,height=600)

		file = os.path.join(dirn,'images/wood_background.jpg')
		cls.image = Image.open(file)
		cls.image = cls.image.resize((1050,600))
		cls.photo = ImageTk.PhotoImage(cls.image)
		cls.label = ttk.Label(cls.warden_solve_complaint, image = cls.photo)
		cls.label.place(x=-3,y=-3,width=1048,height=600)

		complaints_list = complaints_db.get_all_records()

		style = ttk.Style()
		style.configure("Treeview",

        	background = "white",
        	foreground = "black",
        	rowheight = 25,
        	fieldbackground = "white"
    	)
		style.map('Treeview', background = [('selected','lightblue')])

		temp_frame = Frame(cls.label)
		temp_frame.pack( pady = 10,anchor = CENTER)

		temp_scroll = Scrollbar(temp_frame)
		temp_scroll.pack(side = RIGHT, fill = Y)

		complaints_tree = ttk.Treeview(temp_frame,yscrollcommand = temp_scroll.set)

		temp_scroll.config(command=complaints_tree.yview)

		complaints_tree['columns'] = ("ID","Name","complaints", "ATR")
		complaints_tree.column("#0", width = 0,stretch = NO)
		complaints_tree.column("ID",anchor = W, width = 50)
		complaints_tree.column("Name", anchor = W,width = 100)
		complaints_tree.column("complaints", anchor = W,width = 200)
		complaints_tree.column("ATR", anchor = CENTER,width = 200)

		complaints_tree.heading("#0", text = "", anchor = W)
		complaints_tree.heading("ID", text = "ID", anchor = W)
		complaints_tree.heading("Name", text = "Name", anchor = W)
		complaints_tree.heading("complaints", text = 'complaints', anchor = W)
		complaints_tree.heading("ATR", text = "ATR", anchor = CENTER)

		for count,alpha in enumerate(complaints_list):

			if(len(alpha[7]) == 0 ):
				complaints_tree.tag_configure('null_ATR', background = "#FFCCCB")
				complaints_tree.tag_configure('full_ATR', background = "#90EE90")
				complaints_tree.insert(parent = '', index = 'end', iid = count, text  = 'Parent', values =(alpha[0],alpha[2],alpha[6],alpha[7]), tags = ("null_ATR",))
			else:
				complaints_tree.tag_configure('null_ATR', background = "#FFCCCB")
				complaints_tree.tag_configure('full_ATR', background = "#90EE90")
				complaints_tree.insert(parent = '', index = 'end', iid = count, text  = 'Parent', values =(alpha[0],alpha[2],alpha[6],alpha[7]), tags = ("full_ATR",))

		complaints_tree.pack(pady = 10,anchor = CENTER)
		

	@classmethod
	def request_grant(cls):
		cls.request_grants = Frame(cls.Warden_main, borderwidth=4, bg="black")
		cls.request_grants.place(x=-3,y=28,width=1050,height=600)

		file = os.path.join(dirn,'images/wood_background.jpg')
		cls.image = Image.open(file)
		cls.image = cls.image.resize((1050,600))
		cls.photo = ImageTk.PhotoImage(cls.image)
		cls.label = ttk.Label(cls.request_grants, image = cls.photo)
		cls.label.place(x=-3,y=-3,width=1048,height=600)

		cls.grantLabel = Label(cls.request_grants, text="Enter Grant",bg="lightgrey").place(relx=0.35, rely=0.2,anchor=CENTER)
		cls.grant=StringVar()
		cls.grantEntry = Entry(cls.request_grants, textvariable=cls.grant).place(relx=0.35, rely=0.3,anchor=CENTER)

		cls.but120=Button(cls.request_grants,text="Request",bg="Pale Turquoise", width=20,borderwidth=0,command=cls.grantx)
		cls.but120.place(relx=0.35, rely=0.4,anchor=CENTER)

	@classmethod
	def grantx(cls):

		f=open("grant.txt","a")
		lis=warden_db.get_record_by_username(cls.username.get())
		s= lis[0][6]+ ","+cls.grant.get()
		print(s)
		f.write(s)
		f.write()
		f.close()
		tmsg.showinfo('KUDOS','Successful Signup!!!')

class HMCChairman_login:

	@classmethod
	def HMCChairman_login_page(cls):
		cls.loginHMCChairman = Frame(root, borderwidth=4, bg="light grey")
		cls.loginHMCChairman.place(x=0,y=0,width=1050,height=625)
		#cls.loginStudent.tkraise()

		file = os.path.join(dirn,'images/wood_background.jpg')
		cls.image = Image.open(file)
		cls.image = cls.image.resize((1050,625))
		cls.photo = ImageTk.PhotoImage(cls.image)
		cls.label = ttk.Label(cls.loginHMCChairman, image = cls.photo)
		cls.label.pack(fill=BOTH, expand = YES)

		cls.back=Button(cls.loginHMCChairman,text="<---",bg="Pale Turquoise", width=7,borderwidth=0,command=home_page.pack_homepage)
		cls.back.place(relx=0, rely=0.03,anchor="w")


		#username label and text entry box
		cls.usernameLabel = Label(cls.loginHMCChairman, text="User Name",bg="lightgrey").place(relx=0.35, rely=0.2,anchor=CENTER)
		cls.username=StringVar()
		cls.usernameEntry = Entry(cls.loginHMCChairman, textvariable=cls.username).place(relx=0.5, rely=0.2,anchor=CENTER)  

		#password label and password entry box
		cls.passwordLabel = Label(cls.loginHMCChairman,text="Password",bg="light grey").place(relx=0.35, rely=0.3,anchor=CENTER) 
		cls.password=StringVar() 
		cls.passwordEntry = Entry(cls.loginHMCChairman, textvariable=cls.password, show='*').place(relx=0.5, rely=0.3,anchor=CENTER) 


		cls.but0=Button(cls.loginHMCChairman,text="Login",bg="Pale Turquoise", width=20,borderwidth=0,command=cls.validate_login)
		cls.but0.place(relx=0.45, rely=0.4,anchor=CENTER)

	@classmethod
	def validate_login(cls):
	#login validty chck
	#correct aythe HMC page open
		# if(cls.username.get()=="ChairmanHMC"):
		# 	if(cls.password.get()=="Chair@123"):
		# 		cls.hmc_main()
		# 	else :
		# 		tmsg.showerror('ERROR', "Incorrect Username/Password !!!")
		# else :
		# 	tmsg.showerror('ERROR', "Incorrect Username/Password !!!")
		cls.hmc_main()

	@classmethod
	def hmc_main(cls):
		cls.HMC_main = Frame(root, borderwidth=4, bg="light grey")
		cls.HMC_main.place(x=0,y=0,width=1050,height=625)


		cls.hmc_menu = Frame(cls.HMC_main, borderwidth=4, bg="light blue")
		cls.hmc_display = Frame(cls.HMC_main, borderwidth=4, bg="black")
		cls.hmc_menu.place(x=-3,y=-3,width=1055,height=30)
		cls.hmc_display.place(x=-3,y=28,width=1055,height=600)


		file = os.path.join(dirn,'images/wood_background.jpg')
		cls.image = Image.open(file)
		cls.image = cls.image.resize((1050,600))
		cls.photo = ImageTk.PhotoImage(cls.image)
		cls.label = ttk.Label(cls.hmc_display, image = cls.photo)
		cls.label.place(x=-3,y=-3,width=1048,height=600)

		cls.Issue_Grants=Button(cls.hmc_menu, text="Issue Grant",bg="Pale Turquoise", width=20,borderwidth=0,command=cls.issue_grants).grid(row=0,column=0,padx=10)
		cls.Administer_hostel=Button(cls.hmc_menu, text="Administer hostels",bg="Pale Turquoise", width=20,borderwidth=0,command=cls.administer_hostels).grid(row=0,column=1,padx=10)
		cls.Allocate_hostel=Button(cls.hmc_menu, text="Allocate hostel",bg="Pale Turquoise", width=20,borderwidth=0, command=cls.allocate_hostels).grid(row=0,column=2,padx=10)
		cls.Logout=Button(cls.hmc_menu, text="Log Out",bg="Pale Turquoise", width=20,borderwidth=0, command=home_page.pack_homepage).grid(row=0,column=4,padx=10)

	@classmethod
	def issue_grants(cls):
		cls.hmc_issue_grants = Frame(cls.HMC_main, borderwidth=4, bg="black")
		cls.hmc_issue_grants.place(x=-3,y=28,width=1050,height=600)

		file = os.path.join(dirn,'images/wood_background.jpg')
		cls.image = Image.open(file)
		cls.image = cls.image.resize((1050,600))
		cls.photo = ImageTk.PhotoImage(cls.image)
		cls.label = ttk.Label(cls.hmc_issue_grants, image = cls.photo)
		cls.label.place(x=-3,y=-3,width=1048,height=600)

	@classmethod
	def administer_hostels(cls):
		cls.hmc_administer_hostels = Frame(cls.HMC_main, borderwidth=4, bg="black")
		cls.hmc_administer_hostels.place(x=-3,y=28,width=1050,height=600)

		file = os.path.join(dirn,'images/wood_background.jpg')
		cls.image = Image.open(file)
		cls.image = cls.image.resize((1050,600))
		cls.photo = ImageTk.PhotoImage(cls.image)
		cls.label = ttk.Label(cls.hmc_administer_hostels, image = cls.photo)
		cls.label.place(x=-3,y=-3,width=1048,height=600)

		cls.hmc_room = Frame(cls.hmc_administer_hostels, borderwidth=4, bg="peach puff")
		cls.hmc_room.place(x=50,y=40,width=420,height=470)


		cls.title=Label(cls.hmc_room,text="Basic Information",font=("times new roman",12,"bold"),bg="peach puff")
		cls.title.place(x=135,y=25)

		cls.hostelnameLabel = Label(cls.hmc_room, text="hostel Name",bg="peach puff").place(x=5, y=55)
		cls.hostelname=StringVar()
		cls.hostelnameEntry = Entry(cls.hmc_room, textvariable=cls.hostelname).place(x=200, y=55) 

		list=["Type","New","Old"]
		cls.hosteltypelabel = Label(cls.hmc_room, text="hostel Type",bg="peach puff").place(x=5,y=85)
		cls.hosteltypeEntry=ttk.Combobox(cls.hmc_room,values=list,width=17)
		cls.hosteltypeEntry.current(0)
		cls.hosteltypeEntry.place(x=200,y=85) 
		cls.hosteltypeEntry.bind("<<ComboboxSelected>>",cls.passs)

		cls.hostelamenity_chargesLabel = Label(cls.hmc_room, text="Amenities charge",bg="peach puff").place(x=5, y=115)
		cls.hostelamenity_charges=StringVar()
		cls.hostelamenity_chargesEntry = Entry(cls.hmc_room, textvariable=cls.hostelamenity_charges).place(x=200, y=115) 

		cls.title=Label(cls.hmc_room,text="Room details",font=("times new roman",12,"bold"),bg="peach puff")
		cls.title.place(x=135,y=160)

		cls.singlercLabel = Label(cls.hmc_room, text="Single Room Count",bg="peach puff").place(x=5, y=195)
		cls.singlerc=StringVar()
		cls.singlercEntry = Entry(cls.hmc_room, textvariable=cls.singlerc).place(x=200, y=195) 

		cls.doublercLabel = Label(cls.hmc_room, text="Double Room Count",bg="peach puff").place(x=5, y=225)
		cls.doublerc=StringVar()
		cls.doublercEntry = Entry(cls.hmc_room, textvariable=cls.doublerc).place(x=200, y=225) 

		cls.singlerrLabel = Label(cls.hmc_room, text="Single Room Rent",bg="peach puff").place(x=5, y=255)
		cls.singlerr=StringVar()
		cls.singlerrEntry = Entry(cls.hmc_room, textvariable=cls.singlerr).place(x=200, y=255) 

		cls.doublerrLabel = Label(cls.hmc_room, text="Double Room Rent",bg="peach puff").place(x=5, y=285)
		cls.doublerr=StringVar()
		cls.doublerrEntry = Entry(cls.hmc_room, textvariable=cls.doublerr).place(x=200, y=285) 		

		cls.hmc_work = Frame(cls.hmc_administer_hostels, borderwidth=4, bg="peach puff")
		cls.hmc_work.place(x=570,y=40,width=420,height=470)

		cls.title=Label(cls.hmc_work,text="Staff Information",font=("times new roman",12,"bold"),bg="peach puff")
		cls.title.place(x=135,y=15)

		cls.wardennameLabel = Label(cls.hmc_work, text="Warden Name",bg="peach puff").place(x=5, y=55)
		cls.wardenname=StringVar()
		cls.wardennameEntry = Entry(cls.hmc_work, textvariable=cls.wardenname).place(x=200, y=55) 

		cls.wardenpasswordLabel = Label(cls.hmc_work, text="Warden Password",bg="peach puff").place(x=5, y=85)
		cls.wardenpassword=StringVar()
		cls.wardenpasswordEntry = Entry(cls.hmc_work, textvariable=cls.wardenpassword).place(x=200, y=85) 

		cls.wardensalaryLabel = Label(cls.hmc_work, text="Warden Salary",bg="peach puff").place(x=5, y=115)
		cls.wardensalary=StringVar()
		cls.wardensalaryEntry = Entry(cls.hmc_work, textvariable=cls.wardensalary).place(x=200, y=115) 

		cls.clerknameLabel = Label(cls.hmc_work, text="Clerk Name",bg="peach puff").place(x=5, y=145)
		cls.clerkname=StringVar()
		cls.clerknameEntry = Entry(cls.hmc_work, textvariable=cls.clerkname).place(x=200, y=145) 

		cls.clerkpasswordLabel = Label(cls.hmc_work, text="Clerk Password",bg="peach puff").place(x=5, y=175)
		cls.clerkpassword=StringVar()
		cls.clerkpasswordEntry = Entry(cls.hmc_work, textvariable=cls.clerkpassword).place(x=200, y=175) 

		cls.clerksalaryLabel = Label(cls.hmc_work, text="Clerk Salary",bg="peach puff").place(x=5, y=205)
		cls.clerksalary=StringVar()
		cls.clerksalaryEntry = Entry(cls.hmc_work, textvariable=cls.clerksalary).place(x=200, y=205) 

		cls.MessManagernameLabel = Label(cls.hmc_work, text="Mess Manager Name",bg="peach puff").place(x=5, y=235)
		cls.MessManagername=StringVar()
		cls.MessManagernameEntry = Entry(cls.hmc_work, textvariable=cls.MessManagername).place(x=200, y=235) 

		cls.MessManagerPasswordLabel = Label(cls.hmc_work, text="Mess Manager Password",bg="peach puff").place(x=5, y=265)
		cls.MessManagerPassword=StringVar()
		cls.MessManagerPasswordEntry = Entry(cls.hmc_work, textvariable=cls.MessManagerPassword).place(x=200, y=265) 

		cls.MessManagersalaryLabel = Label(cls.hmc_work, text="Mess Manager Salary",bg="peach puff").place(x=5, y=295)
		cls.MessManagersalary=StringVar()
		cls.MessManagersalaryEntry = Entry(cls.hmc_work, textvariable=cls.MessManagersalary).place(x=200, y=295) 

		# cls.title=Label(cls.hmc_work,text="workers Information",font=("times new roman",12,"bold"),bg="peach puff")
		# cls.title.place(x=600,y=25)

		# cls.otherssalarayLabel = Label(cls.hmc_work, text="Workers Salary",bg="peach puff").place(x=5, y=325)
		# cls.otherssalaray=StringVar()
		# cls.otherssalarayEntry = Entry(cls.hmc_work, textvariable=cls.otherssalaray).place(x=200, y=325) 


		cls.Set_up_hostel=Button(cls.hmc_administer_hostels, text="Setup/update hostel",bg="Pale Turquoise", width=20,borderwidth=0, command=cls.setup_hostels).place(x=460,y=530)
		cls.Cancel=Button(cls.hmc_administer_hostels, text="Cancel",bg="Pale Turquoise", width=20,borderwidth=0, command=cls.cancel).place(x=460,y=560)


	@classmethod
	def setup_hostels(cls):
		# if(cls.hosteltypeEntry.get()=="Old")
		hostel_list=hostel_db.get_all_records()
		hostelname_list=[]
		for i in hostel_list:
			hostelname_list.append(i[1])
		if(cls.hostelname.get() not in hostelname_list):
			hostel_db.insert_record((cls.hostelname.get(),cls.hosteltypeEntry.get(),cls.singlerc.get(),cls.doublerc.get(),0,0,cls.singlerr.get(),cls.doublerr.get(),cls.wardenname.get(),cls.MessManagername.get(),cls.clerkname.get(),cls.hostelamenity_charges.get()))
			li=hostel_db.get_record_by_name(cls.hostelname.get())
			warden_db.insert_record((cls.wardenname.get(),cls.wardenname.get(),cls.wardenpassword.get(),"",cls.wardensalary.get(),cls.hostelname.get(),li[0][0],cls.clerksalary.get(),0,0,0,0,0))
			mess_manager_login_db.insert_record((cls.MessManagername.get(),cls.MessManagerPassword.get(),li[0][0]))
			hostel_clerk_login_db.insert_record((cls.clerkname.get(),cls.clerkpassword.get(),li[0][0]))
			warden_login_db.insert_record((cls.wardenname.get(),cls.wardenpassword.get(),li[0][0]))
		else : 
			pass
			

	@classmethod
	def cancel(cls):
		cls.hmc_main()

	@classmethod
	def passs(cls):
		pass


	@classmethod
	def allocate_hostels(cls):
		cls.hmc_allocate_hostel = Frame(cls.HMC_main, borderwidth=4, bg="black")
		cls.hmc_allocate_hostel.place(x=-3,y=28,width=1050,height=600)

		file = os.path.join(dirn,'images/wood_background.jpg')
		cls.image = Image.open(file)
		cls.image = cls.image.resize((1050,600))
		cls.photo = ImageTk.PhotoImage(cls.image)
		cls.label = ttk.Label(cls.hmc_allocate_hostel, image = cls.photo)
		cls.label.place(x=-3,y=-3,width=1048,height=600)

		style = ttk.Style()

		style.configure("Treeview",

				background = "white",
				foreground = "black",
				rowheight = 35,
				fieldbackground = "white"
			)

		style.map('Treeview', background = [('selected','lightblue')])


		allocate_hostels_tree = ttk.Treeview(cls.label)

		#make treeview table
		allocate_hostels_tree['columns'] = ("ID","Name")
		allocate_hostels_tree.column("#0", width = 0,stretch = NO)
		allocate_hostels_tree.column("ID",anchor = W, width = 100)
		allocate_hostels_tree.column("Name", anchor = W,width = 200)

		allocate_hostels_tree.heading("#0", text = "", anchor = W)
		allocate_hostels_tree.heading("ID", text = "ID", anchor = W)
		allocate_hostels_tree.heading("Name", text = "Name", anchor = W)

		#insert values
		stu_list=student_db.get_all_records()
		li=[]
		for i in stu_list :       
			if (i[7]=="not alloted") :
					li.append((i[0],i[1]))       

		count=0
		for value in li:        
			allocate_hostels_tree.insert(parent='',index='end',iid=count,text='Parent',values=value)
			count=count+1

		cls.but6=Button(cls.label,text="Allocate hostel",bg="Pale Turquoise", width=20,borderwidth=0,command=cls.allocate)
		cls.but6.place(x=750,y=250)

		allocate_hostels_tree.place(x=250,y=50)

	@classmethod
	def allocate(cls):
		
		get_all_students = student_db.get_all_records()

		for beta in get_all_students:
			if beta[7] == 'not allocated':
				student_db.update_hostel_name('LBS',beta[0])
				student_db.update_room_type(1,beta[0])
				student_db.update_room_number(beta[0],beta[0])

		

class clerk_login:

	@classmethod
	def clerk_login_page(cls):
		cls.loginclerk = Frame(root, borderwidth=4, bg="light grey")
		cls.loginclerk.place(x=0,y=0,width=1050,height=625)
		#cls.loginStudent.tkraise()

		file = os.path.join(dirn,'images/wood_background.jpg')
		cls.image = Image.open(file)
		cls.image = cls.image.resize((1050,625))
		cls.photo = ImageTk.PhotoImage(cls.image)
		cls.label = ttk.Label(cls.loginclerk, image = cls.photo)
		cls.label.pack(fill=BOTH, expand = YES)


		cls.back=Button(cls.loginclerk,text="<---",bg="Pale Turquoise", width=7,borderwidth=0,command=home_page.pack_homepage)
		cls.back.place(relx=0, rely=0.03,anchor="w")

		#username label and text entry box
		cls.usernameLabel = Label(cls.loginclerk, text="User Name",bg="lightgrey").place(relx=0.35, rely=0.2,anchor=CENTER)
		cls.username=StringVar()
		cls.usernameEntry = Entry(cls.loginclerk, textvariable=cls.username).place(relx=0.5, rely=0.2,anchor=CENTER)  

		#password label and password entry box
		cls.passwordLabel = Label(cls.loginclerk,text="Password",bg="light grey").place(relx=0.35, rely=0.3,anchor=CENTER) 
		cls.password=StringVar() 
		cls.passwordEntry = Entry(cls.loginclerk, textvariable=cls.password, show='*').place(relx=0.5, rely=0.3,anchor=CENTER) 


		cls.but0=Button(cls.loginclerk,text="Login",bg="Pale Turquoise", width=20,borderwidth=0,command=cls.validate_login)
		cls.but0.place(relx=0.45, rely=0.4,anchor=CENTER)

	@classmethod
	def validate_login(cls):
	#login validty chck
	#correct aythe clerk page open
		cls.clerk_main()

		# cls.clelist = hostel_clerk_login_db.get_record_by_username(cls.username.get())

		# if len(cls.clelist)!= 0:

		# 	if(cls.clelist[0][2] == cls.password.get()):
		# 		cls.clerk_main()
		# 	else:
		# 		tmsg.showerror('ERROR', "Incorrect Username/Password !!!")
		# else:
		# 	tmsg.showerror('ERROR', "Incorrect Username/Password !!!")

	@classmethod
	def clerk_main(cls):
		cls.Clerk_main = Frame(root, borderwidth=4, bg="light grey")
		cls.Clerk_main.place(x=0,y=0,width=1050,height=625)


		cls.clerk_menu = Frame(cls.Clerk_main, borderwidth=4, bg="light blue")
		cls.clerk_display = Frame(cls.Clerk_main, borderwidth=4, bg="black")
		cls.clerk_menu.place(x=-3,y=-3,width=1055,height=30)
		cls.clerk_display.place(x=-3,y=28,width=1055,height=600)


		file = os.path.join(dirn,'images/wood_background.jpg')
		cls.image = Image.open(file)
		cls.image = cls.image.resize((1050,600))
		cls.photo = ImageTk.PhotoImage(cls.image)
		cls.label = ttk.Label(cls.clerk_display, image = cls.photo)
		cls.label.place(x=-3,y=-3,width=1048,height=600)

		cls.Mark_Attendence=Button(cls.clerk_menu, text="Mark Attendence",bg="Pale Turquoise", width=20,borderwidth=0, command=cls.mark_attendance).grid(row=0,column=1,padx=10)
		cls.Logout=Button(cls.clerk_menu, text="Log Out",bg="Pale Turquoise", width=20,borderwidth=0, command=home_page.pack_homepage).grid(row=0,column=2,padx=10)

	@classmethod
	def mark_attendance(cls):
		cls.clerk_mark_attendence = Frame(cls.Clerk_main, borderwidth=4, bg="black")
		cls.clerk_mark_attendence.place(x=-3,y=28,width=1050,height=600)

		file = os.path.join(dirn,'images/wood_background.jpg')
		cls.image = Image.open(file)
		cls.image = cls.image.resize((1050,600))
		cls.photo = ImageTk.PhotoImage(cls.image)
		cls.label = ttk.Label(cls.clerk_mark_attendence, image = cls.photo)
		cls.label.place(x=-3,y=-3,width=1048,height=600)

class MessManager_login:

	@classmethod
	def MessManager_login_page(cls):
		cls.loginMessManager = Frame(root, borderwidth=4, bg="light grey")
		cls.loginMessManager.place(x=0,y=0,width=1050,height=625)
		#cls.loginStudent.tkraise()

		file = os.path.join(dirn,'images/wood_background.jpg')
		cls.image = Image.open(file)
		cls.image = cls.image.resize((1050,625))
		cls.photo = ImageTk.PhotoImage(cls.image)
		cls.label = ttk.Label(cls.loginMessManager, image = cls.photo)
		cls.label.pack(fill=BOTH, expand = YES)


		cls.back=Button(cls.loginMessManager,text="<---",bg="Pale Turquoise", width=7,borderwidth=0,command=home_page.pack_homepage)
		cls.back.place(relx=0, rely=0.03,anchor="w")

		#username label and text entry box
		cls.usernameLabel = Label(cls.loginMessManager, text="User Name",bg="lightgrey").place(relx=0.35, rely=0.2,anchor=CENTER)
		cls.username=StringVar()
		cls.usernameEntry = Entry(cls.loginMessManager, textvariable=cls.username).place(relx=0.5, rely=0.2,anchor=CENTER)  

		#password label and password entry box
		cls.passwordLabel = Label(cls.loginMessManager,text="Password",bg="light grey").place(relx=0.35, rely=0.3,anchor=CENTER) 
		cls.password=StringVar() 
		cls.passwordEntry = Entry(cls.loginMessManager, textvariable=cls.password, show='*').place(relx=0.5, rely=0.3,anchor=CENTER) 


		cls.but0=Button(cls.loginMessManager,text="Login",bg="Pale Turquoise", width=20,borderwidth=0,command=cls.validate_login)
		cls.but0.place(relx=0.45, rely=0.4,anchor=CENTER)

	@classmethod
	def validate_login(cls):
	#login validty chck
	#correct aythe clerk page open
		cls.messManager_main()

		# cls.meslist = mess_manager_login_db.get_record_by_username(cls.username.get())

		# if len(cls.meslist)!= 0:

		# 	if(cls.meslist[0][2] == cls.password.get()):
		# 		cls.messManager_main()
		# 	else:
		# 		tmsg.showerror('ERROR', "Incorrect Username/Password !!!")
		# else:
		# 	tmsg.showerror('ERROR', "Incorrect Username/Password !!!")
	@classmethod
	def messManager_main(cls):
		cls.MessManager_main = Frame(root, borderwidth=4, bg="light grey")
		cls.MessManager_main.place(x=0,y=0,width=1050,height=625)


		cls.messmanager_menu = Frame(cls.MessManager_main, borderwidth=4, bg="light blue")
		cls.messmanager_display = Frame(cls.MessManager_main, borderwidth=4, bg="black")
		cls.messmanager_menu.place(x=-3,y=-3,width=1055,height=30)
		cls.messmanager_display.place(x=-3,y=28,width=1055,height=600)


		file = os.path.join(dirn,'images/wood_background.jpg')
		cls.image = Image.open(file)
		cls.image = cls.image.resize((1050,600))
		cls.photo = ImageTk.PhotoImage(cls.image)
		cls.label = ttk.Label(cls.messmanager_display, image = cls.photo)
		cls.label.place(x=-3,y=-3,width=1048,height=600)

		cls.Update_mess_fee=Button(cls.messmanager_menu, text="Update mess fee",bg="Pale Turquoise", width=20,borderwidth=0, command=cls.update_mess_fee).grid(row=0,column=1,padx=10)
		cls.Logout=Button(cls.messmanager_menu, text="Log Out",bg="Pale Turquoise", width=20,borderwidth=0, command=home_page.pack_homepage).grid(row=0,column=2,padx=10)


	@classmethod
	def update_mess_fee(cls):
		cls.messmanager_update = Frame(cls.MessManager_main, borderwidth=4, bg="black")
		cls.messmanager_update.place(x=-3,y=28,width=1050,height=600)

		file = os.path.join(dirn,'images/wood_background.jpg')
		cls.image = Image.open(file)
		cls.image = cls.image.resize((1050,600))
		cls.photo = ImageTk.PhotoImage(cls.image)
		cls.label = ttk.Label(cls.messmanager_update, image = cls.photo)
		cls.label.place(x=-3,y=-3,width=1048,height=600)

		style = ttk.Style()

		style.configure("Treeview",

				background = "white",
				foreground = "black",
				rowheight = 35,
				fieldbackground = "white"
			)

		style.map('Treeview', background = [('selected','lightblue')])


		update_fee_tree = ttk.Treeview(cls.messmanager_update)

		#make treeview table
		update_fee_tree['columns'] = ("ID","Name", "Mess Charge")
		update_fee_tree.column("#0", width = 0,stretch = NO)
		update_fee_tree.column("ID",anchor = W, width = 50)
		update_fee_tree.column("Name", anchor = W,width = 200)
		update_fee_tree.column("Mess Charge", anchor = CENTER,width = 200)

		update_fee_tree.heading("#0", text = "", anchor = W)
		update_fee_tree.heading("ID", text = "ID", anchor = W)
		update_fee_tree.heading("Name", text = "Name", anchor = W)
		update_fee_tree.heading("Mess Charge", text = "Mess Charge", anchor = CENTER)

		#insert values

		update_fee_tree.tag_configure('null_ATR', background = "#FFCCCB")
		update_fee_tree.tag_configure('full_ATR', background = "#90EE90")

		stu_list=student_db.get_all_records()
		print(stu_list)
		li=[]
		count=0
		for i in stu_list :         
			listhostel=hostel_db.get_record_by_name(i[7])
			print(listhostel)
			if  listhostel:
				k=0
				for j in (listhostel[0]):
					if(k==10):
						if(j==cls.username.get()):
							count=count+1
							li.append((count,i[1],''))

					k=k+1

				 

		count=0
		for value in li:        
			update_fee_tree.insert(parent='',index='end',iid=count,text='Parent',values=value)
			count=count+1


		cls.but69=Button(cls.messmanager_update,text="Update mess Fee",bg="Pale Turquoise", width=20,borderwidth=0,command=cls.validate_login)
		cls.but69.place(x=750,y=250)

		cls.update=StringVar()
		cls.updateEntry = Entry(cls.messmanager_update, textvariable=cls.update).place(x=757,y=200) 

		update_fee_tree.place(x=250,y=50)




home_page.pack_homepage()

root.mainloop()
