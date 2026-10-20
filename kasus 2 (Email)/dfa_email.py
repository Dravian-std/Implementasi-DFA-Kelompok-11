"""DFA validasi format email sederhana: username@domain.ekstensi

Aturan:
- Username: alfanumerik, minimal 1 karakter
- Tepat satu simbol @
- Domain: alfanumerik, minimal 1 karakter
- Satu titik (.)
- Ekstensi: huruf, minimal 2 karakter
"""

# ---- Definisi formal M = (Q, Sigma, delta, q0, F) ----
Q = {"q0", "q1", "q2", "q3", "q4", "q5", "q6", "qT"}
SIGMA = {"huruf", "angka", "@", ".", "lain"}
START = "q0"
FINAL = {"q6"}
TRAP = "qT"

# q0: awal | q1: username | q2: habis @ | q3: domain
# q4: habis titik | q5: ekstensi 1 huruf | q6: ekstensi >= 2 huruf (final)
DELTA = {
    ("q0", "huruf"): "q1", ("q0", "angka"): "q1",
    ("q0", "@"): "qT", ("q0", "."): "qT", ("q0", "lain"): "qT",

    ("q1", "huruf"): "q1", ("q1", "angka"): "q1",
    ("q1", "@"): "q2", ("q1", "."): "qT", ("q1", "lain"): "qT",

    ("q2", "huruf"): "q3", ("q2", "angka"): "q3",
    ("q2", "@"): "qT", ("q2", "."): "qT", ("q2", "lain"): "qT",

    ("q3", "huruf"): "q3", ("q3", "angka"): "q3",
    ("q3", "@"): "qT", ("q3", "."): "q4", ("q3", "lain"): "qT",

    ("q4", "huruf"): "q5", ("q4", "angka"): "qT",
    ("q4", "@"): "qT", ("q4", "."): "qT", ("q4", "lain"): "qT",

    ("q5", "huruf"): "q6", ("q5", "angka"): "qT",
    ("q5", "@"): "qT", ("q5", "."): "qT", ("q5", "lain"): "qT",

    ("q6", "huruf"): "q6", ("q6", "angka"): "qT",
    ("q6", "@"): "qT", ("q6", "."): "qT", ("q6", "lain"): "qT",

    ("qT", "huruf"): "qT", ("qT", "angka"): "qT",
    ("qT", "@"): "qT", ("qT", "."): "qT", ("qT", "lain"): "qT",
}


def klasifikasi(ch):
    """Ubah satu karakter menjadi simbol alfabet DFA."""
    if ch.isascii() and ch.isalpha():
        return "huruf"
    if ch.isascii() and ch.isdigit():
        return "angka"
    if ch in ("@", "."):
        return ch
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
        ("budi123@gmail.com", True),
        ("a@b.id", True),
        ("budi@gmail", False),
        ("budi@@gmail.com", False),
        ("@gmail.com", False),
        ("budi@.com", False),
        ("budi@gmail.c", False),
        ("budi@gmail.c0m", False),
        ("bu di@gmail.com", False),
        ("", False),
    ]
    for s, harapan in uji:
        ok, jejak = validasi(s)
        status = "VALID" if ok else "TIDAK VALID"
        cocok = "OK" if ok == harapan else "SALAH"