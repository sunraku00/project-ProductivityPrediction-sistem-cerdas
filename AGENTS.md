# AGENTS.md — Panduan Kerja Proyek Sistem Cerdas

Dokumen ini adalah instruksi utama bagi agen coding (terutama OpenCode) untuk menyiapkan, membangun, menguji, dan mendokumentasikan proyek sistem cerdas berbasis AI/ML. Ikuti instruksi yang relevan dengan tugas yang sedang dikerjakan. Jangan mengasumsikan detail proyek yang belum diberikan.

## 1. Tujuan dan prinsip kerja

- Ubah problem statement menjadi sistem cerdas yang dapat diuji dan dijalankan.
- Pisahkan pekerjaan menjadi dua pipeline yang jelas:
  1. **Pipeline Model AI** — pengolahan data dan pembangunan model, terutama di Google Colab.
  2. **Pipeline Aplikasi Pengguna Model** — integrasi model ke API/UI/prototipe, terutama dengan OpenCode.
- Utamakan solusi sederhana, dapat direproduksi, terukur, dan sesuai kebutuhan.
- Jangan mengarang dataset, hasil eksperimen, metrik, sumber, atau status implementasi.
- Jangan menyatakan suatu tahap selesai sebelum artefak dan kriteria penerimaannya diperiksa.
- Pertahankan pekerjaan yang sudah ada. Sebelum mengubah file, periksa isi dan dampaknya; jangan menimpa file pengguna tanpa alasan.
- Gunakan bahasa yang konsisten dengan dokumentasi proyek. Untuk proyek berbahasa Indonesia, dokumentasi utama ditulis dalam bahasa Indonesia.

## 2. Alur mulai proyek

Jalankan langkah-langkah berikut ketika menerima proyek baru atau konteks proyek yang belum jelas.

### 2.1 Pahami problem statement dan sumber

Problem statement dapat diberikan sebagai satu kalimat, paragraf, teks, presentasi, proposal, atau gabungan beberapa sumber.

1. Baca semua sumber yang disediakan dan identifikasi tujuan, pengguna, masalah, batasan, data yang tersedia, keluaran yang diharapkan, serta kriteria keberhasilan.
2. Bedakan fakta yang tertulis di sumber dari asumsi atau rekomendasi agen. Catat hal yang belum diketahui; jangan mengisi kekosongan sumber seolah-olah fakta.
3. Buat atau perbarui `docs/problem_statement.md` dengan:
   - latar belakang dan masalah;
   - tujuan sistem;
   - pengguna dan skenario penggunaan;
   - input dan output sistem;
   - batasan serta asumsi;
   - kriteria keberhasilan yang terukur jika tersedia;
   - pertanyaan terbuka dan risiko.
4. Jika ada pertentangan antar-sumber, dokumentasikan pertentangan tersebut dan minta klarifikasi bila berpengaruh pada desain atau hasil.
5. Jangan memulai training model sebelum tujuan, target prediksi/tugas, unit observasi, dan definisi keberhasilan cukup jelas.

### 2.2 Periksa repositori dan buat scaffold

1. Periksa direktori kerja, file yang sudah ada, struktur repositori, konfigurasi, dan perubahan pengguna.
2. Jika repositori sudah berisi proyek, pertahankan struktur yang layak dan lakukan penyesuaian minimal. Jangan membuat ulang atau menghapus file hanya agar cocok dengan scaffold contoh.
3. Jika proyek baru atau belum memiliki struktur yang memadai, **buat struktur direktori dua pipeline** pada Bagian 3.
4. Buat file awal yang diperlukan, minimal `AGENTS.md`, `README.md`, `PROJECT_STATUS.md`, `docs/problem_statement.md`, kontrak model bersama, dan file konfigurasi/dependensi yang sesuai.
5. Setelah membuat scaffold, verifikasi keberadaan direktori dan file wajib. Laporkan file yang berhasil dibuat, file yang dilewati karena sudah ada, serta kendala.
6. Jangan mengisi file starter dengan hasil atau konfigurasi fiktif. Gunakan TODO yang spesifik untuk informasi yang belum tersedia.

