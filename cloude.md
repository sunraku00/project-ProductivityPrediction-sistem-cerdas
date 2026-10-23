# Petunjuk Agen Coding — Student Productivity Prediction System

Dokumen ini berisi arahan untuk agen coding yang membantu mengembangkan aplikasi proyek **Student Productivity Prediction System**. Nama file ini dibuat sebagai `cloude.md` sesuai permintaan. Jika proyek memakai Claude Code, nama konvensionalnya biasanya `CLAUDE.md`; gunakan nama yang dikenali oleh tool yang dipakai.

## 1. Konteks proyek

Proyek bertujuan memperkirakan produktivitas belajar berdasarkan pola belajar dan kebiasaan harian, misalnya durasi belajar, tidur, penggunaan perangkat digital, aktivitas fisik, dan manajemen waktu.

Status awal: dataset final, definisi target, model terbaik, nilai metrik, dan hasil pengujian aplikasi **belum dikonfirmasi**. Jangan mengarang dataset, hasil, metrik, path artefak, atau klaim bahwa fitur telah selesai.

## 2. Sumber instruksi dan dokumentasi

Sebelum mengubah kode:

1. Baca `AGENTS.md` sebagai panduan utama proyek.
2. Baca `PROJECT_STATUS.md` untuk status dan pekerjaan yang sedang berlangsung.
3. Baca `shared/model_contract.md` bila tersedia.
4. Periksa `laporan.md` dan `tutorial.md` jika perubahan menyangkut metodologi atau cara menjalankan proyek.
5. Jika instruksi bertentangan, jangan diam-diam menghapus persyaratan; jelaskan konflik dan usulkan keputusan.

## 3. Pemisahan tanggung jawab

- `pipeline_model/`: notebook dan kode eksperimen machine learning yang dijalankan melalui Google Colab.
- `pipeline_app/`: kode aplikasi yang dikembangkan dengan OpenCode atau agen coding yang dipilih.
- `shared/`: kontrak bersama antara pipeline model dan aplikasi, termasuk nama fitur, tipe data, urutan/validasi input, target, preprocessing, format artefak, dan cara memuat model.
- Dokumentasi akar proyek: `README.md`, `PROJECT_STATUS.md`, `laporan.md`, dan `tutorial.md`.

Jangan mencampurkan kode aplikasi dengan notebook eksperimen tanpa alasan yang terdokumentasi. Jangan menyalin preprocessing secara terpisah jika preprocessing yang sama dapat disimpan sebagai bagian dari pipeline model.

## 4. Aturan data dan machine learning

- Pilih dataset hanya setelah sumber, lisensi, fitur, target, unit pengukuran, nilai hilang, duplikasi, dan batasannya diperiksa.
- Pastikan target sesuai dengan tugas. Target numerik mengarah ke regresi; target kategori yang bermakna mengarah ke klasifikasi.
- Jangan membuat target atau label sintetis seolah-olah berasal dari dataset nyata.
- Mulai dengan baseline yang masuk akal, lalu bandingkan minimal dua algoritma yang sesuai.
- Gunakan split data, preprocessing, dan metrik evaluasi yang konsisten untuk perbandingan.
- Cegah data leakage; langkah preprocessing yang mempelajari parameter dari data harus di-*fit* hanya pada data latih.
- Pilih metrik sesuai tugas: regresi menggunakan MAE/RMSE; klasifikasi menggunakan precision/recall/F1 dan confusion matrix.
- Jangan menyebut model sebagai “terbaik” tanpa hasil evaluasi yang dapat diperiksa.
- Catat seed, versi dependensi, fitur yang dipakai, konfigurasi, metrik, dan keterbatasan.
- Interpretasi fitur bukan bukti sebab-akibat.

## 5. Kontrak model dan integrasi aplikasi

Sebelum mengintegrasikan model ke aplikasi, dokumentasikan pada `shared/model_contract.md`:

- sumber dataset dan versi/tanggal pengambilan bila diketahui;
- nama serta definisi target dan jenis tugas;
- daftar fitur, tipe, satuan, nilai yang diperbolehkan, dan penanganan nilai hilang;
- preprocessing dan urutan kolom yang diharapkan;
- format dan lokasi artefak model/preprocessing;
- versi Python dan dependensi yang diperlukan;
- cara memuat artefak dan memanggil prediksi;
- output prediksi, satuan/skala, serta peringatan penggunaan.

Aplikasi wajib menggunakan fitur dan preprocessing yang sesuai dengan pipeline pelatihan. Jangan menebak urutan fitur, rentang validasi, atau nama artefak.

## 6. Persyaratan aplikasi

- Sediakan input yang jelas dan validasi di sisi aplikasi.
- Tampilkan pesan error yang membantu jika input tidak valid atau artefak tidak ditemukan.
- Jangan crash tanpa penjelasan ketika model gagal dimuat atau prediksi gagal.
- Jelaskan bahwa hasil merupakan estimasi, bukan penilaian mutlak.
- Jangan menyatakan aplikasi sudah teruji sebelum pengujian dijalankan.
- Jangan mengumpulkan atau menyimpan data pribadi yang tidak diperlukan.
- Jangan mengekspos rahasia, token, atau kredensial ke source control.

## 7. Pengujian minimum

Sebelum menyatakan fitur siap, uji dan dokumentasikan:

- pemuatan model serta preprocessing;
- validasi input wajib, tipe data, dan rentang yang ditentukan kontrak;
- jalur prediksi yang valid;
- input tidak valid dan penanganan error;
- konsistensi nama/urutan fitur antara pelatihan dan aplikasi;
- cara menjalankan aplikasi dari lingkungan bersih sesuai instruksi proyek.

Catat perintah yang dijalankan dan hasil aktual. Jika tes tidak dapat dijalankan, tulis alasannya secara eksplisit.

## 8. Alur kerja setiap tugas

1. Baca instruksi dan status terkini.
2. Identifikasi bagian yang perlu diubah dan dampak terhadap komponen lain.
3. Buat perubahan sekecil mungkin dan ikuti gaya kode yang sudah ada.
4. Jalankan pemeriksaan atau tes yang relevan.
5. Periksa perubahan dan pastikan tidak ada file/konfigurasi yang tidak sengaja tertimpa.
6. Perbarui dokumentasi yang terdampak.
7. Perbarui `PROJECT_STATUS.md` hanya berdasarkan pekerjaan dan hasil yang benar-benar terverifikasi.
8. Dalam ringkasan akhir, sebutkan file yang berubah, tes yang dijalankan, hasilnya, dan pekerjaan yang masih tertunda.

## 9. Format pembaruan status

Saat memperbarui `PROJECT_STATUS.md`, pisahkan:

- **Selesai dan terverifikasi**
- **Sedang dikerjakan**
- **Belum dimulai**
- **Keputusan yang sudah dibuat**
- **Pertanyaan/risiko terbuka**
- **Langkah berikutnya**

Jangan menandai tugas selesai hanya karena kode ditulis; gunakan bukti yang sesuai seperti eksperimen berjalan, hasil evaluasi tersimpan, atau tes lulus.

## 10. Definisi selesai

Pekerjaan dapat disebut selesai bila perubahan sesuai kebutuhan, pemeriksaan yang relevan telah dilakukan, dokumentasi diperbarui, dan klaim status didukung bukti. Model dan aplikasi belum dapat dianggap selesai hanya berdasarkan rancangan atau kode yang belum diuji.
