
import pandas as pd

# Load the HR dataset
file_name = "Messy_HR_Dataset_Detailed.csv"
df = pd.read_csv(file_name, low_memory=False)

print("========== HR DATASET REPORT ==========")

# Dataset size
print("\n1. Dataset Shape:")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# Column names
print("\n2. Column Names:")
print(df.columns.tolist())

# First 5 rows
print("\n3. First 5 Records:")
print(df.head())

# Missing values
print("\n4. Missing Values:")
print(df.isnull().sum())

# Duplicate records
print("\n5. Duplicate Rows:")
print(df.duplicated().sum())

# Data types
print("\n6. Data Types:")
print(df.dtypes)

print("\n========== REPORT COMPLETE ==========")

# Data Cleaning
print("\n===== DATA CLEANING =====")

# Remove duplicate rows
df = df.drop_duplicates()

# Remove extra spaces from text columns
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].str.strip()

# Check missing values
print("\nMissing values before cleaning:")
print(df.isnull().sum())

# Save cleaned dataset
df.to_csv("HR_Dataset_Cleaned.csv", index=False)

print("\nCleaned dataset saved successfully!")
print("Final dataset shape:", df.shape)

import matplotlib.pyplot as plt
import os

# Create output folder
os.makedirs("charts", exist_ok=True)

# Pivot Table 1: Average salary by department
# Pivot Table 1: Employees by Department
pivot1 = df.pivot_table(
    index="DepartmentType",
    values="Employee ID",
    aggfunc="count"
)

print("\nEmployees by Department:")
print(pivot1)
pivot1.to_csv("Pivot_Employees_By_Department.csv")
print("\nAverage Salary by Department:")
print(pivot1)

pivot1.to_csv("Department_Salary_Pivot.csv")

# Chart 1: Average salary by department
pivot1.plot(kind="bar", legend=False, title="Average Salary by Department")
plt.ylabel("Average Salary")
plt.tight_layout()
plt.savefig("charts/average_salary.png")
plt.close()

# Pivot Table 1: Employees by Department
pivot1 = df.pivot_table(
    index="DepartmentType",
    values="Employee ID",
    aggfunc="count"
)

print("\nEmployees by Department:")
print(pivot1)
pivot1.to_csv("Pivot_Employees_By_Department.csv")

# Pivot Table 2: Employees by Gender
pivot2 = df.pivot_table(
    index="GenderCode",
    values="Employee ID",
    aggfunc="count"
)

print("\nEmployees by Gender:")
print(pivot2)
pivot2.to_csv("Pivot_Employees_By_Gender.csv")

# Pivot Table 3: Average Training Cost by Training Type
pivot3 = df.pivot_table(
    index="Training Type",
    values="Training Cost",
    aggfunc="mean"
)

print("\nAverage Training Cost by Type:")
print(pivot3)
pivot3.to_csv("Pivot_Training_Cost.csv")

print("\nAll 3 pivot tables created successfully!")

import matplotlib.pyplot as plt
import os

os.makedirs("charts", exist_ok=True)

# Chart 1: Employees by Gender
pivot2.plot(kind="bar", legend=False, title="Employees by Gender")
plt.ylabel("Number of Employees")
plt.tight_layout()
plt.savefig("charts/employees_by_gender.png")
plt.close()

# Chart 2: Employees by Department
pivot1.plot(kind="bar", legend=False, title="Employees by Department")
plt.ylabel("Number of Employees")
plt.tight_layout()
plt.savefig("charts/employees_by_department.png")
plt.close()

# Chart 3: Average Training Cost
pivot3.plot(kind="bar", legend=False, title="Average Training Cost by Type")
plt.ylabel("Average Cost")
plt.tight_layout()
plt.savefig("charts/average_training_cost.png")
plt.close()

print("All 3 charts saved in the charts folder!")