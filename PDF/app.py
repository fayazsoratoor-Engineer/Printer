
import tkinter as tk
from tkinter import filedialog, messagebox
import os
import subprocess
import time
import pyautogui
import pyperclip

def select_pdf():
    file_path = filedialog.askopenfilename(
        title="Select Customer Certificate",
        initialdir=os.path.join(os.getcwd(), "PDF"),
        filetypes=[("PDF Files", "*.pdf")]
    )

    if file_path:
        pdf_path.set(file_path)


def open_whatsapp():
    name = name_entry.get().strip()
    file_path = pdf_path.get()

    if not name:
        messagebox.showerror(
            "Error", "Please enter customer name"
        )
        return

    if not file_path or not os.path.isfile(file_path):
        messagebox.showerror(
            "Error", "Please select a valid PDF"
        )
        return

    try:
        os.startfile("whatsapp://")
        root.after(4000, search_customer)

    except Exception as error:
        messagebox.showerror("Error", str(error))


def search_customer():
    name = name_entry.get().strip()

    # WhatsApp Desktop search shortcut
    pyautogui.hotkey("ctrl", "f")
    time.sleep(1)

    pyperclip.copy(name)
    pyautogui.hotkey("ctrl", "v")

    messagebox.showinfo(
        "Customer Search",
        "Check the search results carefully.\n"
        "Open the correct customer's chat.\n"
        "Attach the selected PDF and send manually."
    )


root = tk.Tk()
root.title("Fayaz Online Center PDF Sender")
root.geometry("500x350")
root.resizable(False, False)

tk.Label(
    root,
    text="FAYAZ ONLINE CENTER",
    font=("Arial", 19, "bold")
).pack(pady=20)

tk.Label(
    root,
    text="Customer Name",
    font=("Arial", 12)
).pack()

name_entry = tk.Entry(
    root,
    font=("Arial", 12),
    width=35
)
name_entry.pack(pady=10)

tk.Label(
    root,
    text="Customer Certificate PDF",
    font=("Arial", 12)
).pack()

pdf_path = tk.StringVar()

tk.Entry(
    root,
    textvariable=pdf_path,
    font=("Arial", 10),
    width=48
).pack(pady=10)

tk.Button(
    root,
    text="BROWSE PDF",
    command=select_pdf,
    width=20
).pack(pady=5)

tk.Button(
    root,
    text="OPEN WHATSAPP",
    command=open_whatsapp,
    bg="green",
    fg="white",
    font=("Arial", 12, "bold"),
    width=25
).pack(pady=20)

tk.Label(
    root,
    text="Select customer carefully before sending.",
    font=("Arial", 9)
).pack()

root.mainloop()
