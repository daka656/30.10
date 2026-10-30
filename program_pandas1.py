import pandas as pd
import json
import matplotlib.pyplot as plt

with open("./sala302.json", 'r') as file:
    raw_data = json.load(file)

df = pd.DataFrame(raw_data['data'])
df = df.drop(columns=['_id','location','created_at', 'deviceId'])
#konwersacja na DateTime
df['timestamp'] = pd.to_datetime(df['timestamp'])
df.set_index('timestamp', inplace=True)
df = df.sort_index()

print(df)

print(df.describe())
df['hour'] = df.index.hour
df['date'] = df.index.date
daily_profile = df.groupby('date')[['temperature', 'humidity']].mean()
print(daily_profile)
daily_profile = df.groupby('date')[['temperature', 'humidity']].min()
print(daily_profile)

df[['temperature', 'humidity']].plot(figsize=(16,6), title = "Temperatura i Wilgotność w Laboratorium")
plt.ylabel('Wartość')
plt.grid(True)
plt.show()

df[['pressure']].plot(figsize=(16,6), title = "Ciśnienie w Laboratorium")
plt.ylabel('Wartość')
plt.grid(True)
plt.show()
