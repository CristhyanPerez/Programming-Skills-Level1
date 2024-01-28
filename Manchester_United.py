#Import libraries
import pandas as pd

#Declarate the dataframe
df = pd.DataFrame(columns=["Name", "Goals", "Points Speed", "Points Assists", "Passing accuracy", "Defensive Involving", "Jersey Number"])
data = pd.DataFrame([
    {"Name": "Bruno Fernandez", "Goals": 5, "Points Speed": 6, "Points Assists": 9, "Passing accuracy": 10, "Defensive Involving": 3, "Jersey Number": 8},
    {"Name": "Rasmus Hojlund", "Goals": 12, "Points Speed": 8, "Points Assists": 2, "Passing accuracy": 6, "Defensive Involving": 2, "Jersey Number": 11},
    {"Name": "Harry Maguire", "Goals": 1, "Points Speed": 5, "Points Assists": 1, "Passing accuracy": 7, "Defensive Involving": 9, "Jersey Number": 5},
    {"Name": "Alejandro Garnacho", "Goals": 8, "Points Speed": 7, "Points Assists": 8, "Passing accuracy": 6, "Defensive Involving": 0, "Jersey Number": 17},
    {"Name": "Mason Mount", "Goals": 2, "Points Speed": 6, "Points Assists": 4, "Passing accuracy": 8, "Defensive Involving": 1, "Jersey Number": 7}
])
df = pd.concat([df, data], ignore_index = True)

