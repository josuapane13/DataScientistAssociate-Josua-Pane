import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# asumsi data sudah di-import, cleaning, dan sudah di lakukan EDA
# mulai tahap membuat visualisasi

# visualisasi heatmap correlation 
plt.figure(figsize=(12, 10))
numerical_cols = ['jarak', 'durasi', 'harga', 'driver_rating', 'customer_rating', 'price_per_km']
correlation_matrix = df[numerical_cols].corr()
mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix', fontsize=16)

# contoh visualisasi scatter plot jarak vs harga_per_km
plt.subplot(1, 2, 1) 
sns.scatterplot(x='jarak', y='harga_per_km', 
data=data, alpha=0.7)
plt.title('Correlation harga_per_km dan jarak')
plt.xlabel('Jarak', fontsize=12)
plt.ylabel('Harga per km', fontsize=12)
plt.grid(True, alpha=0.6)
