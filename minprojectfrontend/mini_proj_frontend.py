#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# In[ ]:


import tkinter as tk 
import mysql.connector as mysql
import tkinter.messagebox as MessageBox
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import pandas as pd

main = tk.Tk()
main.title("Student Attendance System")
main.geometry('1280x720')

tab = ttk.Notebook(main)
tab.pack(pady=10, padx=0)

page0 = Frame(tab, width=1280, height=720)
page1 = Frame(tab, width=1280, height=720)
page2 = Frame(tab, width=1280, height=720)

page0.pack(expand=1, fill="both")
page1.pack(expand=1, fill="both")
page2.pack(expand=1, fill="both")

tab.add(page0, text='Welcome and Login')
tab.add(page1, text='Create Admin Account')
tab.add(page2, text='Database Homepage')

tab.hide(1)
tab.hide(2)

# _____________________________________________________________________________________________________________________________________________________________________________________________________

# page0

canvas = tk.Canvas(page0, width=1280, height=720)
canvas.pack(fill="both", expand=True)

bg0 = Image.open("C:/Users/cools/Downloads/mini_frontend0.png")
resize = bg0.resize((1280, 700), Image.ANTIALIAS)
nbg0 = ImageTk.PhotoImage(resize)  # Keep a persistent reference to the PhotoImage

canvas.create_image(640, 360, image=nbg0)  # Use nbg0 directly here

def log_in():
    nuser = username_e.get()
    npw = password_e.get()
    
    if not nuser or not npw:
        MessageBox.showerror("Error", "Enter ALL the following credentials!")
        return
    
    mycon = mysql.connect(host="localhost", user="root", passwd="entonkagutsuchi123AB!!", database="mini_project")
    cursor = mycon.cursor()
    cursor.execute("SELECT User_Name, PASS_WORD FROM admindetails")
    dets = cursor.fetchall()
    
    for x in dets:
        if x[0] == nuser and x[1] == npw:
            tab.select(2)
            tab.hide(0)
            MessageBox.showinfo("Login Process", "Logged in successfully!")
            return
    
    MessageBox.showerror("Error", "Invalid Username OR Password!")
        
        
def topage1():
    tab.select(1)
    tab.hide(0)       
        
        
loginlabel = tk.Label(page0, fg="sky blue", text="WELCOME!", font="Times 35 bold italic", bg="white")
loginlabel.place(x=520, y=10)

titlelabel = tk.Label(page0, fg="sky blue", text="                                               Student Attendance Management System                                       ", font="Times 30 bold italic", bg="white")
titlelabel.place(x=-130, y=90)

loginlabel = tk.Label(page0, fg="sky blue", text="LOGIN HERE!", font="Times 18 bold italic", bg="white")
loginlabel.place(x=550, y=200)

username = tk.Label(page0, fg="gray", text="Enter Username:", font="Arial 11 bold italic", bg="sky blue")
username.place(x=420, y=340)
username_e = tk.Entry(page0, width=17, font="Verdana 13 bold italic", bg="beige", borderwidth=3)
username_e.place(x=650, y=340)

password = tk.Label(page0, text="Enter Password:", font="Arial 11 bold italic", fg="gray", bg="sky blue")
password.place(x=420, y=390)
password_e = tk.Entry(page0, width=17, font="Verdana 13 bold italic", bg="beige", borderwidth=3, show="*")
password_e.place(x=650, y=390)

myimglog = Image.open("C:/Users/cools/Downloads/images.png")
resize = myimglog.resize((100, 50), Image.ANTIALIAS)
logimbut = ImageTk.PhotoImage(resize)

login = tk.Button(page0, bg="white", command=log_in, image=logimbut, borderwidth=0)
login.place(x=570, y=450)

new_user = tk.Label(page0, fg="sky blue", text="New User?", font="Arial 11 bold italic", bg="black", height=2, width=10)
new_user.place(x=480, y=530)
newaccad_button = tk.Button(page0, text="Create New Admin Account!", font="Arial 9 bold italic", bg="white", borderwidth=2, height=2, command=topage1)
newaccad_button.place(x=620, y=530)


