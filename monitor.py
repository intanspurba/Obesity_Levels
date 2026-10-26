import sys
import joblib
import pandas as pd

FILE_LOG = 'prediction_log.csv'
KOLOM = ['Age', 'Height', 'Weight']
AMBANG = 0.5   # selisih (dalam simpangan baku) yang dianggap perlu dicek

scaler = joblib.load('scaler.joblib')

try:
    log = pd.read_csv(FILE_LOG)
except FileNotFoundError:
    print("Belum ada log. Jalankan API dan kirim prediksi dulu.")
    sys.exit()

# Kumpulkan hasil monitoring ke dalam satu daftar
hasil = []

# 1. Penggunaan dan kecepatan
hasil.append(['Penggunaan', 'Jumlah prediksi', len(log), ''])
hasil.append(['Kecepatan', 'Rata-rata latency (ms)', round(log['latency_ms'].mean(), 2), ''])
hasil.append(['Kecepatan', 'Latency maksimum (ms)', round(log['latency_ms'].max(), 2), ''])

# 2. Sebaran prediksi
for kategori, jumlah in log['prediksi'].value_counts().items():
    persen = round(jumlah / len(log) * 100, 1)
    hasil.append(['Sebaran prediksi', kategori, jumlah, f'{persen}%'])

# 3. Data drift
for i, k in enumerate(KOLOM):
    rata_masuk = log[k].mean()
    selisih = (rata_masuk - scaler.mean_[i]) / scaler.scale_[i]
    status = 'PERLU DICEK' if abs(selisih) > AMBANG else 'normal'
    hasil.append(['Data drift', f'{k} (masuk {rata_masuk:.2f} vs latih {scaler.mean_[i]:.2f})',
                  round(selisih, 2), status])

tabel = pd.DataFrame(hasil, columns=['Kategori', 'Metrik', 'Nilai', 'Status'])

# Tampilkan di CMD / terminal
print("\n=== MONITORING MODEL OBESITAS ===\n")
print(tabel.to_string(index=False))

# Simpan untuk Notion bila diminta: python monitor.py notion
if len(sys.argv) > 1 and sys.argv[1] == 'notion':
    tabel.to_csv('monitoring_ringkasan.csv', index=False, encoding='utf-8-sig')
    print("\nBerkas 'monitoring_ringkasan.csv' dibuat. Impor ke Notion.")