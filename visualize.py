import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv')

plt.figure(figsize=(10, 6))
plt.scatter(data['km'], data['price'], color='blue', label='Données réelles')

plt.title("Prix de la voiture selon le kilométrage")
plt.xlabel("Kilométrage (Input)")
plt.ylabel("Prix (Goal Pred)")
plt.grid(True)
plt.show()