# _______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________


# page1

def accdetails():
    n2 = name_e.get()
    n3 = pw_e.get()
    n4 = cpw_e.get()
    
    if n2 == "" or n3 == "" or n4 == "":
        MessageBox.showerror('ERROR', 'Above Details Are Necessary To Enter!')
    elif len(n2) == 0:
        MessageBox.showerror("Error", "Invalid Username")
    elif n3 != n4:
        MessageBox.showerror("Error", "Does not match! Enter again please!")
    else:
        mycon = mysql.connect(host="localhost", user="root", passwd="entonkagutsuchi123AB!!", database="mini_project")
        cursor = mycon.cursor()
        cursor.execute("SELECT * FROM admindetails")
        y = cursor.fetchall()
        count = 0
        for x in y:
            if x[1] == n3:
                count += 1
        
        if count != 0:
            MessageBox.showerror("Error", "User already exists!")
        else:
            cursor.execute("INSERT INTO admindetails (User_Name, PASS_WORD) VALUES (%s, %s)", (n2, n3))
            mycon.commit()
            MessageBox.showinfo("Account Creation", "Your admin account was created successfully!")
            
            name_e.delete(0, 'end')
            pw_e.delete(0, 'end')
            cpw_e.delete(0, 'end')

def topage0():
    tab.select(0)
    tab.hide(1)

canvas = tk.Canvas(page1, width=1280, height=720)
canvas.grid()
bg1 = Image.open("C:/Users/cools/Downloads/6472648a4dd7a6d46d20dfafc4af2bb5.png")
resize = bg1.resize((1280, 700), Image.ANTIALIAS)
nbg1 = ImageTk.PhotoImage(resize)
canvas.create_image(633, 324, image=nbg1)

createadmin = tk.Label(page1, fg="sky blue", text="                                               Create Your Admin Account                                             ", font="Times 30 bold italic", bg="gray")
createadmin.place(x=-60, y=40)

pleaselabel = tk.Label(page1, fg="sky blue", text="Please enter the following details: ", font="Times 20 bold italic", bg="gray")
pleaselabel.place(x=450, y=170)

name = tk.Label(page1, fg="sky blue", text="Your Username:", bg="gray", font="Arial 11 bold italic")
name.place(x=290, y=330)
name_e = tk.Entry(page1, fg="sky blue", width=17, font="Arial 13 italic", bg="gray", borderwidth=3)
name_e.place(x=430, y=330)

pw = tk.Label(page1, text="Your Password:", fg="sky blue", bg="gray", font="Arial 13 bold italic")
pw.place(x=680, y=290)
pw_e = tk.Entry(page1, width=17, font="Arial 13 italic", fg="sky blue", bg="gray", borderwidth=3, show="*")
pw_e.place(x=870, y=290)

cpw = tk.Label(page1, text="Confirm Your Password:", fg="sky blue", bg="gray", font="Arial 11 bold italic")
cpw.place(x=680, y=370)
cpw_e = tk.Entry(page1, width=17, font="Arial 13 italic", fg="sky blue", bg="gray", borderwidth=3, show="*")
cpw_e.place(x=870, y=370)

createaccbutton = tk.Button(page1, fg="sky blue", bg="gray", text="Create Your Account", font="Arial 13 bold italic", command=accdetails, borderwidth=0, height=2)
createaccbutton.place(x=660, y=490)

backbutton = tk.Button(page1, fg="sky blue", bg="gray", text="Back to Login Page", font="Arial 13 bold italic", command=topage0, borderwidth=0, height=2)
backbutton.place(x=440, y=490)   

#page2

# Assuming you have already created your Tkinter window and notebook
# Create a Canvas widget

# Create a Canvas widget
canvas = tk.Canvas(page2, width=1280, height=720)
canvas.grid()

