# Keystroke Logging Demonstration System  
### Cyber Security Awareness Project (Python)

---

## 📌 Overview

The **Keystroke Logging Demonstration System** is an educational Python-based project
designed to demonstrate how keystroke logging works in a **controlled, ethical, and
user-consented environment**.

The objective of this project is **cyber security awareness**, not surveillance or
malicious activity. It helps students and learners understand how attackers may capture
keyboard inputs and why proper security measures are essential.

---

## 🎯 Project Objectives

- Demonstrate the working of keystroke logging techniques
- Create awareness about keyboard-based cyber attacks
- Show how sensitive input data can be captured on compromised systems
- Promote ethical understanding of offensive techniques for defensive learning
- Provide a transparent and user-controlled demonstration tool

---

## 🛠️ Features

- Interactive **Graphical User Interface (GUI)** using Tkinter  
- Manual **Start** and **Stop** control of keylogging  
- Real-time keystroke preview within the GUI  
- Keystroke logs saved in:
  - **Text format (.txt)** for readability
  - **JSON format (.json)** for structured analysis  
- Ethical design: no background execution, no auto-start  
- Clean and modular Python code

---

## 🧱 System Architecture (High-Level)

1. User interacts with the GUI  
2. User manually starts keylogging  
3. Keyboard events are captured in real time  
4. Keystrokes are processed with timestamps  
5. Logs are displayed and stored locally  
6. User manually stops keylogging  

---

## 🧑‍💻 Technologies Used

- **Python** – Core programming language  
- **pynput** – Capturing keyboard input events  
- **Tkinter** – Graphical User Interface  
- **JSON** – Structured log storage  
- **Text Files** – Human-readable logs  

---

## 📂 Project Structure
keystroke-logging-demonstration/
│
├── keylogger.py
├── README.md
├── requirements.txt
├── .gitignore
└── screenshots/
├── gui.png
└── logs.png

