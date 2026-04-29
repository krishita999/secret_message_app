from tkinter import *
from tkinter import messagebox
import base64
import os

last_result = ""
def encrypt():
    global last_result

    password = code.get()

    if password == "":
        messagebox.showerror("Encryption", "Enter password")
        return

    if password != "1234":
        messagebox.showerror("Encryption", "Invalid password")
        return

    message = text1.get(1.0, END)

    if message.strip() == "":
        messagebox.showerror("Encryption", "Enter message")
        return

    encode_message = message.encode("ascii")
    base64_bytes = base64.b64encode(encode_message)
    encrypt = base64_bytes.decode("ascii")

    last_result = encrypt

    screen1 = Toplevel(screen)
    screen1.title("Encryption")
    screen1.geometry("400x200")
    screen1.configure(bg="#ed3833")

    Label(screen1, text="ENCRYPT", font=("Arial", 12, "bold"),
          fg="white", bg="#ed3833").place(x=10, y=10)

    text2 = Text(screen1, font=("Arial", 10),
                 bg="white", relief=SOLID, bd=1, wrap=WORD)
    text2.place(x=10, y=40, width=380, height=120)

    text2.insert(END, encrypt)

def decrypt():
    global last_result

    password = code.get()

    if password == "":
        messagebox.showerror("Decryption", "Enter password")
        return

    if password != "1234":
        messagebox.showerror("Decryption", "Invalid password")
        return

    message = text1.get(1.0, END)

    if message.strip() == "":
        messagebox.showerror("Decryption", "Enter encrypted text")
        return

    try:
        base64_bytes = base64.b64decode(message)
        decrypt = base64_bytes.decode("ascii")
        last_result = decrypt

    except:
        messagebox.showerror("Decryption", "Invalid encrypted text")
        return

    # result window
    screen2 = Toplevel(screen)
    screen2.title("Decryption")
    screen2.geometry("400x200")
    screen2.configure(bg="#00bd56")

    Label(screen2, text="DECRYPT", font=("Arial", 12, "bold"),
          fg="white", bg="#00bd56").place(x=10, y=10)

    text2 = Text(screen2, font=("Arial", 10),
                 bg="white", relief=SOLID, bd=1, wrap=WORD)
    text2.place(x=10, y=40, width=380, height=120)

    text2.insert(END, decrypt)

def copy_text():
    global last_result

    if last_result == "":
        messagebox.showerror("Error", "Nothing to copy")
        return

    screen.clipboard_clear()
    screen.clipboard_append(last_result)

    messagebox.showinfo("Copied", "Result copied successfully")

def toggle_password():
    if show_password.get():
        entry.config(show="")
    else:
        entry.config(show="*")

def reset():
    code.set("")
    text1.delete(1.0, END)
def main_screen():
    global screen, code, text1, entry, show_password

    screen = Tk()
    screen.geometry("500x520")
    screen.title("Secure Message App")
    screen.config(bg="#f4f4f4")

    Label(text="Secure Message App",
          font=("Arial", 18, "bold"),
          fg="#2c3e50",
          bg="#f4f4f4").place(x=120, y=10)

    Label(text="Enter text for encryption and decryption",
          fg="black",
          font=("calibri", 13),
          bg="#f4f4f4").place(x=10, y=70)

    text1 = Text(font=("Arial", 12),
                 bg="white",
                 relief=SOLID,
                 bd=1,
                 wrap=WORD)
    text1.place(x=10, y=100, width=480, height=120)

    Label(text="Enter Password",
          fg="black",
          font=("calibri", 13),
          bg="#f4f4f4").place(x=10, y=230)

    code = StringVar()
    entry = Entry(textvariable=code,
                  width=19,
                  bd=1,
                  relief=SOLID,
                  font=("arial", 20),
                  show="*")
    entry.place(x=10, y=260, width=480)

    show_password = BooleanVar()
    Checkbutton(text="Show Password",
                variable=show_password,
                command=toggle_password,
                bg="#f4f4f4").place(x=10, y=305)

    Button(text="ENCRYPT",
           height="2",
           width=23,
           bg="#ed3833",
           fg="white",
           bd=0,
           command=encrypt).place(x=10, y=340)

    Button(text="DECRYPT",
           height="2",
           width=23,
           bg="#27ae60",
           fg="white",
           bd=0,
           command=decrypt).place(x=250, y=340)

    Button(text="RESET",
           height="2",
           width=65,
           bg="#1089ff",
           fg="white",
           bd=0,
           command=reset).place(x=10, y=390)

    Button(text="COPY",
           height="2",
           width=65,
           bg="#6c5ce7",
           fg="white",
           bd=0,
           command=copy_text).place(x=10, y=440)
    Label(text="Made by Krishita",
          font=("arial",10),
          bg="#f4f4f4",).place(relx=0.5,y=500,anchor="center")

    screen.mainloop()


main_screen()