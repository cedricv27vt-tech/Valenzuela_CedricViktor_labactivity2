from datetime import date


def create_student(records):
    print("\n--- Add New Student ---")
    
    student_id = input("Enter Student ID (e.g., 2026-1001): ").strip()
    if student_id in records:
        print("❌ Error: Student ID already exists.")
        return

    name = input("Enter Full Name: ").strip().title()
    course = input("Enter Degree Program/Course: ").strip().upper()
    
    subjects_input = input("Enter Enrolled Subjects (comma-separated): ").strip()
    subjects_list = [s.strip().upper() for s in subjects_input.split(",") if s.strip()]

    metadata_tuple = (student_id, str(date.today()))

    records[student_id] = {
        "metadata": metadata_tuple,
        "name": name,
        "course": course,
        "subjects": subjects_list
    }
    
    print(f"✅ Record created successfully for {name} ({student_id}).")


def read_students(records):
    print("\n--- Display Student Records ---")
    if not records:
        print("⚠️ No records found.")
        return

    print(f"{'ID':<12} | {'Name':<25} | {'Course':<10} | {'Date Added':<12} | {'Subjects'}")
    print("-" * 75)
    
    for student_id, data in records.items():
        _, date_added = data["metadata"]
        subjects_str = ", ".join(data["subjects"]) if data["subjects"] else "None"
        
        print(f"{student_id:<12} | {data['name']:<25} | {data['course']:<10} | {date_added:<12} | {subjects_str}")


def update_student(records):
    print("\n--- Modify Student Record ---")
    student_id = input("Enter Student ID to update: ").strip()

    if student_id not in records:
        print("❌ Error: Student ID not found.")
        return

    student = records[student_id]
    print(f"Updating record for: {student['name']}")
    print("1. Update Degree Program/Course")
    print("2. Add New Subject to List")
    choice = input("Select an option (1-2): ").strip()

    if choice == "1":
        new_course = input("Enter new Course: ").strip().upper()
        student["course"] = new_course
        print(f"✅ Course updated to {new_course}.")
    elif choice == "2":
        new_subject = input("Enter new Subject code: ").strip().upper()
        if new_subject in student["subjects"]:
            print("⚠️ Subject is already in the list.")
        else:
            student["subjects"].append(new_subject)
            print(f"✅ Added {new_subject} to subject list.")
    else:
        print("❌ Invalid selection.")


def delete_student(records):
    print("\n--- Delete Student Record ---")
    student_id = input("Enter Student ID to delete: ").strip()

    if student_id in records:
        removed_student = records.pop(student_id)
        print(f"✅ Record for {removed_student['name']} ({student_id}) has been deleted successfully.")
    else:
        print("❌ Error: Student ID not found.")


def main():
    student_db = {}

    while True:
        print("\n   STUDENT RECORD SYSTEM (Lab Activity 2)    ")
        print("1. Add New Student Record")
        print("2. View All Student Records")
        print("3. Update Student Record")
        print("4. Delete Student Record")
        print("5. Exit")
        
        choice = input("Enter choice (1-5): ").strip()

        if choice == "1":
            create_student(student_db)
        elif choice == "2":
            read_students(student_db)
        elif choice == "3":
            update_student(student_db)
        elif choice == "4":
            delete_student(student_db)
        elif choice == "5":
            print("\nExiting program... Goodbye!")
            break
        else:
            print("❌ Invalid option. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()