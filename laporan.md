# Laporan Proyek
## Student Productivity Prediction System

**Topik:** Penerapan Machine Learning untuk memprediksi tingkat produktivitas mahasiswa berdasarkan pola belajar dan kebiasaan sehari-hari.

> **Status dokumen:** Laporan perencanaan awal. Dataset final, hasil eksperimen, nilai metrik, model terbaik, dan hasil pengujian aplikasi belum ditetapkan atau diverifikasi. Bagian hasil harus diperbarui setelah eksperimen benar-benar dijalankan.

## 1. Ringkasan

Student Productivity Prediction System dirancang sebagai sistem berbasis supervised machine learning untuk memperkirakan produktivitas mahasiswa dari fitur yang tersedia dalam dataset, misalnya durasi belajar, durasi tidur, penggunaan perangkat digital, aktivitas fisik, dan manajemen waktu.

Sistem direncanakan memiliki dua bagian yang terpisah:

1. **Pipeline Model AI — Google Colab:** pemilihan dan pemeriksaan dataset, EDA, preprocessing, pelatihan dan evaluasi model, interpretabilitas bila sesuai, serta ekspor artefak model.
2. **Pipeline Aplikasi — OpenCode:** pemuatan artefak model, validasi input, proses inference, penyajian hasil prediksi melalui API atau antarmuka pengguna, serta pengujian aplikasi.

Hasil prediksi merupakan estimasi berdasarkan pola yang dipelajari dari data. Hasil tersebut bukan penilaian mutlak atas produktivitas seseorang dan tidak membuktikan hubungan sebab-akibat.

## 2. Latar Belakang dan Rumusan Masalah

Mahasiswa memiliki kebiasaan sehari-hari yang berbeda, termasuk pola belajar, tidur, aktivitas fisik, penggunaan perangkat digital, dan pengelolaan waktu. Faktor-faktor tersebut dapat berkaitan dengan produktivitas, tetapi hubungan dan kekuatan pengaruhnya harus diperiksa melalui data.

**Rumusan masalah:** bagaimana membangun model supervised machine learning yang dapat memperkirakan skor atau kategori produktivitas mahasiswa berdasarkan fitur yang tersedia pada dataset yang relevan, serta menyajikan hasil prediksi melalui aplikasi sederhana?

## 3. Tujuan

1. Menemukan dataset yang relevan, memiliki dokumentasi, dan menyediakan target yang dapat dipertanggungjawabkan.
2. Memahami karakteristik dan kualitas dataset melalui EDA.
3. Menyiapkan preprocessing yang dapat diterapkan secara konsisten pada training dan inference.
4. Melatih serta membandingkan minimal dua algoritma yang sesuai dengan target dan dataset.
5. Menilai model menggunakan metrik yang sesuai dan mendokumentasikan keterbatasannya.
6. Menyimpan model agar dapat digunakan kembali oleh aplikasi.
7. Membuat aplikasi yang menerima input, memvalidasi data, menampilkan prediksi, dan menangani input yang tidak valid.

## 4. Ruang Lingkup

### 4.1 Termasuk dalam proyek

- Pencarian dataset, dengan Kaggle sebagai sumber yang direncanakan.
- Pemeriksaan sumber, lisensi/ketentuan penggunaan, kolom, tipe data, missing values, duplikasi, distribusi target, dan potensi data leakage.
- EDA dan preprocessing.
- Baseline serta model pembanding.
- Evaluasi dan analisis kesalahan.
- Interpretabilitas, misalnya SHAP, jika sesuai dengan model dan kebutuhan.
- Ekspor model dan preprocessing yang diperlukan.
- Aplikasi inference dengan API dan/atau UI sesuai kebutuhan.
- Pengujian, dokumentasi, dan instruksi menjalankan proyek.

### 4.2 Di luar klaim proyek

- Tidak menyatakan bahwa kebiasaan tertentu menyebabkan produktivitas meningkat atau menurun hanya dari model prediksi.
- Tidak menetapkan ambang performa sebelum baseline dan karakteristik dataset diketahui.
- Tidak menganggap kategori rendah/sedang/tinggi valid jika dataset tidak menyediakan label tersebut atau aturan kategorisasinya belum dibenarkan secara metodologis.
- Tidak mengklaim sistem siap produksi sebelum pengujian dan tinjauan yang relevan selesai.

