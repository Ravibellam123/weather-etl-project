
import requests
import pandas as pd

# Extract
response = requests.get("https://wttr.in/New York?format=j1")
weather_data = response.json()

# Transform
current_temp_C = weather_data["current_condition"][0]["temp_C"]
weather_desc = weather_data["current_condition"][0]["weatherDesc"][0]["value"]

# Load
df = pd.DataFrame([{
    "City": "New York",
    "Temperature_C": current_temp_C,
    "Description": weather_desc
}])

df.to_csv("weather_report.csv", index=False)
print(df)
