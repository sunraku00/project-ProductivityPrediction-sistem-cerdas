# Model Contract — Student Productivity Prediction System

## 1. Tujuan

Dokumen ini mendefinisikan kontrak antara model machine learning dan aplikasi agar format input, urutan fitur, dan output prediksi tetap konsisten.

## 2. Jenis masalah

- **Jenis pembelajaran:** supervised learning
- **Jenis tugas:** klasifikasi multikelas
- **Target:** `Produktivitas`

## 3. Fitur input

Aplikasi harus menerima tujuh fitur berikut:

1. `Jam_Belajar_Harian` — numerik, jam belajar per hari.
2. `Jam_Tidur_Harian` — numerik, jam tidur per hari.
3. `Kehadiran_Kuliah_Pct` — numerik, persentase kehadiran kuliah (0–100).
4. `IPK_Terakhir` — numerik, IPK (0–4).
5. `Aktivitas_Organisasi` — kategori, nilai yang digunakan pada dataset, misalnya `Ya` atau `Tidak`.
6. `Tingkat_Stres` — kategori: `Rendah`, `Sedang`, atau `Tinggi`.
7. `Penggunaan_Gadget_Malam_Jam` — numerik, jam penggunaan gadget pada malam hari.

**Urutan fitur harus mengikuti nilai `feature_cols` yang disimpan di dalam artefak model.** Jangan mengandalkan urutan yang ditulis manual jika urutan dari artefak tersedia.

## 4. Kolom yang tidak digunakan sebagai fitur

- `ID_Mahasiswa` — identitas, tidak digunakan sebagai fitur prediksi.
- `Produktivitas` — label target, bukan input saat prediksi.

## 5. Kelas output

Model memprediksi satu kelas produktivitas. Kelas yang diketahui dari dataset:

- `Rendah`
- `Sedang`
- `Tinggi`

Aplikasi sebaiknya membaca daftar kelas dari artefak/model, bukan mengasumsikan urutan kelas tertentu.

## 6. Artefak model

Nama file yang diharapkan:

`student_productivity_model.joblib`

Lokasi yang diharapkan oleh aplikasi:

`pipeline_app/models/student_productivity_model.joblib`

Artefak model diharapkan berupa dictionary yang berisi:

- `model`: pipeline preprocessing dan Random Forest yang sudah dilatih.
- `feature_cols`: daftar nama fitur sesuai urutan yang digunakan model.
- `target_name`: nama kolom target, yaitu `Produktivitas`.
- `classes`: daftar kelas output.

Simpan artefak dari notebook training setelah model final dilatih. Aplikasi memuat artefak tersebut dan tidak melatih ulang model saat dijalankan.

## 7. Aturan integrasi aplikasi

1. Muat artefak menggunakan `joblib`.
2. Buat satu baris data input dengan nama kolom yang cocok dengan `feature_cols`.
3. Susun kolom sesuai urutan `feature_cols` dari artefak.
4. Gunakan `model.predict()` untuk menghasilkan kelas prediksi.
5. Jika `predict_proba()` tersedia, aplikasi boleh menampilkan probabilitas setiap kelas dengan penjelasan bahwa probabilitas tersebut merupakan keluaran model.
6. Validasi rentang input numerik dan kategori sebelum melakukan prediksi.
7. Tampilkan pesan yang jelas jika file model tidak ditemukan atau input tidak cocok dengan model.
8. Jangan menggunakan `ID_Mahasiswa` sebagai fitur.
9. Jangan melatih ulang model setiap kali pengguna mengirim formulir.

## 8. Rentang input aplikasi

Rentang validasi antarmuka yang disarankan:

| Fitur | Rentang / nilai |
|---|---|
| `Jam_Belajar_Harian` | 0–24 jam |
| `Jam_Tidur_Harian` | 0–24 jam |
| `Kehadiran_Kuliah_Pct` | 0–100 |
| `IPK_Terakhir` | 0–4 |
| `Aktivitas_Organisasi` | `Ya` atau `Tidak`, sesuai kategori data training |
| `Tingkat_Stres` | `Rendah`, `Sedang`, `Tinggi`, sesuai kategori data training |
| `Penggunaan_Gadget_Malam_Jam` | 0–24 jam |

Rentang ini merupakan validasi antarmuka. Rentang nilai yang benar-benar ada di dataset dapat lebih sempit; aplikasi perlu menghindari interpretasi prediksi di luar cakupan data training.

## 9. Hasil evaluasi yang tercatat

Berdasarkan eksperimen pada dataset proyek:

- Dataset: 500 baris.
- Validasi silang: `StratifiedGroupKFold` 5 fold, dikelompokkan berdasarkan kombinasi fitur.
- Rata-rata Accuracy: **98,13%**.
- Rata-rata Macro F1: **98,12%**.
- Simpangan baku Accuracy: **1,90%**.
- Simpangan baku Macro F1: **1,74%**.

Angka tersebut merupakan hasil evaluasi pada dataset proyek, bukan jaminan performa pada mahasiswa baru atau populasi lain.

## 10. Batasan dan kehati-hatian

- Asal-usul dataset dan aturan pembentukan label `Produktivitas` belum terverifikasi.
- Skor evaluasi yang tinggi dapat dipengaruhi pola label yang sangat berkaitan dengan fitur input.
- Prediksi tidak membuktikan hubungan sebab-akibat.
- Jangan menyatakan hasil model sebagai penilaian mutlak terhadap mahasiswa.
- Evaluasi pada data eksternal yang representatif diperlukan sebelum penggunaan nyata.

## 11. Kriteria integrasi selesai

Integrasi dapat dianggap berjalan jika:

- Artefak model berhasil dimuat.
- Input tujuh fitur diterima dan disusun sesuai `feature_cols`.
- Prediksi menghasilkan salah satu kelas yang tersedia.
- Kesalahan file atau input ditangani dengan pesan yang mudah dipahami.
- Aplikasi tidak melatih ulang model pada saat runtime.
