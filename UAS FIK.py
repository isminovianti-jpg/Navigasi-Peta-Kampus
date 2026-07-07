#  Kelompok 2 | Struktur Data: Graph, Priority Queue, BFS/Dijkstra
#  APLIKASI NAVIGASI PETA KAMPUS


# Disini kita membuat import library
import heapq
from collections import deque


# GRAPH - REPRESENTASI PETA KAMPUS
class PetaKampus:
    def __init__(self):
        self.graph = {}

    def tambah_gedung(self, nama):
        if nama not in self.graph:
            self.graph[nama] = {}


# Fungsi Tambah Jalur
    def tambah_jalur(self, dari, ke, jarak):
        self.tambah_gedung(dari)
        self.tambah_gedung(ke)
        self.graph[dari][ke] = jarak
        self.graph[ke][dari] = jarak

    def tampilkan_semua(self):
        print("\n=== DAFTAR GEDUNG & KONEKSI ===")
        for gedung, koneksi in self.graph.items():
            print(f"  {gedung}:")
            for tujuan, jarak in koneksi.items():
                print(f"    -> {tujuan} ({jarak} meter)")


# DIJKSTRA - RUTE TERPENDEK
def dijkstra(graph, awal, tujuan):
    antrian = [(0, awal, [awal])]
    sudah_dikunjungi = set()

    while antrian:
        jarak_total, node_sekarang, jalur = heapq.heappop(antrian)

        if node_sekarang in sudah_dikunjungi:
            continue
        sudah_dikunjungi.add(node_sekarang)

        if node_sekarang == tujuan:
            return jarak_total, jalur

        for tetangga, bobot in graph[node_sekarang].items():
            if tetangga not in sudah_dikunjungi:
                heapq.heappush(antrian, (jarak_total + bobot, tetangga, jalur + [tetangga]))

    return float('inf'), []


# ESTIMASI WAKTU TEMPUH
KECEPATAN_JALAN = 80  # meter per menit
def estimasi_waktu(jarak_meter):
    menit = jarak_meter / KECEPATAN_JALAN
    return round(menit, 1)


# MENU UTAMA (CLI)
def menu():
    peta = PetaKampus()

# DATA GEDUNG & JALUR KAMPUS LPKIA BANDUNG
    peta.tambah_jalur("G. Utama",      "G. Serba Guna", 38)
    peta.tambah_jalur("G. Utama",      "G. Kelas",      20)
    peta.tambah_jalur("G. Utama",      "Parkiran",      31)
    peta.tambah_jalur("G. Serba Guna", "G. Kelas",      24)
    peta.tambah_jalur("G. Serba Guna", "Kantin",        81)
    peta.tambah_jalur("G. Kelas",      "Kantin",       104)
    peta.tambah_jalur("Kantin",        "Parkiran",     153)

    while True:
        print("\n=============================")
        print("  NAVIGASI PETA KAMPUS")
        print("=============================")
        print("1. Lihat semua gedung & jalur")
        print("2. Cari rute terpendek")
        print("3. Keluar")
        print("-----------------------------")

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            peta.tampilkan_semua()

        elif pilihan == "2":
            awal   = input("Dari gedung: ").strip()
            tujuan = input("Ke gedung  : ").strip()

            if awal not in peta.graph or tujuan not in peta.graph:
                print("Gedung tidak ditemukan!")
                continue

            jarak, jalur = dijkstra(peta.graph, awal, tujuan)

            if jarak == float('inf'):
                print("Tidak ada jalur yang bisa dilalui.")
            else:
                print(f"\nRute       : {' -> '.join(jalur)}")
                print(f"Jarak total: {jarak} meter")
                print(f"Estimasi   : {estimasi_waktu(jarak)} menit")

        elif pilihan == "3":
            print("Keluar. Sampai jumpa!")
            break

        else:
            print("Pilihan tidak valid.")


# ENTRY POINT Program
if __name__ == "__main__":
    menu()