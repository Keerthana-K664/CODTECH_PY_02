class StudentGrades:
    def __init__(self):
        self.records = {}

    def enroll_student(self, student_name):
        """Enroll a new student."""
        if student_name in self.records:
            return f"Error: {student_name} is already enrolled."
        self.records[student_name] = {}
        return f"Success: {student_name} has been enrolled."

    def record_grades(self, student_name, grades_data):
        """Record grades for a student in various subjects."""
        if student_name not in self.records:
            return f"Error: No record found for {student_name}."
        
        for subject, grades in grades_data.items():
            if subject not in self.records[student_name]:
                self.records[student_name][subject] = []
            self.records[student_name][subject].extend(grades)
        
        return f"Grades recorded for {student_name} in subjects: {', '.join(grades_data.keys())}."

    def average_grade(self, student_name):
        """Compute the average grade for a student."""
        if student_name not in self.records:
            return f"Error: No record found for {student_name}."
        
        all_grades = [grade for subjects in self.records[student_name].values() for grade in subjects]
        
        if not all_grades:
            return f"Notice: No grades available for {student_name}."
        
        avg = sum(all_grades) / len(all_grades)
        return f"{student_name}'s average grade is: {avg:.2f}"

    def display_all_records(self):
        """Display all students' grades and their averages."""
        if not self.records:
            return "Notice: No student records available."
        
        report = []
        for student, subjects in self.records.items():
            report.append(f"\nGrades for {student}:")
            total_grades = []
            for subject, grades in subjects.items():
                report.append(f"  {subject}: {grades}")
                total_grades.extend(grades)

            if total_grades:
                avg = sum(total_grades) / len(total_grades)
                report.append(f"  Average Grade: {avg:.2f}")
            else:
                report.append("  No grades recorded.")
        
        return "\n".join(report)


def main():
    tracker = StudentGrades()

    while True:
        print("\nWelcome to the Student Grade Management System!")
        print("1. Enroll Student")
        print("2. Record Grades")
        print("3. Get Average Grade")
        print("4. Show All Records")
        print("5. Exit")

        choice = input("Please select an option (1-5): ").strip()

        if choice == '1':
            name = input("Enter the name of the student: ").strip()
            result = tracker.enroll_student(name)
            print(result)
        elif choice == '2':
            name = input("Enter the name of the student: ").strip()
            try:
                grades_data = {}
                while True:
                    subject = input("Enter subject name (or type 'exit' to finish): ").strip()
                    if subject.lower() == 'exit':
                        break
                    grades = list(map(float, input(f"Enter grades for {subject} (space-separated): ").split()))
                    grades_data[subject] = grades
                result = tracker.record_grades(name, grades_data)
                print(result)
            except ValueError:
                print("Error: Please enter valid numerical grades.")
        elif choice == '3':
            name = input("Enter the name of the student: ").strip()
            result = tracker.average_grade(name)
            print(result)
        elif choice == '4':
            result = tracker.display_all_records()
            print(result)
        elif choice == '5':
            print("Thank you for using the system. Goodbye!")
            break
        else:
            print("Error: Invalid option. Please try again.")


if __name__ == "__main__":
  main()