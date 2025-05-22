#asumsi data, library yang dibutuhkan sudah di-import, cleaning, dan sudah di eksplorasi
# Statistik Deskriptif

print("Statistik Deskriptif Umum:")
print(df.describe(include='all'))

# Statistik Deskriptif untuk Setiap Fitur
print("\nStatistik Umur:")
print(df['umur'].describe())
print("\nStatistik Gaji:")
print(df['gaji'].describe())

print("\nDistribusi Jenis Kelamin:")
print(df['jenis_kelamin'].value_counts())
print("\nDistribusi Pendidikan:")
print(df['pendidikan'].value_counts())

# Korelasi antar variabel numerik
print("Korelasi antar fitur numerik:")
print(df[['umur', 'lama_bekerja', 'gaji']].corr())
sns.heatmap(df[['umur', 'lama_bekerja', 'gaji']].corr())
plt.title('Korelasi antara Umur, Lama Bekerja, dan Gaji')
plt.show()

# Contoh statistic inferensial
# rata-rata gaji berdasarkan pendidikan
pendidikan_gaji = df.groupby('pendidikan')['gaji'].mean()
print("\nRata-rata Gaji berdasarkan Pendidikan:")
print(pendidikan_gaji)
sns.boxplot(x='pendidikan', y='gaji', data='data3')
plt.title('Gaji berdasarkan Pendidikan')
plt.show()







