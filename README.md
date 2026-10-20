# Implementasi DFA untuk Validasi Input - Kelompok 11

Tugas Kelompok UTS: program yang mengimplementasikan *Deterministic Finite Automata* (DFA) untuk memvalidasi string masukan. Program menentukan apakah masukan **VALID** (diterima) atau **TIDAK VALID** (ditolak), lengkap dengan jejak transisi state.

## Anggota Kelompok

| No | Nama | NIM | Kasus |
|----|------|-----|-------|
| 1 | Danang Rafli Juvianto | K3525054 | TODO |
| 2 | TODO | TODO | TODO |
| 3 | TODO | TODO | TODO |

Universitas Sebelas Maret (UNS), Kelas B

## Kasus yang Diimplementasikan

| No | Kasus | Aturan singkat | Contoh VALID | Contoh TIDAK VALID |
|----|-------|----------------|--------------|--------------------|
| 1 | Variable Name | Karakter pertama huruf atau `_`; karakter berikutnya huruf, angka, atau `_` | `nama_user`, `_count1` | `123name`, `user-name` |
| 2 | Email Sederhana | `username@domain.ekstensi`: username dan domain alfanumerik, tepat satu `@`, satu titik, ekstensi minimal 2 huruf | `budi123@gmail.com` | `budi@gmail`, `budi@@gmail.com` |
| 3 | Format Jam (HH:MM) | Jam 00-23, tanda `:`, menit 00-59, masing-masing 2 digit | `09:30`, `23:59` | `24:00`, `9:30`, `12:60` |

## Struktur Repository

```
.
├── README.md
├── main.py                              # menu untuk menjalankan semua kasus
├── kasus 1 (Variable_name)/dfa_variable.py
├── kasus 2 (Email)/dfa_email.py
├── kasus 3 (Format Jam)/format_jam.py
└── laporan/
```

Setiap file kasus berisi definisi DFA (state, alfabet, tabel transisi `DELTA`, state awal, state akhir), fungsi `validasi(teks)`, dan contoh pengujian.

## Definisi Formal Singkat

| Kasus | Q | Σ | q0 | F |
|-------|---|---|----|---|
| Variable Name | {q0, q1, qT} | {huruf, angka, `_`, lain} | q0 | {q1} |
| Email | {q0, q1, q2, q3, q4, q5, q6, qT} | {huruf, angka, `@`, `.`, lain} | q0 | {q6} |
| Format Jam | {q0, q1, q2, q3, q4, q5, q6, qT} | {0-1, 2, 3, 4-5, 6-9, `:`, lain} | q0 | {q6} |

`qT` adalah state jebakan (trap): setelah masuk, string pasti ditolak. Tabel transisi lengkap ada di variabel `DELTA` pada masing-masing file kasus, dan di laporan.

## Cara Menjalankan

Membutuhkan Python 3.7 atau lebih baru.

```bash
python main.py
```

Pilih nomor kasus, ketik string, lalu program menampilkan status dan jejak state. Ketik `kembali` untuk ke menu, `0` untuk keluar.

Contoh:

```
=== DFA Validator - Kelompok 11 ===
1. Variable Name
2. Email Sederhana
3. Format Jam (HH:MM)
0. Keluar
Pilih kasus: 3

=== Validasi Format Jam (HH:MM) (ketik 'kembali' untuk ke menu) ===
Masukkan string: 23:59
Status : VALID
Jejak  : q0 -> q2 -> q3 -> q4 -> q5 -> q6
Masukkan string: 24:00
Status : TIDAK VALID
Jejak  : q0 -> q2 -> qT -> qT -> qT -> qT
```

Tiap kasus juga bisa dijalankan sendiri untuk melihat hasil pengujian bawaannya:

```bash
python "kasus 1 (Variable_name)/dfa_variable.py"
python "kasus 2 (Email)/dfa_email.py"
python "kasus 3 (Format Jam)/format_jam.py"
```

## Laporan

Laporan lengkap (definisi tuple, tabel/diagram transisi, dan hasil pengujian): TODO (tempel link Google Docs)
