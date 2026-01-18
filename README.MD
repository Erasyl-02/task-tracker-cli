# CLI Task Tracker 📝

A simple, robust Command Line Interface (CLI) application to manage your daily tasks. Built with pure Python, this project focuses on clean architecture, file I/O operations, and JSON data management.

## 🛠 Tech Stack
* **Language:** Python 3.x
* **Storage:** JSON (Local file-based database)
* **Modules:** `sys`, `json`, `datetime`, `pathlib`

## 🚀 Key Features
* **Full CRUD:** Create, Read, Update, and Delete tasks easily.
* **Smart ID Generation:** Uses generator expressions to find the next available ID, preventing duplicates even after deletions.
* **Status Tracking:** Switch tasks between `todo`, `in-progress`, and `done`.
* **Filtering:** View all tasks or filter them by their current status.
* **Timestamps:** Automatically tracks when a task was created and last updated.

## 💻 Installation & Usage

### Setup
1. Clone the repository.
2. Ensure you have Python installed.
3. Run commands directly from your terminal.

### Commands Reference

| Action | Command Example |
| :--- | :--- |
| **Add Task** | `python main.py add "Buy groceries"` |
| **List All Tasks** | `python main.py list` |
| **Filter by Status** | `python main.py list done` (or `todo` / `in-progress`) |
| **Update Description** | `python main.py update [ID] "New description"` |
| **Mark as Progress** | `python main.py mark-in-progress [ID]` |
| **Mark as Done** | `python main.py mark-done [ID]` |
| **Delete Task** | `python main.py delete [ID]` |

## 🏗 Project Architecture
The project follows a modular approach to ensure a **Separation of Concerns**:
* `main.py`: Entry point. Handles CLI arguments and user interaction.
* `logic.py`: Business logic layer. Manages data processing and validation.
* `storage.py`: Data access layer. Handles reading/writing to the JSON file.
* `data.json`: Local storage file (automatically created on first run).

## 🧠 Lessons Learned
* Implementing a **modular architecture** to keep code organized.
* Using **Generator Expressions** for memory-efficient data processing.
* Handling **Edge Cases** (input validation and "idiot-proofing").
* Managing local environments with `.gitignore`.

---
*Developed as part of a backend engineering learning journey.*