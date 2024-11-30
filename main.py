def hitung_harga_tanah(panjang, lebar, harga_per_meter):
    luas = panjang * lebar
    total_harga = luas * harga_per_meter
    return total_harga
harga_daerah = {
    "Jakarta": {
        "Jakarta Selatan": 40000000,
        "Jakarta Timur": 30000000,
        "Jakarta Barat": 25000000,
        "Jakarta Utara": 20000000,
        "Jakarta Pusat": 35000000
    },

    "Bekasi": {
        "Bekasi Selatan": 6000000,
        "Bekasi Timur": 5000000,
        "Bekasi Barat": 6000000,
        "Bekasi Utara": 5000000
    },

    "Tangerang": {
        "Tangerang Selatan": 3000000,
        "Tangerang Kota": 2800000
    },

    "Bogor": {
        "Bogor Barat": 4500000,
        "Bogor Selatan": 12000000,
        "Bogor Tengah": 20000000,
        "Bogor Timur": 7000000,
        "Bogor Utara": 6000000
    }
}

def pilih_daerah_utama():
    while True:
        print("\nDaftar Daerah Utama:")
        for daerah in harga_daerah.keys():
            print(f"- {daerah}")
        daerah_pilihan = input("\nMasukkan nama daerah utama (Jakarta, Bekasi, Tangerang, Bogor): ").strip()
        if daerah_pilihan in harga_daerah:
            return daerah_pilihan
        print("Daerah utama yang Anda masukkan tidak tersedia. Silakan coba lagi.")

# Menampilkan daftar sub-daerah
def pilih_sub_daerah(daerah_pilihan):
    while True:
        print(f"\nDaftar Sub-Daerah di {daerah_pilihan}:")
        sub_daerah_list = harga_daerah[daerah_pilihan]
        for sub_daerah, harga in sub_daerah_list.items():
            print(f"- {sub_daerah}: Rp{harga:,} per meter")
        sub_daerah_pilihan = input("\nMasukkan nama sub-daerah: ").strip()
        if sub_daerah_pilihan in sub_daerah_list:
            return sub_daerah_pilihan
        print("Sub-daerah yang Anda masukkan tidak tersedia. Silakan coba lagi.")

# Input dari pengguna
try:
    daerah_pilihan = pilih_daerah_utama()
    sub_daerah_pilihan = pilih_sub_daerah(daerah_pilihan)

    # Input dimensi tanah
    panjang = float(input("\nMasukkan panjang tanah (meter): "))
    lebar = float(input("Masukkan lebar tanah (meter): "))

    # Mengambil harga berdasarkan sub-daerah
    harga_per_meter = harga_daerah[daerah_pilihan][sub_daerah_pilihan]

    # Menghitung dan menampilkan hasil
    total_harga = hitung_harga_tanah(panjang, lebar, harga_per_meter)
    print(f"\nDaerah yang dipilih: {daerah_pilihan} - {sub_daerah_pilihan}")
    print(f"Luas tanah: {panjang * lebar} meter persegi")
    print(f"Harga tanah per meter: Rp{harga_per_meter:,}")
    print(f"Total harga tanah: Rp{total_harga:,.2f}")
except ValueError:
    print("Input harus berupa angka!")


# Menawarkan pilihan untuk melanjutkan atau keluar
        lanjut = input("\nApakah Anda ingin menghitung harga tanah lagi? (ya/tidak): ").strip().lower()
        if lanjut != "ya":
            print("\nTerima kasih telah menggunakan program ini. Sampai jumpa!")
            break

# Menjalankan program
if __name__ == "__main__":
    main()