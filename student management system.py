from tkinter import*
from tkinter import ttk
import pymysql

class student:
    def __init__(self, root):
        self.root = root
        self.root.title('Student management system')
        self.root.geometry('1200x600+0+0')
        self.root.config(bg='powder blue')

        bg_color='#008080'
        Label(self.root, text='Student Management Sysytem', font='lucida 20 bold', bg=bg_color,bd=10,relief=RIDGE).pack(fill=X)

        #variables
        self.namevar = StringVar()
        self.rollvar = StringVar()
        self.gendervar = StringVar()
        self.emailvar = StringVar()
        self.contactvar = StringVar()
        self.addressvar = StringVar()
        self.dobvar = StringVar()
        self.searchby = StringVar()
        self.searchtext = StringVar()



        frame = Frame(self.root, bg='#00FFFF', bd=20, relief=GROOVE)
        frame.place(x=40, y=60, width=470, height=600)

        frame1 = Frame(self.root, bg='#00FFFF', bd=20, relief=GROOVE)
        frame1.place(x=520, y=60, width=800, height=600)

        title1 = Label(frame, text='Manage Students', font='lucida 20 bold',fg='#0000FF', bg='#00FFFF')
        title1.grid(row=0, columnspan=3, pady=10)

        name = Label(frame, text='Name', font='lucida 14 bold',fg='#0000FF', bg='#00FFFF')
        name.grid(row=2, column=0,padx=10, pady=10, sticky='w')

        rollno = Label(frame, text='Roll no.', font='lucida 14 bold', fg='#0000FF', bg='#00FFFF')
        rollno.grid(row=1, column=0,padx=10, pady=10, sticky='w')

        gender = Label(frame, text='Gender', font='lucida 14 bold', fg='#0000FF', bg='#00FFFF')
        gender.grid(row=3,padx=10, column=0, pady=10, sticky='w')

        combo_gender = ttk.Combobox(frame,textvar=self.gendervar, width=23, font='lucida 14',state='readonly')
        combo_gender['values'] = ('Male','Female','Others')
        combo_gender.grid(row=3,padx=10, column=1, pady=10)

        email = Label(frame, text='Email', font='lucida 14 bold', fg='#0000FF', bg='#00FFFF')
        email.grid(row=4,padx=10, column=0, pady=10, sticky='w')

        contact = Label(frame, text='Contact', font='lucida 14 bold', fg='#0000FF', bg='#00FFFF')
        contact.grid(row=5,padx=10, column=0, pady=10, sticky='w')

        DOB = Label(frame, text='D.O.B', font='lucida 14 bold', fg='#0000FF', bg='#00FFFF')
        DOB.grid(row=6,padx=10, column=0, pady=10, sticky='w')

        address = Label(frame, text='Address', font='lucida 14 bold', fg='#0000FF', bg='#00FFFF')
        address.grid(row=7,padx=10, column=0, pady=10, sticky='w')

        # entry

        nameentry = Entry(frame, textvar=self.namevar, width=25, font='lucida 14 bold')
        nameentry.grid(row=2, column=1, pady=10)
        rollnoentry = Entry(frame, textvar=self.rollvar,width=25, font='lucida 14 bold')
        rollnoentry.grid(row=1, column=1, pady=10)
        emailentry = Entry(frame, textvar=self.emailvar,width=25, font='lucida 14 bold')
        emailentry.grid(row=4, column=1, pady=10)
        dobentry = Entry(frame, textvar=self.dobvar,width=25, font='lucida 14 bold')
        dobentry.grid(row=6, column=1, pady=10)
        contactentry = Entry(frame, textvar=self.contactvar,width=25, font='lucida 14 bold')
        contactentry.grid(row=5, column=1, pady=10)
        addentry = Entry(frame, textvar=self.addressvar,width=25, font='lucida 14 bold')
        addentry.grid(row=7, column=1, pady=10)

        #frame2
        frame3 = Frame(self.root, bg='white')
        frame3.place(x=70, y=530, width=390, height=50)

        b1 = Button(frame3, text='Add',command=self.add_students, font='lucida 14 bold',width=6, relief=GROOVE, bd=10)
        b1.grid(row=0, column=0)
        b2 = Button(frame3, text='Update',command=self.update, font='lucida 14 bold', width=6, relief=GROOVE, bd=10)
        b2.grid(row=0, column=1)

        b3 = Button(frame3, text='Clear',command=self.clear, font='lucida 14 bold', width=6, relief=GROOVE, bd=10)
        b3.grid(row=0, column=2)
        b4 = Button(frame3, text='Delete',command=self.delete, font='lucida 14 bold', width=6, relief=GROOVE, bd=10)
        b4.grid(row=0, column=3)

        # frame3
        search = Label(frame1, text='Search_By', font='lucida 14 bold', fg='#0000FF', bg='#00FFFF')
        search.grid(row=0, column=0, pady=10, padx=10, sticky='w')

        search = ttk.Combobox(frame1, textvar=self.searchby,text='Select Option',state='readonly')
        search['values']=("Roll_no.")
        search.grid(row=0,column=1, pady=10)

        searchentry = Entry(frame1, width=15, textvar=self.searchtext, font='lucida 14 bold')
        searchentry.grid(row=0, column=2,padx=10, pady=10)

        searchbutton = Button(frame1, text='Search',command=self.searchdata, font='lucida 8 bold', width=13, relief=GROOVE, bd=10)
        searchbutton.grid(row=0, column=3,padx=10, pady=10)

        showbutton = Button(frame1, text='Show all',command=self.fetch_data, font='lucida 8 bold', width=13, relief=GROOVE, bd=10)
        showbutton.grid(row=0, column=4, padx=10, pady=10)

        # Output frame
        frame4 = Frame(frame1, bd=4, bg='white')
        frame4.place(x=25, y=80, width=700, height=470)

        scrollx = Scrollbar(frame4, orient=HORIZONTAL)
        scrolly = Scrollbar(frame4, orient=VERTICAL)
        self.table = ttk.Treeview(frame4, columns=('rollno','name','gender','email','contact','dob','address'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.config(command=self.table.xview)
        scrolly.config(command=self.table.yview)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)

        self.table.heading('rollno', text='Roll no.')
        self.table.heading('name', text='Name')
        self.table.heading('gender', text='Gender')
        self.table.heading('email', text='Email')
        self.table.heading('contact', text='Contact')

        self.table.heading('dob', text='D.O.B')
        self.table.heading('address', text='Address')
        self.table['show']='headings'
        self.table.pack(fill=BOTH, expand=1)
        self.table.bind('<Button-1>',self.received)
        self.fetch_data()



    def add_students(self):
        con=pymysql.connect(host='localhost',user='root',password='',database='new_manage')
        cur = con.cursor()
        cur.execute('insert into student values(%s,%s,%s,%s,%s,%s,%s)',(self.rollvar.get(),
                                                                        self.namevar.get(),
                                                                        self.gendervar.get(),
                                                                        self.emailvar.get(),self.contactvar.get(),
                                                                        self.dobvar.get(),
                                                                        self.addressvar.get()
                                                                        ))

        con.commit()
        self.clear()
        self.fetch_data()
        con.close()
    def fetch_data(self):
        con = pymysql.connect(host='localhost', user='root', password='', database='new_manage')
        cur = con.cursor()
        cur.execute('select * from student')
        rows = cur.fetchall()
        if len(rows)!=0:
            self.table.delete(*self.table.get_children())
            for row in rows:
                self.table.insert('',END,values=row)

            con.commit()
        con.close()


    def clear(self):
        self.rollvar.set('')
        self.namevar.set('')
        self.gendervar.set('')
        self.emailvar.set('')
        self.contactvar.set('')
        self.dobvar.set('')
        self.addressvar.set('')

    def received(self,event):
        cur_row = self.table.focus()
        content = self.table.item(cur_row)

        row=content['values']
        self.rollvar.set(row[0])
        self.namevar.set(row[1])

        self.gendervar.set(row[2])
        self.emailvar.set(row[3])
        self.contactvar.set(row[4])
        self.dobvar.set(row[5])
        self.addressvar.set(row[6])
    def update(self):
        con = pymysql.connect(host='localhost', user='root', password='', database='new_manage')
        cur = con.cursor()
        cur.execute('update student set name=%s,gender=%s,email=%s,contact=%s,dob=%s,address=%s where rollno=%s', (self.namevar.get(),
                                                                         self.gendervar.get(),
                                                                         self.emailvar.get(), self.contactvar.get(),
                                                                         self.dobvar.get(),
                                                                         self.addressvar.get(), self.rollvar.get()

                                                                         ))

        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def delete(self):
        con = pymysql.connect(host='localhost', user='root', password='', database='new_manage')
        cur = con.cursor()
        cur.execute('delete from student where rollno=%s',self.rollvar.get())

        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def searchdata(self):
        con = pymysql.connect(host='localhost', user='root', password='', database='new_manage')
        cur = con.cursor()
        cur.execute("select * from student where rollno=%s",(self.searchtext.get()))
        rows = cur.fetchall()
        if len(rows) != 0:
            self.table.delete(*self.table.get_children())
            for row in rows:
                self.table.insert('', END, values=row)
            con.commit()
        con.close()


root=Tk()
x1 = student(root)
root.mainloop()