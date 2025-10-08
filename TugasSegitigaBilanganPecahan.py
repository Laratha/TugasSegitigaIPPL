def hampir_sama(x, y, toleransi=0.01):
    """Mengembalikan True jika x dan y berbeda <= 1%"""
    return abs(x - y) <= toleransi * max(abs(x), abs(y))

def tentukan_segitiga(a, b, c):
    # Jika ada sisi <= 0
    if a <= 0 or b <= 0 or c <= 0:
        return "Tidak dapat membentuk segitiga"

    # Urutkan
    sisi = sorted([a, b, c])
    a, b, c = sisi

    # Cek syarat segitiga
    if c >= a + b:
        return "Tidak dapat membentuk segitiga"

    # Cek jenis segitiga
    if hampir_sama(a, b) and hampir_sama(b, c):
        return "Segitiga Sama Sisi (Equilateral)"
    elif hampir_sama(a, b) or hampir_sama(b, c) or hampir_sama(a, c):
        return "Segitiga Sama Kaki (Isosceles)"
    elif hampir_sama(c ** 2, a ** 2 + b ** 2):
        return "Segitiga Siku-Siku (Right Triangle)"
    else:
        return "Segitiga Bebas (Scalene)"

# Contoh penggunaan
print(tentukan_segitiga(3, 4, 5))
print(tentukan_segitiga(2, 2, 2.01))
print(tentukan_segitiga(1, 2, 3))
