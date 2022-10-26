import streamlit as st
import pandas as pd
from babel.numbers import format_currency

def ekatalog(pilih):

    # Setting CSS
    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    # Dataset
    #urlDatasetKatalog = "https://storage.googleapis.com/lpse_ramadhan/katalogdetail.xlsx"
    DatasetKatalog = "katalogdetail.xlsx"
    DatasetProdukKatalog = "prodkatalog.xlsx"
    #urlDatasetTokoDaring = "tokodaring.xlsx"

    # Konfigurasi Variabel Lokasi
    if pilih == "PROV. KALBAR":
        kodeRUP = "D197"
    if pilih == "KOTA PONTIANAK":
        kodeRUP = "D199"
    if pilih == "KAB. KUBU RAYA":
        kodeRUP = "D202"
    if pilih == "KAB. MEMPAWAH":
        kodeRUP = "D552"
    if pilih == "KOTA SINGKAWANG":
        kodeRUP = "D200"
    if pilih == "KAB. SAMBAS":
        kodeRUP = "D208"
    if pilih == "KAB. BENGKAYANG":
        kodeRUP = "D206"
    if pilih == "KAB. LANDAK":
        kodeRUP = "D205"
    if pilih == "KAB. SANGGAU":
        kodeRUP = "D204"
    if pilih == "KAB. SEKADAU":
        kodeRUP = "D198"
    if pilih == "KAB. SINTANG":
        kodeRUP = "D211"
    if pilih == "KAB. MELAWI":
        kodeRUP = "D210"
    if pilih == "KAB. KAPUAS HULU":
        kodeRUP = "D209"
    if pilih == "KAB. KAYONG UTARA":
        kodeRUP = "D207"
    if pilih == "KAB. KETAPANG":
        kodeRUP = "D201"    

    ## Data E-KATALOG
    df_kat = pd.read_excel(DatasetKatalog)
    df_prod = pd.read_excel(DatasetProdukKatalog)

    df_kat_loc = df_kat[df_kat['kd_klpd'] == kodeRUP]
    df_kat_loc_lokal = df_kat_loc[df_kat_loc['jenis_katalog'] == "Lokal"]
    df_kat_loc_sektoral = df_kat_loc[df_kat_loc['jenis_katalog'] == "Sektoral"]
    df_kat_loc_nasional = df_kat_loc[df_kat_loc['jenis_katalog'] == "Nasional"]
    df_prod_loc = df_prod[df_prod['kd_klpd'] == kodeRUP]


    ## Mulai Tampilkan Data E-KATALOG
    st.title("TRANSAKSI E-KATALOG - " + pilih)
    jumlah_produk = df_prod_loc['nama_produk'].count()
    jumlah_penyedia = df_prod_loc['nama_penyedia'].unique().shape

    jumlah_trx_lokal = df_kat_loc_lokal['no_paket'].unique().shape
    nilai_trx_lokal = df_kat_loc_lokal['total_harga'].sum()
    nilai_trx__lokal_print = format_currency(nilai_trx_lokal, 'Rp. ', locale='id_ID')

    jumlah_trx_sektoral = df_kat_loc_sektoral['no_paket'].unique().shape
    nilai_trx_sektoral = df_kat_loc_sektoral['total_harga'].sum()
    nilai_trx_sektoral_print = format_currency(nilai_trx_sektoral, 'Rp. ', locale='id_ID')

    jumlah_trx_nasional = df_kat_loc_nasional['no_paket'].unique().shape
    nilai_trx_nasional = df_kat_loc_nasional['total_harga'].sum()
    nilai_trx_nasional_print = format_currency(nilai_trx_nasional, 'Rp. ', locale='id_ID')

    dkl1, dkl2, dkl3, dkl4 = st.columns(4)
    dkl1.metric("Jumlah Produk Katalog Lokal", jumlah_produk)
    dkl2.metric("Jumlah Penyedia Katalog Lokal", jumlah_penyedia[0])
    dkl3.metric("Jumlah Transaksi Katalog Lokal", jumlah_trx_lokal[0])
    dkl4.metric("Nilai Transaksi Katalog Lokal", nilai_trx__lokal_print)

    dks1, dks2, dks3 = st.columns(3)
    dks1.metric("Jumlah Produk E-Katalog Sektoral", "Tidak Ada Data")
    dks2.metric("Jumlah Transaksi E-Katalog Sektoral", jumlah_trx_sektoral[0])
    dks3.metric("Nilai Transaksi E-Ketalog Sektoral", nilai_trx_sektoral_print)

    dkn1, dkn2, dkn3 = st.columns(3)
    dkn1.metric("Jumlah Produk E-Katalog Nasional", "Tidak Ada Data")
    dkn2.metric("Jumlah Transaksi E-Katalog Nasional", jumlah_trx_nasional[0])
    dkn3.metric("Nilai Transaksi E-Ketalog Nasional", nilai_trx_nasional_print)

    ## Mulai Tampilkan Data Etalase E-Katalog
    # df_daring.groupby(["nama_satker","kategori"])['valuasi'].count()
    #st.title("DATA ETALASE")
    #etalase = df_prod_loc.groupby(["nama_komoditas"])["nama_penyedia"].count()
    #etalase = df_prod_loc["nama_komoditas"].value_counts()
    #etalase.columns = ['Nama Komoditas', 'Jumlah Produk']
    #st.dataframe(etalase)



#def tokodaring(pilih):
