import importlib.util
from pathlib import Path

BASE = Path(__file__).parent

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


def jalankan_kasus(kode_kasus, nama, path):
    modul = muat_modul(path)
    
    print("\n" + "=" * 70)
    print(f"      PROGRAM VALIDASI {nama.upper()} (DFA)")
    print("=" * 70)
    
    if kode_kasus == "1":
        print("Aturan:")
        print("1. Karakter pertama wajib berupa huruf (a-z, A-Z) atau '_'")
        print("2. Karakter berikutnya boleh huruf, angka (0-9), atau '_'")
        print("3. Karakter selain huruf, angka, dan underscore dianggap tidak valid.")
        print("=" * 70)

    print("(Ketik 'kembali' untuk kembali ke Menu Utama)")

    while True:
        teks = input("\nMasukkan variabel: ").strip()

        if teks.lower() == "kembali":
            print("Kembali ke menu utama...")
            break

        if teks == "":
            print("Input tidak boleh kosong!")
            continue

        ok, jejak = modul.validasi(teks)
        status = "VALID" if ok else "TIDAK VALID"

        print("\n---------------- HASIL VALIDASI ----------------")
        print(f"Input Pengguna : {teks}")
        print(f"Jejak Transisi : {' -> '.join(jejak)}")
        print(f"Status Final   : {status}")
        print("-" * 48)

def main():
    while True:
        print("\n" + "=" * 40)
        print("      DFA VALIDATOR - KELOMPOK 11")
        print("=" * 40)
        for kode, (nama, _) in KASUS.items():
            print(f"[{kode}] Kasus {kode}: {nama}")
        print("[0] Keluar")
        print("=" * 40)

        pilihan = input("Pilih kasus (0-3): ").strip()

        if pilihan == "0":
            print("Program selesai. Terima kasih.")
            break

        if pilihan in KASUS:
            nama, path = KASUS[pilihan]
            jalankan_kasus(pilihan, nama, path)
        else:
            print("Pilihan tidak valid, silakan coba lagi.")


if __name__ == "__main__":
    main()