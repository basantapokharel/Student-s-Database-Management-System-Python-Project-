# Student Database Management System

A simple Python-based command-line application for managing student and teacher data in a database. This system allows students to log in and view their academic results, while teachers can manage student and teacher records.

## Features

### For Students:
- **Login Verification**: Authenticate using name and ID.
- **Check Results**: View pass/fail status.
- **Highest Marks**: Find the highest marks in subjects.
- **Lowest Marks**: Find the lowest marks in subjects.
- **Percentage Calculation**: Compute overall percentage.
- **Rank Calculation**: Determine rank among students.

### For Teachers:
- **Student Management**:
  - Add new students
  - Search for students
  - Update student information
  - Delete students
  - Show all students
- **Teacher Management**:
  - Add new teachers
  - Search for teachers
  - Update teacher information
  - Delete teachers
  - Show all teachers

## Installation

1. **Clone the Repository** (if applicable):
   ```
   git clone <repository-url>
   cd python_project(student_database_management)
   ```

2. **Set Up Virtual Environment**:
   - On Windows:
     ```
     python -m venv env
     env\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     python3 -m venv env
     source env/bin/activate
     ```

3. **Install Dependencies**:
   Since this project uses only the standard library, no additional packages are needed. If `requirements.txt` is updated in the future, run:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Application**:
   ```
   python main.py
   ```

2. **Interactive Menu**:
   - Choose login type: Student (1) or Teacher (2).
   - Enter name and ID for verification.

### Student Login Example:
```
Login:
1. Student   2. Teacher
Enter your choice: 1
Choice entered: 1
Verify as a Student
Enter your name: John Doe
Enter your id: 12345
Login successful
1. Check result     2. Highest-mark     3. Lowest-mark     4. Percentage     5. Rank-Calculation     6. Exit
Enter your choice: 1
```

### Teacher Login Example:
```
Login:
1. Student   2. Teacher
Enter your choice: 2
Choice entered: 2
Verify as a Teacher
Enter your name: Jane Smith
Enter your id: T67890
Login successful
1. Add student     2. Search Student     3. Update student     4. Delete student     5. Show all students     6. Add teacher     7. Search teacher     8. Update teacher     9. Delete teacher     10. Show all teachers     11. Exit
Enter your choice: 5
```

## Data Files

- `data_files/students.json`: Stores student data.
- `data_files/teachers.json`: Stores teacher data.

Ensure these files exist and contain valid JSON data for the application to function properly.

## Project Structure

```
python_project(student_database_management)/
├── main.py                 # Main application script
├── README.md               # This file
├── requirements.txt        # Python dependencies (currently empty)
├── data_files/             # Directory for JSON data files
│   ├── students.json
│   └── teachers.json
└── entities/               # Python classes
    ├── __init__.py
    ├── student.py
    └── teacher.py
```

