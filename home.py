from tkinter import *
from tkinter import messagebox

from PIL import ImageTk, Image

from LoginDbHelper import *


class HomePage():
    def __init__(self, root):
        self.root = root  # passing the same root rather than creating a new root
        self.frame = Frame(self.root, height=400, width=700, bg="gray")
        self.frame.pack(fill=BOTH, expand=True)
        self.setup_homepage()
        # a method that will set my homepage

    def setup_homepage(self):
        self.add_header_section()
        # a method that has all the header

        self.body_frame = Frame(self.frame, bg="white", height=300, width=600)
        self.body_frame.pack(side=TOP, fill=X)
        self.body_frame.pack_propagate(0)

        self.lblFrame = LabelFrame(self.body_frame, width=250, text="Type Of Login", height=100, font=('Times', 15),
                                   bg="white", borderwidth=3)
        self.lblFrame.pack(anchor=CENTER, pady=20)

        self.admin_login_b = Button(self.lblFrame, text="Admin Login", command=lambda: self.login("admin"))
        self.admin_login_b.grid(row=0, column=0, padx=20, pady=10)
        self.user_login_b = Button(self.lblFrame, text="User Login", command=lambda: self.login("user"), font=('', 10))
        self.user_login_b.grid(row=0, column=1, padx=20, pady=10)
        self.lblFrame.grid_propagate(0)
        self.frame.pack_propagate(0)

    def add_header_section(self):
        # self.header_frame = Frame(self.frame, height=150, width=600)
        # self.header_frame.pack(fill=X, side=TOP)
        # self.header_frame.grid_propagate(0)
        # self.raw_login_image = Image.open("Login_Icon.png")
        # self.raw_login_image = self.raw_login_image.resize((120,100))
        # self.login_image
        self.header_frame = Frame(self.frame, height=150, width=600)
        self.header_frame.pack(fill=X, side=TOP)
        self.header_frame.grid_propagate(0)
        self.raw_login_image = Image.open("Login4.jpeg")
        self.raw_login_image = self.raw_login_image.resize((120, 100))
        self.login_img = ImageTk.PhotoImage(self.raw_login_image)
        self.login_label = Label(self.header_frame, image=self.login_img)
        # self.login_label.image = self.login_img
        self.login_label.grid(row=0, column=0, padx=20, pady=20)
        self.welcome_label = Label(self.header_frame, text=" Welcome to My Application", font=("Times", 30))
        self.welcome_label.grid(row=0, column=1)

    def login(self, login_type):
        self.temp_root = Toplevel()
        self.temp_root.title(f"{login_type}login")
        self.temp_frame = Frame(self.temp_root, height=300, width=500, bg="gray")
        self.temp_frame.pack()
        self.lab = Label(self.temp_frame, width=50, text="Enter Login Details below")
        self.lab.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        self.l1 = Label(self.temp_frame, width=20, text="Enter Username: ")
        self.l2 = Label(self.temp_frame, width=20, text="Enter Password: ")

        self.e_username = Entry(self.temp_frame, width=30, fg='black', bg='white')
        self.e_username.focus_set()
        self.e_pwd = Entry(self.temp_frame, width=30, fg='black', bg='white', show='*')
        self.l1.grid(row=1, column=0, padx=10, pady=10)
        self.l2.grid(row=2, column=0, padx=10, pady=10)

        self.e_username.grid(row=1, column=1, padx=10, pady=10)
        self.e_pwd.grid(row=2, column=1, padx=10, pady=10)

        self.b1 = Button(self.temp_frame, text="Submit", height=2, width=10,
                         command=lambda: self.authenticate(login_type))
        self.b1.grid(row=3, column=0, padx=10, sticky='e')

        self.b2 = Button(self.temp_frame, text="Reset", height=2, width=10, command=self.reset)
        self.b2.grid(row=3, column=1, padx=10, sticky='w')
        self.temp_frame.grid_propagate(0)

    def reset(self):
        self.e_username.delete(0, END)
        self.e_pwd.delete(0, END)
        # self.e_re_pwd.delete(0,END)
        self.e_username.focus_set()

    def authenticate(self, login_type):
        user = self.e_username.get()
        pwd = self.e_pwd.get()

        params = (user, pwd)

        if login_type == "admin":
            query = "Select * from practice_admin where Username=%s and Password=SHA(%s)"
        elif login_type == "user":
            query = "Select * from practice_user where Username=%s and Password=SHA(%s)"
        res = get_data(query, params)
        print(res)

        if (res is None):
            messagebox.showerror('Incorrect credentials ', 'The Username or Password Doesnt match. Please re-enter')
            self.temp_root.tkraise()
            self.reset()
        elif (login_type == "admin"):
            self.temp_root.destroy()
            # messagebox.showinfo("Login Succesfully","You have Logined Succesfylly as Admin")
            print("Login Done!")
            self.admin_page(user)
        else:
            self.temp_root.destroy()
            self.user_page(user)

    def user_page(self, username):
        self.lblFrame.destroy()
        self.header_frame.destroy()
        self.l_account = Label(self.body_frame, text="USER ACCOUNT")
        self.l_account.grid(row=0, column=0, pady=10)
        self.l_name = Label(self.body_frame, text=f"WELCOME , {username}")
        self.l_name.grid(row=1, column=0, pady=10)

    def admin_page(self, username):
        self.lblFrame.destroy()
        self.l_account = Label(self.body_frame, text=f"ADMIN ACCOUNT")
        self.l_account.grid(row=0, column=0, pady=10)
        self.l_name = Label(self.body_frame, text=f"WELCOME, {username}")
        self.l_name.grid(row=0, column=1, pady=10)
        self.lab = Label(self.body_frame, width=50, text="Enter below details to create a new user account")
        self.lab.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
        self.l1 = Label(self.body_frame, width=20, text="Enter username: ")
        self.e_username = Entry(self.body_frame, width=30, fg='black', bg='white')
        self.e_username.focus_set()
        self.e_pwd = Entry(self.body_frame, width=30, fg='black', bg='white', show='*')
        self.show_pwd = IntVar()
        self.show_pwd_check = Checkbutton(self.body_frame, text="Show", bg="white", command=self.show_hide_pwd,
                                          variable=self.show_pwd)
        self.l2 = Label(self.body_frame, width=20, text="Enter password: ")
        self.e_re_pwd = Entry(self.body_frame, width=30, fg='black', bg='white', show='*')
        self.l3 = Label(self.body_frame, width=20, text="Re-enter password: ")

        self.l1.grid(row=2, column=1, padx=10, pady=10)
        self.l2.grid(row=3, column=1, padx=10, pady=10)
        self.l3.grid(row=4, column=1, padx=10, pady=10)
        self.e_username.grid(row=2, column=2, padx=10, pady=10)
        self.e_pwd.grid(row=3, column=2, padx=10, pady=10)
        self.show_pwd_check.grid(row=3, column=3, padx=2, pady=10)

        self.e_re_pwd.grid(row=4, column=2, padx=10, pady=10)
        self.b1 = Button(self.body_frame, text="Create user", height=2, width=10, command=self.create_user)
        self.b1.grid(row=5, column=1, columnspan=2, padx=10)
        self.b2 = Button(self.body_frame, text="Reset", height=2, width=10, command=self.reset)
        self.b2.grid(row=5, column=2, columnspan=2, padx=10)

    def show_hide_pwd(self):
        if self.show_pwd.get() == 1:
            self.e_pwd.config(show="")
        else:
            self.e_pwd.config(show="*")

    def create_user(self):
        user = self.e_username.get()
        pwd = self.e_pwd.get()
        re_pwd = self.e_re_pwd.get()
        if (pwd != re_pwd):
            messagebox.showerror("Mismatch", "Passwords don't match. Please re-enter")
        else:
            params = (user, pwd)
            query = "Insert into practice_user(Username,Password) Values(%s,SHA(%s))"
            execute_query(query, params)
            messagebox.showinfo('Success!', f'User with username {user} created successfully. Please login again.')
            self.body_frame.destroy()
            self.header_frame.destroy()
            self.setup_homepage()


# Toplevel() creates a temp window/ child window


root = Tk()

h = HomePage(root)
root.mainloop()
