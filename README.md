# 🌤 Weather ETL Project

This is a mini ETL project that extracts real-time weather data for **New York** using a free weather API, processes the data using **Python**, and saves the results to a clean CSV file.

---

## 📌 What This Project Does

- 📡 **Extract**: Fetches weather data from [wttr.in](https://wttr.in/)
- 🔧 **Transform**: Parses temperature and description from the JSON response
- 💾 **Load**: Exports the results to `weather_report.csv`

---

## 🔧 Technologies Used

- Python
- `requests` (for API call)
- `pandas` (for data manipulation)
- JSON
- CSV

---

## 🧪 Output Example

| City      | Temperature_C | Description   |
|-----------|----------------|---------------|
| New York  | 23             | Partly cloudy |

---

## 🚀 How to Run

```bash
pip install requests pandas
python weather_etl.py
