# Task 1: User Authentication
user_data = {'suraj': '1234',}
# user login
def login():
    username = input("Username: ")
    password = input("Password: ")
    if username in user_data and user_data[username] == password:
        print("Login successful.")
        return True
    else:
        print("Invalid username or password.")
        return False
# user register
def register():
    username = input("username: ")
    if username in user_data:
        print("Username already exists. Please choose a different username.")
        return
    password = input(" password: ")
    user_data[username] = password
    print("Registration successful. You can now login.")

# Task 2: Student Information Management
student_data = {}
# student add
def add_student_record():
    student_id = int(input("Enter student ID: "))

    if student_id in student_data:
        print("Student ID already exists. Use update function to modify the record.")
        return
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    email = input("Enter student email: ")
    student_data[student_id] = { 'name': name, 'age': age,'email': email}
    print("Student record added successfully.")
#student record view
def view_student_record():
    student_id = int(input("Enter student ID: "))
    if student_id in student_data:
        student_info = student_data[student_id]
        print(f"Student ID: {student_id}")
        print(f"Name: {student_info['name']}")
        print(f"Age: {student_info['age']}")
        print(f"Email: {student_info['email']}")
    else:
        print("Student not found.")
#student record update
def update_student_record():
    student_id = int(input("Enter student ID: "))

    if student_id in student_data:
        name = input("Enter updated name: ")
        age = int(input("Enter updated age: "))
        email = input("Enter updated email: ")

        student_data[student_id]['name'] = name
        student_data[student_id]['age'] = age
        student_data[student_id]['email'] = email

        print("Student record updated successfully.")
    else:
        print("Student not found. Use add function to add a new record.")

def delete_student_record():
    student_id = int(input("Enter student ID: "))
    if student_id in student_data:
        del student_data[student_id]
        print("Student record deleted successfully.")
    else:
        print("Student not found.")
# Task 3: Marking Attendance
attendance_records = {}
def display_students_for_attendance():
    print("Available Students for Attendance:")
    for student_id, student_info in student_data.items():
        print(f"{student_id}: {student_info['name']}")
def mark_attendance():
    date = input("Enter the date (YYYY-MM-DD): ")
    display_students_for_attendance()
    while True:
        student_id = int(input("Enter student ID to mark attendance (-1 to stop): "))
        if student_id == -1:
            break
        if student_id in student_data:
            if date not in attendance_records:
                attendance_records[date] = []
            attendance_records[date].append(student_id)
            print(f"Attendance marked for {student_data[student_id]['name']} on {date}.")
        else:
            print("Invalid student ID. Please try again.")
# Task 4: Viewing Attendance Records
def view_attendance_records():
    date = input("Enter the date to view attendance records (YYYY-MM-DD): ")
    if date in attendance_records:
        print(f"Attendance records for {date}:")
        for student_id in attendance_records[date]:
            print(f"Student ID: {student_id}, Name: {student_data[student_id]['name']}")
    else:
        print("No attendance records found for the given date.")
# Task 5: Generating Reports
def generate_monthly_report(year, month):
    start_date = f"{year}-{month:02d}-01"
    end_date = f"{year}-{month:02d}-31"
    total_days = 0
    total_present = 0
    for date in attendance_records:
        if start_date <= date <= end_date:
            total_days += 1
            total_present += len(attendance_records[date])
    print(f"Monthly Attendance Report ({year}-{month:02d}):")
    print(f"Total Days: {total_days}")
    print(f"Total Present: {total_present}")
    print(f"Average Attendance: {total_present / total_days:.2f}")

def generate_weekly_report(year, week_number):
    from datetime import datetime, timedelta
    week_start = datetime.strptime(f"{year}-W{week_number:02d}-1", "%Y-W%W-%w")
    week_end = week_start + timedelta(days=6)

    total_days = 0
    total_present = 0

    for date in attendance_records:
        dt = datetime.strptime(date, "%Y-%m-%d")
        if week_start <= dt <= week_end:
            total_days += 1
            total_present += len(attendance_records[date])

    print(f"Weekly Attendance Report (Week {week_number} - {year}):")
    print(f"Total Days: {total_days}")
    print(f"Total Present: {total_present}")
    print(f"Average Attendance: {total_present / total_days:.2f}")
def generate_daily_report(date):
    if date in attendance_records:
        total_present = len(attendance_records[date])
        print(f"Daily Attendance Report ({date}):")
        print(f"Total Present: {total_present}")
    else:
        print(f"No attendance records found for {date}.")
def export_to_csv(file_name):
    with open(file_name, 'w') as csvfile:
        csvfile.write("Date,Present Students\n")
        for date, students in attendance_records.items():
            csvfile.write(f"{date},{', '.join(str(student_id) for student_id in students)}\n")
# Main program loop
while True:
    print("\nStudent Management System")
    print("1. Login")
    print("2. Register")
    print("3. Add Student Record")
    print("4. View Student Record")
    print("5. Update Student Record")
    print("6. Delete Student Record")
    print("7. Mark Attendance")
    print("8. View Attendance Records")
    print("9. Generate Monthly Report")
    print("10. Generate Weekly Report")
    print("11. Generate Daily Report")
    print("12. Export Attendance Records to CSV")
    print("13. Exit")

    choice = int(input("Enter your choice (1-13): "))

    if choice == 1:
        login()
    elif choice == 2:
        register()
    elif choice == 3:
        add_student_record()
    elif choice == 4:
        view_student_record()
    elif choice == 5:
        update_student_record()
    elif choice == 6:
        delete_student_record()
    elif choice == 7:
        mark_attendance()
    elif choice == 8:
        view_attendance_records()
    elif choice == 9:
        year = int(input("Enter the year: "))
        month = int(input("Enter the month (1-12): "))
        generate_monthly_report(year, month)
    elif choice == 10:
        year = int(input("Enter the year: "))
        week_number = int(input("Enter the week number (1-52): "))
        generate_weekly_report(year, week_number)
    elif choice == 11:
        date = input("Enter the date (YYYY-MM-DD): ")
        generate_daily_report(date)
    elif choice == 12:
        export_to_csv("attendance_records.csv")
        print("Attendance records exported to attendance_records.csv.")
    elif choice == 13:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select again.")