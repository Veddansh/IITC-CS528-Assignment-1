import pandas as pd

# Load the Adult dataset
df = pd.read_csv("adult.data")

# Define k-value for each record
df["k"] = df.apply(lambda df: 4, axis=1)

# Define a function to generalize age
def generalize_age(df):
    age = df[0]
    if age < 18:
        return "<18"
    elif age >= 18 and age <= 25:
        return "18-25"
    elif age > 25 and age <= 35:
        return "26-35"
    elif age > 35 and age <= 45:
        return "36-45"
    elif age > 45 and age <= 55:
        return "46-55"
    else:
        return ">55"

# Apply the generalization function to the age column
df["Age"] = df.apply(lambda df: generalize_age(df), axis=1)

# Define a function to generalize education
def generalize_education(df):
    education = df[3]
    if education in ["Bachelors", "Masters", "Doctorate"]:
        return education
    else:
        return "Other"

# Apply the generalization function to the education column
df["Education"] = df.apply(lambda df: generalize_education(df), axis=1)

# Define a function to generalize marital status
def generalize_marital_status(df):
    status = df[5]
    if status in ["Married-civ-spouse", "Married-spouse-absent", "Married-AF-spouse"]:
        return "Married"
    else:
        return status

# Apply the generalization function to the marital status column
df["Marital-status"] = df.apply(lambda df: generalize_marital_status(df), axis=1)

# Define a function to generalize race
def generalize_race(df):
    race = df[8]
    if race == "White":
        return race
    else:
        return "Other"

# Apply the generalization function to the race column
df["Race"] = df.apply(lambda df: generalize_race(df), axis=1)

# Group the dataframe by the quasi-identifiers
grouped = df.groupby(["Age", "Education", "Marital-status", "Race"])

# Apply suppression

# Calculate the number of original records
num_original_records = df.shape[0]

# Calculate the precision for each quasi-identifier column
age_precision = (grouped["Age"].count().sum() / num_original_records)
education_precision = (grouped["Education"].count().sum() / num_original_records)
marital_status_precision = (grouped["Marital-status"].count().sum() / num_original_records)
race_precision = (grouped["Race"].count().sum() / num_original_records)

# Calculate the overall precision
overall_precision = (age_precision + education_precision + marital_status_precision + race_precision) / 4
print(overall_precision)

