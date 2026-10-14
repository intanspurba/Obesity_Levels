import joblib
import pandas as pd
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


def proses_data(data):
    """Mengubah data mentah dari pengguna menjadi bentuk yang siap diprediksi."""
    df = pd.DataFrame([data])

    # Encoding
    df['Gender'] = df['Gender'].map({'Female': 0, 'Male': 1})
    for k in ['FAVC', 'SCC', 'SMOKE', 'family_history_with_overweight']:
        df[k] = df[k].map(biner)
    for k in ['CALC', 'CAEC']:
        df[k] = df[k].map(tingkat)
    df = pd.get_dummies(df, columns=['MTRANS'])

    # Samakan kolom dengan data latih (kolom yang tidak ada diisi 0)
    df = df.reindex(columns=kolom_fitur, fill_value=0).astype(float)

    # Standardisasi Age, Height, Weight memakai scaler dari data latih
    df[kolom_scale] = scaler.transform(df[kolom_scale])
    return df


@app.route('/')
def home():
    return jsonify({'pesan': 'API prediksi tingkat obesitas berjalan'})


@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        X = proses_data(data)
        kode = int(model.predict(X)[0])
        return jsonify({'kode': kode, 'prediksi': label_target[kode]})
    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)