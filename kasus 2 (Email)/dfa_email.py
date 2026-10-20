"""DFA validasi format jam HH:MM (24 jam).

Aturan:
- Jam 2 digit: 00-23
- Tepat satu titik dua (:)
- Menit 2 digit: 00-59
- Tidak boleh ada karakter lain
"""

# ---- Definisi formal M = (Q, Sigma, delta, q0, F) ----
Q = {"q0", "q1", "q2", "q3", "q4", "q5", "q6", "qT"}
SIGMA = {"0-1", "2", "3", "4-5", "6-9", ":", "lain"}
START = "q0"
FINAL = {"q6"}
TRAP = "qT"

# q0: awal
# q1: digit jam pertama 0/1 (digit kedua bebas 0-9)
# q2: digit jam pertama 2 (digit kedua hanya 0-3)
# q3: jam lengkap, menunggu ':'
# q4: habis ':', menunggu digit menit pertama (0-5)
# q5: digit menit pertama benar, menunggu digit kedua
# q6: menit lengkap (final)
DELTA = {
    ("q0", "0-1"): "q1", ("q0", "2"): "q2", ("q0", "3"): "qT",
    ("q0", "4-5"): "qT", ("q0", "6-9"): "qT", ("q0", ":"): "qT", ("q0", "lain"): "qT",

    ("q1", "0-1"): "q3", ("q1", "2"): "q3", ("q1", "3"): "q3",
    ("q1", "4-5"): "q3", ("q1", "6-9"): "q3", ("q1", ":"): "qT", ("q1", "lain"): "qT",

    ("q2", "0-1"): "q3", ("q2", "2"): "q3", ("q2", "3"): "q3",
    ("q2", "4-5"): "qT", ("q2", "6-9"): "qT", ("q2", ":"): "qT", ("q2", "lain"): "qT",

    ("q3", "0-1"): "qT", ("q3", "2"): "qT", ("q3", "3"): "qT",
    ("q3", "4-5"): "qT", ("q3", "6-9"): "qT", ("q3", ":"): "q4", ("q3", "lain"): "qT",

    ("q4", "0-1"): "q5", ("q4", "2"): "q5", ("q4", "3"): "q5",
    ("q4", "4-5"): "q5", ("q4", "6-9"): "qT", ("q4", ":"): "qT", ("q4", "lain"): "qT",

    ("q5", "0-1"): "q6", ("q5", "2"): "q6", ("q5", "3"): "q6",
    ("q5", "4-5"): "q6", ("q5", "6-9"): "q6", ("q5", ":"): "qT", ("q5", "lain"): "qT",

    ("q6", "0-1"): "qT", ("q6", "2"): "qT", ("q6", "3"): "qT",
    ("q6", "4-5"): "qT", ("q6", "6-9"): "qT", ("q6", ":"): "qT", ("q6", "lain"): "qT",

    ("qT", "0-1"): "qT", ("qT", "2"): "qT", ("qT", "3"): "qT",
    ("qT", "4-5"): "qT", ("qT", "6-9"): "qT", ("qT", ":"): "qT", ("qT", "lain"): "qT",
}


def klasifikasi(ch):
    """Ubah satu karakter menjadi simbol alfabet DFA."""
    if ch in "01":
        return "0-1"
    if ch == "2":
        return "2"
    if ch == "3":
        return "3"
    if ch in "45":
        return "4-5"
    if ch in "6789":
        return "6-9"
    if ch == ":":
        return ":"
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
        ("09:30", True),
        ("23:59", True),
        ("00:00", True),
        ("19:05", True),
        ("24:00", False),
        ("9:30", False),
        ("12:60", False),
        ("12:5", False),
        ("12:300", False),
        ("12-30", False),
        ("ab:cd", False),
        ("", False),
    ]
    for s, harapan in uji:
        ok, jejak = validasi(s)
        status = "VALID" if ok else "TIDAK VALID"
        cocok = "OK" if ok == harapan else "SALAH"
        print(f"{s!r:10} -> {status:12} [{cocok}] | {' -> '.join(jejak)}")