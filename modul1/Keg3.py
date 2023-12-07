def hitung_nilai_akhir(nilai_uts, nilai_uas):
    nilai_akhir = 0.2 * nilai_uts + 0.8 * nilai_uas
    return nilai_akhir

def tampilkan_nilai_akhir(data_nilai_akhir):
    print("Hasil Nilai Akhir Mahasiswa:")
    for nama, nilai_akhir in data_nilai_akhir.items():
        print("Nama: {}\tNilai Akhir: {:.2f}".format(nama, nilai_akhir))

def main():
    data_mahasiswa = {
        "Mahasiswa 1": {"uts": 80, "uas": 90},
        "Mahasiswa 2": {"uts": 70, "uas": 85},
        "Mahasiswa 3": {"uts": 85, "uas": 75},
    }

    data_nilai_akhir = {}
    
    for nama, nilai in data_mahasiswa.items():
        nilai_akhir = hitung_nilai_akhir(nilai["uts"], nilai["uas"])
        data_nilai_akhir[nama] = nilai_akhir

    tampilkan_nilai_akhir(data_nilai_akhir)

if __name__ == "__main__":
    main()