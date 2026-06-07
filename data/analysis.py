import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/genre_trends.csv")

plt.figure(figsize=(12,6))

for column in df.columns[1:]:
    plt.plot(df["year"], df[column], marker="o", label=column)

plt.title("Evolution of Roblox Genres (2012-2026)")
plt.xlabel("Year")
plt.ylabel("Popularity Score")
plt.legend()
plt.grid(True)

plt.show()