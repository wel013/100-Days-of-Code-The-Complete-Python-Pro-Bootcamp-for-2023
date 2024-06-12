from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD SEARCH ------------------------------- #
def search_password():
    web_string = web_entry.get()
    try:
        with open("data1.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showwarning(title="ERROR", message="NO DATA FILE FOUND")
    else:
        if web_string in data:
            messagebox.showinfo(title=web_string, message=f"Email: {data[web_string]['email']}\nPassword: {data[web_string]['password']}")
        else:
            messagebox.showinfo(title="Not Found", message=f"No details for {web_string} exists.")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # password_list = []

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    password_list = [random.choice(letters) for char in range(nr_letters)]

    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    password_list += [random.choice(symbols) for char2 in range(nr_symbols)]

    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)
    password_list += [random.choice(numbers) for char1 in range(nr_numbers)]
    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #   password += char
    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_password():
    web_string = web_entry.get()
    email_string = email_entry.get()
    password_string = password_entry.get()
    string = web_string + " | " + email_string + " | " + password_string
    new_data = {
        web_string: {
            "email": email_string,
            "password": password_string
        }
    }
    if len(web_string) == 0 or len(password_string) == 0 or len(email_string) == 0:
        messagebox.showwarning(title="Empty Fields", message="Please do not leave any of the fields empty")
    else:
        # ok = messagebox.askokcancel(title=web_string, message=f"These are the details entered: \nEmail: {email_string} "
        #                                                       f"\nPassword: {password_string} \nIs it okay to save?")
        # if ok:
        try:
            with open("data.json", "r") as f:
                data = json.load(f)
                #data.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as f:
                json.dump(new_data, f, indent=4)
                # f.write(string)
                # f.write('\n')
                # web_entry.delete(0, END)
                # email_entry.delete(0, END)
                # password_entry.delete(0, END)
        else:
            with open("data.json", "w") as f:
                data.update(new_data)
                json.dump(data, f, indent=4)
        finally:
            web_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

label_website = Label(text="Website:")
label_website.grid(column=0, row=1)

button_search = Button(text="Search", command=search_password, width=14)
button_search.grid(column=2, row=1)

label_email = Label(text="Email/Username:")
label_email.grid(column=0, row=2)

label_password = Label(text="Password:")
label_password.grid(column=0, row=3)


web_entry = Entry(width=25)
web_entry.grid(column=1, row=1, sticky=E)
web_entry.focus()

email_entry = Entry(width=43)
email_entry.grid(column=1, row=2, columnspan=2, sticky=E)
email_entry.insert(0, "myemail@gamil.com")

password_entry = Entry(width=25)
password_entry.grid(column=1, row=3, sticky=E)

button_gen_pass = Button(text="Generate Password", command=generate_password)
button_gen_pass.grid(column=2, row=3)

add_button = Button(width=36, text="Add", command=add_password)
add_button.grid(column=1, row=4, columnspan=2, sticky=E)

window.mainloop()

