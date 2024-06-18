print("\n|   YAZID AQIL ASSALAM   |")
print("|   22343014   |")
print("|   Praktikum Struktur Data   |")
print("|   202223430028   |")

class Simpul:
    def __inisial__(self, nim, nama, prodi, nilai):
        self.nim = nim
        self.nama = nama
        self.prodi = prodi
        self.nilai = nilai
        self.selanjutnya = None

class DaftarSimpul:
    def __inisial__(self):
        self.kepala = None

    def tambah_data(self, nim, nama, prodi, nilai):
        simpul = Simpul(nim, nama, prodi, nilai)
        if self.kepala is None:
            self.kepala = simpul
        else:
            saat_ini = self.kepala
            while saat_ini.selanjutnya is not None:
                saat_ini = saat_ini.selanjutnya
            saat_ini.selanjutnya = simpul
        print("Data berhasil ditambahkan")

    def cetak_data(self):
        if self.kepala is None:
            print("Data masih kosong")
        else:
            saat_ini = self.kepala
            print("\nData dalam daftar:")
            while saat_ini is not None:
                print("NIM: {}, Nama: {}, Prodi: {}, Nilai: {}".format(saat_ini.nim, saat_ini.nama, saat_ini.prodi, saat_ini.nilai))
                saat_ini = saat_ini.selanjutnya

    def cari_data(self, nim):
        saat_ini = self.kepala
        while saat_ini is not None:
            if saat_ini.nim == nim:
                return saat_ini
            saat_ini = saat_ini.selanjutnya
        return None

    def ubah_data(self, nim, nama, prodi, nilai):
        simpul = self.cari_data(nim)
        if simpul is not None:
            simpul.nama = nama
            simpul.prodi = prodi
            simpul.nilai = nilai
            print("Data berhasil diubah")
        else:
            print("Data dengan NIM tersebut tidak ditemukan")

    def hapus_data(self, nim):
        saat_ini = self.kepala
        sebelumnya = None
        while saat_ini is not None:
            if saat_ini.nim == nim:
                if sebelumnya is None:
                    self.kepala = saat_ini.selanjutnya
                else:
                    sebelumnya.selanjutnya = saat_ini.selanjutnya
                print("Data berhasil dihapus")
                return
            sebelumnya = saat_ini
            saat_ini = saat_ini.selanjutnya
        print("Data dengan NIM tersebut tidak ditemukan")

    def tukar_data(self, a, b):
        temp_nilai = a.nilai
        temp_nim = a.nim
        temp_nama = a.nama
        temp_prodi = a.prodi

        a.nilai = b.nilai
        a.nim = b.nim
        a.nama = b.nama
        a.prodi = b.prodi

        b.nilai = temp_nilai
        b.nim = temp_nim
        b.nama = temp_nama
        b.prodi = temp_prodi

    def urut_data(self):
        if self.kepala is None:
            return
        akhir = None
        while akhir != self.kepala:
            saat_ini = self.kepala
            while saat_ini.selanjutnya != akhir:
                if saat_ini.nilai < saat_ini.selanjutnya.nilai:
                    self.tukar_data(saat_ini, saat_ini.selanjutnya)
                saat_ini = saat_ini.selanjutnya
            akhir = saat_ini

daftar_simpul = DaftarSimpul()

while True:
    print("\nMenu:")
    print("1. Tambah Data")
    print("2. Cetak Data")
    print("3. Hapus Data")
    print("4. Ubah Data")
    print("5. Urut Data")
    print("6. Cari Data")
    print("7. Keluar")

    pilihan = int(input("Pilihan Anda: "))

    if pilihan == 1:
        nim = int(input("\nMasukkan NIM: "))
        nama = input("Masukkan Nama: ")
        prodi = input("Masukkan Prodi: ")
        nilai = int(input("Masukkan Nilai: "))
        daftar_simpul.tambah_data(nim, nama, prodi, nilai)
    elif pilihan == 2:
        daftar_simpul.cetak_data()
    elif pilihan == 3:
        nim = int(input("Masukkan NIM yang Akan Dihapus: "))
        daftar_simpul.hapus_data(nim)
    elif pilihan == 4:
        nim = int(input("Masukkan NIM yang Akan Diubah: "))
        nama = input("Masukkan Nama Baru: ")
        prodi = input("Masukkan Prodi Baru: ")
        nilai = int(input("Masukkan Nilai Baru: "))
        daftar_simpul.ubah_data(nim, nama, prodi, nilai)
    elif pilihan == 5:
        daftar_simpul.urut_data()
        print("Data berhasil diurutkan.")
    elif pilihan == 6:
        nim = int(input("Masukkan NIM yang Akan Dicari: "))
        data = daftar_simpul.cari_data(nim)
        if data is not None:
            print("Data ditemukan - NIM: {}, Nama: {}, Prodi: {}, Nilai: {}".format(data.nim, data.nama, data.prodi, data.nilai))
        else:
            print("Data dengan NIM tersebut tidak ditemukan.")
    elif pilihan == 7:
        print("\nTerima kasih telah menggunakan program ini!\n")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")
