# Klasifikasi Tingkat Obesitas (Obesity Levels Classification)

Proyek praktikum Machine Learning untuk memprediksi tingkat obesitas seseorang berdasarkan karakteristik individu dan kebiasaan hidupnya, memakai tiga algoritma klasifikasi.

## Dataset

- **Nama:** Estimation of Obesity Levels Based on Eating Habits and Physical Condition (UCI Machine Learning Repository)
- **Ukuran:** 2.111 baris dan 17 kolom (2.087 baris setelah duplikat dihapus)
- **Target:** `NObeyesdad` dengan 7 kelas: Insufficient_Weight, Normal_Weight, Overweight_Level_I, Overweight_Level_II, Obesity_Type_I, Obesity_Type_II, Obesity_Type_III
- **Catatan:** sekitar 23% data berasal dari survei dan 77% dibangkitkan secara sintetis dengan SMOTE. Label ditentukan dari BMI, sehingga `Height` dan `Weight` sangat berpengaruh pada hasil model.

## Tahapan

1. **Data Loading:** memuat dataset dan memeriksa struktur data
2. **Data Processing:** memisahkan fitur dan target, lalu encoding (biner, ordinal, one-hot)
3. **Data Cleaning dan Transformation:** memeriksa nilai kosong, duplikat (24 baris dihapus), konsistensi kategori, rentang nilai, pencilan, dan membulatkan nilai desimal pada fitur kuesioner
4. **EDA dan ExDA:** eksplorasi distribusi, perbandingan antarkategori, korelasi, dan visualisasi temuan utama
5. **Data Splitting:** pembagian 80:20 (1.669 data latih dan 418 data uji) dengan stratifikasi, lalu standardisasi `Age`, `Height`, dan `Weight`
6. **Modelling:** melatih dan mengevaluasi tiga model klasifikasi

## Hasil

Evaluasi pada 418 data uji (rata-rata macro):

| Model | Accuracy | Precision | Recall | F1-Score |
|---|---|---|---|---|
| K-Nearest Neighbors | 0,847 | 0,852 | 0,843 | 0,837 |
| Logistic Regression | 0,873 | 0,871 | 0,871 | 0,868 |
| **Gradient Boosting** | **0,945** | **0,948** | **0,943** | **0,944** |

Gradient Boosting menjadi model terbaik: 395 dari 418 data uji diprediksi benar. Kesalahan terutama terjadi pada kategori yang bersebelahan, misalnya Overweight_Level_I dan Overweight_Level_II.

## Teknologi

Python, Pandas, Matplotlib, Seaborn, Scikit-learn, Jupyter Notebook

## Cara Menjalankan

```bash
git clone https://github.com/intanspurba/Obesity_Levels.git
cd Obesity_Levels
pip install pandas matplotlib seaborn scikit-learn jupyter
jupyter notebook ObesityDataset.ipynb
```

Pastikan berkas dataset (`ObesityDataSet_raw_and_data_sinthetic.csv`) berada di folder yang sama dengan notebook.

## Keterbatasan

Sebagian besar data bersifat sintetis dan label dihitung dari BMI, sehingga skor yang tinggi belum tentu menggambarkan kondisi nyata. Selain itu, komposisi jenis kelamin sangat timpang pada Obesity_Type_II (hampir semuanya laki-laki) dan Obesity_Type_III (hampir semuanya perempuan).

## Penulis

Intan, Teknik Informatika, Universitas Pamulang (UNPAM)
## Dataset Credit
[Obesity Levels — Kaggle](https://www.kaggle.com/datasets/fatemehmehrparvar/obesity-levels)
