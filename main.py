"""Menu utama: menjalankan validasi DFA untuk semua kasus.

Selain status VALID / TIDAK VALID, program menampilkan:
- tabel transisi langkah demi langkah untuk string yang dimasukkan
- tabel transisi lengkap DFA (ketik 'tabel')

Modul dimuat lewat path file (importlib) supaya nama folder dengan spasi
dan tanda kurung tidak jadi masalah, dan folder `email` tidak bentrok
dengan modul bawaan Python `email`.
"""
import importlib.util
from pathlib import Path

BASE = Path(__file__).parent

# nomor menu -> (nama kasus, path file DFA)
KASUS = {
    "1": ("Variable Name", BASE / "kasus 1 (Variable_name)" / "dfa_variable.py"),
    "2": ("Email Sederhana", BASE / "kasus 2 (Email)" / "dfa_email.py"),
    "3": ("Format Jam (HH:MM)", BASE / "kasus 3 (Format Jam)" / "format_jam.py"),
}


def muat_modul(path):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    modul = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modul)
    return modul


def cetak_tabel(header, baris):
    """Cetak tabel teks dengan lebar kolom menyesuaikan isi."""
    lebar = [max(len(str(r[i])) for r in [header] + baris) for i in range(len(header))]
    garis = "+-" + "-+-".join("-" * w for w in lebar) + "-+"

    def fmt(r):
        return "| " + " | ".join(str(c).ljust(w) for c, w in zip(r, lebar)) + " |"

    print(garis)
    print(fmt(header))
    print(garis)
    for r in baris:
        print(fmt(r))
    print(garis)


def tabel_langkah(modul, teks):
    """Tabel transisi untuk satu string: state asal, karakter, simbol, state tujuan."""
    baris = []
    state = modul.START
    for i, ch in enumerate(teks, start=1):
        simbol = modul.klasifikasi(ch)
        tujuan = modul.DELTA.get((state, simbol), modul.TRAP)
        baris.append([i, state, repr(ch), simbol, tujuan])
        state = tujuan
    if baris:
        print("\nTabel transisi untuk input ini:")
        cetak_tabel(["No", "State asal", "Karakter", "Simbol", "State tujuan"], baris)
    else:
        print("\n(Input kosong: tidak ada transisi, DFA tetap di state awal.)")
    return state


def tabel_dfa(modul):
    """Tabel transisi lengkap DFA: baris = state, kolom = simbol alfabet."""
    simbol = []
    for (_, s) in modul.DELTA:
        if s not in simbol:
            simbol.append(s)
    baris = []
    for q in sorted(modul.Q):
        tanda = ("->" if q == modul.START else "") + ("*" if q in modul.FINAL else "")
        nama = f"{tanda}{q}" if tanda else q
        baris.append([nama] + [modul.DELTA.get((q, s), "-") for s in simbol])
    print("\nTabel transisi lengkap DFA  (-> state awal, * state akhir):")
    cetak_tabel(["State"] + simbol, baris)


def jalankan_kasus(nama, path):
    modul = muat_modul(path)
    print(f"\n=== Validasi {nama} ===")
    print("Ketik 'tabel' untuk melihat tabel transisi lengkap, 'kembali' untuk ke menu.")
    while True:
        teks = input("Masukkan string: ")
        if teks.lower() == "kembali":
            break
        if teks.lower() == "tabel":
            tabel_dfa(modul)
            continue
        ok, jejak = modul.validasi(teks)
        tabel_langkah(modul, teks)
        print("\nJejak  :", " -> ".join(jejak))
        print("Status :", "VALID" if ok else "TIDAK VALID")
        print()


def main():
    while True:
        print("\n=== DFA Validator - Kelompok 11 ===")
        for kode, (nama, _) in KASUS.items():
            print(f"{kode}. {nama}")
        print("0. Keluar")
        pilihan = input("Pilih kasus: ").strip()
        if pilihan == "0":
            break
        if pilihan in KASUS:
            nama, path = KASUS[pilihan]
            jalankan_kasus(nama, path)
        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()