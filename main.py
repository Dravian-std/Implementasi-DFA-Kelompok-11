"""Menu utama: menjalankan validasi DFA untuk semua kasus.

Modul dimuat lewat path file (importlib) supaya folder bernama `email`
tidak bentrok dengan modul bawaan Python `email`.
"""
import importlib.util
from pathlib import Path

BASE = Path(__file__).parent

# nomor menu -> (nama kasus, path file DFA)
KASUS = {
    "1": ("Variable Name", BASE / "kasus 1" / "dfa_variable.py"),
    "2": ("Email Sederhana", BASE / "kasus 2" / "dfa_email.py"),
    "3": ("Validasi Variable", BASE / "kasus 3" / "validasi_variable_name.py"),
}


def muat_modul(path):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    modul = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modul)
    return modul


def jalankan_kasus(nama, path):
    modul = muat_modul(path)
    print(f"\n=== Validasi {nama} (ketik 'kembali' untuk ke menu) ===")
    while True:
        teks = input("Masukkan string: ")
        if teks.lower() == "kembali":
            break
        ok, jejak = modul.validasi(teks)
        print("Status :", "VALID" if ok else "TIDAK VALID")
        print("Jejak  :", " -> ".join(jejak))


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
