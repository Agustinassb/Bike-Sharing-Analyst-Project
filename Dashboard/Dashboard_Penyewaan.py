# -*- coding: utf-8 -*-
"""abcdef.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1W7td-PfPYm7_QDVLmYiq35xkCqHhi50K
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- Konfigurasi Layout Streamlit ---
st.set_page_config(
    page_title="Analisis Data Bike Sharing",
    page_icon="🚴‍♂️"
)

# --- Load Dataset ---
bike_day = pd.read_csv('C:/Users/agustinasb/Downloads/Bike-sharing-dataset/bike_day_modified.csv')
bike_hr = pd.read_csv('C:/Users/agustinasb/Downloads/Bike-sharing-dataset/bike_hr_modified.csv')

# --- Streamlit Title and Description ---
st.title("📊 Analisis Penyewaan Sepeda 🚴‍♂️")
st.markdown("""
Selamat datang di dashboard analisis data *Penyewaan Sepeda*!
Gunakan filter di sisi kiri untuk eksplorasi data berdasarkan musim tertentu.
Analisis meliputi:
1. Pola permintaan harian dan jam.
2. Pengaruh faktor cuaca terhadap jumlah penyewaan.
""")

# --- Sidebar for Filters ---
st.sidebar.header("⚙️ Filter Data")
selected_season = st.sidebar.selectbox("Pilih Musim:", bike_hr['season'].unique())

if selected_season:
    filtered_data_hr = bike_hr[bike_hr['season'] == selected_season]
    filtered_data_day = bike_day[bike_day['season'] == selected_season]

# --- Pola Permintaan ---
st.header("📈 Pola Permintaan Penyewaan Sepeda Weekday Vs Weekend")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Pola Permintaan Harian")
    if selected_season:
        daily_rentals = filtered_data_hr.groupby('day_of_week')['cnt'].mean().sort_values()
        plt.figure(figsize=(8, 4))
        daily_rentals.plot(
            kind='bar',
            color=['#87CEEB' if day in ['Saturday', 'Sunday'] else '#FF7F50' for day in daily_rentals.index]
        )
        plt.title('Rata-rata Penyewaan Sepeda Harian')
        plt.xlabel('Hari dalam Seminggu')
        plt.ylabel('Jumlah Penyewaan Rata-rata')
        plt.xticks(rotation=45, ha='right')
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        st.pyplot(plt)
        plt.close()

with col2:
    st.subheader("Pola Permintaan Berdasarkan Jam")
    if selected_season:
        hourly_rentals = filtered_data_hr.groupby(['hr', 'is_weekend'])['cnt'].mean().reset_index()
        plt.figure(figsize=(8, 4))
        sns.lineplot(
            x='hr',
            y='cnt',
            hue='is_weekend',
            data=hourly_rentals,
            marker='o',
            palette={0: "#FFA07A", 1: "#4682B4"}
        )
        plt.title('Rata-rata Penyewaan Sepeda per Jam')
        plt.xlabel('Jam dalam Sehari')
        plt.ylabel('Jumlah Penyewaan Rata-rata')
        plt.xticks(range(0, 24, 2))
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.legend(title='Jenis Hari', labels=['Hari Kerja', 'Akhir Pekan'])
        st.pyplot(plt)
        plt.close()

# --- Pengaruh Faktor Cuaca ---
st.header("🌦️ Pengaruh Faktor Cuaca terhadap Penyewaan")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Pengaruh Suhu terhadap Penyewaan")
    if selected_season:
        plt.figure(figsize=(8, 4))
        sns.scatterplot(
            x='temp',
            y='cnt',
            data=filtered_data_day,
            color='#20B2AA',
            alpha=0.6
        )
        plt.title('Suhu vs Jumlah Penyewaan')
        plt.xlabel('Suhu (Dinormalisasi)')
        plt.ylabel('Jumlah Penyewaan')
        plt.grid(axis='both', linestyle='--', alpha=0.7)
        st.pyplot(plt)
        plt.close()

with col2:
    st.subheader("Pengaruh Kondisi Cuaca terhadap Penyewaan")
    if selected_season:
        plt.figure(figsize=(8, 4))
        sns.boxplot(
            x='weathersit',
            y='cnt',
            data=filtered_data_day,
            palette="muted"
        )
        plt.title('Kondisi Cuaca vs Jumlah Penyewaan')
        plt.xlabel('Kondisi Cuaca (1: Cerah, 2: Berawan, 3: Hujan)')
        plt.ylabel('Jumlah Penyewaan')
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        st.pyplot(plt)
        plt.close()

# --- Footer ---
st.sidebar.markdown("---")
st.sidebar.markdown("Dikembangkan oleh: **Agustina Setianing Budi** 💻")
st.sidebar.markdown("🌟 *Selamat menganalisis data!* 🌟")