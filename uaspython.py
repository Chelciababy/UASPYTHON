import streamlit as st

# Kelas Barang
class Barang:
    def __init__(self, nama, harga, jumlah, kategori):
        self.nama = nama
        self.harga = harga
        self.jumlah = jumlah
        self.kategori = kategori
        self.is_beli = False

    def __str__(self):
        status = "✅" if self.is_beli else "❌"
        return f"{status} {self.nama} - Harga: Rp{self.harga:,}, Jumlah: {self.jumlah}, Kategori: {self.kategori}"

# Data disimpan di list session_state
if 'data_barang' not in st.session_state:
    st.session_state.data_barang = []

# Fungsi untuk total belanja
def hitung_total():
    total = sum(b.harga * b.jumlah for b in st.session_state.data_barang)
    return f"Rp{total:,}"

# Tampilan utama
st.title("🛒 Aplikasi Daftar Belanja Sederhana")

# Kolom untuk menu dan info total
col1, col2 = st.columns([3, 1])
with col1:
    st.write("### 📋 Menu:")
with col2:
    st.metric("Total Belanja", hitung_total())

# Menu pilihan
st.write("1. Lihat Daftar Barang")
st.write("2. Tambah Barang")
st.write("3. Tandai Barang Sudah Dibeli")
st.write("4. Edit Barang")
st.write("5. Hapus Barang")

menu = st.text_input("Masukkan angka menu (1-5):")


