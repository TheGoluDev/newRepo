# Copilot Instructions for AI Coding Agents

## Project Overview
This workspace contains small Python scripts for basic tasks such as seat booking (`day2.py`), task management (`day.py`), and student data storage (`day3.py`). Each script is standalone and does not use external dependencies or frameworks.

## File Structure and Purpose
- `day.py`: Implements a simple CLI for saving and displaying user tasks in a text file (`userTasks.txt`).
- `day2.py`: Provides a seat booking system for a bus, using a dictionary to track seat status. User input is used to book seats and display availability.
- `day3.py`: Demonstrates basic dictionary usage for storing student data.
- `highscore.txt`, `userTasks.txt`: Text files used for persistent storage by scripts.

## Key Patterns and Conventions
- **No external dependencies**: All scripts use only Python's built-in functions and modules.
- **Persistent storage**: Data is saved in plain text files using file I/O (`open`, `read`, `write`).
- **User interaction**: Scripts use `input()` for CLI interaction and loop until the user exits.
- **Dictionary usage**: Data structures are primarily Python dictionaries for mapping keys to values (e.g., seat numbers, student attributes).
- **Error handling**: Minimal, mostly using `try/except` for file operations.
- **No build or test workflows**: There are no automated build, test, or CI/CD processes defined in this codebase.

## Examples
- **Seat Booking (day2.py):**
  ```python
  seats = {"seat_1": "NOT_BOOKED", ...}
  # User books a seat by entering seat number; status changes to "BOOKED".
  ```
- **Task Management (day.py):**
  ```python
  with open("userTasks.txt", "a") as f:
      f.write(f'{user_task_input}\n')
  ```

## How to Extend
- Add new scripts as separate `.py` files following the pattern of using dictionaries and text files for storage.
- For persistent data, use simple file I/O; avoid databases or external libraries unless necessary.
- Keep user interaction via CLI (`input()`/`print()`).


## Integration Points
- None. Scripts are independent and do not communicate with each other.

## Recommendations for AI Agents
- When generating new scripts, follow the pattern of dictionary-based data management and text file persistence.
- Keep code simple and readable; avoid unnecessary complexity.
- Reference existing scripts for examples of user interaction and file handling.

---

If any section is unclear or missing important details, please provide feedback to improve these instructions.
