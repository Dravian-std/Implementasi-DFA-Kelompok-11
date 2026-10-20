"""DFA validasi nama variabel.

Aturan:
- Karakter pertama: huruf (a-z, A-Z) atau garis bawah (_)
- Karakter berikutnya: huruf, angka (0-9), atau garis bawah (_)
"""

# ---- Definisi formal M = (Q, Sigma, delta, q0, F) ----
Q = {"q0", "q1", "qT"}
SIGMA = {"huruf", "angka", "_", "lain"}
START = "q0"
FINAL = {"q1"}
TRAP = "qT"

# Tabel transisi: (state, kelas_karakter) -> state_berikutnya
DELTA = {
    ("q0", "huruf"): "q1",
    ("q0", "_"): "q1",
    ("q0", "angka"): "qT",
    ("q0", "lain"): "qT",

    ("q1", "huruf"): "q1",
    ("q1", "angka"): "q1",
    ("q1", "_"): "q1",
    ("q1", "lain"): "qT",

    ("qT", "huruf"): "qT",
    ("qT", "angka"): "qT",
    ("qT", "_"): "qT",
    ("qT", "lain"): "qT",
}


def klasifikasi(ch):
    """Ubah satu karakter menjadi simbol alfabet DFA."""
    if ch.isascii() and ch.isalpha():
        return "huruf"
    if ch.isascii() and ch.isdigit():
        return "angka"
    if ch == "_":
        return "_"
    return "lain"


def validasi(teks):
    """Jalankan DFA. Return (diterima: bool, jejak_state: list)."""
    state = START
    jejak = [state]
    for ch in teks:
        state = DELTA.get((state, klasifikasi(ch)), TRAP)
        jejak.append(state)
    return state in FINAL, jejak


if __name__ == "__main__":
    uji = [
        ("nama_user", True),
        ("_count1", True),
        ("x", True),
        ("123name", False),
        ("user-name", False),
        ("user name", False),
        ("", False),
    ]
    for s, harapan in uji:
        ok, jejak = validasi(s)
        status = "VALID" if ok else "TIDAK VALID"
        cocok = "OK" if ok == harapan else "SALAH"
        print(f"{s!r:12} -> {status:12} [{cocok}] | {' -> '.join(jejak)}")
