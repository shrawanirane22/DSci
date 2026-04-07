import pandas as pd
import requests

url = "https://en.wikipedia.org/wiki/List_of_natural_disasters_by_death_toll"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

tables = pd.read_html(response.text)

df = tables[3]

# ✅ Correct number of columns
df.columns = ["Year", "Death_Toll", "Event", "Country", "Type", "Date"]

df.to_csv("disaster_data.csv", index=False)

print("Final disaster dataset created ✅")