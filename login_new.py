from tkinter import *
from tkinter import messagebox
from PIL import ImageTk

class login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login system")
        self.root.wm_iconbitmap("icon.ico")
        self.root.geometry("1000x680+10+10")
        self.root.resizable(False, False)
        ############ Background Image ##############
        self.bg=ImageTk.PhotoImage(file="images/final.jpg")
        self.bg_image=Label(self.root, image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        ########### Login Frame 1 #################
        Frame_Login=Frame(self.root,bg="white")
        Frame_Login.place(x=80,y=200,height=380,width=600)

        title=Label(Frame_Login,text="Login Here",font=("arial 30 bold"),fg="#d77337",bg="white").place(x=90,y=30)
        desc = Label(Frame_Login, text="Programmers Login Area",font=("Goudy Old Style",15,"bold"),fg="#d77337",bg="white").place(x=90, y=80)
        user=Label(Frame_Login, text="Username",font=("Goudy Old Style",15,"bold"),fg="gray",bg="white").place(x=90, y=120)
        self.user_entry=Entry(Frame_Login,font=("times new roman",15),bg="lightgray")
        self.user_entry.place(x=90,y=170,width=350,height=35)

        user_pass=Label(Frame_Login, text="Password",font=("Goudy Old Style",15,"bold"),fg="gray",bg="white").place(x=90,y=210)
        self.pass_entry=Entry(Frame_Login,font=("times new roman",15),bg="lightgray")
        self.pass_entry.place(x=90,y=240,width=350,height=35)

        Login_button=Button(self.root,command=self.Login,text="Login",fg="white",bg="#d77337",activebackground="#d77337",activeforeground="white",font=("times new roman",20))
        Login_button.place(x=285,y=557,width=180,height=40)

        For_button=Button(Frame_Login,command=self.forget_pass,text="Forget Password",fg="#d77337",bg="white",activebackground="white",activeforeground="#d77337",bd=0,font=("times new roman",12))
        For_button.place(x=90,y=280,width=180,height=40)

    def Login(self):
        if self.user_entry.get()=="" or self.pass_entry.get()=="":
            messagebox.showerror("error","The Password or Username is Required.",parent=self.root)
        elif self.user_entry.get()!="Devansh" or self.pass_entry.get()!="Devansh":
            messagebox.showerror("error","The Password or Username is Invalid.",parent=self.root)
        else:
            messagebox.showinfo("Success","Welcome Devansh!",parent=self.root)
    def forget_pass(self):
        messagebox.showinfo("Forget Password","This is forget password button!")

root=Tk()
obj=login(root)
root.mainloop()
