# Tutorial Pengerjaan
## Student Productivity Prediction System

Tutorial ini menjelaskan alur kerja dari problem statement hingga aplikasi prediksi. Ini adalah panduan pelaksanaan; perintah dan contoh perlu disesuaikan dengan struktur serta teknologi yang benar-benar dipilih. Jangan menganggap model atau dataset sudah tersedia sebelum diverifikasi.

## 1. Gambaran alur

1. Pastikan problem statement dan target prediksi jelas.
2. Pilih dan periksa dataset.
3. Jalankan Pipeline Model AI di Google Colab.
4. Evaluasi dan ekspor model beserta preprocessing.
5. Pindahkan artefak ke lingkungan aplikasi secara eksplisit.
6. Bangun Pipeline Aplikasi dengan OpenCode.
7. Jalankan pengujian dan dokumentasikan hasil aktual.

## 2. Struktur direktori

Gunakan `AGENTS.md` sebagai instruksi utama agen coding. Scaffold yang disarankan:

```text
project-root/
├── AGENTS.md
├── README.md
├── PROJECT_STATUS.md
├── pipeline_model/
│   ├── README.md
│   ├── requirements.txt
│   ├── notebooks/
│   ├── data/{raw,interim,processed}/
│   ├── scripts/
│   ├── src/{data,features,training,evaluation,explainability,common}/
│   └── artifacts/{models,metrics,figures,reports}/
├── pipeline_app/
│   ├── README.md
│   ├── requirements.txt
│   ├── src/{inference,utils}/
│   ├── api/
│   ├── ui/
│   └── tests/{unit,integration,smoke}/
├── shared/
│   └── model_contract.md
└── docs/
    ├── problem_statement.md
    ├── dataset_card.md
    ├── model_card.md
    ├── evaluation_report.md
    └── deployment.md
```

Bila repositori telah memiliki struktur, periksa dulu dan sesuaikan tanpa menghapus pekerjaan yang sudah ada. File notebook hanya dibuat jika memang dibutuhkan; skrip Python dapat menjadi alternatif.

## 3. Tahap awal: definisikan masalah

1. Baca problem statement, proposal, atau presentasi yang tersedia.
2. Isi `docs/problem_statement.md` dengan tujuan, pengguna, input, output, batasan, asumsi, dan kriteria keberhasilan.
3. Pastikan unit observasi adalah satu mahasiswa/satu catatan yang definisinya jelas.
4. Tentukan apakah target dataset berupa:
   - **skor numerik** → tugas regresi; atau
   - **kategori produktivitas yang telah didefinisikan** → tugas klasifikasi.
5. Jangan mengubah skor menjadi kategori tanpa aturan kategorisasi yang terdokumentasi dan dapat dibenarkan.
6. Catat pertanyaan yang belum terjawab sebelum training.

## 4. Pilih dan periksa dataset

Kaggle merupakan sumber yang direncanakan, bukan dataset final yang sudah dipastikan.

1. Cari dataset dengan fitur dan target yang sesuai dengan masalah.
2. Periksa deskripsi dataset, pemilik/sumber, lisensi atau ketentuan penggunaan, definisi kolom, tanggal/versi, serta keterbatasannya.
3. Unduh dataset hanya sesuai ketentuan sumber.
4. Simpan data mentah di `pipeline_model/data/raw/` dan jangan mengubahnya langsung.
5. Periksa:
   - jumlah baris dan kolom;
   - nama kolom dan tipe data;
   - nilai kosong dan duplikasi;
   - rentang nilai dan outlier;
   - distribusi target;
   - fitur yang bocor dari target atau tidak tersedia saat prediksi.
6. Catat temuan dalam `docs/dataset_card.md`.

Contoh pemeriksaan awal dengan pandas (ganti `path/to/dataset.csv` dengan lokasi file yang benar):

