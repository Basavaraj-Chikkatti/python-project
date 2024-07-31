#importing tkinter module,sqlite3 database and messagebox
import tkinter as tk
import sqlite3 as sql
import tkinter.messagebox as msgbox

# Creating the main window for the login page
form = tk.Tk()
form.title('LOGIN')
form.config(bg='lightblue')
form.geometry('300x200')
my=tk.Label(form,text='U15IG22S0105',bg='white',fg='red',font=('Times new Roman',15,'bold'))
my.grid(row=0, column=2, sticky=tk.W, padx=10, pady=5)

# Adding labels and entry widgets for UUCMSNO and PASSWORD
lbluno = tk.Label(form, text='UUCMSNO',bg='lightyellow',fg='red',font=('Times new Roman',8,'bold'))
lbluno.grid(row=1, column=1, sticky=tk.W, padx=10, pady=5)
etuno = tk.Entry(form, width=20)
etuno.grid(row=1, column=2, padx=10, pady=5)

lblpas = tk.Label(form, text='PASSWORD',bg='lightyellow',fg='red',font=('Times new Roman',8,'bold'))
lblpas.grid(row=2, column=1, sticky=tk.W, padx=10, pady=5)
etpas = tk.Entry(form, width=20, show='*')
etpas.grid(row=2, column=2, padx=10, pady=5)

# Function to handle login
def login():
    #reading data from entry fields
    uno = etuno.get()
    password = etpas.get()
    #checking uno and password
    con=sql.connect("studentdata1.db")
    cur=con.cursor()
    cur.execute('select * from studentdata123 where uno=? and password=?',(uno,password))
    result=cur.fetchone()
    con.close()
    if result:
        msgbox.showinfo("Message","Login Successfull!")
    else:
        msgbox.showinfo("Message","Enter Valid UUCMSNO and PASSWORD")
    

# Adding the LOGIN button and linking it to the login function
btnlogin = tk.Button(form, text='LOGIN', command=login, bg='lightgreen',fg='blue',font=('italic',8,'bold'))
btnlogin.grid(row=3, column=2, sticky=tk.W, columnspan=1, padx=10, pady=5)

