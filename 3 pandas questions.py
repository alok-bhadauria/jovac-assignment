import pandas as pd
import csv

# Task 1: Working with Series

series_data = [25, 30, 35, 40, 45]
my_series = pd.Series(series_data)

first_three_series = my_series.head(3)
my_series.index = ['A', 'B', 'C', 'D', 'E']

mean_series = my_series.mean()
median_series = my_series.median()
std_dev_series = my_series.std()

print("TASK 1 :\n")
print("Original Series:\n", pd.Series(series_data))
print("First three elements of Series:\n", first_three_series)
print("Series with custom indices:\n", my_series)
print("Mean of Series: ", mean_series)
print("Median of Series: ", median_series)
print("Standard Deviation of Series: ", std_dev_series)
print("\n\n")


# Task 2: Creating and Inspecting DataFrames

df_data = {
    "Name": ["Alice", "Bob", "Carol", "David", "Eve"],
    "Age": [20, 22, 19, 21, 20],
    "Gender": ["Female", "Male", "Female", "Male", "Female"],
    "Marks": [85, 78, 92, 74, 88]
}
df = pd.DataFrame(df_data)

first_two_rows = df.head(2)
column_names = df.columns
data_types = df.dtypes
summary_statistics = df.describe()
df["Passed"] = df["Marks"] >= 80

print("TASK 2 :\n")
print("Original DataFrame:\n", df_data)
print("First two rows of DataFrame:\n", first_two_rows)
print("Column Names:", list(column_names))
print("Data Types:\n", data_types)
print("Summary Statistics:\n", summary_statistics)
print("DataFrame with 'Passed' column:\n", df)
print("\n\n")


# Task 3: Data Selection and Filtering

name_marks = df[["Name", "Marks"]]
high_marks_students = df[df["Marks"] > 80]
highest_marks_student = df.loc[df["Marks"].idxmax()]

print("TASK 3 :\n")
print("Name and Marks columns:\n", name_marks)
print("Records where Marks > 80:\n", high_marks_students)
print("Student with the highest marks:\n", highest_marks_student)
print("\n\n")


# Task 4: Handling Missing Data

df_missing = df.copy()
df_missing.loc[1, "Marks"] = None
df_missing.loc[4, "Age"] = None

missing_values = df_missing.isnull()
marks_mean = df_missing["Marks"].mean()

df_filled_marks = df_missing.copy()
df_filled_marks["Marks"] = df_filled_marks["Marks"].fillna(marks_mean)
df_dropped_age = df_missing.dropna(subset=["Age"])

print("TASK 4 :\n")
print("DataFrame with missing values:\n", df_missing)
print("Missing values identified:\n", missing_values)
print("DataFrame with 'Marks' filled by mean:\n", df_filled_marks)
print("DataFrame with rows dropped where 'Age' is missing:\n", df_dropped_age)
print("\n\n")


# Task 5: Grouping and Aggregation

gender_mean_stats = df.groupby("Gender")[["Age", "Marks"]].mean()
gender_counts = df.groupby("Gender").size().reset_index(name="Count")

print("TASK 5 :\n")
print("Mean Age and Marks by Gender:\n", gender_mean_stats)
print("Number of students in each gender group:\n", gender_counts)
print("\n\n")


# Task 6: Reading and Writing Data

df_filled_marks.to_csv("students_data.csv", index=False)
new_df = pd.read_csv("students_data.csv")
first_five_new_df = new_df.head(5)

print("TASK 6 :\n")
print("DataFrame saved to 'students_data.csv'.")
print("Newly loaded DataFrame (first five rows):\n", first_five_new_df)
print("\n\n")


# Task 7: General

import matplotlib.pyplot as plt
import seaborn as sns

print("TASK 7 :\n")

df_sales = pd.read_csv("Auto Sales data.csv")
df_sales.columns = df_sales.columns.str.lower()

print("Auto Sales data loaded.")
print("Shape:", df_sales.shape)
print("First five rows:\n", df_sales.head())
print("Summary statistics:\n", df_sales.describe())
print("Missing values:\n", df_sales.isnull().sum())

plt.figure(figsize=(8, 5))
sns.histplot(df_sales["sales"], kde=True, color="steelblue")
plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
country_sales = df_sales.groupby("country")["sales"].sum().sort_values(ascending=False)
sns.barplot(x=country_sales.index, y=country_sales.values, palette="mako")
plt.title("Sales by Country")
plt.xlabel("Country")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

df_sales["orderdate"] = pd.to_datetime(df_sales["orderdate"], dayfirst=True)
daily_sales = df_sales.groupby("orderdate")["sales"].sum().reset_index()

plt.figure(figsize=(12, 6))
sns.lineplot(data=daily_sales, x="orderdate", y="sales", color="darkorange")
plt.title("Sales Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Daily Sales")
plt.tight_layout()
plt.show()

print("\nObservations:")
print("- Dataset contains rows with sales, customer details, and order date. No missing values found.")
print("- Sales distribution is right-skewed; most values are moderate with some high outliers.")
print("- Country-wise sales show which locations are driving the most revenue.")
print("- Daily sales trend shows periodic spikes that may relate to promotions or seasonal buying.")