### 2.3 Tentukan pendekatan pengembangan

- Pilih alur kerja sesuai skala proyek dan instruksi pengguna.
- Bila pengguna meminta SDLC atau proyek membutuhkan tahapan formal, nyatakan metode yang dipilih dalam `docs/development_plan.md`.
- **Waterfall** dapat digunakan bila kebutuhan dan keluaran cukup stabil. Pisahkan tahap analisis kebutuhan, desain, implementasi model, implementasi aplikasi, pengujian, dan dokumentasi/demo. Setiap tahap memiliki kriteria penerimaan sebelum melanjutkan.
- Jangan menerapkan proses formal yang berlebihan pada tugas kecil; tetap catat keputusan dan hasil yang penting.

## 3. Scaffold direktori wajib: dua pipeline terpisah

Pada proyek baru, buat scaffold berikut. Direktori boleh disesuaikan berdasarkan problem statement, tetapi batas antara pipeline model dan pipeline aplikasi harus tetap eksplisit.

```text
project-root/
├── AGENTS.md
├── README.md
├── PROJECT_STATUS.md
├── .gitignore
├── .env.example
├── configs/
│   └── config.example.yaml
├── pipeline_model/                    # Pipeline 1: Google Colab
│   ├── README.md
│   ├── requirements.txt
│   ├── notebooks/
│   │   └── 01_model_pipeline.ipynb     # dibuat saat notebook memang dibutuhkan
│   ├── data/
│   │   ├── raw/
│   │   ├── interim/
│   │   └── processed/
│   ├── scripts/
│   │   ├── download_dataset.py
│   │   ├── validate_dataset.py
│   │   ├── train.py
│   │   ├── evaluate.py
│   │   └── export_model.py
│   ├── src/
│   │   ├── data/
│   │   ├── features/
│   │   ├── training/
│   │   ├── evaluation/
│   │   ├── explainability/
│   │   └── common/
│   └── artifacts/
│       ├── models/
│       ├── metrics/
│       ├── figures/
│       └── reports/
├── pipeline_app/                      # Pipeline 2: OpenCode
│   ├── README.md
│   ├── requirements.txt
│   ├── src/
│   │   ├── inference/
│   │   └── utils/
│   ├── api/
│   ├── ui/
│   ├── tests/
│   │   ├── unit/
│   │   ├── integration/
│   │   └── smoke/
│   └── configs/
├── shared/
│   └── model_contract.md              # kontrak input/output dan versi artefak model
├── docs/
│   ├── problem_statement.md
│   ├── assumptions.md
│   ├── development_plan.md
│   ├── dataset_card.md
│   ├── model_card.md
│   ├── evaluation_report.md
│   ├── api_contract.md
│   └── deployment.md
└── tests/                              # tes lintas-pipeline bila diperlukan
```

### 3.1 Aturan pembuatan scaffold

Agen harus melakukan tindakan nyata, bukan hanya menampilkan contoh struktur:

1. Buat direktori yang belum ada menggunakan alat filesystem yang tersedia.
2. Buat file starter yang relevan dengan isi minimum dan TODO yang jelas.
3. Jika format file memerlukan lingkungan tertentu (misalnya notebook Colab), jelaskan bila notebook kosong tidak dapat dibuat dengan aman; buat README atau skrip starter sebagai alternatif.
4. Periksa bahwa `pipeline_model/` dan `pipeline_app/` sama-sama ada dan tidak tercampur tanggung jawabnya.
5. Jangan membuat direktori data/artifact besar atau memasukkan dataset/model ke Git tanpa alasan. Tambahkan aturan `.gitignore` yang sesuai.
6. Jangan menimpa file yang telah berisi konten tanpa memeriksa dan mempertahankannya.
7. Catat hasil scaffold dan keputusan penyesuaian di `PROJECT_STATUS.md`.

## 4. Batas tanggung jawab pipeline

### Pipeline 1 — Model AI (Google Colab)

Tujuan: menghasilkan artefak model yang tervalidasi, metrik evaluasi, dan dokumentasi yang cukup untuk diintegrasikan oleh aplikasi.

