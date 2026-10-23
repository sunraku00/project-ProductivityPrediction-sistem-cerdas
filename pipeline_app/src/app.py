import streamlit as st
import pandas as pd
import joblib
import os
import numpy as np

# Konfigurasi Halaman Streamlit
st.set_page_config(
    page_title="Student Productivity Predictor",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Kompatibilitas unpickling artefak scikit-learn lintas versi (misal Colab 1.6.x vs lokal 1.9.x)
try:
    from sklearn.compose import _column_transformer as _ct
    if not hasattr(_ct, "_RemainderColsList"):
        _ct._RemainderColsList = type("_RemainderColsList", (), {})
        
    from sklearn.impute import SimpleImputer
    if not hasattr(SimpleImputer, "_fill_dtype"):
        SimpleImputer._fill_dtype = property(lambda self: getattr(self, "_fit_dtype", None))
except Exception:
    pass

# Path ke artefak model (resolusi otomatis baik dijalankan dari project-root atau pipeline_app)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_MODEL_PATH = os.path.normpath(os.path.join(BASE_DIR, '..', 'models', 'student_productivity_model.joblib'))
CANDIDATE_PATHS = [
    DEFAULT_MODEL_PATH,
    os.path.join('models', 'student_productivity_model.joblib'),
    os.path.join('pipeline_app', 'models', 'student_productivity_model.joblib'),
]
MODEL_PATH = next((p for p in CANDIDATE_PATHS if os.path.exists(p)), DEFAULT_MODEL_PATH)

@st.cache_resource
def load_model():
    if not os.path.exists(MODEL_PATH):
        return None, f"File model tidak ditemukan di: {MODEL_PATH}"
    try:
        data = joblib.load(MODEL_PATH)
        return data, None
    except Exception as e:
        return None, f"Gagal memuat artefak model: {e}"

def inject_custom_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    /* Header Badge */
    .top-badge {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background-color: #F0FDFA;
        color: #0D9488;
        border: 1px solid #99F6E4;
        padding: 4px 12px;
        border-radius: 9999px;
        font-size: 0.8rem;
        font-weight: 700;
        letter-spacing: 0.05em;
        text-transform: uppercase;
        margin-bottom: 8px;
    }
    
    /* Hero Title & Subtitle */
    .main-title {
        font-size: 2.1rem;
        font-weight: 800;
        color: #0F172A;
        letter-spacing: -0.025em;
        margin-bottom: 4px;
        line-height: 1.2;
    }
    .main-subtitle {
        font-size: 1.0rem;
        color: #475569;
        margin-bottom: 20px;
        line-height: 1.5;
    }
    
    /* Disclaimer Card */
    .disclaimer-banner {
        background-color: #F8FAFC;
        border-left: 4px solid #0D9488;
        border-radius: 6px;
        padding: 12px 16px;
        color: #334155;
        font-size: 0.875rem;
        margin-bottom: 24px;
    }
    
    /* Section Headers */
    .section-header {
        font-size: 1.1rem;
        font-weight: 700;
        color: #1E293B;
        margin-top: 10px;
        margin-bottom: 12px;
        display: flex;
        align-items: center;
        gap: 8px;
        border-bottom: 1px solid #E2E8F0;
        padding-bottom: 6px;
    }
    
    /* Prediction Hero Card */
    .result-card {
        border-radius: 12px;
        padding: 24px;
        margin-bottom: 20px;
        border: 1px solid #E2E8F0;
        background: #FFFFFF;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
    }
    
    .badge-tinggi {
        background-color: #ECFDF5;
        color: #065F46;
        border: 1.5px solid #A7F3D0;
        padding: 6px 16px;
        border-radius: 9999px;
        font-size: 1.2rem;
        font-weight: 800;
        display: inline-block;
    }
    .badge-sedang {
        background-color: #FFFBEB;
        color: #92400E;
        border: 1.5px solid #FDE68A;
        padding: 6px 16px;
        border-radius: 9999px;
        font-size: 1.2rem;
        font-weight: 800;
        display: inline-block;
    }
    .badge-rendah {
        background-color: #FFF1F2;
        color: #9F1239;
        border: 1.5px solid #FECDD3;
        padding: 6px 16px;
        border-radius: 9999px;
        font-size: 1.2rem;
        font-weight: 800;
        display: inline-block;
    }
    
    /* Probability Progress Item */
    .prob-row {
        margin-bottom: 12px;
    }
    .prob-label-row {
        display: flex;
        justify-content: space-between;
        font-size: 0.9rem;
        font-weight: 600;
        color: #1E293B;
        margin-bottom: 4px;
    }
    .prob-bar-container {
        width: 100%;
        background-color: #F1F5F9;
        border-radius: 9999px;
        height: 10px;
        overflow: hidden;
    }
    .prob-bar-fill {
        height: 100%;
        border-radius: 9999px;
        transition: width 0.4s ease;
    }
    
    /* Insight Box */
    .insight-card {
        background-color: #F8FAFC;
        border: 1px solid #E2E8F0;
        border-radius: 10px;
        padding: 16px;
        margin-top: 16px;
    }
    .insight-card ul {
        margin: 0;
        padding-left: 20px;
        color: #334155;
        font-size: 0.88rem;
    }
    .insight-card li {
        margin-bottom: 8px;
    }
    
    /* Placeholder State */
    .placeholder-box {
        background: #F8FAFC;
        border: 2px dashed #CBD5E1;
        border-radius: 12px;
        padding: 40px 24px;
        text-align: center;
        color: #64748B;
    }
    </style>
    """, unsafe_allow_html=True)

def generate_insights(pred, data_dict):
    insights = []
    
    # Evaluasi tidur
    if data_dict['Jam_Tidur_Harian'] < 6.0:
        insights.append("⏱️ **Durasi Istirahat Rendah:** Jam tidur harian di bawah 6 jam dapat menurunkan fokus kognitif dan memori jangka panjang. Dianjurkan mencapai 7–8 jam.")
    elif data_dict['Jam_Tidur_Harian'] >= 7.0:
        insights.append("✅ **Manajemen Tidur Baik:** Jam tidur optimal (≥7 jam) mendukung pemulihan energi dan konsentrasi belajar.")

    # Evaluasi gadget malam
    if data_dict['Penggunaan_Gadget_Malam_Jam'] > 3.0:
        insights.append("📱 **Screentime Malam Tinggi:** Paparan gadget larut malam berpotensi mengganggu ritme sirkadian dan kualitas tidur. Pertimbangkan aturan *digital sunset* 1 jam sebelum tidur.")

    # Evaluasi stres
    if data_dict['Tingkat_Stres'] == "Tinggi":
        insights.append("🧘 **Stres Tinggi Terdeteksi:** Tingkat stres berlebih sering menjadi beban mental. Terapkan teknik dekompresi seperti *Pomodoro*, olahraga ringan, atau konsultasi akademik.")

    # Evaluasi belajar & kehadiran
    if data_dict['Kehadiran_Kuliah_Pct'] < 75.0:
        insights.append("⚠️ **Presensi Kurang dari 75%:** Kehadiran di bawah standar dapat mempersulit pemahaman silabus kuliah dan berisiko syarat ujian.")
    
    if data_dict['Jam_Belajar_Harian'] >= 4.0:
        insights.append("📚 **Komitmen Belajar Mandiri Kuat:** Jam belajar mandiri memadai. Pastikan diselingi istirahat teratur agar tidak terjadi *cognitive burnout*.")

    if pred == "Tinggi":
        insights.append("🎯 **Prediksi Produktivitas Tinggi:** Profil kebiasaan belajar dan istirahat Anda menunjukkan sinergi yang sangat seimbang. Pertahankan ritme kerja berkelanjutan.")
    elif pred == "Sedang":
        insights.append("💡 **Peluang Optimasi:** Produktivitas berada di tingkat sedang. Melakukan penyesuaian kecil pada konsistensi tidur atau alokasi belajar dapat memberi dorongan signifikan.")
    else:
        insights.append("📌 **Langkah Rekomendasi:** Tingkat produktivitas diprediksi rendah. Fokuskan pada penataan ulang jam tidur dan pengurangan distraksi digital malam hari sebagai prioritas pertama.")

    return insights

def main():
    inject_custom_css()
    
    # Inisialisasi Session State Default untuk Form Input
    default_values = {
        'val_belajar': 5.0,
        'val_tidur': 7.0,
        'val_kehadiran': 90.0,
        'val_ipk': 3.50,
        'val_organisasi': "Ya",
        'val_stres': "Sedang",
        'val_gadget': 2.0,
        'last_prediction': None,
        'last_probs': None,
        'last_inputs': None
    }
    for k, v in default_values.items():
        if k not in st.session_state:
            st.session_state[k] = v

    # --- SIDEBAR ---
    with st.sidebar:
        st.markdown("### 🎓 Informasi Sistem")
        st.markdown("""
        **Student Productivity Prediction System** dirancang untuk membantu mahasiswa dan dosen mengevaluasi faktor kebiasaan yang berkaitan dengan tingkat produktivitas akademik.
        """)
        
        st.markdown("---")
        st.markdown("#### ⚙️ Spesifikasi Model")
        st.markdown("""
        - **Algoritma:** Random Forest Classifier
        - **Preprocessing:** Imputasi median + One-Hot Encoding
        - **Validasi:** 5-Fold Stratified Group CV
        - **Akurasi Validasi:** ~98.13% Macro F1
        - **Target:** Produktivitas (`Rendah`, `Sedang`, `Tinggi`)
        """)
        
        st.markdown("---")
        st.markdown("#### 📋 7 Fitur yang Dinilai")
        with st.expander("Lihat Rincian Fitur", expanded=False):
            st.markdown("""
            1. **Jam Belajar Harian** (0–24 jam)
            2. **Jam Tidur Harian** (0–24 jam)
            3. **Kehadiran Kuliah** (0–100%)
            4. **IPK Terakhir** (0.0–4.0)
            5. **Aktivitas Organisasi** (`Ya` / `Tidak`)
            6. **Tingkat Stres** (`Rendah`, `Sedang`, `Tinggi`)
            7. **Gadget Malam** (0–24 jam)
            """)
            
        st.markdown("---")
        st.markdown("#### 🔒 Privasi & Etika")
        st.caption("Aplikasi ini tidak menyimpan data pribadi Anda ke server eksternal. Hasil keluaran adalah estimasi probabilistik dan bukan evaluasi mutlak kemampuan personal.")

    # --- MAIN CONTENT HEADER ---
    st.markdown('<div class="top-badge">🎓 AI Decision Support System</div>', unsafe_allow_html=True)
    st.markdown('<div class="main-title">Student Productivity Prediction</div>', unsafe_allow_html=True)
    st.markdown('<div class="main-subtitle">Analisis estimasi tingkat produktivitas mahasiswa berbasis data pola belajar, ritme istirahat, dan kebiasaan digital harian.</div>', unsafe_allow_html=True)

    # Disclaimer Callout
    st.markdown("""
    <div class="disclaimer-banner">
        <strong>Pemberitahuan:</strong> Model ini memprediksi tingkat produktivitas berdasarkan estimasi matematis dari data historis. Hasil prediksi tidak menggambarkan kapasitas intelektual mutlak dan tidak membuktikan hubungan sebab-akibat langsung.
    </div>
    """, unsafe_allow_html=True)

    # Load Model
    model_data, err_msg = load_model()
    if model_data is None:
        st.error(f"⚠️ {err_msg}")
        st.info("Pastikan artefak model telah diekspor dan tersedia di folder `models/` atau `pipeline_app/models/`.")
        return

    model = model_data['model']
    feature_cols = model_data['feature_cols']
    classes = model_data['classes']

    # --- QUICK PRESETS (DEMO 1-KLIK) ---
    st.markdown("##### ⚡ Contoh Cepat (Quick Demo Presets)")
    p_col1, p_col2, p_col3 = st.columns(3)
    
    with p_col1:
        if st.button("🌟 Mahasiswa Berprestasi", use_container_width=True, help="Isi form dengan profil belajar tinggi dan teratur"):
            st.session_state['val_belajar'] = 7.5
            st.session_state['val_tidur'] = 7.5
            st.session_state['val_kehadiran'] = 96.0
            st.session_state['val_ipk'] = 3.85
            st.session_state['val_organisasi'] = "Ya"
            st.session_state['val_stres'] = "Rendah"
            st.session_state['val_gadget'] = 1.0
            st.rerun()

    with p_col2:
        if st.button("⚖️ Mahasiswa Seimbang", use_container_width=True, help="Isi form dengan profil belajar dan istirahat moderat"):
            st.session_state['val_belajar'] = 4.5
            st.session_state['val_tidur'] = 6.5
            st.session_state['val_kehadiran'] = 85.0
            st.session_state['val_ipk'] = 3.30
            st.session_state['val_organisasi'] = "Ya"
            st.session_state['val_stres'] = "Sedang"
            st.session_state['val_gadget'] = 2.5
            st.rerun()

    with p_col3:
        if st.button("⚠️ Mahasiswa Terbebani", use_container_width=True, help="Isi form dengan profil tidur kurang dan stres tinggi"):
            st.session_state['val_belajar'] = 1.5
            st.session_state['val_tidur'] = 4.5
            st.session_state['val_kehadiran'] = 60.0
            st.session_state['val_ipk'] = 2.40
            st.session_state['val_organisasi'] = "Tidak"
            st.session_state['val_stres'] = "Tinggi"
            st.session_state['val_gadget'] = 5.0
            st.rerun()

    st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)

    # --- DUA KOLOM: INPUT & OUTPUT ---
    col_input, col_output = st.columns([1.1, 1], gap="large")

    # === KOLOM KIRI: FORMULIR INPUT ===
    with col_input:
        st.markdown('<div class="section-header">📝 Parameter Masukan Mahasiswa</div>', unsafe_allow_html=True)
        
        with st.form("student_input_form"):
            # Kelompok 1: Akademik
            st.markdown("##### 📚 Kebiasaan Belajar & Akademik")
            c1, c2 = st.columns(2)
            with c1:
                jam_belajar = st.number_input(
                    "Jam Belajar Mandiri (Harian)",
                    min_value=0.0, max_value=24.0,
                    value=float(st.session_state['val_belajar']),
                    step=0.5,
                    help="Rata-rata jam belajar di luar jam kelas formal"
                )
            with c2:
                ipk = st.number_input(
                    "IPK Terakhir Kumulatif",
                    min_value=0.0, max_value=4.0,
                    value=float(st.session_state['val_ipk']),
                    step=0.01,
                    format="%.2f",
                    help="Indeks Prestasi Kumulatif semester terakhir"
                )
            
            kehadiran = st.slider(
                "Persentase Kehadiran Kuliah (%)",
                min_value=0.0, max_value=100.0,
                value=float(st.session_state['val_kehadiran']),
                step=1.0,
                help="Tingkat kehadiran tatap muka atau daring pada perkuliahan"
            )

            # Kelompok 2: Kesehatan & Stres
            st.markdown("##### 🧘 Pola Istirahat & Beban Mental")
            c3, c4 = st.columns(2)
            with c3:
                jam_tidur = st.number_input(
                    "Durasi Tidur (Jam/Hari)",
                    min_value=0.0, max_value=24.0,
                    value=float(st.session_state['val_tidur']),
                    step=0.5,
                    help="Rata-rata jam tidur malam per 24 jam"
                )
            with c4:
                idx_stres = ["Rendah", "Sedang", "Tinggi"].index(st.session_state['val_stres']) if st.session_state['val_stres'] in ["Rendah", "Sedang", "Tinggi"] else 1
                stres = st.selectbox(
                    "Tingkat Stres yang Dirasakan",
                    options=["Rendah", "Sedang", "Tinggi"],
                    index=idx_stres,
                    help="Tingkat tekanan psikologis atau akademik yang dirasakan"
                )

            # Kelompok 3: Gaya Hidup & Aktivitas
            st.markdown("##### 📱 Aktivitas & Kebiasaan Digital")
            c5, c6 = st.columns(2)
            with c5:
                gadget = st.number_input(
                    "Penggunaan Gadget Malam (Jam)",
                    min_value=0.0, max_value=24.0,
                    value=float(st.session_state['val_gadget']),
                    step=0.5,
                    help="Waktu memakai ponsel/laptop untuk hiburan larut malam"
                )
            with c6:
                idx_org = ["Ya", "Tidak"].index(st.session_state['val_organisasi']) if st.session_state['val_organisasi'] in ["Ya", "Tidak"] else 0
                organisasi = st.selectbox(
                    "Aktif Kegiatan Organisasi",
                    options=["Ya", "Tidak"],
                    index=idx_org,
                    help="Apakah terlibat dalam kepengurusan atau kegiatan BEM/UKM"
                )

            st.markdown("<div style='height: 8px;'></div>", unsafe_allow_html=True)
            submit_btn = st.form_submit_button("🔮 Analisis & Prediksi Produktivitas", use_container_width=True, type="primary")

        if submit_btn:
            input_dict = {
                'Jam_Belajar_Harian': jam_belajar,
                'Jam_Tidur_Harian': jam_tidur,
                'Kehadiran_Kuliah_Pct': kehadiran,
                'IPK_Terakhir': ipk,
                'Aktivitas_Organisasi': organisasi,
                'Tingkat_Stres': stres,
                'Penggunaan_Gadget_Malam_Jam': gadget
            }
            
            input_df = pd.DataFrame([input_dict])
            try:
                input_df = input_df[feature_cols]
                prediction = model.predict(input_df)[0]
                
                probs = None
                if hasattr(model, "predict_proba"):
                    probs = model.predict_proba(input_df)[0]
                
                st.session_state['last_prediction'] = prediction
                st.session_state['last_probs'] = probs
                st.session_state['last_inputs'] = input_dict
                
            except Exception as e:
                st.error(f"Terjadi kesalahan saat memproses inferensi: {e}")

    # === KOLOM KANAN: HASIL PREDIKSI & ANALISIS ===
    with col_output:
        st.markdown('<div class="section-header">📊 Hasil Analisis & Prediksi</div>', unsafe_allow_html=True)
        
        last_pred = st.session_state.get('last_prediction')
        last_probs = st.session_state.get('last_probs')
        last_inputs = st.session_state.get('last_inputs')

        if last_pred is None:
            st.markdown("""
            <div class="placeholder-box">
                <div style="font-size: 2.5rem; margin-bottom: 12px;">📊</div>
                <h4 style="margin: 0; color: #334155;">Belum Ada Data yang Dianalisis</h4>
                <p style="font-size: 0.9rem; margin-top: 8px;">Silakan isi formulir di sebelah kiri atau pilih salah satu <strong>Contoh Cepat (Quick Demo)</strong> di atas, lalu tekan tombol <strong>Analisis & Prediksi</strong>.</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            # Badge Class Styling
            badge_class = "badge-sedang"
            badge_icon = "⚖️"
            if last_pred == "Tinggi":
                badge_class = "badge-tinggi"
                badge_icon = "🚀"
            elif last_pred == "Rendah":
                badge_class = "badge-rendah"
                badge_icon = "⚠️"

            # Hitung confidence
            conf_str = ""
            if last_probs is not None:
                max_prob = np.max(last_probs) * 100
                conf_str = f"Tingkat Keyakinan Model: <strong>{max_prob:.1f}%</strong>"

            # Tampilkan Hero Result Card
            st.markdown(f"""
            <div class="result-card">
                <div style="font-size: 0.85rem; font-weight: 700; color: #64748B; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 8px;">
                    Estimasi Tingkat Produktivitas
                </div>
                <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 10px;">
                    <div class="{badge_class}">
                        {badge_icon} Produktivitas {last_pred}
                    </div>
                    <div style="font-size: 0.88rem; color: #475569;">
                        {conf_str}
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            # Probabilitas Tiap Kelas
            if last_probs is not None:
                st.markdown("##### 📈 Distribusi Probabilitas Kelas")
                
                color_map = {
                    "Tinggi": "#10B981", # Emerald
                    "Sedang": "#F59E0B", # Amber
                    "Rendah": "#EF4444"  # Rose
                }
                
                for i, class_name in enumerate(classes):
                    prob_val = last_probs[i] * 100
                    fill_color = color_map.get(class_name, "#0D9488")
                    
                    st.markdown(f"""
                    <div class="prob-row">
                        <div class="prob-label-row">
                            <span>{class_name}</span>
                            <span>{prob_val:.1f}%</span>
                        </div>
                        <div class="prob-bar-container">
                            <div class="prob-bar-fill" style="width: {prob_val}%; background-color: {fill_color};"></div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

            # Rekomendasi / Insight Adaptif
            st.markdown("##### 💡 Analisis & Rekomendasi Adaptif")
            insights = generate_insights(last_pred, last_inputs)
            
            insight_html = '<div class="insight-card"><ul>'
            for item in insights:
                insight_html += f"<li>{item}</li>"
            insight_html += '</ul></div>'
            
            st.markdown(insight_html, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
