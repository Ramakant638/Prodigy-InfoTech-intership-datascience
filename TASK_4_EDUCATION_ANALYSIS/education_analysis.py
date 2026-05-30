# TASK 4: EDUCATION ANALYSIS
# Student Performance Analysis using Python
# Data Science Internship Project

import pandas as pd
import matplotlib.pyplot as plt

education_data = {
    "Student_ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "Student_Name": ["Amit", "Riya", "Rahul", "Sneha", "Karan", "Priya", "Vikas", "Neha", "Arjun", "Simran"],
    "Class": ["10th"] * 10,
    "Maths": [85, 92, 78, 88, 65, 95, 70, 82, 60, 90],
    "Science": [80, 89, 75, 91, 68, 94, 72, 85, 62, 88],
    "English": [78, 95, 80, 84, 70, 90, 75, 88, 65, 92],
    "Attendance": [92, 96, 85, 90, 78, 98, 82, 88, 75, 94]
}

data = pd.DataFrame(education_data)

data["Total_Marks"] = data["Maths"] + data["Science"] + data["English"]
data["Percentage"] = data["Total_Marks"] / 3

def assign_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    else:
        return "Fail"

data["Grade"] = data["Percentage"].apply(assign_grade)

print("Student Performance Database:")
print(data)

topper = data.loc[data["Percentage"].idxmax()]
lowest_student = data.loc[data["Percentage"].idxmin()]
grade_count = data["Grade"].value_counts()
subject_avg = data[["Maths", "Science", "English"]].mean()

print("\nTopper Details:")
print(topper)

print("\nLowest Performer Details:")
print(lowest_student)

print("\nSubject Average Marks:")
print(subject_avg)

print("\nGrade Summary:")
print(grade_count)

plt.figure(figsize=(10, 5))
plt.bar(data["Student_Name"], data["Percentage"])
plt.title("Student Percentage Analysis")
plt.xlabel("Student Name")
plt.ylabel("Percentage")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 5))
subject_avg.plot(kind="bar")
plt.title("Subject-wise Average Marks")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(data["Student_Name"], data["Attendance"], marker="o", label="Attendance")
plt.title("Student Attendance Analysis")
plt.xlabel("Student Name")
plt.ylabel("Attendance Percentage")
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 5))
grade_count.plot(kind="bar")
plt.title("Grade Distribution")
plt.xlabel("Grade")
plt.ylabel("Number of Students")
plt.grid(True)
plt.show()

print("\nConclusion:")
print("This project analyzes student performance using Python, Pandas, and Matplotlib.")
