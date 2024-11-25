import os
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix

# Load the dataset
file_path = os.path.join(os.path.dirname(__file__), "RollCallVotes.csv")
df = pd.read_csv(file_path)
print("Initial DataFrame shape:", df.shape)

# Drop null values
df.dropna(inplace=True)
print("DataFrame shape after dropping nulls:", df.shape)

# Map voting records
df["Senator's voting record"] = df["Senator's voting record"].map(
    {"Yea": 1, "Nay": 0, "Not Voting": 2}
)
print(
    "Unique values in Senator's voting record after mapping:",
    df["Senator's voting record"].unique(),
)

# Map party affiliation
df["Senator's party affiliation"] = df["Senator's party affiliation"].map(
    {"D": 0, "R": 1, "I": 2}
)
print(
    "Unique values in Senator's party affiliation after mapping:",
    df["Senator's party affiliation"].unique(),
)

# Prepare features and labels
x = df[["Senator's party affiliation", "Senator's state"]]
y = df["Senator's voting record"]

# One-hot encoding for state
x = pd.get_dummies(x, columns=["Senator's state"], drop_first=True)
print("Features after one-hot encoding shape:", x.shape)

# Split the dataset
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

# Fit the model
model = RandomForestClassifier(random_state=42)
model.fit(x_train, y_train)

# Make predictions
y_pred = model.predict(x_test)

# Evaluate the model
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
print(f"Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}")

# Save the model
joblib.dump(model, "senate_vote_classifier.pkl")
