import pandas as pd
import numpy as np

df = pd.read_csv('data1.csv')

#handling nilai yang hilang / dan tanggal yang tidak sesuai
num_cols = ['durasi_film', 'kapasitas_auditorium', 'tiket_terjual', 'harga_tiket']
for col in num_cols:
    df[col] = df[col].fillna(df[col].median())
    df['judul_film'] = df['judul_film'].fillna('Unknown')
    df['tanggal_film'] = pd.to_datetime(df['tanggal_film'])

#drop duplicate value
df = df.drop_duplicates()
df.to_csv('data1_new.csv', index=False)
