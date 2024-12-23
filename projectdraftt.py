import tkinter as tk
import mysql.connector as mysql
import tkinter.messagebox as MessageBox
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import requests
from io import BytesIO

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

bg0 = Image.open(r"/Users/shreyyya/Desktop/face_recognition_attendance/jss_clg_image.webp")
resize = bg0.resize((1280, 700), Image.Resampling.LANCZOS)
nbg0 = ImageTk.PhotoImage(resize)  # Keep a persistent reference to the PhotoImage

canvas.create_image(640, 360, image=nbg0)  # Use nbg0 directly here


def log_in():
    nuser = username_e.get()
    npw = password_e.get()

    if not nuser or not npw:
        MessageBox.showerror("Error", "Enter ALL the following credentials!")
        return

    mycon = mysql.connect(host="localhost", user="root", passwd="shreyyaa_0411", database="mini_project")
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

titlelabel = tk.Label(page0, fg="sky blue",
                      text="                                               Student Attendance Management System                                       ",
                      font="Times 30 bold italic", bg="white")
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

myimglog = Image.open(r"/Users/shreyyya/Desktop/face_recognition_attendance/jss_clg_image.webp")
resize = myimglog.resize((100, 50), Image.Resampling.LANCZOS)
logimbut = ImageTk.PhotoImage(resize)

login = tk.Button(page0, bg="white", command=log_in, image=logimbut, borderwidth=0)
login.place(x=570, y=450)

new_user = tk.Label(page0, fg="sky blue", text="New User?", font="Arial 11 bold italic", bg="black", height=2, width=10)
new_user.place(x=480, y=530)
newaccad_button = tk.Button(page0, text="Create New Admin Account!", font="Arial 9 bold italic", bg="white",
                            borderwidth=2, height=2, command=topage1)
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
        mycon = mysql.connect(host="localhost", user="root", passwd="shreyyaa_0411", database="mini_project")
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
bg1 = Image.open(r"/Users/shreyyya/Desktop/face_recognition_attendance/jss_clg_image.webp")
resize = bg1.resize((1280, 700), Image.Resampling.LANCZOS)
nbg1 = ImageTk.PhotoImage(resize)
canvas.create_image(633, 324, image=nbg1)

createadmin = tk.Label(page1, fg="sky blue",
                       text="                                               Create Your Admin Account                                             ",
                       font="Times 30 bold italic", bg="gray")
createadmin.place(x=-60, y=40)

pleaselabel = tk.Label(page1, fg="sky blue", text="Please enter the following details: ", font="Times 20 bold italic",
                       bg="gray")
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

createaccbutton = tk.Button(page1, fg="sky blue", bg="gray", text="Create Your Account", font="Arial 13 bold italic",
                            command=accdetails, borderwidth=0, height=2)
createaccbutton.place(x=660, y=490)

backbutton = tk.Button(page1, fg="sky blue", bg="gray", text="Back to Login Page", font="Arial 13 bold italic",
                       command=topage0, borderwidth=0, height=2)
backbutton.place(x=440, y=490)

# page2

# Assuming you have already created your Tkinter window and notebook
# Create a Canvas widget

# Create a Canvas widget
canvas = tk.Canvas(page2, width=1280, height=720)
canvas.pack(fill="both", expand=True)

# Load and display the background image
bg2 = Image.open(r"/Users/shreyyya/Desktop/face_recognition_attendance/jss_clg_image.webp")
resize = bg2.resize((1280, 700), Image.Resampling.LANCZOS)
nbg2 = ImageTk.PhotoImage(resize)
canvas.create_image(640, 360, image=nbg2)  # Use nbg2 directly here

