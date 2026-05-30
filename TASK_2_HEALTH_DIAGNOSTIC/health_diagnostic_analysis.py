# TASK 2: HEALTH DIAGNOSTIC
# Health Diagnostic Analysis using Python
# Data Science Internship Project

import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Create health diagnostic database manually
health_data = {
    "Patient_ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "Age": [25, 45, 60, 35, 52, 29, 67, 40, 58, 31],
    "Gender": ["Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female"],
    "Blood_Pressure": [120, 145, 160, 130, 150, 118, 170, 135, 155, 125],
    "Sugar_Level": [90, 160, 210, 110, 180, 85, 240, 130, 190, 100],
    "Cholesterol": [180, 220, 260, 190, 240, 175, 280, 200, 250, 185],
    "Heart_Rate": [72, 85, 95, 78, 88, 70, 100, 80, 92, 76]
}

# Step 2: Convert database into DataFrame
data = pd.DataFrame(health_data)

# Step 3: Create diagnosis function
def diagnose_patient(row):
    risk_score = 0

    if row["Blood_Pressure"] > 140:
        risk_score += 1

    if row["Sugar_Level"] > 140:
        risk_score += 1

    if row["Cholesterol"] > 200:
        risk_score += 1

    if row["Heart_Rate"] > 90:
        risk_score += 1

    if risk_score == 0:
        return "Healthy"
    elif risk_score <= 2:
        return "Moderate Risk"
    else:
        return "High Risk"

# Step 4: Apply diagnosis to each patient
data["Diagnosis"] = data.apply(diagnose_patient, axis=1)

# Step 5: Display database
print("Health Diagnostic Database:")
print(data)

# Step 6: Diagnosis summary
diagnosis_count = data["Diagnosis"].value_counts()
print("\nDiagnosis Summary:")
print(diagnosis_count)

# Step 7: Find high-risk patients
high_risk_patients = data[data["Diagnosis"] == "High Risk"]
print("\nHigh Risk Patients:")
print(high_risk_patients)

# Step 8: Average health values
print("\nAverage Health Values:")
print("Average Blood Pressure:", data["Blood_Pressure"].mean())
print("Average Sugar Level:", data["Sugar_Level"].mean())
print("Average Cholesterol:", data["Cholesterol"].mean())
print("Average Heart Rate:", data["Heart_Rate"].mean())

# Step 9: Diagnosis category graph
plt.figure(figsize=(8, 5))
diagnosis_count.plot(kind="bar")
plt.title("Health Diagnosis Category Count")
plt.xlabel("Diagnosis")
plt.ylabel("Number of Patients")
plt.grid(True)
plt.show()

# Step 10: Blood pressure analysis graph
plt.figure(figsize=(10, 5))
plt.plot(data["Patient_ID"], data["Blood_Pressure"], marker="o", label="Blood Pressure")
plt.title("Patient Blood Pressure Analysis")
plt.xlabel("Patient ID")
plt.ylabel("Blood Pressure")
plt.legend()
plt.grid(True)
plt.show()

# Step 11: Sugar level analysis graph
plt.figure(figsize=(10, 5))
plt.plot(data["Patient_ID"], data["Sugar_Level"], marker="o", label="Sugar Level")
plt.title("Patient Sugar Level Analysis")
plt.xlabel("Patient ID")
plt.ylabel("Sugar Level")
plt.legend()
plt.grid(True)
plt.show()

# Step 12: Cholesterol analysis graph
plt.figure(figsize=(10, 5))
plt.plot(data["Patient_ID"], data["Cholesterol"], marker="o", label="Cholesterol")
plt.title("Patient Cholesterol Analysis")
plt.xlabel("Patient ID")
plt.ylabel("Cholesterol")
plt.legend()
plt.grid(True)
plt.show()

print("\nConclusion:")
print("This project analyzes patient health data using Python, Pandas, and Matplotlib.")
print("It classifies patients as Healthy, Moderate Risk, or High Risk based on health parameters.")
