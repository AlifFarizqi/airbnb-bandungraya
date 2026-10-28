import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Airbnb Bandung Raya Dashboard", layout="wide")

# Load data, gunakan @st.cache_data untuk caching data agar lebih cepat
@st.cache_data
def load_data():
    df = pd.read_csv("data/processed/airbnb_clean.csv")
    df = df[df['region'].isin(['Bandung Raya','Bogor'])]
    return df

df = load_data()

# Header

st.title("Airbnb Bandung Raya: Analisis Harga dan Rating Properti")
st.markdown("""
    Dashboard ini meneksplorasi faktor-faktor yang mempengaruhi harga properti Airbnb di wilayah Bandung Raya dan Bogor.
    Dibuat berdasarkan dataset Airbnb
    """)

# Sidebar

st.sidebar.header("Filter Data")
selected_region = st.sidebar.multiselect(
    "Pilih Region:",
    options=df['region'].unique(),
    default=df['region'].unique()
)
selected_tipe =  st.sidebar.multiselect(
    "Pilih Tipe Properti:",
    options=df['tipe_raw'].unique(),
    default=df['tipe_raw'].unique()
)   
df_filtered = df[df['region'].isin(selected_region) & df['tipe_raw'].isin(selected_tipe)]

# KPI

st.subheader("Key Performance Indicators (KPI) atau Ringkasan Metrik")
col1, col2, col3 = st.columns(3)
col1.metric("Total Properti", f"{len(df_filtered):,}")
col2.metric("Median Harga", f"Rp {df_filtered['harga'].median():,.0f}")
col3.metric("Rata-rata Rating", f"{df_filtered['rating'].mean():.2f} / 5.0")

st.markdown("---")

# Visualisasi 1: Harga Median per Kecamatan (Top 10)
st.subheader("Harga Median per Kecamatan (Top 10)")
top_kec = df_filtered.groupby('kecamatan')['harga'].median().sort_values(ascending=True).head(10).reset_index()

fig_bar = px.bar(
    top_kec,
    x='harga',
    y='kecamatan',
    orientation='h',
    text='harga',
    title="Berdasarkan Median Harga (Rp)",
    color='harga',
    color_continuous_scale='Viridis'
)

fig_bar.update_traces(texttemplate='%{text:,.0f}', textposition='outside')
fig_bar.update_layout(xaxis_title="Harga (Rp)",yaxis_title="Kecamatan", coloraxis_showscale=False)
st.plotly_chart(fig_bar, use_container_width=True)

# Visualisasi 2: Scatter Plot Rating vs Harga
st.subheader("Hubungan Rating vs Harga Properti")
st.markdown("""
    Ukuran gelembung (Bubble) merepresentasikan jumlah review, Perhatikan bahwa lokasi (warna) sangat mempengaruhi harga setiap properti.
    """)   

fig_scatter = px.scatter(
    df_filtered.dropna(subset=['rating_adj']),
    x='rating_adj',
    y='harga',
    color='region',
    size='jumlah_review',
    hover_name='nama',
    hover_data=['tipe_raw', 'kecamatan'],
    log_y=True, # Harga diubah ke skala logaritmik agar sebaran lebih mudah dilihat 
    labels={'rating_adj': 'Rating Properti (disesuaikan oleh Bayesian)', 'Harga': 'Harga (Rp) - Skala Log'},
    title='Rating vs Harga (Skala Logaritmik)'
    ) 

st.plotly_chart(fig_scatter, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("Dashboard ini dibuat oleh Mochamad Alif Shihab Al-Farizqi | Data bersumber dari dataset Airbnb Bandung Raya di kaggle")