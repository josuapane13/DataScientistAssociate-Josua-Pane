#asumsi data, library yang dibutuhkan sudah di-import, cleaning, dan sudah di eksplorasi

#asumsi diperoleh data calon nasabah kartu kredit dengan informasi : 
data_nasabah = pd.DataFrame({
    'pelanggan_id':,
    'usia':,
    'jenis_kelamin':,
    'pendapatan':,
    'jml_kartu_kredit',
    'pengeluaran_bulanan',
})
# set variabel target prediksi Y
df['tertarik'] = (
    (df['pendapatan'] > 80000000) & 
    (df['jml_kartu_kredit'] < 3) &
    (df['pengeluaran_bulanan'] > 5000000)
).astype(int)

print("\nStatistik Deskriptif:")
print(df.describe(include='all'))
print("\nDistribusi Target (tertarik):")
print(df['tertarik'].value_counts())

sns.countplot(x='tertarik', data=df)
plt.title('Distribusi Target (Tertarik)')
plt.show()

features = ['usia', 'pendapatan', 'jml_kartu_kredit', 'pengeluaran_bulanan']
X = df[features]
y = df['tertarik']

# Normalisasi data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

#latih data
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, stratify=y, random_state=42)
clf = RandomForestClassifier(random_state=42, n_estimators=100)
clf.fit(X_train, y_train)

# Prediksi ke data baru
y_pred = clf.predict(X_test)
y_proba = clf.predict_proba(X_test)[:,1]

# Evaluasi Hasil 
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
