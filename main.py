import importlib.util
import os
from pathlib import Path

BASE = Path(__file__).parent

KASUS = {
    "1": ("Variable Name", BASE / "kasus 1 (Variable_name)" / "dfa_variable.py"),
    "2": ("Email Sederhana", BASE / "kasus 2 (Email)" / "dfa_email.py"),
    "3": ("Format Jam (HH:MM)", BASE / "kasus 3 (Format Jam)" / "format_jam.py"),
}


def bersihkan_layar():
    """Membersihkan layar terminal (cls untuk Windows, clear untuk Linux/Mac)."""
    os.system("cls" if os.name == "nt" else "clear")


def muat_modul(path):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    modul = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modul)
    return modul


def jalankan_kasus(kode_kasus, nama, path):
    modul = muat_modul(path)

    print("=" * 70)
    print(f"      PROGRAM VALIDASI {nama.upper()} (DFA)")
    print("=" * 70)

    # Menampilkan aturan dan label input sesuai kasus
    if kode_kasus == "1":
        label_input = "variabel"
        print("Aturan:")
        print("1. Karakter pertama wajib berupa huruf (a-z, A-Z) atau '_'")
        print("2. Karakter berikutnya boleh huruf, angka (0-9), atau '_'")
        print("3. Karakter selain huruf, angka, dan underscore dianggap tidak valid.")
        print("=" * 70)

    elif kode_kasus == "2":
        label_input = "email"
        print("Aturan:")
        print("1. Username berupa alfanumerik (minimal 1 karakter)")
        print("2. Diikuti tepat satu simbol '@'")
        print("3. Diikuti nama domain alfanumerik (minimal 1 karakter)")
        print("4. Diikuti satu karakter titik ('.')")
        print("5. Diakhiri ekstensi berupa huruf (minimal 2 huruf, misal: com, id)")
        print("=" * 70)

    elif kode_kasus == "3":
        label_input = "jam"
        print("Aturan:")
        print("1. Jam 2 digit: bernilai 00-23")
        print("2. Tepat satu titik dua (:)")
        print("3. Menit 2 digit: bernilai 00-59")
        print("4. Tidak boleh ada karakter/digit tambahan")
        print("=" * 70)

    print("(Ketik 'kembali' untuk kembali ke Menu Utama)")

    while True:
        teks = input(f"\nMasukkan {label_input}: ").strip()

        if teks.lower() == "kembali":
            print("\nKembali ke menu utama...")
            input("Tekan Enter untuk melanjutkan...")
            bersihkan_layar()
            break

        if teks == "":
            print(">> Input tidak boleh kosong!")
            continue

        ok, jejak = modul.validasi(teks)
        status = "VALID" if ok else "TIDAK VALID"

        print("\n------------------ HASIL VALIDASI ------------------")
        print(f"Input Pengguna : '{teks}'")
        print(f"Jejak Transisi : {' -> '.join(jejak)}")
        print(f"Status Final   : {status}")
        print("-" * 48)


def main():
    bersihkan_layar()
    while True:
        print("=" * 40)
        print("     DFA VALIDATOR - KELOMPOK 11")
        print("=" * 40)
        for kode, (nama, _) in KASUS.items():
            print(f"[{kode}] Kasus {kode}: {nama}")
        print("[0] Keluar")
        print("=" * 40)

        pilihan = input("Pilih kasus (0-3): ").strip()

        if pilihan == "0":
            bersihkan_layar()
            print("Program selesai. Terima kasih.")
            break

        if pilihan in KASUS:
            nama, path = KASUS[pilihan]
            jalankan_kasus(pilihan, nama, path)
        else:
            print(">> Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()