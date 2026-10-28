# Analisis Harga & Rating Properti Airbnb (Bandung Raya & Puncak/Bogor)

## Latar Belakang Proyek
Proyek ini bertujuan untuk menganalisis faktor-faktor yang mempengaruhi harga sewa penginapan (Airbnb) di wilayah Bandung Raya dan Puncak/Bogor. Secara spesifik, proyek ini menjawab dua pertanyaan utama:
1. Apakah rating properti berkorelasi dengan harga sewa?
2. Apakah jumlah ulasan (review) dapat memvalidasi kualitas sebuah properti?

## 📊 Data & Metodologi
- **Data**: Dataset berisi 572 properti Airbnb (Home, Villa, Apartment, dll) beserta harga, rating, dan jumlah ulasan.
- **Pembersihan Data**: 
  - Mengekstrak informasi lokasi (kecamatan) dan tipe properti dari teks nama properti.
  - Normalisasi nama kecamatan menggunakan *mapping table* manual.
  - Transformasi Logaritma (`log1p`) pada harga untuk mengatasi distribusi *right-skewed*.
  - **Bayesian Average** untuk menyesuaikan rating (menyeimbangkan rating tinggi dari properti dengan sedikit ulasan).
- **Analisis**: Eksplorasi Data (EDA), Uji Korelasi (Pearson & Spearman), dan Regresi Linear Berganda (OLS).

## 💡 Temuan Utama (Key Insights)
1. **Korelasi Rating vs Harga Sangat Lemah**: Secara mentah (bivariat), rating tidak memiliki korelasi yang signifikan dengan harga (r = -0.013, p > 0.05). Rating tinggi tidak menjamin harga lebih mahal.
2. **Lokasi Mempengaruhi Perbedaan Harga**: Setelah mengontrol variabel lain, properti di Puncak/Bogor harganya rata-rata **27% lebih mahal** dibandingkan Bandung Raya. Median harga di Puncak (~Rp 10.2 Juta) hampir dua kali lipat Bandung Raya (~Rp 5.8 Juta).
3. **Omitted Variable Bias**: Saat kita membandingkan properti dengan **tipe yang sama** di **lokasi yang sama** (menggunakan Regresi Linear), rating yang tinggi terbukti memberikan *premium* harga (sekitar 8% lebih tinggi untuk setiap kenaikan 0.1 poin rating).
4. **Tipe Properti Sangat Berpengaruh**: Villa secara signifikan memiliki harga tertinggi, sedangkan tipe "Room" memiliki harga terendah.

## 📂 Struktur Proyek
- `data/raw/`: Dataset asli.
- `data/reference/`: File *mapping* untuk normalisasi lokasi.
- `data/processed/`: Dataset bersih yang siap dianalisis.
- `notebooks/`: 
  - `01_data_audit.ipynb` (Pengecekan kualitas data).
  - `02_cleaning.ipynb` (Pembersihan & rekayasa fitur).
  - `03_eda.ipynb` (Eksplorasi data & pemodelan regresi).
- `dashboard/app.py`: Aplikasi *dashboard* interaktif Streamlit.

## 🚀 Cara Menjalankan Dashboard Secara Lokal
1. Clone repositori ini.
2. Buat *virtual environment* dan install dependensi:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