```python
import pandas as pd

df = pd.read_csv("path/to/dataset.csv")

print("Ukuran:", df.shape)
print("\nKolom dan tipe data:")
print(df.dtypes)
print("\nNilai kosong:")
print(df.isna().sum().sort_values(ascending=False))
print("\nDuplikasi:", df.duplicated().sum())
print("\nRingkasan:")
print(df.describe(include="all").T)
```

Jangan jalankan kode ini sebelum memastikan format file dan path dataset yang sebenarnya.

## 5. Kerjakan Pipeline Model AI di Google Colab

### 5.1 Siapkan lingkungan

1. Buka Google Colab dan buat notebook untuk pipeline model.
2. Hubungkan atau unggah dataset sesuai aturan penggunaannya.
3. Catat versi Python dan library utama.
4. Instal hanya dependensi yang diperlukan. Hindari menulis versi library fiktif sebelum kebutuhan dan lingkungan diketahui.

### 5.2 EDA dan preprocessing

- Visualisasikan distribusi target dan fitur utama.
- Periksa hubungan antarfitur serta potensi outlier.
- Tentukan fitur yang digunakan dan alasan pengecualiannya.
- Pisahkan data training dan test sebelum melakukan pemilihan model berdasarkan hasil evaluasi.
- Fit imputasi, encoding, scaling, atau transformasi lain pada training data saja; gunakan transformasi yang sama untuk validation/test dan inference.
- Gunakan validation set atau cross-validation untuk pemilihan model jika sesuai.

### 5.3 Latih dan bandingkan model

Jika target berupa skor numerik, kandidat awal yang dapat diuji:
- Linear Regression sebagai baseline.
- Random Forest Regressor sebagai pembanding.
- XGBoost Regressor jika layak dan dependensinya tersedia.

Jika target berupa kategori, gunakan estimator klasifikasi yang sesuai, misalnya Logistic Regression sebagai baseline dan Random Forest Classifier sebagai pembanding. XGBoost classifier hanya dipakai jika sesuai. Algoritma final dipilih berdasarkan data dan evaluasi, bukan ditentukan sebelumnya.

Gunakan skema split dan metrik yang konsisten:
- **Regresi:** MAE dan RMSE; pertimbangkan metrik lain bila diperlukan.
- **Klasifikasi:** Precision, Recall, F1-score, confusion matrix, serta metrik tambahan bila relevan.

Catat konfigurasi, seed bila relevan, hasil aktual, analisis error, dan keterbatasan. Jangan mengisi laporan dengan angka contoh seolah-olah hasil eksperimen.

### 5.4 Interpretabilitas

Gunakan SHAP atau metode interpretabilitas lain bila sesuai dengan model dan kebutuhan. Jelaskan hasil sebagai pola asosiasi/prediksi; jangan menyimpulkan sebab-akibat hanya dari nilai interpretabilitas.

### 5.5 Ekspor model

Ekspor artefak yang dibutuhkan untuk inference, yang dapat mencakup:
- model terlatih;
- preprocessing yang sudah di-fit;
- label mapping jika klasifikasi;
- metadata fitur dan urutan fitur;
- versi Python/library;
- metrik evaluasi dan versi artefak.

Pilih format berdasarkan model dan kebutuhan keamanan. Jangan memuat artefak serialisasi yang tidak tepercaya. Catat cara memuat model dan contoh inference di `shared/model_contract.md`.

## 6. Pindahkan artefak ke aplikasi

Google Colab dan OpenCode mungkin tidak menggunakan filesystem yang sama.

1. Identifikasi file artefak yang benar-benar dihasilkan oleh eksperimen.
2. Unduh artefak dari Colab atau gunakan media transfer yang telah disetujui dan dikonfigurasi.
3. Letakkan artefak di lokasi aplikasi yang disepakati, misalnya direktori artefak lokal yang tidak dimasukkan ke Git bila ukurannya besar.
4. Catat nama file, format, versi, dan dependensinya.
5. Pastikan aplikasi dapat memuat artefak dan menjalankan prediksi contoh.
6. Jangan membuat path, URL, token, atau kredensial berdasarkan asumsi.

## 7. Kerjakan Pipeline Aplikasi dengan OpenCode