# Function to handle registration 
def reg():
    from tkinter import ttk
    form = tk.Tk()
    form.title('REGISTRATION')
    form.config(bg='lightblue')
    form.geometry('300x300')
    me=tk.Label(form,text='U15IG22S0105',bg='white', fg='red',font=('Times new Roman',15,'bold'))
    me.grid(row=0, column=1, sticky=tk.W, padx=10, pady=5)
    # creating Labels and Entry widgets for uucmsno
    lbluno = tk.Label(form, text='UUCMSNO',bg='lightyellow',fg='red',font=('Times new Roman',8,'bold'))
    lbluno.grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
    etuno = tk.Entry(form, width=20)
    etuno.grid(row=2, column=1, padx=10, pady=5)

    # creating Labels and Entry widgets for name
    lblname = tk.Label(form, text='NAME',bg='lightyellow',fg='red',font=('Times new Roman',8,'bold'))
    lblname.grid(row=3, column=0, sticky=tk.W, padx=10, pady=5)
    etname = tk.Entry(form, width=20)
    etname.grid(row=3, column=1, padx=10, pady=5)

    # creating Labels and Entry widgets for course
    lblcourse = tk.Label(form, text='COURSE',bg='lightyellow',fg='red',font=('Times new Roman',8,'bold'))
    lblcourse.grid(row=4, column=0, sticky=tk.W, padx=10, pady=5)
    options = ['BA', 'BSC', 'BCOM', 'BCA', 'BBA']
    course = ttk.Combobox(form, values=options, state='readonly')
    course.grid(row=4, column=1, padx=10, pady=5)

    # creating Labels and Entry widgets for semister
    sem = tk.Label(form, text='SEMESTER',bg='lightyellow',fg='red',font=('Times new Roman',8,'bold'))
    sem.grid(row=5, column=0, sticky=tk.W, padx=10, pady=5)
    options = ['1st', '2nd', '3rd', '4th', '5th', '6th']
    semvar = ttk.Combobox(form, values=options, state='readonly')
    semvar.grid(row=5, column=1, padx=10, pady=5)

    # creating Labels and Entry widgets for password
    pas = tk.Label(form, text='PASSWORD',bg='lightyellow',fg='red',font=('Times new Roman',8,'bold'))
    pas.grid(row=6, column=0, sticky=tk.W, padx=10, pady=5)
    etpas = tk.Entry(form, width=15, show='*')
    etpas.grid(row=6, column=1, padx=10, pady=5)

    # Gender selection using radio button and creating gender lable
    gen = tk.Label(form, text='GENDER',bg='lightyellow',fg='red',font=('Times new Roman',8,'bold'))
    gen.grid(row=7, column=0, sticky=tk.W, padx=10, pady=5)
    genvar = tk.StringVar()
    genvar.set("Male")
    rdbmale = tk.Radiobutton(form,text="Male", variable=genvar, value="Male",bg='lightblue',font=('italic',8,'bold'))
    rdbfemale = tk.Radiobutton(form,text="Female", variable=genvar, value="Female",bg='lightblue',font=('italic',8,'bold'))
    rdbmale.grid(row=7, column=1,sticky=tk.W, padx=10, pady=5)
    rdbfemale.grid(row=7, column=1,sticky=tk.E, padx=10, pady=5)

    # Function to save data
    def save():
        uno = etuno.get()
        name = etname.get()
        course_val = course.get()
        sem_val = semvar.get()
        password = etpas.get()
        gender = genvar.get()
    
        # Check if any field is left blank
        if uno == '' or name == '' or course_val == '' or sem_val == '' or password == '':
            msgbox.showinfo('Message', 'All fields need to be filled')
            return  # Exit the function if any field is blank

        try:
            # Connecting to the SQLite database 'studentdata1.db'
            con = sql.connect("studentdata1.db")
            cur = con.cursor()
        
            # Creating the table if it doesn't exist
            st = """
                CREATE TABLE IF NOT EXISTS studentdata123 (
                    uno VARCHAR(15) PRIMARY KEY,
                    name VARCHAR(20),
                    course VARCHAR(7),
                    sem VARCHAR(7),
                    password VARCHAR(12),
                    gender VARCHAR(6)
                )
            """
            cur.execute(st)
        
            # Inserting the retrieved values into the table
            cur.execute("INSERT INTO studentdata123 (uno, name, course, sem, password, gender) VALUES (?, ?, ?, ?, ?, ?)", 
                        (uno, name, course_val, sem_val, password, gender))
        
            # Committing the transaction
            con.commit()
        
            # Displaying a success message
            msgbox.showinfo("Message", "Data Saved Successfully")
    
        except sql.Error as e:
            # Handling any SQLite errors
            msgbox.showerror("Error", "enter different uucmsno")
    
        finally:
        # Closing the database connection
            if con:
                con.close()

    #creating save button
    btnsave = tk.Button(form, text='SAVE', command=save, bg='lightgreen',fg='blue',font=('italic',8,'bold'))
    btnsave.grid(row=8, column=1, columnspan=2,sticky=tk.W, padx=10, pady=5)

    # Function to display data
    def display():
        #Connecting to the SQLite database
        con = sql.connect('studentdata1.db')
        #creating cursor to interact with database
        cur = con.cursor()
        #selecting data from the table
        cur.execute("SELECT uno, name, course, sem, gender FROM studentdata123")
        #fetching all rows from the table
        rows = cur.fetchall()
        con.close()
        #creating display form and giving name to the form
        display_form = tk.Tk()
        display_form.title("Student Details")
        #creating a treeview widget to display the data
        tree = ttk.Treeview(display_form, columns=('UUCMSNO', 'NAME', 'COURSE', 'SEM', 'GENDER'), show='headings')
        #setting up the column headings
        tree.heading('UUCMSNO', text='UUCMSNO')
        tree.heading('NAME', text='NAME')
        tree.heading('COURSE', text='COURSE')
        tree.heading('SEM', text='SEM')
        tree.heading('GENDER', text='GENDER')
        # Inserting the rows of data into the Treeview
        for row in rows:
            tree.insert('', tk.END, values=row)
        #Packing the Treeview widget to make it visible
        tree.pack()
        #running the main event loop for display the data
        display_form.mainloop()
    #Creating the DISPLAY button and linking it to the display function
    btndis = tk.Button(form, text='DISPLAY', command=display, bg='lightgreen',fg='blue',font=('italic',8,'bold'))
    btndis.grid(row=8, column=1, columnspan=2,sticky=tk.E, padx=10, pady=5)
def regi():
	form.destroy()
	reg()


# Adding the REGISTER button and linking it to the reg function
btnreg = tk.Button(form, text='REGISTER', command=regi, bg='lightgreen',fg='blue',font=('italic',8,'bold'))
btnreg.grid(row=3, column=2, sticky=tk.E, columnspan=20, padx=10, pady=5)

# Running the main event loop
form.mainloop()