Urutan kerja umum:

1. **Dataset** — cari atau gunakan dataset yang diizinkan dan sesuai problem statement. Catat sumber, lisensi/ketentuan penggunaan, cara memperoleh, target, fitur, dan batasan. Jangan mengunduh data tanpa memeriksa sumber dan izin yang relevan.
2. **Validasi data** — periksa format, skema, tipe data, duplikasi, nilai hilang, label, ketidakseimbangan, kebocoran data, dan konsistensi. Simpan data mentah secara terpisah dari data olahan.
3. **EDA** — ringkas distribusi, kualitas, hubungan antarfitur, ketidakseimbangan kelas, dan anomali. Buat visualisasi yang menjawab pertanyaan proyek.
4. **Feature engineering / preprocessing** — buat transformasi yang dapat direproduksi. Fit preprocessing hanya pada data training untuk mencegah data leakage; simpan transformasi yang dibutuhkan saat inference.
5. **Baseline model** — bangun baseline sederhana sebagai pembanding. Tentukan metrik berdasarkan tugas dan biaya kesalahan.
6. **Advanced model** — coba model yang lebih sesuai bila baseline belum memadai. Bandingkan dengan evaluasi yang konsisten dan catat konfigurasi eksperimen.
7. **Explainability** — gunakan SHAP atau metode interpretabilitas lain bila relevan dengan tipe model dan kebutuhan pengguna. Jangan mengklaim penjelasan kausal dari feature importance.
8. **Evaluation** — evaluasi pada validation/test set yang tepat; hindari memilih model berdasarkan test set berulang kali. Laporkan metrik, batasan, error penting, dan potensi bias.
9. **Export** — ekspor model beserta preprocessing, label mapping, metadata versi, dan dependensi yang diperlukan. Gunakan format yang aman dan kompatibel dengan aplikasi.
10. **Dokumentasi dan handoff** — perbarui `dataset_card.md`, `model_card.md`, `evaluation_report.md`, dan `shared/model_contract.md`.

Kriteria selesai Pipeline 1:
- dataset dan sumbernya terdokumentasi;
- preprocessing dan model dapat direproduksi sejauh lingkungan memungkinkan;
- evaluasi menyertakan metrik yang relevan dan batasan;
- artefak model berhasil dimuat ulang melalui uji sederhana;
- kontrak model dan instruksi penggunaan tersedia.

### Pipeline 2 — Aplikasi pengguna model (OpenCode)

Tujuan: membangun aplikasi yang memuat artefak dari Pipeline 1 dan menyediakan alur penggunaan yang dibutuhkan pengguna.

Urutan kerja umum:

1. **Periksa handoff model** — pastikan artefak tersedia, formatnya diketahui, versi tercatat, dan preprocessing/label mapping yang diperlukan ikut tersedia.
2. **Implementasi inference** — buat modul pemuatan model dan prediksi yang mematuhi `shared/model_contract.md`. Hindari menyalin ulang logika preprocessing secara berbeda.
3. **API (bila diperlukan)** — definisikan endpoint, skema request/response, validasi input, kode error, dan penanganan kegagalan. Dokumentasikan di `docs/api_contract.md`.
4. **UI/dashboard/prototipe (bila diperlukan)** — implementasikan alur pengguna berdasarkan problem statement; tampilkan hasil, satuan, dan pesan kesalahan secara jelas.
5. **Integrasi** — hubungkan UI/API ke inference dan pastikan format data sesuai kontrak.
6. **Pengujian** — tambahkan unit test, integration test, dan smoke test. Uji input valid, input tidak valid, nilai batas, model hilang/tidak kompatibel, dan kasus error yang relevan.
7. **Konfigurasi dan keamanan** — gunakan environment variables untuk rahasia; jangan commit token/password. Validasi input dan hindari mengekspos detail internal pada pesan error publik.
8. **Packaging/deployment** — dokumentasikan perintah instalasi, menjalankan aplikasi, konfigurasi, serta batasan deployment.