1. Buka repositori proyek di lingkungan OpenCode.
2. Pastikan `AGENTS.md` tersedia pada root dan memuat instruksi dua pipeline.
3. Minta agen memeriksa repositori, membuat/menyesuaikan scaffold, dan melaporkan perubahan sebelum implementasi besar.
4. Implementasikan modul inference yang memuat model dan preprocessing sesuai `shared/model_contract.md`.
5. Validasi input: kolom wajib, tipe data, nilai yang masuk akal, nilai kosong, dan kategori yang diizinkan.
6. Bangun API dan/atau UI sesuai kebutuhan proyek. Jangan membuat keduanya jika tidak diperlukan.
7. Tampilkan hasil prediksi dengan penjelasan yang jelas bahwa hasil adalah estimasi, bukan penilaian mutlak.
8. Tangani model yang hilang/tidak kompatibel dan input tidak valid dengan pesan yang aman dan informatif.
9. Tambahkan tes unit, integrasi, dan smoke test yang relevan.

Contoh prompt untuk OpenCode:

```text
Baca AGENTS.md dan docs/problem_statement.md terlebih dahulu.
Periksa struktur repositori dan file yang sudah ada sebelum mengubah apa pun.
Implementasikan Pipeline Aplikasi pada pipeline_app/ untuk memuat artefak
model dan preprocessing sesuai shared/model_contract.md.
Jangan mengarang path, fitur, target, metrik, atau file model yang belum tersedia.
Tambahkan validasi input dan tes untuk input valid, input tidak valid,
serta kondisi artefak model tidak tersedia.
Jalankan tes yang tersedia dan laporkan hasil aktual beserta file yang diubah.
```

## 8. Pengujian

Minimal, uji kasus berikut sesuai implementasi:

- input dengan semua fitur wajib dan nilai valid;
- input dengan kolom wajib yang hilang;
- tipe data salah;
- nilai di luar rentang atau kategori yang diperbolehkan;
- nilai kosong;
- artefak model tidak ditemukan;
- artefak tidak cocok dengan kontrak/versi yang diharapkan;
- alur lengkap input → inference → output.

Pastikan tes benar-benar dijalankan sebelum melaporkan lulus. Jika tidak dapat dijalankan, tulis alasan dan statusnya.

## 9. Dokumentasi yang harus diperbarui

- `README.md`: ringkasan dan cara menjalankan.
- `PROJECT_STATUS.md`: status pekerjaan, perubahan, tes, kendala, dan langkah selanjutnya.
- `docs/problem_statement.md`: masalah, pengguna, input/output, batasan.
- `docs/dataset_card.md`: sumber, lisensi/ketentuan, skema, target, kualitas, keterbatasan.
- `docs/model_card.md`: tujuan model, data, evaluasi, batasan, penggunaan yang tidak dianjurkan.
- `docs/evaluation_report.md`: metode dan hasil aktual.
- `shared/model_contract.md`: fitur, preprocessing, input/output, format dan versi artefak.
- `docs/deployment.md`: cara konfigurasi dan menjalankan aplikasi jika diperlukan.

`laporan.md` digunakan untuk rangkuman perencanaan dan hasil proyek. Perbarui bagian hasil setelah eksperimen. `tutorial.md` digunakan sebagai panduan proses kerja.

## 10. Checklist akhir

- [ ] Dataset dan target telah diverifikasi.
- [ ] EDA dan preprocessing terdokumentasi.
- [ ] Tidak ada data leakage yang diketahui dalam proses evaluasi.
- [ ] Minimal dua algoritma yang sesuai telah dibandingkan.
- [ ] Metrik aktual dan analisis error tercatat.
- [ ] Model serta preprocessing berhasil diekspor dan dimuat kembali.
- [ ] Aplikasi menjalankan inference sesuai kontrak model.
- [ ] Input tidak valid ditangani.
- [ ] Tes relevan dijalankan dan hasilnya dicatat.
- [ ] Dokumentasi diperbarui tanpa klaim yang belum dibuktikan.