## 5. Data dan Target Prediksi

**Sumber yang direncanakan:** Kaggle. Dataset final belum dipilih.

**Fitur kandidat:** durasi belajar, durasi tidur, penggunaan perangkat digital, aktivitas fisik, manajemen waktu, dan fitur kebiasaan lain yang benar-benar tersedia serta relevan pada dataset terpilih.

**Target utama yang direncanakan:** skor produktivitas mahasiswa.

- Jika target berupa nilai numerik, gunakan pendekatan regresi.
- Jika dataset hanya menyediakan label kategori yang sahih, gunakan klasifikasi.
- Jika kategori dibuat dari skor numerik, dokumentasikan dasar, ambang, dan konsekuensi kategorisasi. Jangan memilih ambang semata-mata untuk memperbaiki metrik.

Sebelum training, dokumentasikan nama kolom target, satuan/arti target, unit observasi, dan cara menangani data yang tidak lengkap.

## 6. Rencana Metodologi

1. **Pemilihan dataset:** tinjau relevansi, dokumentasi, izin penggunaan, definisi target, ukuran dan kualitas data.
2. **Validasi data:** periksa skema, tipe data, nilai hilang, duplikasi, rentang nilai, outlier, distribusi target, dan potensi leakage.
3. **EDA:** gunakan ringkasan statistik dan visualisasi yang menjawab pertanyaan terkait data.
4. **Pembagian data:** pisahkan training dan test sebelum keputusan yang dapat menyebabkan leakage. Gunakan validation set atau cross-validation bila sesuai.
5. **Preprocessing:** tangani missing values, kategori, scaling jika dibutuhkan, dan transformasi lain menggunakan pipeline yang dapat dipakai ulang. Fit transformasi pada data training saja.
6. **Baseline dan pembanding:** untuk regresi, Linear Regression dapat menjadi baseline dan Random Forest Regressor sebagai pembanding; XGBoost Regressor dapat dicoba jika sesuai. Untuk klasifikasi, gunakan versi algoritma klasifikasi yang tepat dan baseline yang sesuai.
7. **Evaluasi:** gunakan MAE dan RMSE untuk regresi. Untuk klasifikasi, gunakan Precision, Recall, F1-score, dan confusion matrix, serta metrik tambahan jika dibutuhkan.
8. **Interpretabilitas:** gunakan SHAP atau metode lain bila kompatibel dan bermanfaat. Interpretasi fitur bukan bukti kausalitas.
9. **Ekspor:** simpan model bersama preprocessing, label mapping bila ada, versi dependensi, dan metadata.
10. **Integrasi aplikasi:** implementasikan inference sesuai kontrak model bersama.
11. **Pengujian dan dokumentasi:** jalankan tes yang relevan dan catat hasil aktual, termasuk kegagalan dan keterbatasan.

## 7. Rencana Arsitektur

```text
Dataset
   |
   v
pipeline_model/ (Google Colab)
   |-- Validasi data dan EDA
   |-- Preprocessing
   |-- Baseline dan model pembanding
   |-- Evaluasi dan interpretabilitas
   |-- Ekspor model + preprocessing + metadata
   |
   v
Artefak model + shared/model_contract.md
   |
   |  Pemindahan artefak melalui mekanisme yang disetujui
   v
pipeline_app/ (OpenCode)
   |-- Validasi input
   |-- Inference
   |-- API dan/atau UI
   |-- Pengujian
   v
Hasil prediksi untuk pengguna
```

Google Colab dan lingkungan OpenCode mungkin tidak berbagi filesystem. Karena itu, ekspor dan pemindahan artefak harus menjadi langkah eksplisit.

## 8. Rencana Evaluasi

| Aspek | Rencana pemeriksaan | Status |
|---|---|---|
| Relevansi dataset | Sumber, dokumentasi, target, dan fitur diperiksa | Belum dilakukan |
| Kualitas data | Missing values, duplikasi, rentang, distribusi, leakage | Belum dilakukan |
| Perbandingan model | Minimal dua algoritma yang sesuai, split evaluasi yang sama | Belum dilakukan |
| Regresi | MAE dan RMSE; metrik lain bila diperlukan | Menunggu target dan eksperimen |
| Klasifikasi | Precision, Recall, F1-score, confusion matrix | Hanya jika target kategori |
| Artefak model | Model dan preprocessing dapat dimuat kembali | Belum dilakukan |
| Aplikasi | Input valid/tidak valid dan alur prediksi diuji | Belum dilakukan |
| Reproduksibilitas | Langkah, dependensi, konfigurasi, dan seed dicatat | Belum dilakukan |

**Hasil aktual:** isi bagian ini setelah eksperimen. Jangan mengisi nilai metrik perkiraan sebagai hasil.

### 8.1 Tabel hasil eksperimen

| Model | Jenis target | Metrik utama | Hasil aktual | Catatan |
|---|---|---|---|---|
| Baseline | Belum ditentukan | Sesuai target | Belum tersedia | Isi setelah training |
| Model pembanding | Belum ditentukan | Sesuai target | Belum tersedia | Isi setelah training |
| Model lanjutan (opsional) | Belum ditentukan | Sesuai target | Belum tersedia | Uji bila relevan |

## 9. Kriteria Keberhasilan

Proyek dapat dinyatakan berhasil setelah bukti berikut tersedia:

1. Dataset relevan dan target prediksinya jelas serta terdokumentasi.
2. Pipeline pengolahan data dan training dapat dijalankan kembali dengan prosedur terdokumentasi.
3. Minimal dua algoritma yang sesuai berhasil dilatih dan dibandingkan pada skema evaluasi yang sama.
4. Evaluasi menggunakan metrik yang sesuai dengan tipe target.
5. Model terbaik yang dipilih berdasarkan evaluasi dapat disimpan dan digunakan kembali.
6. Aplikasi menerima input, menampilkan prediksi, dan menangani input tidak valid.
7. Dokumentasi penggunaan, hasil evaluasi aktual, keterbatasan model, dan struktur proyek tersedia.

Target angka performa ditetapkan setelah baseline diperoleh dan karakteristik dataset dianalisis.

## 10. Risiko dan Mitigasi

- **Dataset tidak sesuai:** periksa definisi target dan fitur sebelum memilih dataset; jangan menganggap dataset dengan nama serupa otomatis relevan.
- **Target tidak valid atau ambigu:** dokumentasikan definisi target dan minta klarifikasi bila perlu.
- **Data leakage:** pisahkan data dengan benar dan fit preprocessing hanya pada training set.
- **Generalisasi terbatas:** laporkan sumber data, ukuran sampel, kemungkinan bias, dan keterbatasan penerapan pada populasi lain.
- **Perbedaan training dan inference:** simpan preprocessing dalam artefak atau implementasikan dengan kontrak yang teruji.
- **Artefak tidak dapat dipindahkan/dimuat:** catat format, versi dependensi, dan langkah transfer dari Colab ke aplikasi.
- **Interpretasi berlebihan:** jelaskan bahwa prediksi adalah estimasi dan feature importance bukan hubungan sebab-akibat.
- **Privasi:** hindari mengumpulkan data pribadi yang tidak diperlukan dan jangan menyimpan rahasia dalam repositori.

## 11. Status dan Pekerjaan Berikutnya

Status saat dokumen ini dibuat: **perencanaan awal**.

- [ ] Memilih dan memverifikasi dataset.
- [ ] Menyelesaikan `docs/problem_statement.md` dan definisi target.
- [ ] Menjalankan validasi data dan EDA.
- [ ] Menentukan split dan preprocessing.
- [ ] Melatih baseline dan minimal satu pembanding yang sesuai.
- [ ] Membandingkan model dan mengisi hasil aktual.
- [ ] Mengekspor model serta preprocessing.
- [ ] Membuat aplikasi inference.
- [ ] Menjalankan tes dan mendokumentasikan hasilnya.
- [ ] Memperbarui laporan berdasarkan bukti eksperimen.

## 12. Kesimpulan Sementara

Proyek ini merencanakan sistem prediksi produktivitas mahasiswa dengan dua pipeline yang terpisah: pembangunan model di Google Colab dan pembangunan aplikasi di OpenCode. Keberhasilan dan kualitas prediksi belum dapat disimpulkan sebelum dataset final dipilih, eksperimen dijalankan, dan aplikasi diuji. Kesimpulan akhir harus berdasarkan hasil aktual serta memuat keterbatasan model.
