import tkinter as tk
import subprocess

button_width = 10

def ou_script():
    domain = domain_entry.get()
    domain_s = domain.split(".")
    domain_line = (f"dc={domain_s[0]},dc={domain_s[1]}")
    new_ou = ou_entry.get()
    ou_scrip = f"New-ADOrganizationalUnit -Name \"{new_ou}\" -Path \"{domain_line}\""
    text01.delete("1.0", tk.END)
    text01.insert(tk.END, ou_scrip)
    with open("script.ps1", "w") as file:
        file.write(ou_scrip)

def group_script():
    domain = domain_entry.get()
    domain_s = domain.split(".")
    ou = gou_entry.get()
    group = group_entry01.get()
    domain_line = (f"ou={ou},dc={domain_s[0]},dc={domain_s[1]}")
    group_script = f"New-ADGroup -Name \"{group}\" -GroupScope Global -Path \"{domain_line}\""
    text01.delete("1.0", tk.END)
    text01.insert(tk.END, group_script)
    with open("script.ps1", "w") as file:
        file.write(group_script)

def user_script():
    domain = domain_entry.get()
    domain_s = domain.split(".")
    ou = uou_entry.get()
    user = user_entry02.get()
    user_principal_name = f"{user}@{domain}"
    domain_line = (f"ou={ou},dc={domain_s[0]},dc={domain_s[1]}")
    user_script= f"New-ADUser -Name \"{user}\" -UserPrincipalName \"{user_principal_name}\" -DisplayName \"{user}\" -AccountPassword(ConvertTo-SecureString \"1234abcD\" -AsPlainText -Force) -Enabled $true -ChangePasswordAtLogon $false -Path \"{domain_line}\""
    text01.delete("1.0", tk.END)
    text01.insert(tk.END, user_script)
    with open("script.ps1", "w") as file:
        file.write(user_script)

def create_ou():
    pass

def open_script():
    subprocess.run(["notepad.exe", "script.ps1"])

def open_bat_file():
    bat_txt = "powershell.exe -ExecutionPolicy Bypass -File script.ps1"
    with open("script.bat", "w") as bat_file:
        bat_file.write(bat_txt)
    subprocess.run(["notepad.exe", "script.bat"])




window = tk.Tk()
window.geometry("500x450")

frame01 = tk.Frame(window)
frame01.grid(row = 0, column = 0, columnspan = 2)
frame02 = tk.Frame(window)
frame02.grid(row = 1, column = 0, columnspan = 4)
frame03 = tk.Frame(window)
frame03.grid(row = 2, column = 0, columnspan = 1)
frame04 = tk.Frame(window)
frame04.grid(row = 3, column = 0, columnspan = 1)

label01 = tk.Label(frame01, text = "Create OU's, Groups and Users", font=("Arial", "20"))
label01.grid(row = 0, column = 0, columnspan = 3)

domain_label = tk.Label(frame02, text = "Domain Name:", font=("Arial", "16"))
domain_label.grid(row = 0, column = 0)
domain_entry = tk.Entry(frame02, width = "15")
domain_entry.grid(row = 0, column = 1)

ou_label = tk.Label(frame02, text = "New OU:", font=("Arial", "16"))
ou_label.grid(row = 1, column = 0)
ou_entry = tk.Entry(frame02, width = "15")
ou_entry.grid(row = 1, column = 1)
create_ou_script_button = tk.Button(frame02, text = "create script", width = button_width, command = ou_script)
create_ou_script_button.grid(row = 1, column = 4)


group_label = tk.Label(frame02, text = "New Group:", font=("Arial", "16"))
group_label.grid(row = 2, column = 0)
group_entry01 = tk.Entry(frame02, width = "15")
group_entry01.grid(row = 2, column = 1)
gou_label = tk.Label(frame02, text = "OU:", font=("Arial", "16"))
gou_label.grid(row = 2, column = 2)
gou_entry = tk.Entry(frame02, width = "15")
gou_entry.grid(row = 2, column = 3)

create_g_script_button = tk.Button(frame02, text = "create script", width = button_width, command = group_script)
create_g_script_button.grid(row = 2, column = 4)

user_label = tk.Label(frame02, text = "New User:", font=("Arial", "16"))
user_label.grid(row = 3, column = 0)
user_entry02 = tk.Entry(frame02, width = "15")
user_entry02.grid(row = 3, column = 1)
uou_label = tk.Label(frame02, text = "OU:", font=("Arial", "16"))
uou_label.grid(row = 3, column = 2)
uou_entry = tk.Entry(frame02, width = "15")
uou_entry.grid(row = 3, column = 3)
create_user_script_button = tk.Button(frame02, text = "create script", width = button_width, command = user_script)
create_user_script_button.grid(row = 3, column = 4)

text01 = tk.Text(frame03,  width=60,  height=15)
text01.grid(columnspan = 2, pady = 10, padx = 10)

#copy_scrip = tk.Button(frame03, text = "copy script (PS)", width = button_width, command = copy_scrip)
#copy_scrip.grid()
open_scrip = tk.Button(frame03, text = "open script.ps1", width = button_width+3, command = open_script)
open_scrip.grid(row = 1, column = 0)
open_bat = tk.Button(frame03, text = "open script.bat", width = button_width+3, command = open_bat_file)
open_bat.grid(row = 1, column = 1)


window.mainloop()
