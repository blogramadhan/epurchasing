import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from babel.numbers import format_currency

def ekatalog(pilih):

    # Fungsi-fungsi buatan
    def convert_trxkatalog(dftrx):
        return dftrx.to_csv().encode('utf-8')

    def convert_prodkatalog(dfprod):
        return dfprod.to_csv().encode('utf-8')

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
    jumlah_penyedia = df_prod_loc['nama_penyedia'].value_counts().shape

    jumlah_trx_lokal = df_kat_loc_lokal['no_paket'].value_counts().shape
    nilai_trx_lokal = df_kat_loc_lokal['total_harga'].sum()
    nilai_trx_lokal_print = format_currency(nilai_trx_lokal, 'Rp. ', locale='id_ID')

    jumlah_trx_sektoral = df_kat_loc_sektoral['no_paket'].value_counts().shape
    nilai_trx_sektoral = df_kat_loc_sektoral['total_harga'].sum()
    nilai_trx_sektoral_print = format_currency(nilai_trx_sektoral, 'Rp. ', locale='id_ID')

    jumlah_trx_nasional = df_kat_loc_nasional['no_paket'].value_counts().shape
    nilai_trx_nasional = df_kat_loc_nasional['total_harga'].sum()
    nilai_trx_nasional_print = format_currency(nilai_trx_nasional, 'Rp. ', locale='id_ID')

    dkl1, dkl2, dkl3, dkl4 = st.columns(4)
    dkl1.metric("Jumlah Produk Katalog Lokal", jumlah_produk)
    dkl2.metric("Jumlah Penyedia Katalog Lokal", jumlah_penyedia[0])
    dkl3.metric("Jumlah Transaksi Katalog Lokal", jumlah_trx_lokal[0])
    dkl4.metric("Nilai Transaksi Katalog Lokal", nilai_trx_lokal_print)

    dks1, dks2, dks3 = st.columns(3)
    dks1.metric("Jumlah Produk E-Katalog Sektoral", "Tidak Ada Data")
    dks2.metric("Jumlah Transaksi E-Katalog Sektoral", jumlah_trx_sektoral[0])
    dks3.metric("Nilai Transaksi E-Ketalog Sektoral", nilai_trx_sektoral_print)

    dkn1, dkn2, dkn3 = st.columns(3)
    dkn1.metric("Jumlah Produk E-Katalog Nasional", "Tidak Ada Data")
    dkn2.metric("Jumlah Transaksi E-Katalog Nasional", jumlah_trx_nasional[0])
    dkn3.metric("Nilai Transaksi E-Ketalog Nasional", nilai_trx_nasional_print)

    # Buat grafik Data E-Katalog   
    #opdtrxcount = df_kat_loc_lokal.nama_satker.value_counts().sort_values(ascending=False)
    tmp_kat_loc_lokal = df_kat_loc_lokal[['nama_satker', 'no_paket']]
    pv_kat_loc_lokal = tmp_kat_loc_lokal.pivot_table(
        index = ['nama_satker', 'no_paket'],
        #values = ['no_paket']
    )
    tmp_kat_loc_lokal_ok = pv_kat_loc_lokal.reset_index()
    opdtrxcount = tmp_kat_loc_lokal_ok['nama_satker'].value_counts()
    opdtrxsum = df_kat_loc_lokal.groupby(by='nama_satker').sum().sort_values(by='total_harga', ascending=False)['total_harga']    

    # Tampilkan Grafik jika ada Data
    if jumlah_trx_lokal[0] > 0: 
        # Jumlah Transaksi Katalog Lokal OPD
        st.markdown('### Jumlah Transaksi OPD')
        tc1, tc2 = st.columns((3,7))
        with tc1:
            st.dataframe(opdtrxcount)
        with tc2:
            figtc = plt.figure(figsize=(10,6))
            sns.barplot(x = opdtrxcount, y = opdtrxcount.index)
            st.pyplot(figtc)

        # Nilai Transaksi Katalog Lokal OPD 
        st.markdown('### Nilai Transaksi OPD')
        ts1, ts2 = st.columns((3.3,6.7))
        with ts1:
            st.dataframe(opdtrxsum)
        with ts2:
            figts = plt.figure(figsize=(10,6))
            sns.barplot(x = opdtrxsum, y = opdtrxsum.index)
            st.pyplot(figts)
    else:
        st.error('BELUM ADA TRANSAKSI DI KATALOG LOKAL ...')
        #with st.expander("BELUM ADA TRANSAKSI DI KATALOG LOKAL ..."):
        #    st.write("""
        #        Data transaksi tidak tersedia, ayo donk belanja di Katalog Lokal agar ada data transaksi yang bisa diolah 
        #        untuk kemudian disajikan.
        #    """)
 
    # Download Data Button
    df1_download = convert_trxkatalog(df_kat_loc)
    df2_download = convert_prodkatalog(df_prod_loc)

    st.download_button(
        label = '📥 Download Data Transaksi E-KATALOG',
        data = df1_download,
        file_name = 'trxkatalog-' + kodeRUP + '.csv',
        mime = 'text/csv'
    )

    st.download_button(
        label = '📥 Download Data Produk E-KATALOG',
        data = df2_download,
        file_name = 'prodkatalog-' + kodeRUP + '.csv',
        mime = 'text/csv'
    )

    ## Data Transaksi Toko Daring
    #st.title("DATA TRANSAKSI TOKO DARING - " + pilih)


#def tokodaring(pilih):