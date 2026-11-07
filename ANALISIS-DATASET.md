# Analisis Dataset Binary, Multiclass, dan Multilabel

## Dataset Binary

Ketiga dataset ini adalah **klasifikasi binary**: targetnya kategori dengan tepat 2 kelas, dan setiap baris hanya punya satu label.

### 1. Bank Customer Churn Prediction

- **Sumber:** [Kaggle: Customer Churn Data](https://www.kaggle.com/datasets/bhuviranga/customer-churn-data)
- **Ukuran:** 10.000 baris, 12 kolom. Tidak ada data kosong.
- **Target:** `churn`, bernilai 0 (tetap menjadi nasabah) atau 1 (berhenti).
- **Jenis tugas:** klasifikasi, bukan regresi. Targetnya hanya dua nilai tetap (0 dan 1), bukan angka kontinu.
- **Bukti:** `churn` = 0 ada 7.963 baris (79,6%) dan `churn` = 1 ada 2.037 baris (20,4%). Tidak ada nilai ketiga.
- **Alasan binary:** hanya 2 kelas, dan satu nasabah tidak mungkin churn dan tidak churn sekaligus.
- **Fitur:** `credit_score`, `country`, `gender`, `age`, `tenure`, `balance`, `products_number`, `credit_card`, `active_member`, `estimated_salary`. Kolom `customer_id` hanya ID.
- **Catatan:** file versi "selected columns" tidak punya kolom `churn`, jadi tidak bisa dipakai. Gunakan file lengkap.

### 2. Breast Cancer Wisconsin (BRCA)

- **Sumber:** [Kaggle: Breast Cancer Wisconsin Diagnostic](https://www.kaggle.com/datasets/utkarshx27/breast-cancer-wisconsin-diagnostic-dataset)
- **Ukuran:** 569 baris, 32 kolom. Tidak ada data kosong.
- **Target:** `y`, berisi huruf B (Benign, jinak) atau M (Malignant, ganas).
- **Jenis tugas:** klasifikasi. Target berupa huruf kategori, bukan angka kontinu.
- **Bukti:** B ada 357 baris (62,7%) dan M ada 212 baris (37,3%).
- **Alasan binary:** hanya 2 kelas yang saling eksklusif. Satu sampel sel tidak bisa jinak dan ganas sekaligus.
- **Fitur:** 30 kolom numerik hasil pengukuran sel (`x.radius_mean`, `x.area_worst`, dan seterusnya). Kolom `Unnamed: 0` hanya nomor urut.

### 3. Credit Card Fraud

- **Sumber:** [Kaggle: Credit Card Fraud Detection (notebook)](https://www.kaggle.com/code/abdelazizelserty/credit-card-fraud-detection-dataset/input)
- **Ukuran:** 10.000 baris, 10 kolom. Tidak ada data kosong.
- **Target:** `is_fraud`, bernilai 0 (transaksi normal) atau 1 (penipuan).
- **Jenis tugas:** klasifikasi. Targetnya hanya dua nilai tetap, bukan angka kontinu.
- **Bukti:** `is_fraud` = 0 ada 9.849 baris (98,5%) dan `is_fraud` = 1 ada 151 baris (1,5%).
- **Alasan binary:** hanya 2 kelas, dan satu transaksi hanya bisa normal atau penipuan.
- **Fitur:** `amount`, `transaction_hour`, `merchant_category`, `foreign_transaction`, `location_mismatch`, `device_trust_score`, `velocity_last_24h`, `cardholder_age`. Kolom `transaction_id` hanya ID.
- **Catatan:** datanya sangat tidak seimbang (fraud hanya 1,5%).

## Dataset Multiclass

Ketiga dataset ini adalah **klasifikasi multiclass**: targetnya kategori dengan 3 kelas atau lebih, saling eksklusif, dan setiap baris hanya punya satu label pasti.

### 1. Wine Quality (Red)

- **Sumber:** [Kaggle: XGBoost Multi-class Classification (notebook)](https://www.kaggle.com/code/emmanuelfwerr/xgboost-multi-class-classification/input)
- **Ukuran:** 1.599 baris, 12 kolom. Tidak ada data kosong.
- **Target:** `quality`, skor kualitas anggur.
- **Jenis tugas:** klasifikasi. Targetnya hanya 6 nilai bulat tetap (3 sampai 8), bukan angka kontinu. Skor ini berurutan (ordinal), jadi secara teori bisa diperlakukan sebagai regresi. Dalam tugas ini ia dipakai sebagai kategori.
- **Bukti:** kelas 3 = 10 baris, kelas 4 = 53, kelas 5 = 681, kelas 6 = 638, kelas 7 = 199, kelas 8 = 18.
- **Alasan multiclass:** ada 6 kelas, dan satu sampel anggur hanya punya satu skor kualitas.
- **Fitur:** 11 kolom numerik hasil uji kimia (`fixed acidity`, `volatile acidity`, `citric acid`, `residual sugar`, `chlorides`, `free sulfur dioxide`, `total sulfur dioxide`, `density`, `pH`, `sulphates`, `alcohol`).
- **Catatan:** kelas 5 dan 6 mencakup sekitar 82% data, jadi tidak seimbang.

### 2. Car Evaluation

- **Sumber:** [Kaggle: Decision Tree Classifier Tutorial (notebook)](https://www.kaggle.com/code/prashant111/decision-tree-classifier-tutorial/input?select=car_evaluation.csv)
- **Ukuran:** 1.728 baris, 7 kolom. Tidak ada data kosong.
- **Target:** `class`, penilaian kelayakan mobil.
- **Jenis tugas:** klasifikasi. Targetnya berupa kata (kategori), bukan angka.
- **Bukti:** `unacc` = 1.210 baris, `acc` = 384, `good` = 69, `vgood` = 65.
- **Alasan multiclass:** ada 4 kelas, dan satu mobil hanya mendapat satu penilaian.
- **Fitur:** 6 kolom kategorikal: `buying`, `maint`, `doors`, `persons`, `lug_boot`, `safety`.
- **Catatan:** file ini tidak punya baris header, jadi saat dibaca di Python pakai `header=None` dan beri nama kolom sendiri.

### 3. Website Phishing

- **Sumber:** [Kaggle: Website Phishing Data Set](https://www.kaggle.com/datasets/ahmednour/website-phishing-data-set)
- **Ukuran:** 1.353 baris, 10 kolom. Tidak ada data kosong.
- **Target:** `Result`, bernilai -1 (phishing), 0 (mencurigakan), atau 1 (sah).
- **Jenis tugas:** klasifikasi. Angka -1, 0, dan 1 hanyalah kode kategori, bukan besaran yang bisa dihitung.
- **Bukti:** -1 (phishing) = 702 baris, 1 (sah) = 548, 0 (mencurigakan) = 103.
- **Alasan multiclass:** ada 3 kelas, dan satu situs hanya masuk satu kelas.
- **Fitur:** 9 kolom (`SFH`, `popUpWidnow`, `SSLfinal_State`, `Request_URL`, `URL_of_Anchor`, `web_traffic`, `URL_Length`, `age_of_domain`, `having_IP_Address`), semuanya sudah berupa kode -1, 0, 1.
- **Catatan:** kelas 0 hanya sekitar 7,6% data.

## Dataset Multilabel

Ketiga dataset ini adalah **klasifikasi multilabel**: ada beberapa kolom label 0/1, dan satu baris boleh punya lebih dari satu label sekaligus. Sumbernya [repositori Mulan](https://mulan.sourceforge.net/datasets-mlc.html), kumpulan dataset multilabel standar ([Tsoumakas dkk., JMLR 2011](https://jmlr2020.csail.mit.edu/papers/volume12/tsoumakas11a/tsoumakas11a.pdf)).

### 1. Emotions (musik)

- **Sumber:** [emotions.rar (Mulan)](http://sourceforge.net/projects/mulan/files/datasets/emotions.rar)
- **Ukuran:** 593 baris, 72 fitur numerik, 6 kolom label. Tidak ada data kosong.
- **Target:** 6 kolom label 0/1: `amazed-suprised`, `happy-pleased`, `relaxing-calm`, `quiet-still`, `sad-lonely`, `angry-aggresive` (ejaan sesuai file asli).
- **Jenis tugas:** klasifikasi. Setiap label hanya bernilai 0 atau 1, bukan angka kontinu.
- **Bukti:** 415 dari 593 baris (70,0%) punya 2 label atau lebih. Sisanya 178 baris punya 1 label, dan tidak ada baris tanpa label. Rata-rata 1,87 label per baris, dengan 27 kombinasi label berbeda. Jumlah per label: 173, 166, 264, 148, 168, 189.
- **Alasan multilabel:** satu lagu bisa punya beberapa emosi sekaligus, dan label-labelnya tidak saling eksklusif.

### 2. Scene (gambar)

- **Sumber:** [scene.rar (Mulan)](http://sourceforge.net/projects/mulan/files/datasets/scene.rar)
- **Ukuran:** 2.407 baris, 294 fitur numerik, 6 kolom label. Tidak ada data kosong. Fiturnya hasil ekstraksi dari gambar, bukan foto mentah.
- **Target:** 6 kolom label 0/1: `Beach`, `Sunset`, `FallFoliage`, `Field`, `Mountain`, `Urban`.
- **Jenis tugas:** klasifikasi. Setiap label hanya bernilai 0 atau 1.
- **Bukti:** 177 baris (7,4%) punya 2 label atau lebih (176 baris dua label, 1 baris tiga label). Sebanyak 2.230 baris punya 1 label, dan tidak ada baris tanpa label. Rata-rata 1,07 label per baris, dengan 15 kombinasi label berbeda. Jumlah per label: 427, 364, 397, 433, 533, 431.
- **Alasan multilabel:** satu gambar bisa memuat beberapa adegan sekaligus, misalnya pantai dan matahari terbenam.
- **Catatan:** sebagian besar baris hanya punya satu label, tapi tetap multilabel karena 177 baris punya lebih dari satu.

### 3. Yeast (biologi)

- **Sumber:** [yeast.rar (Mulan)](http://sourceforge.net/projects/mulan/files/datasets/yeast.rar)
- **Ukuran:** 2.417 baris, 103 fitur numerik, 14 kolom label. Tidak ada data kosong.
- **Target:** 14 kolom label 0/1: `Class1` sampai `Class14` (kelompok fungsi gen ragi).
- **Jenis tugas:** klasifikasi. Setiap label hanya bernilai 0 atau 1.
- **Bukti:** 2.385 dari 2.417 baris (98,7%) punya 2 label atau lebih. Hanya 32 baris punya 1 label, dan tidak ada baris tanpa label. Rata-rata 4,24 label per baris, maksimal 11, dengan 198 kombinasi label berbeda. Label paling sering: `Class12` (1.816 baris) dan `Class13` (1.799 baris). Paling jarang: `Class14` (34 baris).
- **Alasan multilabel:** satu gen bisa punya beberapa fungsi sekaligus, sehingga label-labelnya tumpang tindih.

## Ringkasan

Semua 9 dataset yang diperiksa adalah klasifikasi, karena targetnya kategori dengan jumlah nilai terbatas.

| Dataset | Jenis | Target | Jumlah kelas / label | Tugas |
| --- | --- | --- | --- | --- |
| Bank Customer Churn | Binary | `churn` | 2 | Klasifikasi |
| Breast Cancer (BRCA) | Binary | `y` | 2 | Klasifikasi |
| Credit Card Fraud | Binary | `is_fraud` | 2 | Klasifikasi |
| Wine Quality (Red) | Multiclass | `quality` | 6 | Klasifikasi |
| Car Evaluation | Multiclass | `class` | 4 | Klasifikasi |
| Website Phishing | Multiclass | `Result` | 3 | Klasifikasi |
| Emotions | Multilabel | 6 kolom label 0/1 | 6 | Klasifikasi |
| Scene | Multilabel | 6 kolom label 0/1 | 6 | Klasifikasi |
| Yeast | Multilabel | 14 kolom label 0/1 | 14 | Klasifikasi |

## Sumber Dataset

| Dataset | Jenis | Sumber |
| --- | --- | --- |
| Bank Customer Churn | Binary | [Kaggle: Customer Churn Data](https://www.kaggle.com/datasets/bhuviranga/customer-churn-data) |
| Breast Cancer (BRCA) | Binary | [Kaggle: Breast Cancer Wisconsin Diagnostic](https://www.kaggle.com/datasets/utkarshx27/breast-cancer-wisconsin-diagnostic-dataset) |
| Credit Card Fraud | Binary | [Kaggle: Credit Card Fraud Detection (notebook)](https://www.kaggle.com/code/abdelazizelserty/credit-card-fraud-detection-dataset/input) |
| Wine Quality (Red) | Multiclass | [Kaggle: XGBoost Multi-class Classification (notebook)](https://www.kaggle.com/code/emmanuelfwerr/xgboost-multi-class-classification/input) |
| Car Evaluation | Multiclass | [Kaggle: Decision Tree Classifier Tutorial (notebook)](https://www.kaggle.com/code/prashant111/decision-tree-classifier-tutorial/input?select=car_evaluation.csv) |
| Website Phishing | Multiclass | [Kaggle: Website Phishing Data Set](https://www.kaggle.com/datasets/ahmednour/website-phishing-data-set) |
| Emotions | Multilabel | [emotions.rar (Mulan)](http://sourceforge.net/projects/mulan/files/datasets/emotions.rar) |
| Scene | Multilabel | [scene.rar (Mulan)](http://sourceforge.net/projects/mulan/files/datasets/scene.rar) |
| Yeast | Multilabel | [yeast.rar (Mulan)](http://sourceforge.net/projects/mulan/files/datasets/yeast.rar) |