Kriteria selesai Pipeline 2:
- aplikasi dapat memuat artefak model yang disepakati;
- alur utama bekerja dari input hingga hasil;
- kontrak API/UI terdokumentasi jika ada;
- tes yang relevan dijalankan dan hasilnya dilaporkan;
- README menjelaskan cara menjalankan aplikasi.

## 5. Pertukaran artefak antara Google Colab dan OpenCode

Google Colab dan lingkungan OpenCode mungkin berjalan pada filesystem atau lingkungan yang berbeda. **Jangan mengasumsikan kedua pipeline berbagi file secara otomatis.**

- Pipeline model harus menghasilkan paket ekspor yang eksplisit, misalnya file model, preprocessing, metadata versi, dan petunjuk dependensi.
- Catat nama file, format, versi model, checksum bila relevan, versi Python/library, skema input/output, dan cara memuat model.
- Pindahkan artefak melalui mekanisme yang disetujui pengguna, seperti unduhan/upload, penyimpanan bersama yang telah dikonfigurasi, atau artifact registry yang tersedia.
- Pipeline aplikasi harus memvalidasi keberadaan, versi, dan kompatibilitas artefak sebelum inference.
- Jangan membuat atau mengasumsikan URL penyimpanan, kredensial, lokasi file, atau model hasil training yang belum tersedia.
- Jangan memasukkan artefak besar ke repositori kecuali diminta atau memang sesuai kebijakan proyek.

## 6. Kontrak model bersama

`shared/model_contract.md` setidaknya mendefinisikan:

- tujuan model dan versi;
- format artefak serta lokasi konfigurasi (tanpa rahasia);
- urutan/nama fitur dan tipe data;
- aturan preprocessing yang harus sama saat training dan inference;
- format input dan output prediksi;
- label mapping, satuan, ambang keputusan jika ada;
- perilaku untuk input tidak valid atau nilai hilang;
- versi Python dan dependensi utama;
- contoh pemuatan dan inference;
- metrik evaluasi yang relevan dan keterbatasan model.

Jika detail belum diketahui, gunakan TODO yang eksplisit. Jangan membuat kontrak seolah-olah sudah disepakati.

## 7. Evaluasi dan kualitas

- Pilih metrik sesuai problem: misalnya classification, regression, ranking, clustering, atau generative task memerlukan ukuran yang berbeda.
- Laporkan baseline dan pembanding secara adil.
- Periksa data leakage, duplikasi antar-split, class imbalance, serta kemungkinan perbedaan distribusi.
- Gunakan random seed bila relevan dan catat sumber ketidakreproduksian.
- Jangan menyajikan angka metrik contoh sebagai hasil aktual.
- Pisahkan hasil eksperimen, interpretasi, keterbatasan, dan rekomendasi.
- Gunakan tes otomatis untuk perilaku kritis; jangan menyatakan tes lulus jika belum dijalankan.

## 8. SDLC Waterfall (bila dipilih)

1. **Analisis kebutuhan:** problem statement, pengguna, ruang lingkup, batasan, acceptance criteria.
2. **Desain:** arsitektur dua pipeline, aliran artefak, kontrak model, desain API/UI, dan rencana pengujian.
3. **Implementasi Pipeline Model:** data, EDA, preprocessing, baseline/advanced model, explainability yang relevan, evaluasi, ekspor.
4. **Implementasi Pipeline Aplikasi:** inference, API/UI, integrasi artefak, konfigurasi.
5. **Pengujian:** unit, integrasi, smoke test, validasi hasil model dan aplikasi.
6. **Dokumentasi dan serah terima:** README, laporan evaluasi, instruksi menjalankan, status dan keterbatasan.

Jangan melanjutkan melewati gerbang tahap jika kriteria penerimaan belum terpenuhi. Catat hambatan dan minta keputusan pengguna bila diperlukan.

## 9. Dokumentasi dan status

