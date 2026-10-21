import importlib.util

spec = importlib.util.spec_from_file_location("jam", "kasus 3 (Format Jam)/format_jam.py")
jam = importlib.util.module_from_spec(spec)
spec.loader.exec_module(jam)

salah = 0
for h in range(100):
    for m in range(100):
        teks = f"{h:02d}:{m:02d}"
        harapan = h <= 23 and m <= 59
        hasil, jejak = jam.validasi(teks)
        if hasil != harapan:
            salah += 1
            print("SALAH:", teks)

print("Total diuji: 10000, salah:", salah)
