import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

# Creează DataFrame cu vânzări lunare
data = {
    "Luna": ["Ianuarie", "Februarie", "Martie", "Aprilie", "Mai", "Iunie"],
    "Vânzări": [1500, 2000, 1800, 2500, 3000, 2800]
}
df = pd.DataFrame(data)

# Creează graficul de tip linie
plt.figure(figsize=(10, 6))
plt.plot(df["Luna"], df["Vânzări"], marker='o', linewidth=2, markersize=8, color='blue')

# Adaugă valori numerice deasupra fiecărui punct
for i, val in enumerate(df["Vânzări"]):
    plt.text(i, val + 50, str(val), ha='center', va='bottom', fontsize=10)

plt.xlabel("Luna", fontsize=12)
plt.ylabel("Vânzări", fontsize=12)
plt.title("Evoluția Vânzărilor Lunare", fontsize=14)
plt.grid(True, alpha=0.3)
plt.tight_layout()

# Salvează graficul
plt.savefig("vanzari_grafic.png", dpi=300)
print("Graficul a fost salvat în 'vanzari_grafic.png'")

# Salvează DataFrame-ul în CSV
df.to_csv("vanzari_date.csv", index=False, encoding='utf-8')
print("Datele au fost salvate în 'vanzari_date.csv'")

plt.show()