- `README.md`: ringkasan proyek, prasyarat, cara menjalankan pipeline, dan tautan ke dokumentasi.
- `PROJECT_STATUS.md`: tahap saat ini, pekerjaan selesai, pekerjaan tertunda, keputusan, tes yang dijalankan, dan hambatan.
- `docs/problem_statement.md`: definisi masalah dan kriteria keberhasilan.
- `docs/dataset_card.md`: sumber, lisensi/ketentuan, skema, batasan, dan preprocessing data.
- `docs/model_card.md`: tujuan model, data pelatihan, metrik, batasan, dan penggunaan yang tidak dianjurkan.
- `docs/evaluation_report.md`: metode evaluasi, hasil aktual, pembanding, analisis error, dan keterbatasan.
- `docs/api_contract.md`: kontrak API bila aplikasi menggunakan API.
- `docs/deployment.md`: konfigurasi dan instruksi deployment bila diperlukan.

Perbarui status setelah menyelesaikan tahap bermakna. Bedakan jelas antara “direncanakan”, “sedang dikerjakan”, “selesai”, dan “terverifikasi”.

## 10. Praktik coding dan perubahan file

- Periksa file yang relevan sebelum mengedit.
- Buat perubahan sekecil mungkin yang memenuhi kebutuhan.
- Ikuti gaya, framework, dan pola yang telah digunakan proyek.
- Hindari duplikasi logika preprocessing atau definisi skema.
- Pisahkan konfigurasi dari kode dan jangan menyimpan rahasia di repositori.
- Tambahkan komentar untuk alasan/keputusan yang tidak jelas, bukan untuk mengulang kode.
- Jangan menghapus data, model, konfigurasi, atau pekerjaan pengguna tanpa persetujuan eksplisit.
- Setelah mengubah kode, jalankan tes/lint yang tersedia dan laporkan hasil aktual. Jika tidak dapat dijalankan, jelaskan alasannya.

## 11. Pelaporan setiap tugas

Pada akhir tugas, berikan ringkasan singkat berisi:
1. perubahan yang benar-benar dilakukan;
2. file/direktori yang dibuat atau diubah;
3. tes/validasi yang dijalankan beserta hasilnya;
4. asumsi, kekurangan, atau keputusan yang masih membutuhkan pengguna;
5. langkah berikutnya yang paling relevan.

Jangan mengklaim telah membuat, menjalankan, menguji, mengunduh, atau menerapkan sesuatu jika tindakan tersebut belum dilakukan.

## 12. Konteks khusus proyek: Student Productivity Prediction System

Bagian ini berlaku untuk proyek **Student Productivity Prediction System**. Gunakan sebagai konteks awal proyek, bukan sebagai bukti bahwa dataset, model, atau aplikasi sudah dibuat. Semua hasil harus dibuktikan melalui proses dan artefak yang benar-benar tersedia.

### 12.1 Nama, topik, dan tujuan

- **Nama proyek:** Student Productivity Prediction System.
- **Topik:** Penerapan Machine Learning untuk memprediksi tingkat produktivitas mahasiswa berdasarkan pola belajar dan kebiasaan sehari-hari.
- **Masalah:** Mahasiswa memiliki pola belajar dan kebiasaan yang berbeda, misalnya durasi belajar, kualitas/durasi tidur, penggunaan perangkat digital, aktivitas fisik, dan manajemen waktu. Perbedaan ini dapat berkaitan dengan tingkat produktivitas.
- **Tujuan sistem:** Memprediksi produktivitas berdasarkan faktor yang tersedia dalam dataset dan membantu pengguna memahami faktor yang berkaitan dengan hasil prediksi.
- **Batas interpretasi:** Hasil adalah estimasi berdasarkan pola data, bukan penilaian mutlak terhadap produktivitas atau nilai personal mahasiswa. Jangan menyimpulkan hubungan sebab-akibat hanya dari model prediktif.

### 12.2 Jenis tugas dan target prediksi

Gunakan **supervised machine learning**. Sebelum pemodelan, periksa dataset dan tetapkan jenis target berdasarkan kolom target yang benar-benar tersedia:

- **Regresi** jika target adalah skor produktivitas numerik.
- **Klasifikasi** jika target adalah kategori produktivitas, misalnya rendah, sedang, dan tinggi, serta labelnya memiliki dasar yang dapat dipertanggungjawabkan.