def cse_function():
    try:
        # Connect to the MySQL database
        mycon = mysql.connect(host="localhost", user="root", passwd="shreyyaa_0411", database="mini_project")
        cursor = mycon.cursor()

        # Fetch student details from the MySQL table
        cursor.execute("SELECT `Timestamp`, `Name:`, `Branch:`, `USN:`, `Section:`, `Photo` FROM student_details")
        students = cursor.fetchall()

        # Close the database connection
        mycon.close()

        # Extract student details into separate lists
        timestamps = [student[0] for student in students]
        names = [student[1] for student in students]
        branches = [student[2] for student in students]
        usns = [student[3] for student in students]
        sections = [student[4] for student in students]
        photo_urls = [student[5] for student in students]

        # Open a new Tkinter window to display student information
        display_students(timestamps, names, branches, usns, sections, photo_urls)

        MessageBox.showinfo("MySQL Data", "Student details have been fetched and displayed successfully.")
    except Exception as e:
        MessageBox.showerror("Error", f"Failed to fetch data: {e}")

def display_students(timestamps, names, branches, usns, sections, photo_urls):
    # Create a new Tkinter window (Toplevel widget)
    display_window = Toplevel(main)
    display_window.title("Student Information")
    display_window.geometry('1000x800')  # Adjust the size as needed

    # Create a Canvas widget to hold the student information
    canvas = tk.Canvas(display_window, width=1000, height=800)
    canvas.pack(fill="both", expand=True)

    # Create a Frame to hold the student details
    frame = tk.Frame(canvas)
    frame.pack(padx=10, pady=10)

    # Add a scrollbar to the canvas
    scrollbar = tk.Scrollbar(canvas, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    canvas.create_window((0, 0), window=frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Calculate the number of rows and columns needed
    num_students = len(names)
    rows = (num_students + 3) // 4  # Number of rows needed, rounded up
    cols = 4  # Number of columns

    # Display student information in a grid layout
    for i in range(num_students):
        row = i // cols
        col = i % cols

        label_timestamp = tk.Label(frame, text=f"Timestamp: {timestamps[i]}", font="Arial 10 italic", anchor="w")
        label_timestamp.grid(row=row * 6, column=col * 2, padx=5, pady=5, sticky="w")

        label_name = tk.Label(frame, text=f"Name: {names[i]}", font="Arial 12 bold", anchor="w")
        label_name.grid(row=row * 6 + 1, column=col * 2, padx=5, pady=5, sticky="w")

        label_branch = tk.Label(frame, text=f"Branch: {branches[i]}", font="Arial 10 italic", anchor="w")
        label_branch.grid(row=row * 6 + 2, column=col * 2, padx=5, pady=5, sticky="w")

        label_usn = tk.Label(frame, text=f"USN: {usns[i]}", font="Arial 10 italic", anchor="w")
        label_usn.grid(row=row * 6 + 3, column=col * 2, padx=5, pady=5, sticky="w")

        label_section = tk.Label(frame, text=f"Section: {sections[i]}", font="Arial 10 italic", anchor="w")
        label_section.grid(row=row * 6 + 4, column=col * 2, padx=5, pady=5, sticky="w")

        # Load and display student photo if available
        if photo_urls[i]:
            try:
                response = requests.get(photo_urls[i])
                img = Image.open(BytesIO(response.content))
                img = img.resize((100, 100), Image.Resampling.LANCZOS)
                img_tk = ImageTk.PhotoImage(img)
                label_image = tk.Label(frame, image=img_tk)
                label_image.image = img_tk  # Keep a reference to prevent garbage collection
                label_image.grid(row=row * 6, column=col * 2 + 1, padx=5, pady=5)
            except Exception as e:
                label_no_image = tk.Label(frame, text=f"Error loading image: {e}", font="Arial 10 italic", anchor="w")
                label_no_image.grid(row=row * 6, column=col * 2 + 1, padx=5, pady=5, sticky="w")
        else:
            label_no_image = tk.Label(frame, text="No image available", font="Arial 10 italic", anchor="w")
            label_no_image.grid(row=row * 6, column=col * 2 + 1, padx=5, pady=5, sticky="w")

    # Update the canvas scroll region
    frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))
# Create and place the buttons
cse_button = tk.Button(page2, text="CSE", fg="indigo", bg="silver", font="Arial 13 bold italic", command=cse_function, borderwidth=0, height=1)
cse_button.place(x=580, y=320)

main.mainloop()
