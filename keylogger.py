import tkinter as tk
from tkinter import messagebox, scrolledtext
from pynput import keyboard
import json
import threading
from datetime import datetime

# ---------------- GLOBAL VARIABLES ----------------
listener = None
is_logging = False
key_logs = []

TXT_FILE = "logs.txt"
JSON_FILE = "logs.json"

# ---------------- LOGGING FUNCTIONS ----------------
def on_press(key):
    global key_logs
    log_entry = {
        "event": "pressed",
        "key": str(key),
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    key_logs.append(log_entry)
    update_preview(log_entry)

def on_release(key):
    global key_logs
    log_entry = {
        "event": "released",
        "key": str(key),
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    key_logs.append(log_entry)
    update_preview(log_entry)

# ---------------- FILE HANDLING ----------------
def save_logs():
    with open(TXT_FILE, "w") as f:
        for log in key_logs:
            f.write(f"{log['time']} - {log['event']} - {log['key']}\n")

    with open(JSON_FILE, "w") as f:
        json.dump(key_logs, f, indent=4)

# ---------------- KEYLOGGER CONTROL ----------------
def start_keylogger():
    global listener, is_logging

    if is_logging:
        messagebox.showinfo("Info", "Keylogger is already running.")
        return

    is_logging = True
    status_label.config(text="Status: RUNNING", fg="green")

    listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release
    )
    listener.start()

def stop_keylogger():
    global listener, is_logging

    if not is_logging:
        messagebox.showinfo("Info", "Keylogger is not running.")
        return

    is_logging = False
    listener.stop()
    save_logs()
    status_label.config(text="Status: STOPPED", fg="red")

    messagebox.showinfo(
        "Stopped",
        "Keylogging stopped.\nLogs saved to logs.txt and logs.json"
    )

def clear_logs():
    global key_logs
    key_logs = []
    log_box.delete(1.0, tk.END)

# ---------------- GUI UPDATE ----------------
def update_preview(log):
    log_box.insert(
        tk.END,
        f"{log['time']} | {log['event']} | {log['key']}\n"
    )
    log_box.see(tk.END)

# ---------------- GUI DESIGN ----------------
root = tk.Tk()
root.title("Keystroke Logging Demonstration")
root.geometry("700x500")
root.resizable(False, False)

title = tk.Label(
    root,
    text="Keystroke Logging Demonstration",
    font=("Verdana", 16, "bold")
)
title.pack(pady=10)

status_label = tk.Label(
    root,
    text="Status: STOPPED",
    font=("Verdana", 12),
    fg="red"
)
status_label.pack(pady=5)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

start_btn = tk.Button(
    btn_frame,
    text="Start Keylogging",
    width=20,
    bg="green",
    fg="white",
    command=start_keylogger
)
start_btn.grid(row=0, column=0, padx=10)

stop_btn = tk.Button(
    btn_frame,
    text="Stop Keylogging",
    width=20,
    bg="red",
    fg="white",
    command=stop_keylogger
)
stop_btn.grid(row=0, column=1, padx=10)

clear_btn = tk.Button(
    root,
    text="Clear Preview",
    width=20,
    command=clear_logs
)
clear_btn.pack(pady=5)

log_box = scrolledtext.ScrolledText(
    root,
    width=80,
    height=15
)
log_box.pack(pady=10)

root.mainloop()