Target awal yang diharapkan adalah **skor produktivitas mahasiswa**, tetapi jangan menganggap kolom tersebut pasti ada pada dataset. Jika dataset hanya memiliki kategori, gunakan target kategori yang tersedia. Jangan membuat label rendah/sedang/tinggi dari skor numerik tanpa mendokumentasikan aturan kategorisasi dan alasan metodologisnya. Jika target yang valid tidak ditemukan, hentikan pemodelan dan laporkan pilihan dataset/target yang perlu diputuskan.

### 12.3 Dataset dan fitur

- **Sumber yang direncanakan:** Kaggle.
- Pilih dataset produktivitas atau kebiasaan mahasiswa yang relevan, memiliki dokumentasi, target yang jelas, serta ketentuan penggunaan yang dapat diperiksa.
- Kandidat fitur yang diharapkan, jika tersedia: durasi belajar, durasi/kualitas tidur, penggunaan perangkat digital, aktivitas fisik, manajemen waktu, dan kebiasaan relevan lainnya.
- Jangan mengasumsikan seluruh fitur tersebut ada. Gunakan kolom yang benar-benar ditemukan dan dokumentasikan pemetaan nama kolom ke fitur proyek.
- Catat URL/sumber dataset, nama pemilik/penerbit jika diketahui, lisensi/ketentuan penggunaan, tanggal akses, ukuran data, skema kolom, definisi target, keterbatasan, dan kemungkinan bias di `docs/dataset_card.md`.
- Jangan mengunduh atau menggunakan dataset sebelum memeriksa relevansi, skema, target, dokumentasi, dan izin penggunaan yang tersedia.

### 12.4 Algoritma kandidat

Pilih algoritma sesuai jenis target dan hasil pemeriksaan data; jangan memaksakan satu algoritma untuk semua kondisi.

- **Regresi:** Linear Regression sebagai baseline; Random Forest Regressor sebagai pembanding; XGBoost Regressor dapat dicoba sebagai model lanjutan jika sesuai dan dependensinya layak.
- **Klasifikasi:** gunakan baseline klasifikasi yang sesuai, lalu bandingkan dengan Random Forest Classifier dan, bila relevan, XGBoost Classifier. Linear Regression tidak digunakan untuk klasifikasi; pilih algoritma baseline klasifikasi yang sesuai dan dokumentasikan alasannya.
- Bandingkan minimal dua algoritma yang sesuai dengan target pada pembagian data uji yang sama dan prosedur evaluasi yang adil.
- XGBoost bersifat opsional, bukan kewajiban. Pertimbangkan ukuran dataset, kualitas data, biaya komputasi, dan kebutuhan proyek.

### 12.5 Pipeline Model AI — Google Colab

Kerjakan pipeline model di `pipeline_model/`, dengan Google Colab sebagai lingkungan utama bila sesuai. Urutan kerja:

1. Identifikasi kandidat dataset Kaggle dan verifikasi target serta relevansinya.
2. Unduh/muat data dan catat sumbernya; simpan data mentah secara terpisah.
3. Validasi skema, tipe data, nilai hilang, duplikasi, nilai tidak wajar, distribusi target, dan potensi kebocoran data.
4. Lakukan EDA dan dokumentasikan temuan yang relevan terhadap target serta kandidat fitur.
5. Tentukan apakah masalah berupa regresi atau klasifikasi berdasarkan target aktual.
6. Bagi data menjadi train/test dengan prosedur yang sesuai; lakukan preprocessing dan pemilihan fitur tanpa kebocoran informasi dari test set. Untuk klasifikasi, pertimbangkan stratifikasi bila sesuai.
7. Latih baseline dan minimal satu model pembanding yang sesuai.
8. Evaluasi semua kandidat menggunakan data uji dan metrik yang sesuai.
9. Pilih model berdasarkan hasil aktual, bukan asumsi awal. Simpan model dan seluruh preprocessing/label mapping yang dibutuhkan untuk inference.
10. Perbarui `docs/dataset_card.md`, `docs/model_card.md`, `docs/evaluation_report.md`, dan `shared/model_contract.md`.

