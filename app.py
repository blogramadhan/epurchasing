# Import Core PKGS
import streamlit as st

# Import Fungsi E-Purchasing
from epurchasing import ekatalog

def main():
    # Setting Halaman Awal
    st.set_page_config(page_title="Dashboard E-Purchasing Provinsi Kalimantan Barat", layout="wide")

    st.title("DASHBOARD E-PURCHASING")
    daerah = ["HOME", "PROV. KALBAR", "KOTA PONTIANAK", "KAB. KUBU RAYA", "KAB. MEMPAWAH", "KOTA SINGKAWANG", "KAB. SAMBAS", "KAB. BENGKAYANG", "KAB. LANDAK",
              "KAB. SANGGAU", "KAB. SEKADAU", "KAB. SINTANG", "KAB. MELAWI", "KAB. KAPUAS HULU", "KAB. KAYONG UTARA", "KAB. KETAPANG"]
    pilih = st.selectbox("Pilih daerah yang diinginkan :", daerah)

    if pilih == "HOME":
        st.subheader("E-Purchasing Provinsi Kalimantan Barat")
        st.write("Dashboard ini dibuat untuk menampilkan data transaksi E-Purchasing di Provinsi Kalimantan Barat. \
                Saat ini data yang bisa ditampilkan hanya data E-Katalog saja, sedangkan data transakssi Toko Daring \
                masih dalam pengembangan. Silahkan pilih daerah UKPBJ yang diinginkan.")
    else:
        ekatalog(pilih)

if __name__ == '__main__':
    main()