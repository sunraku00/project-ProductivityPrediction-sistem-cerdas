# Student Productivity Prediction System

Sistem prediksi produktivitas belajar mahasiswa/siswa berdasarkan pola belajar dan kebiasaan sehari-hari, seperti durasi belajar, tidur, penggunaan perangkat digital, aktivitas fisik, dan manajemen waktu.

> **Status:** tahap perencanaan dan persiapan. Dataset final, target prediksi, hasil eksperimen, dan hasil pengujian aplikasi belum ditetapkan. Jangan menganggap metrik atau hasil model sudah tersedia sebelum eksperimen benar-benar dijalankan.

## Tujuan

- Menentukan dataset yang relevan dan mendokumentasikan sumber serta lisensinya.
- Menyiapkan pipeline machine learning yang dapat diulang.
- Membandingkan setidaknya dua algoritma dengan pembagian data dan metrik evaluasi yang konsisten.
- Menyimpan model beserta preprocessing yang dibutuhkan agar dapat digunakan kembali.
- Membuat aplikasi untuk menerima input, memvalidasi data, dan menampilkan prediksi.
- Mendokumentasikan proses, keputusan, hasil, keterbatasan, dan cara menjalankan proyek.

## Pilihan pendekatan

Jenis tugas harus ditentukan dari target dataset yang benar-benar dipilih:

- **Regresi** jika target berupa skor produktivitas numerik. Kandidat awal: Linear Regression sebagai baseline dan Random Forest Regressor; XGBoost dapat dipertimbangkan jika sesuai.
- **Klasifikasi** jika target memiliki label kategori yang jelas dan valid. Gunakan estimator klasifikasi serta metrik seperti precision, recall, F1-score, dan confusion matrix.

Jangan mengubah angka menjadi kategori hanya demi memaksakan klasifikasi tanpa alasan yang terdokumentasi.

## Struktur proyek yang disarankan

```text
project-root/
├── AGENTS.md
├── README.md
├── cloude.md
├── PROJECT_STATUS.md
├── laporan.md
├── tutorial.md
├── pipeline_model/       # eksperimen dan pelatihan di Google Colab
├── pipeline_app/         # aplikasi yang dibangun dengan OpenCode
├── shared/
│   └── model_contract.md # kontrak fitur, target, preprocessing, dan artefak
└── docs/                 # catatan tambahan dan dokumentasi
```

Nama `cloude.md` dipertahankan sesuai permintaan; jika sebenarnya yang dimaksud adalah `CLAUDE.md`, sesuaikan nama file dengan tool yang digunakan.

## Alur kerja

1. Tinjau `AGENTS.md` dan `PROJECT_STATUS.md`.
2. Pilih dan periksa dataset; pastikan target, fitur, lisensi, dan kualitas data dipahami.
3. Catat kontrak data dan model di `shared/model_contract.md`.
4. Kerjakan EDA, preprocessing, baseline, pelatihan, dan evaluasi di `pipeline_model/` menggunakan Google Colab.
5. Bandingkan minimal dua algoritma yang sesuai dengan jenis target.
6. Simpan model dan preprocessing dalam artefak yang dapat digunakan ulang; dokumentasikan versi dan cara memuatnya.
7. Bangun aplikasi di `pipeline_app/` dengan OpenCode, mengikuti kontrak model yang sama.
8. Uji validasi input, pemuatan artefak, prediksi, dan penanganan error.
9. Perbarui laporan serta status proyek berdasarkan hasil nyata.

## Evaluasi

- **Regresi:** MAE dan RMSE; metrik tambahan dapat digunakan bila relevan.
- **Klasifikasi:** precision, recall, F1-score, dan confusion matrix.
- Semua model yang dibandingkan harus menggunakan split data dan prosedur evaluasi yang sebanding.
- Hindari kebocoran data (*data leakage*). Lakukan preprocessing yang belajar dari data hanya pada data latih, misalnya melalui pipeline.
- Catat random seed, versi pustaka, fitur yang digunakan, dan hasil eksperimen.

## Batasan penggunaan

Prediksi merupakan estimasi berdasarkan pola dalam dataset, bukan penilaian mutlak atas kemampuan seseorang dan bukan bukti hubungan sebab-akibat. Performa model dapat berubah ketika diterapkan pada populasi atau konteks yang berbeda. Hindari memasukkan data pribadi yang tidak diperlukan.

## Dokumentasi

- `AGENTS.md` — pedoman kerja dan aturan proyek.
- `cloude.md` — petunjuk khusus untuk agen/tool coding yang dipakai; pastikan isinya sesuai tool sebenarnya.
- `PROJECT_STATUS.md` — status terkini, keputusan, hambatan, dan langkah berikutnya.
- `laporan.md` — laporan proyek dan hasil eksperimen yang akan dilengkapi berdasarkan bukti.
- `tutorial.md` — panduan langkah demi langkah untuk menjalankan pipeline dan aplikasi.

## Menjalankan Aplikasi

Aplikasi dibangun menggunakan Streamlit. Untuk menjalankannya:

1. Masuk ke direktori `pipeline_app`:
   ```bash
   cd pipeline_app
   ```
2. Pastikan dependensi terinstall:
   ```bash
   pip install -r requirements.txt
   ```
3. Jalankan aplikasi dengan perintah berikut:
   ```bash
   streamlit run src/app.py
   ```
4. Buka tautan URL yang muncul di terminal (biasanya `http://localhost:8501`).