### 12.6 Metrik evaluasi dan kriteria keberhasilan

Proyek dianggap memenuhi kriteria apabila bukti berikut tersedia:

1. Dataset relevan, sumbernya terdokumentasi, dan target prediksi jelas.
2. Pipeline pengolahan data dan training dapat dijalankan kembali dengan prosedur yang didokumentasikan.
3. Minimal dua algoritma yang sesuai berhasil dilatih dan dibandingkan pada data uji yang sama.
4. Metrik sesuai jenis tugas:
   - **Regresi:** MAE dan RMSE; metrik tambahan dapat digunakan jika bermanfaat dan dijelaskan.
   - **Klasifikasi:** Precision, Recall, F1-score, dan confusion matrix; jelaskan averaging/macro/micro/weighted serta metrik per kelas bila relevan.
5. Model terbaik disimpan, dapat dimuat kembali, dan lulus uji inference pada data baru.
6. Aplikasi menerima input, memvalidasi masukan, menampilkan hasil prediksi, dan menangani input tidak valid dengan aman.
7. Hasil evaluasi, keterbatasan, dokumentasi penggunaan, dan struktur proyek tersedia.

Jangan menetapkan target angka performa sebelum baseline dan karakteristik dataset dianalisis. Laporkan nilai metrik aktual, metode validasi, ukuran split, seed bila digunakan, dan keterbatasan. Jangan mengklaim keberhasilan hanya karena kode berjalan.

### 12.7 Pipeline Aplikasi Pengguna Model — OpenCode

Bangun aplikasi pada `pipeline_app/` menggunakan model yang diekspor dari Pipeline Model.

- Sediakan input untuk fitur yang benar-benar dipakai model; label dan satuan harus jelas.
- Validasi tipe, rentang, nilai kosong, dan format input berdasarkan skema data serta kontrak model. Jangan membuat rentang validasi arbitrer tanpa dasar; jika batas belum diketahui, dokumentasikan keputusan atau TODO.
- Muat model dan preprocessing yang telah diekspor. Jangan melatih ulang model secara diam-diam ketika aplikasi dijalankan.
- Tampilkan skor prediksi untuk regresi atau kelas prediksi untuk klasifikasi. Jika probabilitas kelas tersedia dan sesuai, beri label yang jelas dan jangan menafsirkannya sebagai kepastian.
- Jelaskan bahwa hasil adalah estimasi berbasis data, bukan penilaian mutlak atau diagnosis terhadap individu.
- Tambahkan tes untuk input valid, input tidak valid, fitur hilang, model/artefak tidak tersedia, serta integrasi alur input hingga prediksi.
- Dokumentasikan cara menjalankan aplikasi dan cara memasang/memperbarui artefak model.

### 12.8 Artefak dan dokumentasi khusus proyek

Pastikan dokumentasi berikut dibuat atau diperbarui saat tahap terkait dikerjakan:

- `docs/problem_statement.md` — konteks masalah, tujuan, pengguna, input/output, batasan, dan kriteria keberhasilan.
- `docs/dataset_card.md` — sumber dataset, skema, target, lisensi/ketentuan, kualitas data, dan keterbatasan.
- `docs/model_card.md` — tujuan model, jenis tugas, fitur, algoritma, penggunaan yang sesuai, dan batasan.
- `docs/evaluation_report.md` — split data, metode, metrik aktual, perbandingan model, analisis error, dan keterbatasan.
- `shared/model_contract.md` — fitur input, preprocessing, format artefak, output, versi, dependensi, dan contoh inference.
- `pipeline_model/README.md` — instruksi menjalankan pipeline model.
- `pipeline_app/README.md` — instruksi menjalankan aplikasi dan menggunakan model ekspor.
- `PROJECT_STATUS.md` — status aktual, pekerjaan selesai/tertunda, tes yang dijalankan, dan hambatan.

Jangan mengarang nama kolom, jumlah baris, URL dataset, hasil EDA, skor model, atau hasil tes. Jika belum diketahui, catat sebagai TODO dan selesaikan melalui pemeriksaan data yang nyata.
