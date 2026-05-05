Website Blocker

Overview

Website Blocker is a Python-based desktop application developed to help users reduce distractions and improve productivity by temporarily blocking access to selected websites. The application uses a simple graphical user interface (GUI) where users can enter website names and specify the blocking time.

The project works by modifying the system host file and redirecting selected websites to the localhost address (127.0.0.1), preventing them from opening in the browser.

Features

* Simple and user-friendly GUI
* Block multiple websites at once
* Automatic website unblocking
* Accepts simple website names
* Lightweight and easy to use
* Background blocking process using threading

Technologies Used

* Python
* Tkinter
* Datetime
* Time
* Threading

Requirements

* Python 3.x
* Windows Operating System
* Visual Studio Code or any Python IDE

How to Run

1. Install Python on your system.
2. Open the project folder in VS Code.
3. Run VS Code as Administrator.
4. Execute the Python file:
   python blocker.py

How It Works

1. Enter website names in the GUI.
2. Specify the blocking end date and time.
3. Click the “Start Blocking” button.
4. The selected websites are blocked by modifying the host file.
5. After the specified time ends, the websites are automatically unblocked.

Future Improvements

* Password protection
* Daily scheduling
* Usage statistics
* Dark mode GUI
* Cross-platform support

Author

Developed as a Python project for learning GUI development, file handling, and automation by Harsh Kanwar under the guidance of Dr. Abhishek Tomar.