# Load and resize background image
bg3 = Image.open("C:/Users/cools/Downloads/istockphoto-1134227742-612x612.png")
resize_bg3 = bg3.resize((1280, 700), Image.ANTIALIAS)
nbg3 = ImageTk.PhotoImage(resize_bg3)
canvas.create_image(640, 360, image=nbg3)

# Load and resize logo image
logo = Image.open("C:/Users/cools/Downloads/jsslogo.png")
resize_logo = logo.resize((150, 150), Image.ANTIALIAS)
nlogo = ImageTk.PhotoImage(resize_logo)
canvas.create_image(640, 100, image=nlogo)

# Create and place the main label
mainpagelabel = tk.Label(page2, text="JSS Academy of Technical Education", font="Times 32 bold italic", fg="indigo", bg="silver")
mainpagelabel.place(x=330, y=40)

# Function to handle logout
def logout():
    tab.select(0)
    tab.hide(1)
    tab.hide(2)
    tab.hide(3)
    tab.hide(4)
    tab.hide(5)
    tab.hide(6)
    tab.hide(7)
    tab.hide(8)
    tab.hide(9)
    tab.hide(10)

# Function to open Excel sheet for CSE
def cse_function():
    try:
        # Replace the file path with the path to your Excel file
        file_path = "C:/Users/cools/Downloads/attendance - Sheet1.csv"
        df = pd.read_csv(file_path)  # Assuming CSV format here, adjust if it's an Excel file
        
        # Extract student names and possibly image paths from the DataFrame
        student_names = df['Student Name'].tolist()  # Adjust column name as per your Excel file
        image_paths = df['Image Path'].tolist()  # Adjust column name for image paths
        usn = df['USN'].tolist()
        
        # Open a new Tkinter window to display student information
        display_students(student_names, image_paths)
        
        MessageBox.showinfo("Excel Sheet Opened", "CSE Excel sheet has been opened successfully.")
    except Exception as e:
        MessageBox.showerror("Error", f"Failed to open Excel sheet: {e}")

# Function to display student information in a new Tkinter window
def display_students(names, image_paths):
    # Create a new Tkinter window (Toplevel widget)
    display_window = Toplevel(main)
    display_window.title("Student Information")
    display_window.geometry('800x600')
    
    # Create a Canvas widget to display students
    canvas = tk.Canvas(display_window, width=800, height=600)
    canvas.pack(fill="both", expand=True)
    
    # Load and display student information (names and images)
    for i, name in enumerate(names):
        label_name = tk.Label(display_window, text=name, font="Arial 12 bold")
        label_name.pack(pady=10)
        
        # Load and display student image if available
        if image_paths[i]:
            img = Image.open(image_paths[i])
            img = img.resize((100, 100), Image.ANTIALIAS)
            img_tk = ImageTk.PhotoImage(img)
            label_image = tk.Label(display_window, image=img_tk)
            label_image.image = img_tk  # Keep a reference to prevent garbage collection
            label_image.pack(pady=10)
        else:
            label_no_image = tk.Label(display_window, text="No image available", font="Arial 10 italic")
            label_no_image.pack(pady=10)

# Create and place the buttons
cse_button = tk.Button(page2, text="CSE", fg="indigo", bg="silver", font="Arial 13 bold italic", command=cse_function, borderwidth=0, height=1)
#ece_button = tk.Button(page2, text="ECE", fg="indigo", bg="silver", font="Arial 13 bold italic", command=ece_function, borderwidth=0, height=1)
#aiml_button = tk.Button(page2, text="AIML", fg="indigo", bg="silver", font="Arial 13 bold italic", command=aiml_function, borderwidth=0, height=1)
logout_button = tk.Button(page2, text="Log Out", fg="indigo", bg="silver", font="Arial 13 bold italic", borderwidth=0, height=1, command=logout)

cse_button.place(x=330, y=230)
#ece_button.place(x=530, y=230)
#aiml_button.place(x=730, y=230)
logout_button.place(x=90, y=200)


main.mainloop()


# In[ ]:




