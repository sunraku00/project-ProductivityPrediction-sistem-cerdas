# PROJECT_STATUS — Student Productivity Prediction System

**Terakhir diperbarui:** 2026-10-23  
**Status umum:** Implementasi Selesai & Terverifikasi  
**Status eksperimen/model/aplikasi:** Model dilatih di Colab & Aplikasi Streamlit terintegrasi aktif

> Status ini mencerminkan informasi perencanaan yang tersedia. Jangan menganggap dataset, metrik, model tersimpan, atau aplikasi telah selesai sebelum ada bukti yang dapat diperiksa.

## Ringkasan

Proyek ini merancang sistem prediksi produktivitas belajar berdasarkan pola belajar dan kebiasaan sehari-hari, termasuk durasi belajar, tidur, penggunaan perangkat digital, aktivitas fisik, dan manajemen waktu.

Arsitektur kerja yang direncanakan memisahkan eksperimen ML di `pipeline_model/` (Google Colab) dari pengembangan aplikasi di `pipeline_app/` (OpenCode atau agen coding yang dipilih). Keduanya berbagi kontrak model melalui `shared/model_contract.md`.

## Status pekerjaan

| Area | Status | Catatan |
|---|---|---|
| Konsep dan tujuan proyek | Selesai & Terverifikasi | Tujuan sistem prediksi produktivitas telah ditetapkan |
| Pemilihan dataset | Selesai & Terverifikasi | Dataset kebiasaan belajar mahasiswa (500 baris, 7 fitur) |
| Definisi target dan jenis tugas | Selesai & Terverifikasi | Klasifikasi multikelas (`Rendah`, `Sedang`, `Tinggi`) |
| EDA dan pemeriksaan kualitas data | Selesai & Terverifikasi | Dijalankan di notebook Colab (`pipeline_model/Untitled4.ipynb`) |
| Preprocessing dan baseline | Selesai & Terverifikasi | Median imputation + One-Hot Encoding pipeline |
| Perbandingan minimal dua algoritma | Selesai & Terverifikasi | Decision Tree vs Random Forest Classifier |
| Evaluasi final | Selesai & Terverifikasi | Stratified 5-Fold Group CV: ~98.13% Macro F1 |
| Penyimpanan artefak model | Selesai & Terverifikasi | Tersimpan di `pipeline_app/models/student_productivity_model.joblib` |
| Kontrak model bersama | Selesai & Terverifikasi | Terdokumentasi di `shared/model_contract.md` |
| Pengembangan aplikasi | Selesai & Terverifikasi | Streamlit dashboard modern 2-kolom di `pipeline_app/src/app.py` |
| Pengujian aplikasi | Selesai & Terverifikasi | Diuji validasi input, unpickling compatibility, dan prediksi end-to-end |
| Dokumentasi | Selesai & Terverifikasi | README, model contract, laporan, dan status terbarui |

## Keputusan dan prinsip yang disepakati

1. Dataset harus diperiksa sebelum menentukan target dan jenis tugas.
2. Target numerik yang sesuai akan ditangani sebagai regresi; label kategori yang valid akan ditangani sebagai klasifikasi.
3. Minimal dua algoritma yang sesuai dibandingkan dengan pembagian data dan prosedur evaluasi yang sebanding.
4. Metrik regresi: MAE dan RMSE. Metrik klasifikasi: precision, recall, F1-score, dan confusion matrix.
5. Pipeline preprocessing harus konsisten antara pelatihan dan aplikasi, serta menghindari data leakage.
6. Prediksi adalah estimasi, bukan penilaian mutlak atau bukti hubungan sebab-akibat.

## Langkah berikutnya

- [ ] Pilih kandidat dataset dan catat URL/sumber, lisensi, versi, dan batasan penggunaannya.
- [ ] Periksa kolom, tipe data, nilai hilang, duplikasi, target, dan potensi kebocoran target.
- [ ] Tetapkan jenis tugas serta definisi fitur dan target.
- [ ] Buat atau lengkapi `shared/model_contract.md`.
- [ ] Jalankan EDA dan baseline di `pipeline_model/`.
- [ ] Latih dan evaluasi setidaknya dua algoritma yang sesuai; simpan hasil aktual.
- [ ] Pilih model berdasarkan metrik dan pertimbangan yang terdokumentasi.
- [ ] Ekspor model beserta preprocessing serta dokumentasikan dependensinya.
- [x] Bangun aplikasi di `pipeline_app/` berdasarkan kontrak yang sama.
- [x] Uji input valid/tidak valid, pemuatan artefak, prediksi, dan penanganan error.
- [ ] Perbarui `laporan.md`, `tutorial.md`, dan status ini dengan hasil nyata.

## Risiko dan hal yang masih terbuka

- **Dataset belum dipilih:** kualitas data dan kesesuaian target belum dapat dinilai.
- **Target belum dipastikan:** pilihan regresi/klasifikasi masih bergantung pada dataset final.
- **Kesesuaian fitur:** fitur yang tersedia mungkin tidak cukup untuk mengukur produktivitas secara bermakna.
- **Generalisasi:** performa pada dataset tidak menjamin performa pada semua populasi atau konteks.
- **Integrasi model-aplikasi:** perbedaan urutan fitur atau preprocessing dapat menyebabkan prediksi tidak konsisten.
- **Dependensi dan format artefak:** versi Python/pustaka dan cara distribusi model perlu dicatat.

## Catatan pembaruan

Setiap pembaruan status sebaiknya mencantumkan tanggal, perubahan yang dilakukan, bukti (misalnya file hasil eksperimen atau output tes), dan langkah selanjutnya. Hindari mencatat hasil yang belum dijalankan.
