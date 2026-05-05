import tkinter as tk
from tkinter import messagebox
import datetime
import time
import threading

HOST_PATH = r"C:\Windows\System32\drivers\etc\hosts"
REDIRECT = "127.0.0.1"

def format_website(name):
    """
    Convert simple names into website domains
    Example:
    facebook -> www.facebook.com
    youtube -> www.youtube.com
    """
    name = name.strip().lower()

    if "." not in name:
        return f"www.{name}.com"

    return name

def block_websites(websites, end_time):
    while True:
        current_time = datetime.datetime.now()
        if current_time < end_time:
            with open(HOST_PATH, "r+") as host_file:
                content = host_file.read()
                for website in websites:
                    if website not in content:
                        host_file.write(REDIRECT + " " + website + "\n")
            print("Websites blocked")

        else:
            with open(HOST_PATH, "r+") as host_file:
                content = host_file.readlines()
                host_file.seek(0)
                for line in content:
                    if not any(site in line for site in websites):
                        host_file.write(line)
                host_file.truncate()
            print("Blocking ended")
            break

        time.sleep(5)


def start_blocking():
    websites_input = website_entry.get()
    date_input = date_entry.get()
    time_input = time_entry.get()

    if not websites_input or not date_input or not time_input:
        messagebox.showerror("Error", "Please fill all fields")
        return

    try:
        end_time = datetime.datetime.strptime(
            date_input + " " + time_input,
            "%Y-%m-%d %H:%M"
        )

    except:
        messagebox.showerror(
            "Error",
            "Date/Time format should be:\nDate: YYYY-MM-DD\nTime: HH:MM"
        )
        return

    websites = [
        format_website(site)
        for site in websites_input.split(",")
    ]

    thread = threading.Thread(
        target=block_websites,
        args=(websites, end_time),
        daemon=True
    )

    thread.start()

    messagebox.showinfo(
        "Started",
        f"Blocking started for:\n{', '.join(websites)}"
    )


# GUI

root = tk.Tk()
root.title("Website Blocker")
root.geometry("400x300")

title = tk.Label(
    root,
    text="Website Blocker",
    font=("Arial", 18, "bold")
)
title.pack(pady=10)

# Websites

tk.Label(root, text="Website Names (comma separated)").pack()

website_entry = tk.Entry(root, width=40)
website_entry.pack(pady=5)

# Date

tk.Label(root, text="End Date (YYYY-MM-DD)").pack()

date_entry = tk.Entry(root, width=30)
date_entry.pack(pady=5)

# Time

tk.Label(root, text="End Time (HH:MM)").pack()

time_entry = tk.Entry(root, width=30)
time_entry.pack(pady=5)

# Button

start_button = tk.Button(
    root,
    text="Start Blocking",
    command=start_blocking,
    bg="red",
    fg="white",
    font=("Arial", 12)
)

start_button.pack(pady=20)

root.mainloop()