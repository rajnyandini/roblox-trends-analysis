import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("roblox_growth.csv")

plt.figure(figsize=(8,5))

plt.plot(
    df["year"],
    df["dau"],
    marker="o"
)

plt.title("Roblox Daily Active Users Growth")
plt.xlabel("Year")
plt.ylabel("Users (Millions)")
plt.grid(True)

plt.show()