#baru
import os
import time
import joblib
import pandas as pd
from datetime import datetime
from flask import Flask, request, jsonify

app = Flask(__name__)

# Memuat model, scaler, dan daftar kolom fitur
model = joblib.load('gbc_model.joblib')
scaler = joblib.load('scaler.joblib')
kolom_fitur = joblib.load('kolom_fitur.joblib')

# Kamus encoding (sama seperti di notebook)
biner = {'no': 0, 'yes': 1}
tingkat = {'no': 0, 'Sometimes': 1, 'Frequently': 2, 'Always': 3}
label_target = {
    0: 'Insufficient_Weight', 1: 'Normal_Weight',
    2: 'Overweight_Level_I', 3: 'Overweight_Level_II',
    4: 'Obesity_Type_I', 5: 'Obesity_Type_II', 6: 'Obesity_Type_III'
}
kolom_scale = ['Age', 'Height', 'Weight']

# BARU: berkas log untuk menyimpan riwayat prediksi
FILE_LOG = 'prediction_log.csv'


def proses_data(data):
    """Mengubah data mentah dari pengguna menjadi bentuk yang siap diprediksi."""
    df = pd.DataFrame([data])

    df['Gender'] = df['Gender'].map({'Female': 0, 'Male': 1})
    for k in ['FAVC', 'SCC', 'SMOKE', 'family_history_with_overweight']:
        df[k] = df[k].map(biner)
    for k in ['CALC', 'CAEC']:
        df[k] = df[k].map(tingkat)
    df = pd.get_dummies(df, columns=['MTRANS'])

    df = df.reindex(columns=kolom_fitur, fill_value=0).astype(float)
    df[kolom_scale] = scaler.transform(df[kolom_scale])
    return df


# BARU: mencatat setiap prediksi ke berkas CSV
def catat_log(data, prediksi, latency_ms):
    baris = pd.DataFrame([{
        'waktu': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'Age': data['Age'],
        'Height': data['Height'],
        'Weight': data['Weight'],
        'prediksi': prediksi,
        'latency_ms': round(latency_ms, 2)
    }])
    baris.to_csv(FILE_LOG, mode='a', header=not os.path.exists(FILE_LOG), index=False)


@app.route('/')
def home():
    return jsonify({'pesan': 'API prediksi tingkat obesitas berjalan'})


@app.route('/predict', methods=['POST'])
def predict():
    try:
        mulai = time.perf_counter()          # BARU: mulai hitung waktu
        data = request.get_json()
        X = proses_data(data)
        kode = int(model.predict(X)[0])
        prediksi = label_target[kode]
        latency_ms = (time.perf_counter() - mulai) * 1000   # BARU
        catat_log(data, prediksi, latency_ms)               # BARU
        return jsonify({'kode': kode, 'prediksi': prediksi})
    except Exception as e:
        return jsonify({'error': str(e)}), 400


# BARU: halaman monitoring
@app.route('/stats')
def stats():
    if not os.path.exists(FILE_LOG):
        return jsonify({'pesan': 'Belum ada prediksi yang tercatat'})

    log = pd.read_csv(FILE_LOG)

    # Data drift: selisih rata-rata data masuk vs data pelatihan,
    # dihitung dalam satuan simpangan baku data pelatihan
    drift = {}
    for i, k in enumerate(kolom_scale):
        rata_masuk = log[k].mean()
        rata_latih = scaler.mean_[i]
        selisih = (rata_masuk - rata_latih) / scaler.scale_[i]
        drift[k] = {
            'rata_data_masuk': round(float(rata_masuk), 2),
            'rata_data_latih': round(float(rata_latih), 2),
            'selisih_simpangan_baku': round(float(selisih), 2),
            'status': 'PERLU DICEK' if abs(selisih) > 0.5 else 'normal'
        }

    return jsonify({
        'jumlah_prediksi': int(len(log)),
        'rata_latency_ms': round(float(log['latency_ms'].mean()), 2),
        'latency_maks_ms': round(float(log['latency_ms'].max()), 2),
        'sebaran_prediksi': log['prediksi'].value_counts().to_dict(),
        'data_drift': drift
    })


if __name__ == '__main__':
    app.run(debug=True)